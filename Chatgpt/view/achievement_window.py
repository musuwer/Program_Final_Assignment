# view/achievement_window.py

from threading import Thread
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QMenu, QAction, QMessageBox
from ui.achievement_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import msg_box, DELETE_ICON, EDIT_ICON, get_uuid, get_current_time
# 假设你有AddAchievementWindow/EditAchievementWindow，或共用AddLogWindow
from view.add_log_window import AddLogWindow

class AchievementWindow(Ui_Form, QWidget):
    init_data_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None, username=None):
        super(AchievementWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.achievement_id = []
        self.add_win = None
        self.init_data_done_signal.connect(self.show_info)
        self.refresh_pushButton.clicked.connect(self.init_data)
        self.add_achievement_pushButton.clicked.connect(self.add_achievement)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)
        self.init_ui()
        self.init_data()

    def init_ui(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def generate_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        menu = QMenu()
        edit_action = QAction('编辑成就')
        edit_action.setIcon(EDIT_ICON)
        menu.addAction(edit_action)
        delete_action = QAction('删除成就')
        delete_action.setIcon(DELETE_ICON)
        menu.addAction(delete_action)
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == edit_action:
            # 建议自行实现 EditAchievementWindow（类似AddLogWindow），可传成就ID
            msg_box(self, '提示', '请实现成就编辑窗口')
        if action == delete_action:
            reply = QMessageBox.warning(self, '消息', '确定删除该成就吗?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                db = DBHelp()
                db.delete(table='achievement', key_col='id', key_val=self.achievement_id[row_num])
                db.db_commit()
                del db
                self.refresh_pushButton.click()
                msg_box(self, '提示', '删除成就操作成功!')

    def init_data(self):
        th = Thread(target=self.achievement_info_th)
        th.start()

    def achievement_info_th(self):
        db = DBHelp()
        # 管理员看到所有，普通用户只看到自己的
        if self.user_role == '管理员':
            _, res = db.query_all('achievement')
        else:
            _, res = db.query_super('achievement', 'username', self.username)
        self.achievement_id = [item[0] for item in res]
        self.init_data_done_signal.emit(res)
        del db

    def show_info(self, infos):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)
        for info in infos:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            # 假定info = [id, username, title, category, score, feelings, achieve_date, record_time]
            # 列顺序可调整成你UI对应的
            col_map = [2, 3, 4, 5, 6, 7, 1]  # 名称、类别、分数、感想、达成日期、记录时间、用户名
            for j, idx in enumerate(col_map):
                item = QTableWidgetItem(str(info[idx]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, item)

    def add_achievement(self):
        self.add_win = AddLogWindow('achievement', self.username)
        self.add_win.add_log_done_signal.connect(self.init_data)
        self.add_win.show()
