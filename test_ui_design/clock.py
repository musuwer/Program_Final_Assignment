from PyQt5.QtCore import Qt, QTimer, QTime, QPoint, QRectF
from PyQt5.QtGui import QPainter, QColor, QPolygon, QFont, QPen, QLinearGradient, QBrush
from PyQt5.QtWidgets import QWidget

class AnalogClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle('渐变指针模拟时钟')  # 嵌入式不用标题
        # self.resize(400, 400)                 # 尺寸交给父级/布局管理
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        current_time = QTime.currentTime()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor("#ffffff"))
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        # 画12、3、6、9数字
        painter.setPen(QColor(40, 40, 40))
        font = QFont("Arial", 22, QFont.Bold)
        painter.setFont(font)
        positions = {
            '12': (0, -85),
            '3': (85, 0),
            '6': (0, 95),
            '9': (-88, 0)
        }
        for num, (x, y) in positions.items():
            painter.drawText(QRectF(x-20, y-20, 40, 40), Qt.AlignCenter, num)

        # 刻度线（长短/颜色不同）
        for i in range(60):
            painter.save()
            painter.rotate(i * 6)
            if i % 5 == 0:
                painter.setPen(QPen(QColor(80, 80, 80), 3))  # 小时线
                painter.drawLine(0, -88, 0, -100)
            else:
                painter.setPen(QPen(QColor(220, 180, 130), 1.5))  # 分钟线
                painter.drawLine(0, -92, 0, -100)
            painter.restore()

        # 时针渐变
        hour_gradient = QLinearGradient(0, 0, 0, -50)
        hour_gradient.setColorAt(0, QColor(90, 196, 255))
        hour_gradient.setColorAt(1, QColor(0, 70, 180))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(hour_gradient))
        hour_hand = QPolygon([QPoint(7, 8), QPoint(-7, 8), QPoint(0, -50)])
        painter.save()
        painter.rotate(30 * ((current_time.hour() % 12) + current_time.minute() / 60.0))
        painter.drawConvexPolygon(hour_hand)
        painter.restore()

        # 分针渐变
        min_gradient = QLinearGradient(0, 0, 0, -70)
        min_gradient.setColorAt(0, QColor(255, 160, 70))
        min_gradient.setColorAt(1, QColor(200, 100, 20))
        painter.setBrush(QBrush(min_gradient))
        minute_hand = QPolygon([QPoint(5, 8), QPoint(-5, 8), QPoint(0, -70)])
        painter.save()
        painter.rotate(6 * (current_time.minute() + current_time.second() / 60.0))
        painter.drawConvexPolygon(minute_hand)
        painter.restore()

        # 秒针渐变
        sec_gradient = QLinearGradient(0, 0, 0, -85)
        sec_gradient.setColorAt(0, QColor(255, 110, 110))
        sec_gradient.setColorAt(1, QColor(255, 30, 30))
        painter.setBrush(QBrush(sec_gradient))
        second_hand = QPolygon([QPoint(2, 12), QPoint(-2, 12), QPoint(0, -85)])
        painter.save()
        painter.rotate(6 * current_time.second())
        painter.drawConvexPolygon(second_hand)
        painter.restore()

        # 圆心小圆点
        painter.setBrush(QColor(70, 70, 70))
        painter.drawEllipse(QPoint(0, 0), 6, 6)

# 作为模块导入时，不会自动运行主窗口
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())
