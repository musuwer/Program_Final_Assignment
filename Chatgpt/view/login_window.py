# view/login_window.py

from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.login_window import Ui_Form
from util.dbutil import DBHelp

class LoginWindow(Ui_Form, QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.login_pushButton.clicked.connect(self.login)
        self.register_pushButton.clicked.connect(self.register)

    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        db = DBHelp()
        row = db.get_one('user', 'username', username)
        if row is None or row[2] != password:
            QMessageBox.warning(self, '登录失败', '用户名或密码错误')
            return
        # 登录成功，发信号到主窗口（如有需要可传用户名、角色）
        # self.login_success_signal.emit(row[1], row[3])
        QMessageBox.information(self, '提示', '登录成功')
        # 可根据你的主窗口管理流程进行跳转
        self.close()
        del db

    def register(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        db = DBHelp()
        if db.check_exist('user', 'username', username):
            QMessageBox.warning(self, '注册失败', '用户名已存在')
            return
        role = 1  # 默认注册为普通用户
        user_info = [
            None,  # id 主键自增或get_uuid()
            username,
            password,
            role,
            get_current_time(),
            0,
            ''
        ]
        db.add_user(user_info)
        db.db_commit()
        del db
        QMessageBox.information(self, '提示', '注册成功，请登录！')
