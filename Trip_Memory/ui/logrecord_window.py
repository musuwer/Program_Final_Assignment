# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logrecord_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(644, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_comboBox = QtWidgets.QComboBox(Form)
        self.search_comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_comboBox.setStyleSheet("font: 12pt \"宋体\";")
        self.search_comboBox.setObjectName("search_comboBox")
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.search_comboBox)
        self.book_search_content_lineEdit = QtWidgets.QLineEdit(Form)
        self.book_search_content_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.book_search_content_lineEdit.setObjectName("book_search_content_lineEdit")
        self.horizontalLayout.addWidget(self.book_search_content_lineEdit)
        self.search_book_pushButton = QtWidgets.QPushButton(Form)
        self.search_book_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.search_book_pushButton.setObjectName("search_book_pushButton")
        self.horizontalLayout.addWidget(self.search_book_pushButton)
        self.add_book_pushButton = QtWidgets.QPushButton(Form)
        self.add_book_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.add_book_pushButton.setObjectName("add_book_pushButton")
        self.horizontalLayout.addWidget(self.add_book_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(Form)
        self.refresh_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.book_total_label = QtWidgets.QLabel(Form)
        self.book_total_label.setStyleSheet("font: 12pt \"宋体\";")
        self.book_total_label.setObjectName("book_total_label")
        self.verticalLayout.addWidget(self.book_total_label)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 2))
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
        self.search_comboBox.setItemText(0, _translate("Form", "名称"))
        self.search_comboBox.setItemText(1, _translate("Form", "类型"))
        self.search_comboBox.setItemText(2, _translate("Form", "地点"))
        self.search_book_pushButton.setText(_translate("Form", "搜索"))
        self.add_book_pushButton.setText(_translate("Form", "添加事件"))
        self.refresh_pushButton.setText(_translate("Form", "刷新"))
        self.book_total_label.setText(_translate("Form", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "地点"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "内容"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "影响"))
