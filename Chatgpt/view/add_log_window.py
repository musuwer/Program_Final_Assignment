# view/add_log_window.py

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ui.add_log_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import get_uuid, get_current_time

class AddLogWindow(Ui_Form, QWidget):
    # type_: 'event', 'achievement', 'goal'等
    add_log_done_signal = pyqtSignal()

    def __init__(self, type_, username):
        super(AddLogWindow, self).__init__()
        self.setupUi(self)
        self.type_ = type_
        self.username = username
        self.add_log_pushButton.clicked.connect(self.add_record)
        self.cancel_pushButton.clicked.connect(self.close)
        self.setWindowTitle(f"添加{self._type_display()}")

    def _type_display(self):
        return {
            'event': '事件',
            'achievement': '成就',
            'goal': '目标'
        }.get(self.type_, '记录')

    def add_record(self):
        db = DBHelp()
        if self.type_ == 'event':
            title = self.lineEdit1.text()
            content = self.lineEdit2.text()
            event_date = self.lineEdit3.text()
            category = self.lineEdit4.text()
            if '' in [title, content, event_date]:
                QMessageBox.warning(self, '警告', '请填写完整的事件标题、内容和日期')
                return
            evt_info = [get_uuid(), self.username, title, content, event_date, category]
            db.add_event(evt_info)
        elif self.type_ == 'achievement':
            title = self.lineEdit1.text()
            category = self.lineEdit2.text()
            score = self.lineEdit3.text()
            feelings = self.lineEdit4.text()
            achieve_date = self.lineEdit5.text()
            if '' in [title, category, score, achieve_date]:
                QMessageBox.warning(self, '警告', '请填写完整的成就名称、类型、得分和达成日期')
                return
            ach_info = [get_uuid(), self.username, title, category, int(score), feelings, achieve_date, get_current_time()]
            db.add_achievement(ach_info)
        elif self.type_ == 'goal':
            title = self.lineEdit1.text()
            description = self.lineEdit2.text()
            due_date = self.lineEdit3.text()
            status = self.lineEdit4.text()
            if '' in [title, description, due_date, status]:
                QMessageBox.warning(self, '警告', '请填写完整的目标信息')
                return
            goal_info = [get_uuid(), self.username, title, description, due_date, status]
            db.add_goal(goal_info)
        else:
            QMessageBox.warning(self, '警告', '未知记录类型')
            return
        db.db_commit()
        del db
        self.add_log_done_signal.emit()
        QMessageBox.information(self, '提示', '添加成功！')
        self.close()
