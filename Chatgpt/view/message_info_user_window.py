# view/message_info_user_window.py

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from ui.message_info_user_window import Ui_Form
from util.dbutil import DBHelp

class MessageInfoUserWindow(Ui_Form, QWidget):
    def __init__(self, username):
        super(MessageInfoUserWindow, self).__init__()
        self.setupUi(self)
        self.username = username
        self.refresh_pushButton.clicked.connect(self.init_data)
        self.send_pushButton.clicked.connect(self.send_message)
        self.init_data()

    def init_data(self):
        db = DBHelp()
        messages = db.query_user_message(self.username)
        self.tableWidget.setRowCount(0)
        for msg in messages:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            # [id, sender_name, receiver_name, send_content, send_time, is_replied, reply_content, reply_time]
            col_map = [1, 3, 4, 5, 6, 7]
            for j, idx in enumerate(col_map):
                item = QTableWidgetItem(str(msg[idx]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, item)
        del db

    def send_message(self):
        receiver = self.receiver_lineEdit.text()
        content = self.content_textEdit.toPlainText()
        if not receiver or not content:
            QMessageBox.warning(self, '警告', '请填写接收人和内容')
            return
        db = DBHelp()
        msg_info = [
            None,  # id 主键自增或用uuid（可改为 get_uuid()）
            self.username,
            receiver,
            content,
            get_current_time(),
            0,  # is_replied
            '',  # reply_content
            '',  # reply_time
        ]
        db.insert_message(msg_info)
        db.db_commit()
        del db
        self.init_data()
        QMessageBox.information(self, '提示', '消息发送成功！')
