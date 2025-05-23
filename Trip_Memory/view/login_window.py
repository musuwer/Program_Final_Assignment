"""
文件名：login_window.py
描述：实现登录窗口的交互以及登录验证
"""

from threading import Thread  # 导入线程类，用于多线程执行登录验证
from PyQt5.QtGui import QIcon  # 导入QIcon类，用于设置窗口图标
from PyQt5.QtWidgets import QWidget  # 导入QWidget作为自定义窗口基类
from PyQt5.QtCore import pyqtSignal, Qt  # 导入信号与常量

from ui.login_window import Ui_Form  # 导入自动生成的UI类

from view.main_window import MainWindow  # 导入主窗口类

from util.dbutil import DBHelp  # 导入数据库工具类

from util.common_util import msg_box, get_md5, APP_ICON, SYS_STYLE  # 导入常用工具函数和常量
from view.register_window import RegisterWindow  # 导入注册窗口类
import ctypes  # 导入ctypes库用于设置应用图标

# 设置Windows任务栏图标（Windows特有，防止打包exe后图标不显示）
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import datetime # 用于输出测试卡顿和时间点

class LoginWindow(Ui_Form, QWidget):
    # 定义一个登录完成的信号，参数为整数类型
    login_done_signal = pyqtSignal(int)
    # login_done_signal 是自定义信号，用于在登录线程结束后通知主线程处理结果

    def __init__(self):
        """
        登陆界面类构造函数,初始化类属性等.
        """
        super(LoginWindow, self).__init__()  # 调用父类构造函数
        self.setupUi(self)  # 初始化UI界面元素
        self.init_ui()  # 初始化UI样式

        self.role = None  # 当前登录用户角色，默认为None
        self.main_window = None  # 主窗口对象
        self.register_win = None  # 注册窗口对象

        self.init_slot()  # 绑定信号与槽

    def init_ui(self):
        """
        初始化界面UI元素
        """
        self.setWindowTitle('用户登录')  # 设置窗口标题
        self.setWindowIcon(QIcon(APP_ICON))  # 设置窗口图标


        # 可个性化按钮位置：！！！
        self.login_pushButton.setProperty('class', 'Aqua')  # 登录按钮样式
        self.register_pushButton.setProperty('class', 'Aqua')  # 注册按钮样式


        self.setStyleSheet(SYS_STYLE)  # 设置窗口整体样式
        # 只允许关闭和最小化
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowMinimizeButtonHint)


    def init_slot(self):
        """
        初始化登录界面的信号槽连接
        """
        #页面切换

        # 注册按钮点击，跳转到注册页面
        self.register_pushButton.clicked.connect(lambda: self.btn_slot('register'))
        # 登录按钮点击，进行登录处理
        self.login_pushButton.clicked.connect(lambda: self.btn_slot('login'))
        # 登录完成信号，处理登录结果
        self.login_done_signal.connect(self.handle_login)

    def btn_slot(self, tag):
        """
        按钮点击事件槽函数
        :param tag: 点击的按钮的TAG
        :return: 出错返回,不执行后续操作逻辑
        """
        # 注册流程
        if tag == 'register':
            self.register_win = RegisterWindow(self)  # 创建注册窗口，父窗口为当前窗口
            self.hide()  # 隐藏登录窗口
            self.register_win.show()  # 显示注册窗口

        # 登录流程
        if tag == 'login':
            username = self.username_lineEdit.text()  # 获取用户名
            password = self.password_lineEdit.text()  # 获取密码
            if '' in [username, password]:  # 若用户名或密码为空
                msg_box(self, '提示', '请输入用户名或密码!')  # 弹出提示
                return

            # 创建新线程进行登录(执行login函数操作)，避免多个用户同时登录阻塞UI
            login_th = Thread(target=self.login, args=(username, password))
            login_th.start()

    def login(self, username, password):
        """
        登陆子线程用户验证
        :param username: 需要验证的用户名
        :param password: 匹配的密码
        :return: 验证出错返回,并发射相应TAG的信号
        """

        #修改为SQlite语句！！！
        db = DBHelp()  # 创建数据库操作对象
        count, res = db.query_super('user', 'username', username)  # 查询该用户名用户记录
        # 返回的 res 是一个二维数组/列表，只有一行

        if count == 0:
            # 用户名不存在
            self.login_done_signal.emit(1)  # 发送登录结果信号：1
            return
        if get_md5(password) != res[0][2]:  # 密码加密比对（数据库存的也是MD5）
            # 密码错误
            self.login_done_signal.emit(11)  # 发送登录结果信号：11
            return
        self.role = res[0][3]  # 获取用户角色
        self.login_done_signal.emit(111)  # 发送登录成功信号：111


    def handle_login(self, login_result):
        """
        执行登陆结果
        :param login_result: 登陆处理TAG
        :return: 登陆出错返回
        """
        # 判断login()线程返回的信号，分别弹窗提示或进入主窗口
        if login_result == 1:
            msg_box(self, '提示', '用户名不存在,请重试!')  # 用户不存在
            return
        if login_result == 11:
            msg_box(self, '提示', '用户名或密码错误!')  # 密码错误
            return
        if login_result == 111:
            # 登录成功
            username = self.username_lineEdit.text()  # 获取当前用户名

            self.main_window = MainWindow(login=self, username=username, role=self.role)  # 创建主窗口对象

            print("最终登入系统时间:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 打印当前时间
            self.main_window.show()  # 显示主窗口
            self.close()  # 关闭登录窗口

    def keyPressEvent(self, QKeyEvent):
        """
        监听键盘触发事件,通过判断是否按下的按键为Enter或者Return键
        :param QKeyEvent: 键盘触发事件
        """
        # 如果用户按下了回车/Enter键，则触发登录按钮点击事件
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.login_pushButton.click()
