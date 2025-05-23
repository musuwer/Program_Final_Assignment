# view/main_window.py

from PyQt5.QtWidgets import QWidget, QStackedWidget
from ui.main_window import Ui_Form
from view.home_window import HomeWindow
from view.achievement_window import AchievementWindow
from view.logrecord_window import LogRecordWindow
from view.message_info_user_window import MessageInfoUserWindow

class MainWindow(Ui_Form, QWidget):
    def __init__(self, user_role, username):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.init_ui()

    def init_ui(self):
        self.stackedWidget = QStackedWidget(self)
        self.verticalLayout.addWidget(self.stackedWidget)
        # 页面
        self.home_win = HomeWindow(self.user_role, self.username)
        self.achievement_win = AchievementWindow(self.user_role, self.username)
        self.log_win = LogRecordWindow(self.user_role, self.username)
        self.msg_win = MessageInfoUserWindow(self.username)
        # 加入stacked
        self.stackedWidget.addWidget(self.home_win)
        self.stackedWidget.addWidget(self.achievement_win)
        self.stackedWidget.addWidget(self.log_win)
        self.stackedWidget.addWidget(self.msg_win)
        # 按钮切换
        self.home_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_win))
        self.achievement_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.achievement_win))
        self.logrecord_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.log_win))
        self.message_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.msg_win))
        # 显示用户名
        self.username_label.setText(self.username)
        self.role_label.setText(self.user_role)
