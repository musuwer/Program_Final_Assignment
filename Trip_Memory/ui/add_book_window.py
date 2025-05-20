# -*- coding: utf-8 -*-
"""
该文件由PyQt5 UI代码生成器自动生成，对应UI文件为'add_book_window.ui'
警告：手动修改此文件可能导致生成的界面功能异常，所有修改将在重新生成UI时丢失
"""

# 导入PyQt5核心模块
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        """
        初始化添加书籍窗口的UI界面
        """
        # 设置窗口基本属性
        Form.setObjectName("Form")
        Form.resize(286, 263)  # 设置窗口大小

        # 创建网格布局管理器，用于管理窗口内的所有控件
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        # -------------------- 书名输入区域 --------------------
        # 创建水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 创建"书名"标签，设置最小宽度和字体样式
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(72, 0))
        self.label.setStyleSheet("font: 12pt \"宋体\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # 创建书名输入框，设置字体样式
        self.book_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.book_name_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.book_name_lineEdit.setObjectName("book_name_lineEdit")
        self.horizontalLayout.addWidget(self.book_name_lineEdit)

        # 将水平布局添加到网格布局的第0行第0列
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # -------------------- 作者输入区域 --------------------
        # 创建水平布局
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # 创建"作者"标签，设置最小宽度和字体样式
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(72, 0))
        self.label_2.setStyleSheet("font: 12pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        # 创建作者输入框，设置字体样式
        self.author_lineEdit = QtWidgets.QLineEdit(Form)
        self.author_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.author_lineEdit.setObjectName("author_lineEdit")
        self.horizontalLayout_2.addWidget(self.author_lineEdit)

        # 将水平布局添加到网格布局的第1行第0列
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        # -------------------- 出版社输入区域 --------------------
        # 创建水平布局
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 创建"出版社"标签，设置最小宽度和字体样式
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(72, 0))
        self.label_3.setStyleSheet("font: 12pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        # 创建出版社输入框，设置字体样式
        self.publish_company_lineEdit = QtWidgets.QLineEdit(Form)
        self.publish_company_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.publish_company_lineEdit.setObjectName("publish_company_lineEdit")
        self.horizontalLayout_3.addWidget(self.publish_company_lineEdit)

        # 将水平布局添加到网格布局的第2行第0列
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        # -------------------- 出版日期输入区域 --------------------
        # 创建水平布局
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # 创建"出版日期"标签，设置字体样式
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("font: 12pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        # 创建出版日期输入框，设置字体样式
        self.publish_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.publish_date_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.publish_date_lineEdit.setObjectName("publish_date_lineEdit")
        self.horizontalLayout_4.addWidget(self.publish_date_lineEdit)

        # 将水平布局添加到网格布局的第3行第0列
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        # -------------------- 库存数量输入区域 --------------------
        # 创建水平布局
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # 创建"库存数量"标签，设置字体样式
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("font: 12pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)

        # 创建库存数量输入框，设置字体样式
        self.store_num_lineEdit = QtWidgets.QLineEdit(Form)
        self.store_num_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.store_num_lineEdit.setObjectName("store_num_lineEdit")
        self.horizontalLayout_5.addWidget(self.store_num_lineEdit)

        # 将水平布局添加到网格布局的第4行第0列
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        # -------------------- 添加按钮区域 --------------------
        # 创建水平布局
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # 添加一个伸缩项，用于将按钮推到右侧
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)

        # 创建"添加"按钮，设置字体样式
        self.add_book_pushButton = QtWidgets.QPushButton(Form)
        self.add_book_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.add_book_pushButton.setObjectName("add_book_pushButton")
        self.horizontalLayout_6.addWidget(self.add_book_pushButton)

        # 将水平布局添加到网格布局的第5行第0列
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        # 设置窗口标题和控件文本
        self.retranslateUi(Form)

        # 自动连接信号和槽（基于对象名称）
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        设置窗口和控件的显示文本，支持国际化翻译
        """
        _translate = QtCore.QCoreApplication.translate

        # 设置窗口标题
        Form.setWindowTitle(_translate("Form", "添加书籍"))

        # 设置各个标签的文本
        self.label.setText(_translate("Form", "书    名:"))
        self.label_2.setText(_translate("Form", "作    者:"))
        self.label_3.setText(_translate("Form", "出 版 社:"))
        self.label_4.setText(_translate("Form", "出版日期:"))
        self.label_5.setText(_translate("Form", "库存数量:"))

        # 设置按钮文本
        self.add_book_pushButton.setText(_translate("Form", "添加"))