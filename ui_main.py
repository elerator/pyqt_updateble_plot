# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(820, 650)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)

        #####-------------horizontalLayout----------#####
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)


        self.btnAdd = QtGui.QPushButton(self.centralwidget) #Button ins centralwidget einfuegen
        self.horizontalLayout.addWidget(self.btnAdd)#Links ausrichten

        #self.btnAdd2 = QtGui.QPushButton(self.centralwidget)
        #self.horizontalLayout.addWidget(self.btnAdd2) #rechts davon

        #self.btnAdd3 = QtGui.QPushButton(self.centralwidget)
        #self.horizontalLayout.addWidget(self.btnAdd3) #rechts davon

        self.chkMore = QtGui.QCheckBox(self.centralwidget)
        self.horizontalLayout.addWidget(self.chkMore)


        ##verticalLayout||||-----horizontalLayout-----||||verticalLayout
        self.verticalLayout.addLayout(self.horizontalLayout) #Ausrichtung horizontal und Vertikal verknüpfen. Alles was im Horizontalen Kasten is kommt oben rein.
        self.grPlot = PlotWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.grPlot) #Der Rest kommt unten rein bzw unten dran. Hier der Plot also...


        #self.grPlot = PlotWidget(self.centralwidget)
        #self.verticalLayout.addWidget(self.grPlot)


        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnAdd.setText(_translate("MainWindow", "update sine wave", None))

        self.chkMore.setText(_translate("MainWindow", "keep updating", None))

from pyqtgraph import PlotWidget
