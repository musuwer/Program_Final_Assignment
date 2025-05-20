# -*- coding: utf-8 -*-
"""
该文件由PyQt5 UI代码生成器自动生成，对应UI文件为'book_borrow_info_window.ui'
功能：图书借阅信息管理窗口，支持搜索、查看借阅记录
警告：手动修改此文件可能导致界面功能异常，建议通过Qt Designer调整.ui文件
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        """
        初始化图书借阅信息窗口的界面布局
        """
        # 设置窗口基本属性
        Form.setObjectName("Form")
        Form.resize(827, 452)  # 设置窗口大小

        # 创建网格布局（整个窗口使用）
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # 设置边距为0
        self.gridLayout.setObjectName("gridLayout")

        # 创建垂直布局（包含搜索区域和表格）
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # -------------------- 搜索区域布局 --------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 创建搜索类型下拉框
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setStyleSheet("font: 12pt \"宋体\";")  # 设置字体为12pt宋体
        self.comboBox.setObjectName("comboBox")
        # 添加搜索类型选项
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)

        # 创建搜索输入框
        self.borrow_user_search_lineEdit = QtWidgets.QLineEdit(Form)
        self.borrow_user_search_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.borrow_user_search_lineEdit.setObjectName("borrow_user_search_lineEdit")
        self.horizontalLayout.addWidget(self.borrow_user_search_lineEdit)

        # 创建搜索按钮
        self.search_borrow_user_pushButton = QtWidgets.QPushButton(Form)
        self.search_borrow_user_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.search_borrow_user_pushButton.setObjectName("search_borrow_user_pushButton")
        self.horizontalLayout.addWidget(self.search_borrow_user_pushButton)

        # 创建刷新按钮
        self.refresh_pushButton = QtWidgets.QPushButton(Form)
        self.refresh_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)

        # 将搜索区域布局添加到垂直布局
        self.verticalLayout.addLayout(self.horizontalLayout)

        # -------------------- 表格区域 --------------------
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("font: 12pt \"宋体\";")  # 设置表格字体
        self.tableWidget.setObjectName("tableWidget")

        # 设置表格列数为8
        self.tableWidget.setColumnCount(8)
        # 初始行数为0（数据将在运行时动态加载）
        self.tableWidget.setRowCount(0)

        # 设置表格列标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        # 将表格添加到垂直布局
        self.verticalLayout.addWidget(self.tableWidget)

        # 将垂直布局添加到网格布局
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # 设置界面文本并连接信号槽
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        设置界面文本（支持多语言翻译）
        """
        _translate = QtCore.QCoreApplication.translate

        # 设置窗口标题（需在业务代码中修改为实际标题）
        Form.setWindowTitle(_translate("Form", "图书借阅信息"))

        # 设置下拉框选项文本
        self.comboBox.setItemText(0, _translate("Form", "用户"))
        self.comboBox.setItemText(1, _translate("Form", "书名"))
        self.comboBox.setItemText(2, _translate("Form", "出版社"))

        # 设置按钮文本
        self.search_borrow_user_pushButton.setText(_translate("Form", "搜索"))
        self.refresh_pushButton.setText(_translate("Form", "刷新"))

        # 设置表格列标题文本
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "借阅人"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书名"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出版社"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "出版日期"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "借出数量"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "借出日期"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "应还日期"))

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "借还状态"))