import sys
import math
from PyQt5.QtCore import Qt, QTimer, QPoint, QRectF
from PyQt5.QtGui import (
    QPainter, QColor, QPolygon, QBrush, QPen, QRadialGradient, QPainterPath
)
from PyQt5.QtWidgets import QWidget

class SailingBoatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.boat_x = 60
        self.boat_dir = 1
        self.sun_angle = 0
        self.wave_offset = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(30)

    def update_animation(self):
        max_x = self.width() - 60  # 帆船横向范围更灵活
        min_x = 60
        self.boat_x += self.boat_dir * 1.5  # 移动速度略减，因船更小
        if self.boat_x >= max_x:
            self.boat_x = max_x
            self.boat_dir = -1
        if self.boat_x <= min_x:
            self.boat_x = min_x
            self.boat_dir = 1
        self.sun_angle = (self.sun_angle + 2) % 360
        self.wave_offset += 0.21
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w, h = self.width(), self.height()

        # 背景白色
        painter.fillRect(self.rect(), Qt.white)

        # 画带圆角的水面底部
        water_height = h // 5
        water_radius = 30

        grad = QRadialGradient(w // 2, h - water_height//2, w // 1.5, w // 2, h - water_height//2)
        grad.setColorAt(0, QColor(95, 190, 255))
        grad.setColorAt(0.75, QColor(190, 220, 255, 200))
        grad.setColorAt(1, QColor(255, 255, 255, 0))

        # 圆角矩形路径（仅左右下角圆角）
        path = QPainterPath()
        path.moveTo(0, h - water_height)
        path.lineTo(0, h - water_radius)
        path.quadTo(0, h, water_radius, h)
        path.lineTo(w - water_radius, h)
        path.quadTo(w, h, w, h - water_radius)
        path.lineTo(w, h - water_height)
        path.closeSubpath()
        painter.setBrush(grad)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        # 画水面波浪（clip到圆角水面内）
        painter.save()
        painter.setClipPath(path)
        path_wave = QPainterPath()
        base_y = h - water_height + 12
        amplitude = 8  # 波浪高度
        wave_len = 80  # 波长
        path_wave.moveTo(0, base_y)
        for x in range(0, w+8, 4):
            y = base_y + math.sin((x / wave_len * 2 * math.pi) + self.wave_offset) * amplitude * 0.6 \
                      + math.sin((x / (wave_len*0.62) * 2 * math.pi) + self.wave_offset * 1.7) * amplitude * 0.33
            path_wave.lineTo(x, y)
        path_wave.lineTo(w, h)
        path_wave.lineTo(0, h)
        path_wave.closeSubpath()
        painter.setBrush(QColor(120, 180, 255, 65))
        painter.setPen(QPen(QColor(120, 180, 255, 100), 2))
        painter.drawPath(path_wave)
        painter.restore()

        # 右上角更小太阳+光芒
        sun_radius = min(w, h) // 38 + 5  # 更小的太阳
        sun_x = w - sun_radius - 22
        sun_y = sun_radius + 18
        painter.save()
        for i in range(12):
            angle = self.sun_angle + i * 30
            r1 = sun_radius + 5
            r2 = sun_radius + 16
            x1 = sun_x + r1 * math.cos(math.radians(angle))
            y1 = sun_y + r1 * math.sin(math.radians(angle))
            x2 = sun_x + r2 * math.cos(math.radians(angle))
            y2 = sun_y + r2 * math.sin(math.radians(angle))
            painter.setPen(QPen(QColor(255, 215, 80, 130), 2))
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        painter.setBrush(QColor(255, 235, 90))
        painter.setPen(QPen(QColor(255, 200, 20), 1))
        painter.drawEllipse(sun_x - sun_radius, sun_y - sun_radius, sun_radius * 2, sun_radius * 2)
        painter.restore()

        # 帆船（整体缩小！）
        painter.save()
        y_base = h - water_height - 8
        x = int(self.boat_x)
        scale = 0.75  # 船缩小到原来的70%
        # 船体
        painter.setBrush(QColor(139, 69, 19))
        painter.setPen(Qt.NoPen)
        boat_poly = QPolygon([
            QPoint(int(x-22*scale), int(y_base)),
            QPoint(int(x+22*scale), int(y_base)),
            QPoint(int(x+13*scale), int(y_base+12*scale)),
            QPoint(int(x-13*scale), int(y_base+12*scale)),
        ])
        painter.drawPolygon(boat_poly)
        # 桅杆
        painter.setPen(QPen(QColor(80, 80, 80), int(3*scale)))
        painter.drawLine(x, y_base, x, int(y_base-36*scale))
        # 白帆
        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(QPen(QColor(150, 150, 150), 1))
        sail1 = QPolygon([
            QPoint(x, int(y_base-36*scale)),
            QPoint(int(x+18*scale), int(y_base-13*scale)),
            QPoint(x, int(y_base-13*scale)),
        ])
        painter.drawPolygon(sail1)
        # 粉帆
        painter.setBrush(QColor(255, 182, 193))
        sail2 = QPolygon([
            QPoint(x, int(y_base-36*scale)),
            QPoint(x, int(y_base-13*scale)),
            QPoint(int(x-14*scale), int(y_base-7*scale)),
        ])
        painter.drawPolygon(sail2)
        painter.restore()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = SailingBoatWidget()
    w.resize(420, 340)
    w.show()
    sys.exit(app.exec_())
