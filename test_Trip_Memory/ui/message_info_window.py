# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_info_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(725, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"宋体\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sender_search_lineEdit = QtWidgets.QLineEdit(Form)
        self.sender_search_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.sender_search_lineEdit.setObjectName("sender_search_lineEdit")
        self.horizontalLayout.addWidget(self.sender_search_lineEdit)
        self.search_sender_pushButton = QtWidgets.QPushButton(Form)
        self.search_sender_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.search_sender_pushButton.setObjectName("search_sender_pushButton")
        self.horizontalLayout.addWidget(self.search_sender_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(Form)
        self.refresh_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.noreply_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.noreply_pushButton.setFont(font)
        self.noreply_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.noreply_pushButton.setObjectName("noreply_pushButton")
        self.horizontalLayout.addWidget(self.noreply_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.message_total_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.message_total_label.setFont(font)
        self.message_total_label.setStyleSheet("font: 12pt \"宋体\";")
        self.message_total_label.setObjectName("message_total_label")
        self.verticalLayout.addWidget(self.message_total_label)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("font: 12pt \"宋体\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
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
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "发送者："))
        self.search_sender_pushButton.setText(_translate("Form", "搜索"))
        self.refresh_pushButton.setText(_translate("Form", "刷新"))
        self.noreply_pushButton.setText(_translate("Form", "筛选未回复"))
        self.message_total_label.setText(_translate("Form", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "发送者"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "消息"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "发送时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "是否回复"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "回复内容"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "回复时间"))
