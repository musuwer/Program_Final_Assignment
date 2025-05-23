from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QDialog, QTextEdit, QLineEdit, QDateEdit
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
import os
import sqlite3
import frozen_dir

SUPER_DIR = frozen_dir.app_path() # 当前项目的绝对路径

# 地图省份坐标（按你的图片像素）
PROVINCE_POINTS = {
    "新疆": (90, 200),
    "西藏": (100, 510),
    "青海": (260, 410),
    "甘肃": (330, 285),
    "内蒙古": (530, 130),
    "宁夏": (430, 345),
    "陕西": (480, 370),
    "四川": (360, 520),
    "重庆": (470, 560),
    "云南": (340, 680),
    "贵州": (480, 650),
    "广西": (570, 720),
    "广东": (670, 700),
    "海南": (830, 830),
    "湖南": (630, 600),
    "湖北": (620, 500),
    "河南": (700, 410),
    "江西": (790, 570),
    "福建": (900, 590),
    "安徽": (820, 480),
    "浙江": (970, 480),
    "江苏": (950, 410),
    "上海": (1020, 440),
    "山东": (980, 340),
    "北京": (1000, 200),
    "天津": (1050, 250),
    "河北": (950, 270),
    "山西": (850, 330),
    "辽宁": (1060, 160),
    "吉林": (1120, 110),
    "黑龙江": (1200, 80),
    "台湾": (1100, 720),
    "香港": (1010, 760),
    "澳门": (970, 780)
}

class TravelMapWindow(QWidget):
    def __init__(self, db_path='data.db'):
        super().__init__()
        self.setWindowTitle("旅行地图")
        layout = QVBoxLayout(self)

        # 标题
        self.title = QLabel("旅行地图-点击省份打卡")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size:24px;font-weight:bold;")
        layout.addWidget(self.title)

        # 加载原始地图图片
        map_img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), SUPER_DIR + r"/res/img/map.jpg"))
        self.map_label = QLabel()
        self.map_pixmap = QPixmap(map_img_path)

        # 新增：缩放到800宽
        target_width = 800
        scale_ratio = target_width / self.map_pixmap.width()
        scaled_pixmap = self.map_pixmap.scaledToWidth(target_width, Qt.SmoothTransformation)
        self.map_label.setPixmap(scaled_pixmap)
        self.map_label.setFixedSize(scaled_pixmap.size())
        layout.addWidget(self.map_label)

        # 自动窗口大小
        self.resize(scaled_pixmap.width(), scaled_pixmap.height() + 60)
        self.setMinimumSize(scaled_pixmap.width(), scaled_pixmap.height() + 60)

        # 省份按钮坐标也要乘以 scale_ratio
        self.province_buttons = []
        for province, (x, y) in PROVINCE_POINTS.items():
            btn = QPushButton(province, self.map_label)
            btn.setStyleSheet("background:rgba(255,255,255,0.7);border-radius:8px;font-size:12px;")
            # 坐标也缩放
            btn.move(int(x * scale_ratio), int(y * scale_ratio))
            btn.clicked.connect(lambda _, p=province: self.mark_travel(p))
            btn.setFixedSize(42, 24)
            btn.setToolTip(f"点击记录 {province}")
            btn.show()
            self.province_buttons.append(btn)


        # 数据库
        self.conn = sqlite3.connect(db_path)
        self.create_table()

        # 地图按钮
        self.province_buttons = []
        for province, (x, y) in PROVINCE_POINTS.items():
            btn = QPushButton(province, self.map_label)
            btn.setStyleSheet("background:rgba(255,255,255,0.7);border-radius:8px;font-size:12px;")
            btn.move(x, y)
            btn.clicked.connect(lambda _, p=province: self.mark_travel(p))
            btn.setFixedSize(42, 24)
            btn.setToolTip(f"点击记录 {province}")
            btn.show()
            self.province_buttons.append(btn)

        # 刷新已打卡省份（绿色高亮）
        self.refresh_buttons()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS travel_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province TEXT,
                city TEXT,
                visit_date TEXT,
                mood TEXT,
                note TEXT,
                photo_path TEXT,
                user TEXT
            )
        ''')
        self.conn.commit()

    def refresh_buttons(self):
        # 查询已打卡省份
        c = self.conn.cursor()
        c.execute("SELECT DISTINCT province FROM travel_records")
        marked = {row[0] for row in c.fetchall()}
        for btn in self.province_buttons:
            if btn.text() in marked:
                btn.setStyleSheet("background:#5bd065;color:white;font-weight:bold;border-radius:8px;")
            else:
                btn.setStyleSheet("background:rgba(255,255,255,0.7);border-radius:8px;font-size:12px;")

    def mark_travel(self, province):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"{province} - 新打卡")
        dlg_layout = QVBoxLayout(dialog)
        dlg_layout.addWidget(QLabel(f"省份：{province}"))
        city_edit = QLineEdit()
        city_edit.setPlaceholderText("城市名（可选）")
        dlg_layout.addWidget(city_edit)
        date_edit = QDateEdit()
        date_edit.setDate(QDate.currentDate())
        dlg_layout.addWidget(date_edit)
        mood_edit = QLineEdit()
        mood_edit.setPlaceholderText("今日心情/标签")
        dlg_layout.addWidget(mood_edit)
        note_edit = QTextEdit()
        note_edit.setPlaceholderText("游记内容")
        dlg_layout.addWidget(note_edit)

        # 图片选择
        photo_path = ""
        def choose_photo():
            nonlocal photo_path
            fname, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp)")
            if fname:
                photo_path = fname
                img_label.setPixmap(QPixmap(fname).scaledToHeight(100))

        img_label = QLabel()
        img_label.setFixedHeight(100)
        btn_img = QPushButton("选择图片")
        btn_img.clicked.connect(choose_photo)
        dlg_layout.addWidget(btn_img)
        dlg_layout.addWidget(img_label)

        btn_save = QPushButton("保存")
        dlg_layout.addWidget(btn_save)
        btn_save.clicked.connect(lambda: dialog.accept())

        if dialog.exec() == QDialog.Accepted:
            city = city_edit.text()
            date = date_edit.date().toString("yyyy-MM-dd")
            mood = mood_edit.text()
            note = note_edit.toPlainText()
            self.conn.execute(
                "INSERT INTO travel_records (province, city, visit_date, mood, note, photo_path, user) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (province, city, date, mood, note, photo_path, 'default')
            )
            self.conn.commit()
            self.refresh_buttons()
