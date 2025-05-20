# -*- coding: utf-8 -*-
"""
该文件由PyQt5 UI代码生成器自动生成，对应UI文件为'annouce_window.ui'
功能：公告编辑窗口，用于创建或修改系统公告
警告：手动修改此文件可能导致界面功能异常，建议通过Qt Designer调整.ui文件
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        """
        初始化公告编辑窗口的界面布局
        """
        # 设置窗口基本属性
        Form.setObjectName("Form")                  # 设置对象名称（用于信号槽和样式表）
        Form.resize(400, 300)                      # 设置窗口初始大小（宽400px，高300px）
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")  # 设置白色背景

        # ---------------------- 整体布局：网格布局 ---------------------- #
        self.gridLayout = QtWidgets.QGridLayout(Form)  # 创建网格布局管理器
        self.gridLayout.setObjectName("gridLayout")    # 设置布局名称

        # ---------------------- 垂直布局：包含所有子组件 ---------------------- #
        self.verticalLayout = QtWidgets.QVBoxLayout()   # 创建垂直布局（从上到下排列组件）
        self.verticalLayout.setObjectName("verticalLayout")

        # ---------------------- 第一行：公告标题输入区域 ---------------------- #
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()  # 水平布局（标签+输入框）

        # 创建"公告标题"标签
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")         # 设置字体为宋体
        font.setPointSize(12)          # 字体大小12号
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # 标签内容居中对齐
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)   # 将标签添加到水平布局

        # 创建公告标题输入框
        self.annouce_title_lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)          # 输入框字体稍小（11号）
        self.annouce_title_lineEdit.setFont(font)
        self.annouce_title_lineEdit.setObjectName("annouce_title_lineEdit")
        self.horizontalLayout_6.addWidget(self.annouce_title_lineEdit)  # 添加输入框到水平布局

        self.verticalLayout.addLayout(self.horizontalLayout_6)  # 将水平布局添加到垂直布局

        # ---------------------- 第二行：公告内容编辑区域 ---------------------- #
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()  # 水平布局（仅包含文本编辑框）

        # 创建多行文本编辑框（用于输入公告内容）
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)  # 将文本框添加到水平布局

        self.verticalLayout.addLayout(self.horizontalLayout_5)  # 添加到垂直布局

        # ---------------------- 第三行：操作按钮区域 ---------------------- #
        self.horizontalLayout = QtWidgets.QHBoxLayout()  # 水平布局（取消按钮 + 伸缩项 + 发送按钮）

        # 创建"取消"按钮
        self.cancel_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)  # 添加按钮到布局

        # 添加伸缩项（用于将按钮推到右侧）
        spacerItem = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Expanding,  # 水平方向可扩展
            QtWidgets.QSizePolicy.Minimum      # 垂直方向固定大小
        )
        self.horizontalLayout.addItem(spacerItem)

        # 创建"发送"按钮
        self.send_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setObjectName("send_pushButton")
        self.horizontalLayout.addWidget(self.send_pushButton)  # 添加按钮到布局

        self.verticalLayout.addLayout(self.horizontalLayout)  # 添加到垂直布局

        # 将垂直布局添加到网格布局（占据第0行第0列，跨1行1列）
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # 初始化界面文本并连接信号槽
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        设置界面文本（支持多语言翻译）
        使用Qt的翻译系统，可通过.qm文件加载不同语言文本
        """
        _translate = QtCore.QCoreApplication.translate  # 获取翻译函数

        # 设置窗口标题（需在业务代码中修改为实际标题，如"发布公告"）
        Form.setWindowTitle(_translate("Form", "公告编辑"))

        # 设置标签文本
        self.label.setText(_translate("Form", "公告标题"))

        # 设置文本编辑框的占位符提示
        self.textEdit.setPlaceholderText(_translate("Form", "请输入公告内容（支持多行文本）"))

        # 设置按钮文本
        self.cancel_pushButton.setText(_translate("Form", "取消"))
        self.send_pushButton.setText(_translate("Form", "发布"))