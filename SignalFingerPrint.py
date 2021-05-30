# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'songRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi


class Ui_MainWindow( QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Song1_FileName = QtWidgets.QLineEdit(self.centralwidget)
        self.Song1_FileName.setGeometry(QtCore.QRect(10, 30, 251, 20))
        self.Song1_FileName.setObjectName("Song1_FileName")
        self.Song1_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Song1_Browse.setGeometry(QtCore.QRect(280, 30, 101, 23))
        self.Song1_Browse.setObjectName("Song1_Browse")
        self.Song2_FileName = QtWidgets.QLineEdit(self.centralwidget)
        self.Song2_FileName.setGeometry(QtCore.QRect(10, 70, 251, 20))
        self.Song2_FileName.setObjectName("Song2_FileName")
        self.Song2_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Song2_Browse.setGeometry(QtCore.QRect(280, 70, 101, 23))
        self.Song2_Browse.setObjectName("Song2_Browse")
        self.Song2_Percentage = QtWidgets.QSlider(self.centralwidget)
        self.Song2_Percentage.setGeometry(QtCore.QRect(490, 70, 181, 22))
        self.Song2_Percentage.setOrientation(QtCore.Qt.Horizontal)
        self.Song2_Percentage.setObjectName("Song2_Percentage")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 130, 401, 201))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidget.verticalHeader().setVisible(True)
        self.Mix_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Mix_Button.setGeometry(QtCore.QRect(540, 100, 75, 23))
        self.Mix_Button.setObjectName("Mix_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Song1_Browse.clicked.connect(lambda:self.browsefiles(self.Song1_Browse))
        self.Song2_Browse.clicked.connect(lambda:self.browsefiles(self.Song2_Browse))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def browsefiles(self,button):
        fname=QFileDialog.getOpenFileName(self, 'Open file','C:/')
        if button==self.Song1_Browse:
            self.Song1_FileName.setText(fname[0])
        else:
            self.Song2_FileName.setText(fname[0])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Song1_Browse.setText(_translate("MainWindow", "Song1_Browse"))
        self.Song2_Browse.setText(_translate("MainWindow", "Song2_Browse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "             Song-Name                  Similarity-Index"))
        self.Mix_Button.setText(_translate("MainWindow", "Mix"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

