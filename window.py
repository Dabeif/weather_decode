# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import data
import utils
from form import Ui_Form


class MainForm(QtWidgets.QWidget, Ui_Form):
    date = '0101'
    hour = '00'
    station = ''

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

    def showResult(self):
        if self.station == '':
            QMessageBox.information(self, '提示', '请先输入台站号')
        elif len(self.station) != 5 or not self.station.isdigit():
            QMessageBox.information(self, '提示', '请输入正确的台站号')
        else:
            self.textEdit.setPlainText('')
            filepath = data.BASE_DIR + f'AAXX{self.date}.T{self.hour}'
            ans = utils.search(filepath, self.station)
            if ans == data.FILE_NOT_FOUND:
                QMessageBox.information(self, '提示', '文件未找到')
            elif ans == data.STATION_NOT_FOUND:
                QMessageBox.information(self, '提示', '无此台站号')
            elif ans == data.NOT_GROUND_MSG:
                QMessageBox.information(self, '提示', '不是地面报文资料')
            elif ans == data.TRANSLATE_ERROR:
                QMessageBox.information(self, '提示', '译码出错')
            else:
                self.label_2.setText(filepath)
                self.textEdit.setPlainText(ans)

    def updateDate(self):
        date = self.dateEdit.text()
        tmp = date.split('/')
        self.date = '{:02}{:02}'.format(int(tmp[1]), int(tmp[2]))

    def updateTime(self):
        t = self.comboBox.currentText()
        self.hour = '{:02}'.format(int(t))

    def updateStation(self):
        self.station = self.lineEdit.text()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
