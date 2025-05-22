"""
文件名：main_window.py
描述：实现主窗口的交互
"""

# 从PyQt5.QtGui模块导入QIcon类，用于处理图标
from PyQt5.QtGui import QIcon

# 从PyQt5.QtWidgets模块导入QMainWindow和QMessageBox类
# QMainWindow是主窗口的基类，QMessageBox用于显示消息框
from PyQt5.QtWidgets import QMainWindow, QMessageBox

# 从ui.main_window模块导入Ui_MainWindow类，该类用于设置主窗口的UI界面
from ui.main_window import Ui_MainWindow

# 从util.common_util模块导入ROLE_MAP、APP_ICON和SYS_STYLE常量
# ROLE_MAP用于映射用户角色，APP_ICON是应用程序的图标，SYS_STYLE是系统样式
from util.common_util import ROLE_MAP, APP_ICON, SYS_STYLE

# 从view包导入各个窗口类，用于在主窗口中显示不同的功能页面
from view.home_window import HomeWindow
from view.logrecord_window import LogRecordWindow
from view.achievement_window import AchievementWindow
from view.about_window import AboutWindow
from view.message_info_window import MessageInfoWindow
from view.message_info_user_window import MessageInfoUserWindow


import datetime # 测试卡顿原因



# 定义MainWindow类，继承自Ui_MainWindow和QMainWindow
# 该类用于实现主窗口的交互功能
class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, login=None, username=None, role=None):

        # 调用父类的构造函数
        super(MainWindow, self).__init__()

        # 设置UI界面
        self.setupUi(self)

        # 标记进入主页后用户不是登出状态
        self.is_change_user = False

        # 存储当前登录用户的用户名
        self.username = username

        # 存储登录窗口的引用，用于登出后显示登录窗口
        self.login_win = login

        # 通过ROLE_MAP获取用户的角色，将传入的角色转换为具体的角色名称
        self.role = ROLE_MAP.get(str(role))

        # 初始化信号槽连接
        self.init_slot()


        # 初始化UI界面
        self.init_ui()
        print("系统时间Final:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 登录进去系统时间

    def init_ui(self):

        # 为登出按钮设置名为'Aqua'的属性，可能用于样式设置
        self.pushButton.setProperty('class', 'Aqua')

        # 设置登出按钮的最小宽度为60像素
        self.pushButton.setMinimumWidth(60)

        # 设置主窗口的样式表，应用系统样式
        self.setStyleSheet(SYS_STYLE)

        # 设置主窗口的图标
        self.setWindowIcon(QIcon(APP_ICON))

        # 设置主窗口的标题
        self.setWindowTitle('亿途Trip Memory')

        # 默认选中左侧导航列表的第一项，即主页
        self.listWidget.setCurrentRow(0)

        # 在界面上显示当前登录用户的用户名
        self.current_username_label.setText(self.username)

        # 在界面上显示当前登录用户的角色
        self.current_role_label.setText(self.role)


        # 从堆叠窗口中移除原有的两页
        self.stackedWidget.removeWidget(self.page)
        self.stackedWidget.removeWidget(self.page_2)


        """
        管理页面的顺序，重点！！！
        """

        # 向堆叠窗口中添加主页窗口，传入用户角色
        self.stackedWidget.addWidget(HomeWindow(user_role=self.role))

        # 向堆叠窗口中添加借阅信息窗口，传入用户角色和用户名
        self.stackedWidget.addWidget(AchievementWindow(user_role=self.role, username=self.username))

        # 向堆叠窗口中添加图书管理窗口，传入用户角色和用户名
        self.stackedWidget.addWidget(LogRecordWindow(self.role, self.username))

        # 向堆叠窗口中添加借阅信息窗口，传入用户角色和用户名
        self.stackedWidget.addWidget(AchievementWindow(user_role=self.role, username=self.username))

        # 向堆叠窗口中添加图书管理窗口，传入用户角色和用户名
        self.stackedWidget.addWidget(LogRecordWindow(self.role, self.username))


        # 根据用户角色添加不同的消息信息窗口
        if self.role == '管理员':
            # 管理员角色添加管理员消息信息窗口
            self.stackedWidget.addWidget(MessageInfoWindow(user_role=self.role, username=self.username))
        else:
            # 普通用户角色添加普通用户消息信息窗口
            self.stackedWidget.addWidget(MessageInfoUserWindow(user_role=self.role, username=self.username))

        # 向堆叠窗口中添加关于窗口
        self.stackedWidget.addWidget(AboutWindow())

    def init_slot(self):
        """
        主窗口信号槽连接
        :return:
        """

        # 当左侧导航列表的当前项发生改变时，调用item_changed方法更新右侧堆叠窗口的显示
        self.listWidget.currentItemChanged.connect(self.item_changed)
        # 当登出按钮被点击时，调用log_out方法处理登出操作
        self.pushButton.clicked.connect(self.log_out)

    def item_changed(self):
        """
        与list导航窗口进行同步右侧显示stacked窗口
        :return:
        """

        # 根据左侧导航列表当前选中项的索引，设置右侧堆叠窗口显示对应的页面
        self.stackedWidget.setCurrentIndex(self.listWidget.currentRow())

    def log_out(self):
        """
        登出时设置用户是否登出状态
        :return:
        """
        # 标记用户为登出状态
        self.is_change_user = True
        # 关闭主窗口
        self.close()

    def closeEvent(self, event):
        """
        登出时提示语，健壮性处理
        :param event: 关闭事件对象
        :return:
        """
        if self.is_change_user:
            # 如果是登出操作，弹出确认框询问是否退出当前账号
            reply = QMessageBox.question(self, '消息', '确定退出当前账号吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            # 如果是直接关闭窗口，弹出确认框询问是否退出系统
            reply = QMessageBox.question(self, '消息', '确定退出系统吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 如果用户选择是，则接受关闭事件
            event.accept()
            if self.is_change_user:
                # 如果是登出操作，显示登录窗口
                self.login_win.show()
        else:
            # 如果用户选择否，则忽略关闭事件
            event.ignore()
            # 重置用户登出状态标记
            self.is_change_user = False