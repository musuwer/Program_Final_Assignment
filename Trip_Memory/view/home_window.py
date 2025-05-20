"""
文件名：home_window.py
描述：主页
"""

from threading import Thread
from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox, QMenu, \
    QAction, QLabel
from ui.home_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import SYS_STYLE, msg_box, accept_box, DELETE_ICON, get_uuid, \
    get_current_time, MESSAGE_STATUS_MAP
from view.annoucement_window import AnnouceWindow
import sys
import traceback
import requests
from PyQt5.QtGui import QPixmap


import datetime # 测试卡顿原因

class HomeWindow(Ui_Form, QWidget):
    init_annouce_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None):
        super(HomeWindow, self).__init__()



        self.setupUi(self)
        self.user_role = user_role
        self.add_annou_win = None

        self.init_ui()
        self.get_annouce_info()
        self.annouce_info_id = []

        self.init_annouce_done_signal.connect(self.show_annouce)  # 信号槽,显示公告

        self.add_annou_pushButton.clicked.connect(self.add_annou)
        self.refresh_pushButton.clicked.connect(self.get_annouce_info)

        #主要登录费时间的代码部分：
        # print("系统时间1:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 登录进去系统时间
        # self.show_douban()
        # print("系统时间2:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 登录进去系统时间

    def init_ui(self):
        self.annou_info_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        # self.annou_info_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        # self.annou_info_tableWidget.setColumnWidth(2,100)
        self.annou_info_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.annou_info_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.book_recommend_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.book_recommend_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)#随内容自适应宽度
        self.book_recommend_tableWidget.setColumnWidth(0, 80)

        self.book_recommend_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.annou_info_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)#设置右击菜单
        self.annou_info_tableWidget.customContextMenuRequested.connect(self.generate_menu)  # 关联菜单


        self.add_annou_pushButton.setProperty('class', 'Aqua')
        self.add_annou_pushButton.setMinimumWidth(60)
        self.refresh_pushButton.setVisible(False)
        if self.user_role == '普通用户':
            self.add_annou_pushButton.setVisible(False)


    def show_annouce(self,annouce_info_result):
        """
        将数据显示到页面上
        :param db:
        :param res:
        :return:
        """
        # print('\n33333\n')
        # 先把原来显示的公告信息删除
        for i in range(self.annou_info_tableWidget.rowCount()):
            self.annou_info_tableWidget.removeRow(0)

        count, res = annouce_info_result[0],annouce_info_result[1]

        self.totol_annouce_label.setText('本图书馆共有公告' + str(count) + '条')

        for record in res:
            self.annou_info_tableWidget.insertRow(self.annou_info_tableWidget.rowCount())
            self.annouce_info_id.append(record[0])
            for i in range(1,4):
                item = QTableWidgetItem(str(record[i]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.annou_info_tableWidget.setItem(self.annou_info_tableWidget.rowCount() - 1, i-1, item)

    def generate_menu(self, pos):
        """
        公告列表界面，生成管理员右键删除菜单
        :param pos:
        :return:
        """
        row_num = -1
        for i in self.annou_info_tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return

        # 添加菜单
        menu = QMenu()
        del_action = QAction(u'删除')
        del_action.setIcon(QIcon(DELETE_ICON))
        menu.addAction(del_action)
        action = menu.exec_(self.annou_info_tableWidget.mapToGlobal(pos))

        if action == del_action:
            rep = accept_box(self, '警告', '确定删除该条消息吗?')
            if rep == QMessageBox.Yes:
                db = DBHelp()
                db.delete(table_name='annoucement', column_name='id', condition=self.annouce_info_id[row_num])
                db.db_commit()
                db.instance = None
                del db
                self.refresh_pushButton.click()
                msg_box(self, '提示', '删除消息操作成功!')

    def add_annou(self):
        '''
        添加公告槽函数，跳出窗口
        :return:
        '''
        self.add_annou_win = AnnouceWindow()
        self.add_annou_win.annouce_don_signal.connect(self.add_annou_done)
        self.add_annou_win.show()

    def add_annou_done(self):
        '''
        发公告按钮点击结束,启动刷新按钮
        :return:
        '''
        self.refresh_pushButton.click()

    def get_annouce_info(self):
        '''
        线程，一直监听是否有新的数据
        :return:
        '''
        th = Thread(target=self.annouce_info_th)
        th.start()

    def annouce_info_th(self):
        '''
        获取公告信息，并发出信号
        :return:
        '''
        db = DBHelp()
        count, res = db.query_annouce()

        self.init_annouce_done_signal.emit([count, res])
        # print(res)
        # return count, res

    def douban_info(self):
        '''
        随机获取15本推荐书籍信息，并发出信号
        :return:
        '''
        db = DBHelp()
        count, res = db.query_douban()

        #self.init_annouce_done_signal.emit([count, res])
        # print(res)
        # return count, res

    def show_douban(self):
        """
        将随机取的15本书的数据显示到页面上
        :param db:
        :param res:
        :return:
        """
        # print('\n33333\n')

        # 清空表格中原有数据，确保只显示最新的推荐书籍
        for i in range(self.book_recommend_tableWidget.rowCount()):
            self.book_recommend_tableWidget.removeRow(0)

        # 创建数据库连接，查询豆瓣推荐书籍数据
        db = DBHelp()
        count, res = db.query_douban()

        # 遍历查询结果，将每本书的信息添加到表格中
        for record in res:
            # 在表格末尾插入新行
            self.book_recommend_tableWidget.insertRow(self.book_recommend_tableWidget.rowCount())

            # 获取书籍封面图片URL并下载
            url = str(record[0])
            res = requests.get(url)  # 发送HTTP请求获取图片内容

            # 将图片数据转换为QPixmap格式并设置为表格项的图标
            img = QPixmap()
            img.loadFromData(res.content)
            icon = QIcon(img)

            # 设置第一列为书籍封面图片
            item = QTableWidgetItem()
            item.setIcon(icon)
            self.book_recommend_tableWidget.setItem(self.book_recommend_tableWidget.rowCount() - 1, 0, item)

            # 设置第二列为书籍名称
            item = QTableWidgetItem(str(record[1]))
            self.book_recommend_tableWidget.setItem(self.book_recommend_tableWidget.rowCount() - 1, 1, item)

            # 设置第三列为书籍作者
            item = QTableWidgetItem(str(record[2]))
            self.book_recommend_tableWidget.setItem(self.book_recommend_tableWidget.rowCount() - 1, 2, item)

            # 设置第四列为书籍评分
            item = QTableWidgetItem(str(record[6]))
            self.book_recommend_tableWidget.setItem(self.book_recommend_tableWidget.rowCount() - 1, 3, item)

            # 设置第五列为书籍出版信息
            item = QTableWidgetItem(str(record[8]))
            self.book_recommend_tableWidget.setItem(self.book_recommend_tableWidget.rowCount() - 1, 4, item)





if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        win = HomeWindow('管理员')
        win.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e.args)
        traceback.print_exc()
