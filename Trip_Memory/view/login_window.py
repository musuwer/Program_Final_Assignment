"""
文件名：login_window.py
描述：实现登录窗口的交互以及登录验证
"""

from threading import Thread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, Qt
from ui.login_window import Ui_Form
from view.main_window import MainWindow
from util.dbutil import DBHelp
from util.common_util import msg_box, get_md5, APP_ICON, SYS_STYLE
from view.register_window import RegisterWindow
import ctypes
# 将exe的图标在状态栏显示
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import datetime # 测试卡顿原因

class LoginWindow(Ui_Form, QWidget):

    # 定义一个信号，用于在登录验证完成后发送登录结果，参数为整数类型
    login_done_signal = pyqtSignal(int)
    # login_done_signal 是一个 pyqtSignal 类型的对象，也就是一个自定义信号，用于在登录验证完成后传递登录结果，从而实现不同方法之间的通信。


    def __init__(self):
        """
        登陆界面类构造函数,初始化类属性等.
        """

        # 调用父类的构造函数
        super(LoginWindow, self).__init__()

        # 调用Ui_Form类的setupUi方法，用于设置界面的UI元素
        self.setupUi(self)

        # 初始化用户角色，初始值为None
        self.role = None

        # 调用init_ui方法，初始化界面的UI元素
        self.init_ui()

        # 初始化主窗口对象，初始值为None
        self.main_window = None
        # 初始化注册窗口对象，初始值为None
        self.register_win = None
        # 调用init_slot方法，初始化登录界面的信号槽连接
        self.init_slot()

    def init_ui(self):

        """
        初始化界面UI元素
        """
        # 设置窗口的标题为“用户登录”
        self.setWindowTitle('用户登录')

        # 设置窗口的图标，图标路径从APP_ICON获取
        self.setWindowIcon(QIcon(APP_ICON))

        # 给登录按钮设置qss样式，样式类名为'Aqua'
        self.login_pushButton.setProperty('class', 'Aqua')
        # 给注册按钮设置qss样式，样式类名为'Aqua'
        self.register_pushButton.setProperty('class', 'Aqua')

        # 设置窗口的样式表，样式表内容从SYS_STYLE获取
        self.setStyleSheet(SYS_STYLE)
        # 设置窗口的标志，允许关闭和最小化操作
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowMinimizeButtonHint)

    def init_slot(self):

        """
        初始化登录界面的信号槽连接
        """

        # 当注册按钮被点击时，调用btn_slot方法，并传入'register'参数
        self.register_pushButton.clicked.connect(lambda: self.btn_slot('register'))
        # 当登录按钮被点击时，调用btn_slot方法，并传入'login'参数
        self.login_pushButton.clicked.connect(lambda: self.btn_slot('login'))

        # 当login_done_signal信号被发射时，调用handle_login方法处理登录结果
        self.login_done_signal.connect(self.handle_login)

    def btn_slot(self, tag):
        """
        按钮点击事件槽函数
        :param tag: 点击的按钮的TAG
        :return: 出错返回,不执行后续操作逻辑
        """

        # 注册
        if tag == 'register':
            # 创建注册窗口对象，并传入当前登录窗口作为父窗口
            self.register_win = RegisterWindow(self)
            # 隐藏当前登录窗口
            self.hide()
            # 显示注册窗口
            self.register_win.show()

        # 登陆
        if tag == 'login':
            # 获取用户名输入框中的文本
            username = self.username_lineEdit.text()
            # 获取密码输入框中的文本
            password = self.password_lineEdit.text()
            # 如果用户名或密码为空
            if '' in [username, password]:
                # 弹出提示框，提示用户输入用户名或密码
                msg_box(self, '提示', '请输入用户名或密码!')
                return

            # 创建一个线程，用于执行登录验证操作
            login_th = Thread(target=self.login, args=(username, password))
            # 启动线程
            login_th.start()

    def login(self, username, password):
        """
        登陆子线程用户验证
        :param username: 需要验证的用户名
        :param password: 匹配的密码
        :return: 验证出错返回,并发射相应TAG的信号
        """
        # 创建数据库帮助类的对象


        db = DBHelp()
        # 查询用户表中用户名等于输入用户名的记录
        count, res = db.query_super(table_name='user', column_name='username', condition=username)


        # 如果查询结果为空，说明用户名不存在
        if count == 0:
            # 发射登录结果信号，结果码为1，表示用户名不存在
            self.login_done_signal.emit(1)
            return
        # 如果输入的密码经过MD5加密后与数据库中存储的密码不匹配
        if get_md5(password) != res[0][2]:
            # 发射登录结果信号，结果码为11，表示用户名或密码错误
            self.login_done_signal.emit(11)
            return
        # 获取用户的角色
        self.role = res[0][3]
        # 发射登录结果信号，结果码为111，表示登录成功
        self.login_done_signal.emit(111)
        print("开始进入系统时间:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #开始登录时间

    def handle_login(self, login_result):
        """
        执行登陆结果
        :param login_result: 登陆处理TAG
        :return: 登陆出错返回
        """


        #是由上个login函数来决定返回的信号
        # 如果登录结果码为1，表示用户名不存在
        if login_result == 1:
            # 弹出提示框，提示用户用户名不存在，请重试
            msg_box(self, '提示', '用户名不存在,请重试!')
            return

        # 如果登录结果码为11，表示用户名或密码错误
        if login_result == 11:
            # 弹出提示框，提示用户用户名或密码错误
            msg_box(self, '提示', '用户名或密码错误!')
            return

        # 如果登录结果码为111，表示登录成功
        if login_result == 111:

            # 获取用户名输入框中的文本
            username = self.username_lineEdit.text()
            # 创建主窗口对象，并传入当前登录窗口、用户名和用户角色
            self.main_window = MainWindow(login=self, username=username, role=self.role)
            # 显示主窗口

            print("最终登入系统时间:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #登录进去系统时间

            self.main_window.show()
            # 关闭当前登录窗口
            self.close()

    def keyPressEvent(self, QKeyEvent):
        """
        监听键盘触发事件,通过判断是否按下的按键为Enter或者Return键
        :param QKeyEvent: 键盘触发事件
        """
        # 如果按下的按键是Enter或者Return键
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            # 模拟点击登录按钮
            self.login_pushButton.click()