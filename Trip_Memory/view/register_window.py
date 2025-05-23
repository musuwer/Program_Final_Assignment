"""
文件名：register_window.py
描述：实现注册窗口的交互以及注册验证
"""

import sys
from PyQt5.QtCore import Qt  # Qt常量，窗口模态等
from PyQt5.QtGui import QIcon  # 设置窗口图标
from PyQt5.QtWidgets import QWidget, QApplication  # QWidget基类和应用对象
from ui.register_window import Ui_Form  # 导入自动生成的UI类
from util.common_util import msg_box, get_md5, get_uuid, get_current_time, SYS_STYLE, APP_ICON  # 通用工具
from util.dbutil import DBHelp  # 数据库工具类


class RegisterWindow(Ui_Form, QWidget):
    def __init__(self, login):
        super(RegisterWindow, self).__init__()  # 调用父类构造
        self.setupUi(self)  # 初始化UI
        self.setWindowTitle('用户注册')  # 设置窗口标题
        self.init_ui()  # 初始化窗口UI样式

        self.register_pushButton.clicked.connect(self.register)  #注册按钮绑定注册处理函数
        self.return_pushButton.clicked.connect(self.retu_login)  # 返回按钮绑定返回登录函数

        self.loginWindow = login  # 保存传入的登录窗口对象，便于返回时显示

    def init_ui(self):

        #可个性化更改按钮样式
        self.register_pushButton.setProperty('class', 'Aqua')  # 按钮样式
        self.return_pushButton.setProperty('class', 'Aqua')

        self.setStyleSheet(SYS_STYLE)  # 应用全局QSS样式

        self.register_pushButton.setMinimumWidth(60)
        self.return_pushButton.setMinimumWidth(60)
        self.setWindowIcon(QIcon(APP_ICON))  # 设置窗口图标

        self.setWindowModality(Qt.ApplicationModal)  # 设置为应用模态（注册时不能操作主界面）
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 只允许关闭

    def register(self):
        """
        注册处理槽函数
        :return:
        """
        username = self.username_lineEdit.text()  # 获取用户名
        password = self.password_lineEdit.text()  # 获取密码
        confirm = self.confirm_password_lineEdit.text()  # 获取确认密码

        if '' in [username, password, confirm]:  # 有任意一项为空
            msg_box(self, '提示', '关键信息不能为空!')
            return

        #需要修改为SQlite ！！！
        db = DBHelp()
        count, res = db.query_super('user', 'username', username)  # 检查用户名是否存在


        if count != 0:
            msg_box(self, '提示', '用户名已存在!')
            return
        if password != confirm:  # 两次输入密码不一致
            msg_box(self, '错误', '两次输入密码不一致!')
            return

        # 构造用户信息列表
        user_info = [get_uuid(), username, get_md5(password), 1, get_current_time(), 0, get_current_time()]

        db.add_user(user_info)  # mysql插入用户到数据库中，能否改成sqlite
        db.db_commit()

        db.instance = None
        del db  # 释放数据库对象

        msg_box(self, '提示', '注册成功!')  # 弹窗提示
        self.loginWindow.show()  # 返回登录窗口
        self.close()  # 关闭注册窗口

    def retu_login(self):
        """
        返回登录界面
        :return:
        """
        self.loginWindow.show()  # 显示登录窗口
        self.close()  # 关闭注册窗口

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用对象
    win = RegisterWindow()  # 实例化注册窗口
    win.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主事件循环
