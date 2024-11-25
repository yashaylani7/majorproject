# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\v_player.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 561)
        Form.setMinimumSize(QtCore.QSize(690, 560))
        Form.setStyleSheet("background-color: bisque;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_window = QtWidgets.QFrame(Form)
        self.video_window.setMinimumSize(QtCore.QSize(600, 500))
        self.video_window.setStyleSheet("border: 2px solid blue;")
        self.video_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_window.setObjectName("video_window")
        self.verticalLayout.addWidget(self.video_window)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openfile = QtWidgets.QPushButton(Form)
        self.openfile.setObjectName("openfile")
        self.horizontalLayout.addWidget(self.openfile)
        self.playBtn = QtWidgets.QPushButton(Form)
        self.playBtn.setEnabled(False)
        self.playBtn.setFlat(False)
        self.playBtn.setObjectName("playBtn")
        self.horizontalLayout.addWidget(self.playBtn)
        self.volume_Slider = QtWidgets.QSlider(Form)
        self.volume_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_Slider.setObjectName("volume_Slider")
        self.horizontalLayout.addWidget(self.volume_Slider)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(350, 0))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openfile.setText(_translate("Form", "Open File"))
        self.playBtn.setText(_translate("Form", "Play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
