# view/log_edit_window.py

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ui.log_edit_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import get_current_time

class LogEditWindow(Ui_Form, QWidget):
    edit_log_done_signal = pyqtSignal()

    def __init__(self, record_type, record_id):
        super(LogEditWindow, self).__init__()
        self.setupUi(self)
        self.record_type = record_type  # 'event' 或 'achievement'
        self.record_id = record_id
        self.save_pushButton.clicked.connect(self.save_edit)
        self.cancel_pushButton.clicked.connect(self.close)
        self.init_data()

    def init_data(self):
        db = DBHelp()
        if self.record_type == 'event':
            row = db.get_one('event', 'id', self.record_id)
            if row:
                # [id, username, title, content, event_date, category]
                self.lineEdit1.setText(row[2])  # 标题
                self.lineEdit2.setText(row[3])  # 内容
                self.lineEdit3.setText(row[4])  # 日期
                self.lineEdit4.setText(row[5])  # 类别
        elif self.record_type == 'achievement':
            row = db.get_one('achievement', 'id', self.record_id)
            if row:
                # [id, username, title, category, score, feelings, achieve_date, record_time]
                self.lineEdit1.setText(row[2])  # 名称
                self.lineEdit2.setText(row[3])  # 类型
                self.lineEdit3.setText(str(row[4]))  # 分数
                self.lineEdit4.setText(row[5])  # 感想
                self.lineEdit5.setText(row[6])  # 达成日期
        del db

    def save_edit(self):
        db = DBHelp()
        if self.record_type == 'event':
            title = self.lineEdit1.text()
            content = self.lineEdit2.text()
            event_date = self.lineEdit3.text()
            category = self.lineEdit4.text()
            if '' in [title, content, event_date]:
                QMessageBox.warning(self, '警告', '请填写完整的事件标题、内容和日期')
                return
            update_dict = {
                'title': title,
                'content': content,
                'event_date': event_date,
                'category': category
            }
            db.update('event', update_dict, 'id', self.record_id)
        elif self.record_type == 'achievement':
            title = self.lineEdit1.text()
            category = self.lineEdit2.text()
            score = self.lineEdit3.text()
            feelings = self.lineEdit4.text()
            achieve_date = self.lineEdit5.text()
            if '' in [title, category, score, achieve_date]:
                QMessageBox.warning(self, '警告', '请填写完整的成就名称、类型、得分和达成日期')
                return
            update_dict = {
                'title': title,
                'category': category,
                'score': int(score),
                'feelings': feelings,
                'achieve_date': achieve_date,
                'record_time': get_current_time()
            }
            db.update('achievement', update_dict, 'id', self.record_id)
        db.db_commit()
        del db
        self.edit_log_done_signal.emit()
        QMessageBox.information(self, '提示', '保存成功！')
        self.close()
