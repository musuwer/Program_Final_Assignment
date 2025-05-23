# view/home_window.py

from PyQt5.QtWidgets import QWidget
from ui.home_window import Ui_Form
from util.dbutil import DBHelp

class HomeWindow(Ui_Form, QWidget):
    def __init__(self, user_role=None, username=None):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.init_announcements()
        self.init_mood_calendar()

    def init_announcements(self):
        db = DBHelp()
        announcements = db.query_announcement()
        self.annouce_textEdit.clear()
        for ann in announcements:
            self.annouce_textEdit.append(f"{ann[1]}（{ann[3]}）\n{ann[2]}\n")
        del db

    def init_mood_calendar(self):
        # 假设你有心情日历的UI控件，数据部分如下
        db = DBHelp()
        _, moods = db.query_super('mood', 'username', self.username)
        # 示例：遍历moods, 在日历控件标记（需配合你的UI方法）
        for mood in moods:
            # mood = [id, username, mood_name, proportion, mood_date]
            date_str = mood[4]
            mood_name = mood[2]
            # TODO: 用你的日历控件 API，在 date
