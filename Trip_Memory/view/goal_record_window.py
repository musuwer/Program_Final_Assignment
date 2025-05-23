from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from ui.goal_record_window import Ui_Form
from util.common_util import msg_box, get_current_time, APP_ICON, SYS_STYLE, get_uuid
import sqlite3
import sys
import os

class GoalRecordWindow(Ui_Form, QWidget):
    goal_record_signal = pyqtSignal()  # 自定义信号

    def __init__(self):
        super(GoalRecordWindow, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('添加目标')
        self.pushButton.setMinimumWidth(60)
        self.pushButton_2.setMinimumWidth(60)
        self.pushButton.clicked.connect(self.cancel)     # 取消
        self.pushButton_2.clicked.connect(self.add_goal) # 添加
        self.setWindowIcon(QIcon(APP_ICON))
        self.pushButton_2.setProperty('class', 'Aqua')
        self.pushButton.setProperty('class', 'Aqua')
        self.setStyleSheet(SYS_STYLE)
        self.db_path = os.path.abspath("data.db")
        self.create_goal_table()

    def create_goal_table(self):
        """初始化时建表"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS goals (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        plan TEXT,
                        progress TEXT,
                        achievement TEXT,
                        create_time TEXT
                    )''')
        conn.commit()
        conn.close()

    def add_goal(self):
        """插入到 SQLite 数据库"""
        name = self.lineEdit.text()
        plan = self.lineEdit_2.text()
        progress = self.lineEdit_3.text()
        achievement = self.lineEdit_4.text()
        create_time = self.lineEdit_5.text() or get_current_time()
        if not name or not plan:
            msg_box(self, '错误', '请填写目标名称和计划!')
            return
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute("INSERT INTO goals (id, name, plan, progress, achievement, create_time) VALUES (?, ?, ?, ?, ?, ?)",
                      (get_uuid(), name, plan, progress, achievement, create_time))
            conn.commit()
            conn.close()
            self.goal_record_signal.emit()  # 发出数据已更新的信号
            self.close()
            msg_box(self, '提示', '目标添加成功!')
        except Exception as e:
            msg_box(self, '错误', f"添加失败: {e}")

    def cancel(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GoalRecordWindow()
    win.show()
    sys.exit(app.exec())
