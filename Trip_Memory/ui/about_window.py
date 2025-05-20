# -*- coding: utf-8 -*-
"""
该文件由PyQt5 UI代码生成器自动生成，对应UI文件为'about_window.ui'
警告：手动修改此文件可能导致生成的界面功能异常，所有修改将在重新生成UI时丢失
"""

# 导入PyQt5核心模块
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        """
        界面初始化方法，负责创建和布局界面组件

        参数：
        - Form: 主窗口对象，继承自QWidget或QMainWindow
        """
        # 设置主窗口基本属性
        Form.setObjectName("Form")  # 设置对象名称（用于信号槽关联和样式表）
        Form.resize(689, 484)  # 设置窗口初始大小（宽度689，高度484）

        # ---------------------- 创建选项卡部件 ---------------------- #
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 651, 451))  # 设定位置和大小（x=20,y=10,宽651,高451）

        # 配置尺寸策略：允许水平和垂直方向扩展
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tabWidget.setSizePolicy(sizePolicy)

        # 配置字体：宋体，12号字，加粗
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)

        self.tabWidget.setObjectName("tabWidget")  # 设置对象名称

        # ---------------------- 创建"使用帮助"选项卡 ---------------------- #
        self.tab_help = QtWidgets.QWidget()  # 创建选项卡页面容器
        self.tab_help.setObjectName("tab_help")  # 设置对象名称

        # 创建文本编辑框（用于显示帮助内容）
        self.textEdit = QtWidgets.QTextEdit(self.tab_help)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 631, 441))  # 填充整个选项卡页面
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)  # 移除边框
        self.textEdit.setLineWidth(0)  # 边框宽度设为0
        self.textEdit.setReadOnly(True)  # 设置为只读模式
        self.textEdit.setObjectName("textEdit")  # 设置对象名称

        # 将选项卡添加到选项卡部件中
        self.tabWidget.addTab(self.tab_help, "")

        # ---------------------- 创建"版本信息"选项卡 ---------------------- #
        self.tab_about = QtWidgets.QWidget()  # 创建选项卡页面容器
        self.tab_about.setObjectName("tab_about")  # 设置对象名称

        # 创建文本编辑框（用于显示版本和开发者信息）
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_about)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 631, 401))  # 预留底部空间
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)  # 移除边框
        self.textEdit_2.setLineWidth(0)  # 边框宽度设为0
        self.textEdit_2.setObjectName("textEdit_2")  # 设置对象名称

        # 将选项卡添加到选项卡部件中
        self.tabWidget.addTab(self.tab_about, "")

        # ---------------------- 界面初始化收尾操作 ---------------------- #
        self.retranslateUi(Form)  # 执行界面文本翻译
        self.tabWidget.setCurrentIndex(0)  # 默认显示第一个选项卡（使用帮助）
        QtCore.QMetaObject.connectSlotsByName(Form)  # 自动连接信号槽（基于对象名称）

    def retranslateUi(self, Form):
        """
        界面文本翻译方法，用于处理多语言支持
        使用Qt的翻译系统，支持通过.qm文件加载翻译文本
        """
        _translate = QtCore.QCoreApplication.translate  # 获取翻译函数

        # 设置主窗口标题
        Form.setWindowTitle(_translate("Form", "关于"))

        # ---------------------- 设置"使用帮助"文本内容 ---------------------- #
        # 使用HTML格式定义富文本内容，包含：
        # - 功能操作步骤
        # - 常见问题解答
        # - 字体样式：宋体，非加粗（400权重）
        self.textEdit.setHtml(_translate("Form", """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><style>p, li { white-space: pre-wrap; }</style></head>
            <body style="font-family:'宋体'; font-size:12pt; font-weight:400;">
                <h3>一. 使用帮助</h3>
                <p>1. 先进行注册</p>
                <p>2. 注册完毕后，使用自己的账号进行登录</p>
                <p>3. 登陆后，主页会有书籍推荐和公告：
                    <ul>
                        <li>管理员可通过右键菜单添加/删除公告</li>
                        <li>普通用户仅可查看公告</li>
                    </ul>
                </p>
                <p>4. 借阅记录功能：
                    <ul>
                        <li>管理员可查看所有用户借阅记录并催还</li>
                        <li>普通用户仅可查看自己的借阅记录，支持还书/续借</li>
                    </ul>
                </p>
                <p>5. 图书管理：管理员可通过右键菜单对图书进行增删改查</p>
                <p>6. 消息系统：支持用户与管理员互相发送消息</p>

                <h3>二. 常见问题</h3>
                <p>1. 注册失败：可能因账号已存在</p>
                <p>2. 登录失败：可能因用户不存在或密码错误</p>
                <p>3. 添加失败：可能因图书已存在</p>
            </body></html>
        """))

        # 设置选项卡标签文本
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), _translate("Form", "使用帮助"))

        # ---------------------- 设置"版本信息"文本内容 ---------------------- #
        self.textEdit_2.setHtml(_translate("Form", """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><style>p, li { white-space: pre-wrap; }</style></head>
            <body style="font-family:'宋体'; font-size:12pt; font-weight:400;">
                <h3>版本信息</h3>
                <p>1. 版本号：亿途 1.0初版</p>
                <p>2. 开发周期：2021/06/01 - 2021/06/12</p>
                <p>3. 开发者信息：
                    <ul>
                        <li>学校：东莞理工学院</li>
                        <li>学院：学生社区知行学院</li>
                        <li>专业：软件工程</li>
                        <li>班级：2023级杨振宁创新班</li>
                        <li>姓名：柴承源</li>
                        <li>学号：2023414290102</li>
                    </ul>
                </p>
            </body></html>
        """))

        # 设置选项卡标签文本
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), _translate("Form", "版本信息"))