# view/logrecord_window.py

from threading import Thread
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QMenu, QAction, QMessageBox
from ui.logrecord_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import msg_box, DELETE_ICON, EDIT_ICON
from view.add_log_window import AddLogWindow
# 如果有事件编辑窗口，可from view.log_edit_window import LogEditWindow

class LogRecordWindow(Ui_Form, QWidget):
    query_event_info_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None, username=None):
        super(LogRecordWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.add_event_win = None
        self.event_edit_win = None
        self.event_id = []
        self.init_ui()
        self.init_slot()
        self.init_data()

    def init_ui(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.refresh_pushButton.setProperty('class', 'Aqua')
        self.add_event_pushButton.setProperty('class', 'Aqua')
        self.search_event_pushButton.setProperty('class', 'Aqua')
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)
        self.add_event_pushButton.setMinimumWidth(80)
        self.refresh_pushButton.setMinimumWidth(60)
        self.search_event_pushButton.setMinimumWidth(60)

    def generate_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        menu = QMenu()
        edit_action = QAction('编辑事件')
        edit_action.setIcon(EDIT_ICON)
        menu.addAction(edit_action)
        delete_action = QAction('删除事件')
        delete_action.setIcon(DELETE_ICON)
        menu.addAction(delete_action)
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == edit_action:
            msg_box(self, '提示', '请实现事件编辑窗口')
            # self.event_edit_win = LogEditWindow(event_id=self.event_id[row_num])
            # self.event_edit_win.show()
        if action == delete_action:
            reply = QMessageBox.warning(self, '消息', '确定删除该事件吗?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                db = DBHelp()
                db.delete('event', 'id', self.event_id[row_num])
                db.db_commit()
                del db
                self.refresh_pushButton.click()
                msg_box(self, '提示', '删除事件成功！')

    def init_slot(self):
        self.add_event_pushButton.clicked.connect(lambda: self.btn_slot('add'))
        self.search_event_pushButton.clicked.connect(lambda: self.btn_slot('search'))
        self.query_event_info_done_signal.connect(self.show_event)
        self.refresh_pushButton.clicked.connect(lambda: self.btn_slot('refresh'))

    def init_data(self):
        self.get_event_info()

    def show_event(self, event_info_result):
        self.event_id = []
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)
        events = event_info_result
        for event in events:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.event_id.append(event[0])
            # event = [id, username, title, content, event_date, category]
            col_map = [2, 3, 4, 5, 1]  # 标题、内容、日期、类别、用户名
            for j, idx in enumerate(col_map):
                item = QTableWidgetItem(str(event[idx]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, item)

    def btn_slot(self, tag):
        if tag == 'add':
            self.add_event_win = AddLogWindow('event', self.username)
            self.add_event_win.add_log_done_signal.connect(self.init_data)
            self.add_event_win.show()
        if tag == 'search':
            db = DBHelp()
            key = self.search_event_lineEdit.text()
            if not key:
                self.init_data()
                return
            # 按标题或类别模糊查，用户名精确查
            if self.search_comboBox.currentText() == "事件标题":
                _, res = db.query_search('event', 'title', key)
            elif self.search_comboBox.currentText() == "事件类别":
                _, res = db.query_search('event', 'category', key)
            elif self.search_comboBox.currentText() == "用户":
                _, res = db.query_super('event', 'username', key)
            else:
                _, res = db.query_search('event', 'title', key)
            self.query_event_info_done_signal.emit(res)
            del db
        if tag == 'refresh':
            self.get_event_info()

    def get_event_info(self):
        th = Thread(target=self.event_info_th)
        th.start()

    def event_info_th(self):
        db = DBHelp()
        # 管理员全部，普通用户只查自己的
        if self.user_role == '管理员':
            _, res = db.query_all('event')
        else:
            _, res = db.query_super('event', 'username', self.username)
        self.query_event_info_done_signal.emit(res)
        del db
