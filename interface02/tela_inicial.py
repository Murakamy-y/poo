# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controleestoque.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 90, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonMainCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMainCadastrar.setGeometry(QtCore.QRect(140, 270, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMainCadastrar.setFont(font)
        self.pushButtonMainCadastrar.setObjectName("pushButtonMainCadastrar")
        self.pushButtonMainBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMainBuscar.setGeometry(QtCore.QRect(500, 270, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMainBuscar.setFont(font)
        self.pushButtonMainBuscar.setObjectName("pushButtonMainBuscar")
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
        self.label.setText(_translate("MainWindow", "Controle de Estoque"))
        self.pushButtonMainCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButtonMainBuscar.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
