# view/annoucement_window.py

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ui.annouce_window import Ui_Form  # 注意UI文件名可能需同步更正
from util.dbutil import DBHelp
from util.common_util import get_uuid, get_current_time

class AnnoucementWindow(Ui_Form, QWidget):
    annoucement_done_signal = pyqtSignal()

    def __init__(self):
        super(AnnoucementWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_annoucement)

    def add_annoucement(self):
        title = self.lineEdit.text()
        content = self.textEdit.toPlainText()
        if '' in [title, content]:
            QMessageBox.warning(self, '警告', '请填写完整的公告标题和内容')
            return
        db = DBHelp()
        ann_info = [get_uuid(), title, content, get_current_time()]
        db.insert_announcement(ann_info)
        db.db_commit()
        del db
        self.annoucement_done_signal.emit()
        QMessageBox.information(self, '提示', '公告发布成功！')
        self.close()
