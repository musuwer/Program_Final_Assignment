"""
文件名：main_window.py
描述：实现主窗口的交互
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.main_window import Ui_MainWindow
from util.common_util import ROLE_MAP, APP_ICON, SYS_STYLE

from view.home_window import HomeWindow
from view.logrecord_window import LogRecordWindow
from view.achievement_window import AchievementWindow
from view.about_window import AboutWindow
from view.message_info_window import MessageInfoWindow
from view.message_info_user_window import MessageInfoUserWindow

from view.mood_calendar_window import MoodCalendarWindow
from view.travel_map_window import TravelMapWindow

import datetime  # 打印测试时间用

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, login=None, username=None, role=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # 初始化UI

        self.is_change_user = False  # 是否登出状态
        self.username = username  # 当前用户名

        self.login_win = login    # 登录窗口引用:由login_window中handle_login函数传入的login

        self.role = ROLE_MAP.get(str(role))  # 用户角色名

        self.init_slot()   # 信号槽绑定
        self.init_ui()     # 初始化界面
        print("系统时间Final:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 打印当前时间

    def init_ui(self):
        self.pushButton.setProperty('class', 'Aqua')      # 登出按钮样式
        self.pushButton.setMinimumWidth(60)
        self.setStyleSheet(SYS_STYLE)                     # 应用样式
        self.setWindowIcon(QIcon(APP_ICON))               # 设置窗口图标
        self.setWindowTitle('亿途Trip Memory')            # 窗口标题

        self.listWidget.setCurrentRow(0)                  # 默认选中主页

        self.current_username_label.setText(self.username)  # 显示用户名
        self.current_role_label.setText(self.role)           # 显示角色

        # 移除UI设计自带的两个页面
        self.stackedWidget.removeWidget(self.page)
        self.stackedWidget.removeWidget(self.page_2)

        # 添加各功能页面到堆叠窗口
        self.stackedWidget.addWidget(HomeWindow(user_role=self.role))
        self.stackedWidget.addWidget(AchievementWindow(user_role=self.role, username=self.username))
        self.stackedWidget.addWidget(LogRecordWindow(self.role, self.username))

        self.stackedWidget.addWidget(MoodCalendarWindow())  # 关于情绪日历
        self.stackedWidget.addWidget(TravelMapWindow())

        # 添加消息页面：根据角色分别加入不同消息管理界面
        if self.role == '管理员':
            self.stackedWidget.addWidget(MessageInfoWindow(user_role=self.role, username=self.username))
        else:
            self.stackedWidget.addWidget(MessageInfoUserWindow(user_role=self.role, username=self.username))

        self.stackedWidget.addWidget(AboutWindow())  # 关于页面

    def init_slot(self):
        """
        主窗口信号槽连接
        """
        self.listWidget.currentItemChanged.connect(self.item_changed)  # 左侧导航栏切换页面
        self.pushButton.clicked.connect(self.log_out)                  # 登出按钮

    def item_changed(self):
        """
        左侧导航切换右侧页面
        """
        self.stackedWidget.setCurrentIndex(self.listWidget.currentRow())

    def log_out(self):
        """
        登出
        """
        self.is_change_user = True
        self.close()

    def closeEvent(self, event):
        """
        关闭事件，区分是退出系统还是登出
        """
        if self.is_change_user:
            reply = QMessageBox.question(self, '消息', '确定退出当前账号吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.question(self, '消息', '确定退出系统吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            if self.is_change_user:
                self.login_win.show()
        else:
            event.ignore()
            self.is_change_user = False
