# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(736, 657)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 260, 641, 341))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 210, 651, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 220, 561, 29))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 220, 81, 29))
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(100, 40, 152, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(270, 40, 51, 31))
        self.comboBox.setToolTip("")
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 160, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 40, 31, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 51, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.dateEdit.dateChanged['QDate'].connect(Form.updateDate)
        self.comboBox.currentTextChanged['QString'].connect(Form.updateTime)
        self.pushButton_2.clicked.connect(Form.showResult)
        self.lineEdit.editingFinished.connect(Form.updateStation)
        self.lineEdit.editingFinished.connect(Form.updateStation)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "地面报文译码"))
        self.label_2.setText(_translate("Form", "无"))
        self.label.setText(_translate("Form", "当前文件："))
        self.comboBox.setCurrentText(_translate("Form", "0"))
        self.comboBox.setItemText(0, _translate("Form", "0"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "6"))
        self.comboBox.setItemText(3, _translate("Form", "8"))
        self.comboBox.setItemText(4, _translate("Form", "12"))
        self.comboBox.setItemText(5, _translate("Form", "14"))
        self.comboBox.setItemText(6, _translate("Form", "18"))
        self.comboBox.setItemText(7, _translate("Form", "20"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.label_3.setText(_translate("Form", "时"))
        self.label_4.setText(_translate("Form", "台站号："))
        self.label_5.setText(_translate("Form", "日期："))