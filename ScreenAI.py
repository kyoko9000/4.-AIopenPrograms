# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenai.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tom_Chat = QtWidgets.QLabel(self.centralwidget)
        self.Tom_Chat.setGeometry(QtCore.QRect(90, 150, 561, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Tom_Chat.setFont(font)
        self.Tom_Chat.setFrameShape(QtWidgets.QFrame.Box)
        self.Tom_Chat.setObjectName("Tom_Chat")
        self.Me_Chat = QtWidgets.QLabel(self.centralwidget)
        self.Me_Chat.setGeometry(QtCore.QRect(90, 360, 561, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Me_Chat.setFont(font)
        self.Me_Chat.setFrameShape(QtWidgets.QFrame.Box)
        self.Me_Chat.setObjectName("Me_Chat")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(160, 520, 75, 23))
        self.Start_Button.setObjectName("Start_Button")
        self.Stop_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_Button.setGeometry(QtCore.QRect(460, 520, 75, 23))
        self.Stop_Button.setObjectName("Stop_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.On_off_screen = QtWidgets.QLabel(self.centralwidget)
        self.On_off_screen.setGeometry(QtCore.QRect(106, 19, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.On_off_screen.setFont(font)
        self.On_off_screen.setFrameShape(QtWidgets.QFrame.Box)
        self.On_off_screen.setLineWidth(4)
        self.On_off_screen.setObjectName("On_off_screen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tom_Chat.setText(_translate("MainWindow", "......."))
        self.Me_Chat.setText(_translate("MainWindow", "......."))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Stop_Button.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Tom"))
        self.label_2.setText(_translate("MainWindow", "Me"))
        self.On_off_screen.setText(_translate("MainWindow", "nothing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())