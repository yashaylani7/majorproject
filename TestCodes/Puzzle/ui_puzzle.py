# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'puzzle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_puzzleMainWidget(object):
    def setupUi(self, puzzleMainWidget):
        puzzleMainWidget.setObjectName("puzzleMainWidget")
        puzzleMainWidget.resize(786, 562)
        self.gridLayoutWidget = QtWidgets.QWidget(puzzleMainWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 150, 351, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.container_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.container_1.setStyleSheet(" background-color: #f0f0f0;\n"
"        border: 1px solid #dcdcdc;\n"
"        border-radius: 4px;\n"
"        padding: 4px;\n"
"        margin: 4px;\n"
"        font-size: 20px;\n"
"        font-weight: bold;")
        self.container_1.setText("")
        self.container_1.setObjectName("container_1")
        self.gridLayout.addWidget(self.container_1, 0, 0, 1, 1)
        self.container_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.container_2.setStyleSheet(" background-color: #f0f0f0;\n"
"        border: 1px solid #dcdcdc;\n"
"        border-radius: 4px;\n"
"        padding: 4px;\n"
"        margin: 4px;\n"
"        font-size: 20px;\n"
"        font-weight: bold;")
        self.container_2.setText("")
        self.container_2.setObjectName("container_2")
        self.gridLayout.addWidget(self.container_2, 0, 1, 1, 1)
        self.container_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.container_4.setStyleSheet(" background-color: #f0f0f0;\n"
"        border: 1px solid #dcdcdc;\n"
"        border-radius: 4px;\n"
"        padding: 4px;\n"
"        margin: 4px;\n"
"        font-size: 20px;\n"
"        font-weight: bold;")
        self.container_4.setText("")
        self.container_4.setObjectName("container_4")
        self.gridLayout.addWidget(self.container_4, 1, 1, 1, 1)
        self.container_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.container_3.setStyleSheet(" background-color: #f0f0f0;\n"
"        border: 1px solid #dcdcdc;\n"
"        border-radius: 4px;\n"
"        padding: 4px;\n"
"        margin: 4px;\n"
"        font-size: 20px;\n"
"        font-weight: bold;")
        self.container_3.setText("")
        self.container_3.setObjectName("container_3")
        self.gridLayout.addWidget(self.container_3, 1, 0, 1, 1)

        self.retranslateUi(puzzleMainWidget)
        QtCore.QMetaObject.connectSlotsByName(puzzleMainWidget)

    def retranslateUi(self, puzzleMainWidget):
        _translate = QtCore.QCoreApplication.translate
        puzzleMainWidget.setWindowTitle(_translate("puzzleMainWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    puzzleMainWidget = QtWidgets.QWidget()
    ui = Ui_puzzleMainWidget()
    ui.setupUi(puzzleMainWidget)
    puzzleMainWidget.show()
    sys.exit(app.exec_())
