# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xbot_qt.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1439, 900)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 811, 891))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 310, 581, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(14, 51, 121, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(14, 87, 121, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(14, 123, 121, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(14, 159, 121, 30))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(371, 51, 39, 22))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(371, 90, 54, 22))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(371, 120, 19, 30))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(371, 160, 19, 30))
        self.label_12.setObjectName("label_12")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 50, 202, 140))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_linear_x = QtWidgets.QLabel(self.layoutWidget)
        self.l_linear_x.setMinimumSize(QtCore.QSize(200, 30))
        self.l_linear_x.setAutoFillBackground(True)
        self.l_linear_x.setText("")
        self.l_linear_x.setObjectName("l_linear_x")
        self.verticalLayout_5.addWidget(self.l_linear_x)
        self.l_angular_z = QtWidgets.QLabel(self.layoutWidget)
        self.l_angular_z.setMinimumSize(QtCore.QSize(200, 30))
        self.l_angular_z.setAutoFillBackground(True)
        self.l_angular_z.setText("")
        self.l_angular_z.setObjectName("l_angular_z")
        self.verticalLayout_5.addWidget(self.l_angular_z)
        self.l_left_encoder = QtWidgets.QLabel(self.layoutWidget)
        self.l_left_encoder.setMinimumSize(QtCore.QSize(200, 30))
        self.l_left_encoder.setAutoFillBackground(True)
        self.l_left_encoder.setText("")
        self.l_left_encoder.setObjectName("l_left_encoder")
        self.verticalLayout_5.addWidget(self.l_left_encoder)
        self.l_right_encoder = QtWidgets.QLabel(self.layoutWidget)
        self.l_right_encoder.setMinimumSize(QtCore.QSize(200, 30))
        self.l_right_encoder.setAutoFillBackground(True)
        self.l_right_encoder.setText("")
        self.l_right_encoder.setObjectName("l_right_encoder")
        self.verticalLayout_5.addWidget(self.l_right_encoder)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 40, 581, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(13, 88, 141, 30))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(13, 124, 141, 30))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(13, 160, 141, 30))
        self.label_16.setObjectName("label_16")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(384, 54, 81, 30))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(384, 90, 71, 30))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(384, 126, 71, 30))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(15, 196, 101, 30))
        self.label_24.setObjectName("label_24")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 51, 202, 176))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.l_power = QtWidgets.QLabel(self.layoutWidget1)
        self.l_power.setMinimumSize(QtCore.QSize(200, 30))
        self.l_power.setAutoFillBackground(True)
        self.l_power.setText("")
        self.l_power.setObjectName("l_power")
        self.verticalLayout_2.addWidget(self.l_power)
        self.l_yaw_degree = QtWidgets.QLabel(self.layoutWidget1)
        self.l_yaw_degree.setMinimumSize(QtCore.QSize(200, 30))
        self.l_yaw_degree.setAutoFillBackground(True)
        self.l_yaw_degree.setText("")
        self.l_yaw_degree.setObjectName("l_yaw_degree")
        self.verticalLayout_2.addWidget(self.l_yaw_degree)
        self.l_pitch_degree = QtWidgets.QLabel(self.layoutWidget1)
        self.l_pitch_degree.setMinimumSize(QtCore.QSize(200, 30))
        self.l_pitch_degree.setAutoFillBackground(True)
        self.l_pitch_degree.setText("")
        self.l_pitch_degree.setObjectName("l_pitch_degree")
        self.verticalLayout_2.addWidget(self.l_pitch_degree)
        self.l_switch_state = QtWidgets.QLabel(self.layoutWidget1)
        self.l_switch_state.setMinimumSize(QtCore.QSize(200, 30))
        self.l_switch_state.setAutoFillBackground(True)
        self.l_switch_state.setText("")
        self.l_switch_state.setObjectName("l_switch_state")
        self.verticalLayout_2.addWidget(self.l_switch_state)
        self.l_mute_state = QtWidgets.QLabel(self.layoutWidget1)
        self.l_mute_state.setMinimumSize(QtCore.QSize(200, 30))
        self.l_mute_state.setAutoFillBackground(True)
        self.l_mute_state.setText("")
        self.l_mute_state.setObjectName("l_mute_state")
        self.verticalLayout_2.addWidget(self.l_mute_state)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 52, 141, 30))
        self.label_13.setMinimumSize(QtCore.QSize(130, 30))
        self.label_13.setObjectName("label_13")
        self.layoutWidget.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_13.raise_()
        self.label_24.raise_()
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 580, 801, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_49 = QtWidgets.QLabel(self.groupBox_7)
        self.label_49.setGeometry(QtCore.QRect(16, 52, 101, 30))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_7)
        self.label_50.setGeometry(QtCore.QRect(16, 88, 101, 30))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_7)
        self.label_51.setGeometry(QtCore.QRect(16, 124, 101, 30))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.groupBox_7)
        self.label_52.setGeometry(QtCore.QRect(411, 51, 131, 30))
        self.label_52.setObjectName("label_52")
        self.label_57 = QtWidgets.QLabel(self.groupBox_7)
        self.label_57.setGeometry(QtCore.QRect(341, 51, 41, 30))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_7)
        self.label_58.setGeometry(QtCore.QRect(341, 87, 51, 30))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_7)
        self.label_59.setGeometry(QtCore.QRect(341, 123, 51, 30))
        self.label_59.setObjectName("label_59")
        self.label_53 = QtWidgets.QLabel(self.groupBox_7)
        self.label_53.setGeometry(QtCore.QRect(10, 181, 121, 30))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_7)
        self.label_54.setGeometry(QtCore.QRect(9, 217, 121, 30))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_7)
        self.label_55.setGeometry(QtCore.QRect(9, 253, 121, 30))
        self.label_55.setObjectName("label_55")
        self.line = QtWidgets.QFrame(self.groupBox_7)
        self.line.setGeometry(QtCore.QRect(390, 40, 20, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_7)
        self.line_2.setGeometry(QtCore.QRect(10, 160, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_56 = QtWidgets.QLabel(self.groupBox_7)
        self.label_56.setGeometry(QtCore.QRect(411, 87, 131, 30))
        self.label_56.setObjectName("label_56")
        self.label_60 = QtWidgets.QLabel(self.groupBox_7)
        self.label_60.setGeometry(QtCore.QRect(411, 123, 131, 30))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.groupBox_7)
        self.label_61.setGeometry(QtCore.QRect(340, 180, 61, 30))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.groupBox_7)
        self.label_62.setGeometry(QtCore.QRect(340, 220, 61, 30))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_7)
        self.label_63.setGeometry(QtCore.QRect(340, 250, 61, 30))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.groupBox_7)
        self.label_64.setGeometry(QtCore.QRect(411, 181, 131, 30))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.groupBox_7)
        self.label_65.setGeometry(QtCore.QRect(411, 217, 131, 30))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.groupBox_7)
        self.label_66.setGeometry(QtCore.QRect(411, 253, 151, 30))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.groupBox_7)
        self.label_67.setGeometry(QtCore.QRect(740, 180, 61, 30))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_7)
        self.label_68.setGeometry(QtCore.QRect(740, 220, 61, 30))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_7)
        self.label_69.setGeometry(QtCore.QRect(740, 250, 61, 30))
        self.label_69.setObjectName("label_69")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget2.setGeometry(QtCore.QRect(130, 50, 202, 104))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.l_yaw = QtWidgets.QLabel(self.layoutWidget2)
        self.l_yaw.setMinimumSize(QtCore.QSize(200, 30))
        self.l_yaw.setAutoFillBackground(True)
        self.l_yaw.setText("")
        self.l_yaw.setObjectName("l_yaw")
        self.verticalLayout_7.addWidget(self.l_yaw)
        self.l_pitch = QtWidgets.QLabel(self.layoutWidget2)
        self.l_pitch.setMinimumSize(QtCore.QSize(200, 30))
        self.l_pitch.setAutoFillBackground(True)
        self.l_pitch.setText("")
        self.l_pitch.setObjectName("l_pitch")
        self.verticalLayout_7.addWidget(self.l_pitch)
        self.l_roll = QtWidgets.QLabel(self.layoutWidget2)
        self.l_roll.setMinimumSize(QtCore.QSize(200, 30))
        self.l_roll.setAutoFillBackground(True)
        self.l_roll.setText("")
        self.l_roll.setObjectName("l_roll")
        self.verticalLayout_7.addWidget(self.l_roll)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget3.setGeometry(QtCore.QRect(130, 180, 202, 104))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.l_acc_x = QtWidgets.QLabel(self.layoutWidget3)
        self.l_acc_x.setMinimumSize(QtCore.QSize(200, 30))
        self.l_acc_x.setAutoFillBackground(True)
        self.l_acc_x.setText("")
        self.l_acc_x.setObjectName("l_acc_x")
        self.verticalLayout_12.addWidget(self.l_acc_x)
        self.l_acc_y = QtWidgets.QLabel(self.layoutWidget3)
        self.l_acc_y.setMinimumSize(QtCore.QSize(200, 30))
        self.l_acc_y.setAutoFillBackground(True)
        self.l_acc_y.setText("")
        self.l_acc_y.setObjectName("l_acc_y")
        self.verticalLayout_12.addWidget(self.l_acc_y)
        self.l_acc_z = QtWidgets.QLabel(self.layoutWidget3)
        self.l_acc_z.setMinimumSize(QtCore.QSize(200, 30))
        self.l_acc_z.setAutoFillBackground(True)
        self.l_acc_z.setText("")
        self.l_acc_z.setObjectName("l_acc_z")
        self.verticalLayout_12.addWidget(self.l_acc_z)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget4.setGeometry(QtCore.QRect(530, 180, 202, 104))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.l_w_x = QtWidgets.QLabel(self.layoutWidget4)
        self.l_w_x.setMinimumSize(QtCore.QSize(200, 30))
        self.l_w_x.setAutoFillBackground(True)
        self.l_w_x.setText("")
        self.l_w_x.setObjectName("l_w_x")
        self.verticalLayout_14.addWidget(self.l_w_x)
        self.l_w_y = QtWidgets.QLabel(self.layoutWidget4)
        self.l_w_y.setMinimumSize(QtCore.QSize(200, 30))
        self.l_w_y.setAutoFillBackground(True)
        self.l_w_y.setText("")
        self.l_w_y.setObjectName("l_w_y")
        self.verticalLayout_14.addWidget(self.l_w_y)
        self.l_w_z = QtWidgets.QLabel(self.layoutWidget4)
        self.l_w_z.setMinimumSize(QtCore.QSize(200, 30))
        self.l_w_z.setAutoFillBackground(True)
        self.l_w_z.setText("")
        self.l_w_z.setObjectName("l_w_z")
        self.verticalLayout_14.addWidget(self.l_w_z)
        self.widget = QtWidgets.QWidget(self.groupBox_7)
        self.widget.setGeometry(QtCore.QRect(530, 50, 202, 104))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_mag_x = QtWidgets.QLabel(self.widget)
        self.l_mag_x.setMinimumSize(QtCore.QSize(200, 30))
        self.l_mag_x.setAutoFillBackground(True)
        self.l_mag_x.setText("")
        self.l_mag_x.setObjectName("l_mag_x")
        self.verticalLayout.addWidget(self.l_mag_x)
        self.l_mag_y = QtWidgets.QLabel(self.widget)
        self.l_mag_y.setMinimumSize(QtCore.QSize(200, 30))
        self.l_mag_y.setAutoFillBackground(True)
        self.l_mag_y.setText("")
        self.l_mag_y.setObjectName("l_mag_y")
        self.verticalLayout.addWidget(self.l_mag_y)
        self.l_mag_z = QtWidgets.QLabel(self.widget)
        self.l_mag_z.setMinimumSize(QtCore.QSize(200, 30))
        self.l_mag_z.setAutoFillBackground(True)
        self.l_mag_z.setText("")
        self.l_mag_z.setObjectName("l_mag_z")
        self.verticalLayout.addWidget(self.l_mag_z)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 30, 811, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setGeometry(QtCore.QRect(0, 300, 811, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(0, 570, 811, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(830, 0, 591, 891))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 310, 581, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(330, 170, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 90, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 250, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 170, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 170, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_25 = QtWidgets.QLabel(self.groupBox_5)
        self.label_25.setGeometry(QtCore.QRect(10, 40, 131, 31))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        self.label_26.setGeometry(QtCore.QRect(10, 260, 131, 31))
        self.label_26.setObjectName("label_26")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 80, 131, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 300, 131, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.line_8 = QtWidgets.QFrame(self.groupBox_5)
        self.line_8.setGeometry(QtCore.QRect(0, -10, 581, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 310, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 40, 581, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider.setGeometry(QtCore.QRect(180, 50, 381, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(180, 170, 381, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setGeometry(QtCore.QRect(190, 70, 171, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 200, 171, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_37 = QtWidgets.QLabel(self.groupBox_6)
        self.label_37.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_6)
        self.label_38.setGeometry(QtCore.QRect(10, 170, 111, 21))
        self.label_38.setObjectName("label_38")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 680, 581, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton.setGeometry(QtCore.QRect(40, 100, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 100, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 100, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_4.setGeometry(QtCore.QRect(400, 100, 100, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.line_11 = QtWidgets.QFrame(self.groupBox_8)
        self.line_11.setGeometry(QtCore.QRect(0, -10, 581, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_7 = QtWidgets.QFrame(self.groupBox_4)
        self.line_7.setGeometry(QtCore.QRect(0, 30, 581, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(810, 10, 16, 881))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "状态显示"))
        self.groupBox_2.setTitle(_translate("Dialog", "速度监控"))
        self.label.setText(_translate("Dialog", "实时线速度："))
        self.label_2.setText(_translate("Dialog", "实时角速度："))
        self.label_3.setText(_translate("Dialog", "左轮码盘数："))
        self.label_4.setText(_translate("Dialog", "右轮码盘数："))
        self.label_9.setText(_translate("Dialog", "m/s"))
        self.label_10.setText(_translate("Dialog", "rad/s"))
        self.label_11.setText(_translate("Dialog", "码"))
        self.label_12.setText(_translate("Dialog", "码"))
        self.groupBox_3.setTitle(_translate("Dialog", "状态监控："))
        self.label_14.setText(_translate("Dialog", "水平舵机角度："))
        self.label_15.setText(_translate("Dialog", "竖直舵机角度："))
        self.label_16.setText(_translate("Dialog", "急停开关状态："))
        self.label_21.setText(_translate("Dialog", "％"))
        self.label_22.setText(_translate("Dialog", "度"))
        self.label_23.setText(_translate("Dialog", "度"))
        self.label_24.setText(_translate("Dialog", "静音状态："))
        self.label_13.setText(_translate("Dialog", "当前电量："))
        self.groupBox_7.setTitle(_translate("Dialog", "九轴陀螺仪数据"))
        self.label_49.setText(_translate("Dialog", "水平角度："))
        self.label_50.setText(_translate("Dialog", "俯仰角度："))
        self.label_51.setText(_translate("Dialog", "偏航角度："))
        self.label_52.setText(_translate("Dialog", "X轴磁力计："))
        self.label_57.setText(_translate("Dialog", "度"))
        self.label_58.setText(_translate("Dialog", "度"))
        self.label_59.setText(_translate("Dialog", "度"))
        self.label_53.setText(_translate("Dialog", "X轴加速度："))
        self.label_54.setText(_translate("Dialog", "Y轴加速度："))
        self.label_55.setText(_translate("Dialog", "Z轴加速度："))
        self.label_56.setText(_translate("Dialog", "Y轴磁力计："))
        self.label_60.setText(_translate("Dialog", "Z轴磁力计："))
        self.label_61.setText(_translate("Dialog", "m/s2"))
        self.label_62.setText(_translate("Dialog", "m/s2"))
        self.label_63.setText(_translate("Dialog", "m/s2"))
        self.label_64.setText(_translate("Dialog", "X轴角速度："))
        self.label_65.setText(_translate("Dialog", "Y轴角速度："))
        self.label_66.setText(_translate("Dialog", "Z轴角速度："))
        self.label_67.setText(_translate("Dialog", "rad/s"))
        self.label_68.setText(_translate("Dialog", "rad/s"))
        self.label_69.setText(_translate("Dialog", "rad/s"))
        self.groupBox_4.setTitle(_translate("Dialog", "控制面板"))
        self.groupBox_5.setTitle(_translate("Dialog", "速度控制"))
        self.pushButton.setText(_translate("Dialog", "停止"))
        self.pushButton_2.setText(_translate("Dialog", "前进"))
        self.pushButton_5.setText(_translate("Dialog", "后退"))
        self.pushButton_6.setText(_translate("Dialog", "左转"))
        self.pushButton_7.setText(_translate("Dialog", "右转"))
        self.label_25.setText(_translate("Dialog", "线速度设置："))
        self.label_26.setText(_translate("Dialog", "角速度设置："))
        self.pushButton_4.setText(_translate("Dialog", "持续运动"))
        self.groupBox_6.setTitle(_translate("Dialog", "舵机控制"))
        self.label_37.setText(_translate("Dialog", "水平舵机"))
        self.label_38.setText(_translate("Dialog", "竖直舵机"))
        self.groupBox_8.setTitle(_translate("Dialog", "状态灯控制"))
        self.radioButton.setText(_translate("Dialog", "Led1"))
        self.radioButton_2.setText(_translate("Dialog", "Led2"))
        self.radioButton_3.setText(_translate("Dialog", "Led3"))
        self.radioButton_4.setText(_translate("Dialog", "Led4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

