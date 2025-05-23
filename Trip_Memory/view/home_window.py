"""
文件名：home_window.py
描述：亿途主页面——包含公告和目标管理，均用SQLite实现
"""
import os
import sys
import sqlite3
import traceback
from threading import Thread
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QApplication, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox,
    QMenu, QAction
)
from ui.home_window import Ui_Form
from util.common_util import SYS_STYLE, msg_box, accept_box, DELETE_ICON, get_uuid, get_current_time
from view.goal_record_window import GoalRecordWindow
from view.annoucement_window import  AnnouceWindow  # 你的弹窗类名可能是annouce_window

#存在bug:点击添加公告的时候卡退


class HomeWindow(Ui_Form, QWidget):
    """
    主页面类，包含目标和公告管理
    """
    def __init__(self, user_role=None):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.add_goal_win = None
        self.add_annou_win = None

        # 初始化UI
        self.init_ui()

        # 初始加载数据
        self.refresh_goal_table()
        self.refresh_annouce_table()

        # 目标表右键菜单
        self.book_recommend_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.book_recommend_tableWidget.customContextMenuRequested.connect(self.generate_goal_menu)
        # 公告表右键菜单
        self.annou_info_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.annou_info_tableWidget.customContextMenuRequested.connect(self.generate_annou_menu)

        # 按钮绑定
        self.add_goal_pushButton.clicked.connect(self.add_goal)
        self.add_annou_pushButton.clicked.connect(self.add_annou)
        self.refresh_pushButton.clicked.connect(self.refresh_annouce_table)
        self.totol_goal_label.setText('')  # 初始目标统计为空
        self.totol_annouce_label.setText('')

        if self.user_role == '普通用户':
            self.add_annou_pushButton.setVisible(False)
            self.add_goal_pushButton.setVisible(True)

    def init_ui(self):
        """初始化表格等UI属性"""
        # 目标表格
        self.book_recommend_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.book_recommend_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.book_recommend_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.book_recommend_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.book_recommend_tableWidget.setColumnCount(5)
        self.book_recommend_tableWidget.setHorizontalHeaderLabels(["名称", "计划", "进度", "成就", "创建时间"])

        # 公告表格
        self.annou_info_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.annou_info_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.annou_info_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.annou_info_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.annou_info_tableWidget.setColumnCount(3)
        self.annou_info_tableWidget.setHorizontalHeaderLabels(["标题", "内容", "时间"])

        self.add_goal_pushButton.setProperty('class', 'Aqua')
        self.add_goal_pushButton.setMinimumWidth(60)
        self.add_annou_pushButton.setProperty('class', 'Aqua')
        self.add_annou_pushButton.setMinimumWidth(60)

    # ---------- 目标表相关 ----------
    def refresh_goal_table(self):
        """刷新目标表格，读取并显示所有目标数据"""
        db_path = os.path.abspath("data.db")
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS goals (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        plan TEXT,
                        progress TEXT,
                        achievement TEXT,
                        create_time TEXT
                    )''')
        c.execute("SELECT id, name, plan, progress, achievement, create_time FROM goals")
        res = c.fetchall()
        conn.close()
        self.book_recommend_tableWidget.setRowCount(0)
        for record in res:
            row = self.book_recommend_tableWidget.rowCount()
            self.book_recommend_tableWidget.insertRow(row)
            for i in range(1, 6):
                item = QTableWidgetItem(str(record[i]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.book_recommend_tableWidget.setItem(row, i - 1, item)
        self.totol_goal_label.setText(f"共{len(res)}个目标")

    def generate_goal_menu(self, pos):
        """目标表格右键菜单，支持删除目标"""
        row_num = -1
        for i in self.book_recommend_tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        menu = QMenu()
        del_action = QAction(u'删除')
        del_action.setIcon(QIcon(DELETE_ICON))
        menu.addAction(del_action)
        action = menu.exec_(self.book_recommend_tableWidget.mapToGlobal(pos))
        if action == del_action:
            rep = accept_box(self, '警告', '确定删除该目标吗?')
            if rep == QMessageBox.Yes:
                # 用名称定位删除（如需唯一性可用id字段）
                goal_name = self.book_recommend_tableWidget.item(row_num, 0).text()
                db_path = os.path.abspath("data.db")
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute("DELETE FROM goals WHERE name = ?", (goal_name,))
                conn.commit()
                conn.close()
                self.refresh_goal_table()
                msg_box(self, '提示', '删除目标成功!')

    def add_goal(self):
        """弹出添加目标窗口"""
        self.add_goal_win = GoalRecordWindow()
        self.add_goal_win.goal_record_signal.connect(self.refresh_goal_table)
        self.add_goal_win.show()

    # ---------- 公告表相关 ----------
    def refresh_annouce_table(self):
        """刷新公告表格"""
        db_path = os.path.abspath("data.db")
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS annoucement (
                        id TEXT PRIMARY KEY,
                        title TEXT,
                        content TEXT,
                        create_time TEXT
                    )''')
        c.execute("SELECT id, title, content, create_time FROM annoucement")
        res = c.fetchall()
        conn.close()
        self.annou_info_tableWidget.setRowCount(0)
        for record in res:
            row = self.annou_info_tableWidget.rowCount()
            self.annou_info_tableWidget.insertRow(row)
            # 列顺序对应：标题、内容、时间
            for i in range(1, 4):
                item = QTableWidgetItem(str(record[i]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.annou_info_tableWidget.setItem(row, i-1, item)
        self.totol_annouce_label.setText(f"亿途共有公告{len(res)}条")

    def generate_annou_menu(self, pos):
        """公告右键删除菜单"""
        row_num = -1
        for i in self.annou_info_tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        menu = QMenu()
        del_action = QAction(u'删除')
        del_action.setIcon(QIcon(DELETE_ICON))
        menu.addAction(del_action)
        action = menu.exec_(self.annou_info_tableWidget.mapToGlobal(pos))
        if action == del_action:
            reply = accept_box(self, '警告', '确定删除该公告吗?')
            if reply == QMessageBox.Yes:
                annou_title = self.annou_info_tableWidget.item(row_num, 0).text()
                db_path = os.path.abspath("data.db")
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute("DELETE FROM annoucement WHERE title = ?", (annou_title,))
                conn.commit()
                conn.close()
                self.refresh_annouce_table()
                msg_box(self, '提示', '删除公告成功!')

    def add_annou(self):
        """弹出公告添加窗口"""
        self.add_annou_win = AnnouceWindow()
        self.add_annou_win.annouce_don_signal.connect(self.refresh_annouce_table)
        self.add_annou_win.show()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        win = HomeWindow('管理员')
        win.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e.args)
        traceback.print_exc()
