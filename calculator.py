# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):

    def add2Screen(self, op, equal):
        screen_text = self.screen_result.text()

        # Fazer com que o primeiro caractere não seja nenhumas das operações ou o .


        # Fazer com que 0.0 seja substiuíto por 0
        # if op not in ['.', '+', 'x', '/', '-', '=']:
                
        # The operation will replace what is in screen if only if:
        # There is just 0 in screen or
        # There is just ERROR in screen or
        # It's a equal operation 
        # AND
        # The operation not be in ['.', '+', 'x', '/', '-', '=']
        if (screen_text == '0' or screen_text == 'ERROR' or  equal) and op not in ['.', '+', 'x', '/', '-', '=']:
                self.screen_result.setText(op)
        else:
                # Verify if operation is one of these simbols
                if op in ['.', '+', 'x', '/', '-', '=']:
                        # If so, verify is the last character in screen isn't
                        # already one one of these simbols
                        if screen_text[len(screen_text)-1] not in ['.', '+', 'x', '/', '-', '=']:
                                # Just put . if the last character isn't in ['+', 'x', '/', '-', '='] or is '0' or 'ERROR'
                                if (screen_text == '0' or screen_text == 'ERROR') and op not in ['+', 'x', '/', '-', '=']:
                                        self.screen_result.setText(screen_text + op)                          
                                else:
                                        self.screen_result.setText(screen_text + op)
                # If not so, it's a number, so just put it
                else:
                        self.screen_result.setText(screen_text + op)

    def key1(self):
            self.add2Screen('1', False)
    def key2(self):
            self.add2Screen('2', False)
    def key3(self):
            self.add2Screen('3', False)
    def key4(self):
            self.add2Screen('4', False)
    def key5(self):
            self.add2Screen('5', False)
    def key6(self):
            self.add2Screen('6', False)
    def key7(self):
            self.add2Screen('7', False)
    def key8(self):
            self.add2Screen('8', False)
    def key9(self):
            self.add2Screen('9', False)
    def keyBar(self):
            self.add2Screen('/', False)
    def keyMult(self):
            self.add2Screen('x', False)
    def keyMinus(self):
            self.add2Screen('-', False)
    def keyPlus(self):
            self.add2Screen('+', False)
    def keyPoint(self):
            self.add2Screen('.', False)
    def key0(self):
            self.add2Screen('0', False)
    # Diferent
    def keyEqual(self):
            # This function return just integer part of a number
            # or zero, if there is no integer part
            def getJustIteger(nString):
                number = ''
                for i in nString:
                        if i != '.':
                                number += i
                        else:
                                if number == '':
                                        return 0
                                else:
                                        return int(number)

            operation = self.screen_result.text().replace('x', '*')
            try:

                # Convert to float to don't have conflict with
                # function getJustInteger
                result = str(float(eval(operation)))

                # Verfify if this number need to have numbers after
                # point
                if (getJustIteger(result) - float(result) in [0, 0.0]):
                        result = str(getJustIteger(result))
                self.add2Screen(result, True)
            except Exception as e:
                self.add2Screen(f'ERROR', True)
    #     
    # FUNCTIONS WITH KEYS PRESSED
    # 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 501)
        MainWindow.setMinimumSize(QtCore.QSize(400, 501))
        MainWindow.setMaximumSize(QtCore.QSize(400, 501))
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.screen = QtWidgets.QFrame(self.centralwidget)
        self.screen.setEnabled(True)
        self.screen.setMinimumSize(QtCore.QSize(400, 80))
        self.screen.setMaximumSize(QtCore.QSize(400, 80))
        self.screen.setStyleSheet("background-color: rgb(10, 10, 10);")
        self.screen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen.setObjectName("screen")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.screen)
        self.verticalLayout_3.setContentsMargins(13, -1, 13, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.screen_result = QtWidgets.QLabel(self.screen)
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(36)
        self.screen_result.setFont(font)
        self.screen_result.setStyleSheet("color: rgb(180, 180, 180);")
        self.screen_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.screen_result.setObjectName("screen_result")
        self.verticalLayout_3.addWidget(self.screen_result)
        self.verticalLayout.addWidget(self.screen)
        self.screen_numbers = QtWidgets.QFrame(self.centralwidget)
        self.screen_numbers.setMinimumSize(QtCore.QSize(400, 400))
        self.screen_numbers.setMaximumSize(QtCore.QSize(400, 400))
        self.screen_numbers.setStyleSheet("background-color: rgb(10, 10, 10);")
        self.screen_numbers.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.screen_numbers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_numbers.setObjectName("screen_numbers")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.screen_numbers)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.screen_numbers)
        self.line_2.setMinimumSize(QtCore.QSize(400, 100))
        self.line_2.setMaximumSize(QtCore.QSize(400, 100))
        self.line_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.line_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_1 = QtWidgets.QPushButton(self.line_2)
        self.btn_1.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_1.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_7.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.line_2)
        self.btn_2.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_2.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_7.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.line_2)
        self.btn_3.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_3.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_7.addWidget(self.btn_3)
        self.btn_bar = QtWidgets.QPushButton(self.line_2)
        self.btn_bar.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_bar.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_bar.setFont(font)
        self.btn_bar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_bar.setObjectName("btn_bar")
        self.horizontalLayout_7.addWidget(self.btn_bar)
        self.verticalLayout_2.addWidget(self.line_2)
        self.line_4 = QtWidgets.QFrame(self.screen_numbers)
        self.line_4.setMinimumSize(QtCore.QSize(400, 100))
        self.line_4.setMaximumSize(QtCore.QSize(400, 100))
        self.line_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.line_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_4 = QtWidgets.QPushButton(self.line_4)
        self.btn_4.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_4.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_9.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.line_4)
        self.btn_5.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_5.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_9.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.line_4)
        self.btn_6.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_6.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_9.addWidget(self.btn_6)
        self.btn_mult = QtWidgets.QPushButton(self.line_4)
        self.btn_mult.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_mult.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_mult.setObjectName("btn_mult")
        self.horizontalLayout_9.addWidget(self.btn_mult)
        self.verticalLayout_2.addWidget(self.line_4)
        self.line_3 = QtWidgets.QFrame(self.screen_numbers)
        self.line_3.setMinimumSize(QtCore.QSize(400, 100))
        self.line_3.setMaximumSize(QtCore.QSize(400, 100))
        self.line_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.line_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_7 = QtWidgets.QPushButton(self.line_3)
        self.btn_7.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_7.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout_8.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.line_3)
        self.btn_8.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_8.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout_8.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.line_3)
        self.btn_9.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_9.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout_8.addWidget(self.btn_9)
        self.btn_minus = QtWidgets.QPushButton(self.line_3)
        self.btn_minus.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_minus.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_minus.setObjectName("btn_minus")
        self.horizontalLayout_8.addWidget(self.btn_minus)
        self.verticalLayout_2.addWidget(self.line_3)
        self.line_1 = QtWidgets.QFrame(self.screen_numbers)
        self.line_1.setMinimumSize(QtCore.QSize(400, 100))
        self.line_1.setMaximumSize(QtCore.QSize(400, 100))
        self.line_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_1.setObjectName("line_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.line_1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_0 = QtWidgets.QPushButton(self.line_1)
        self.btn_0.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_0.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.horizontalLayout.addWidget(self.btn_0)
        self.btn_point = QtWidgets.QPushButton(self.line_1)
        self.btn_point.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_point.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_point.setFont(font)
        self.btn_point.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_point.setObjectName("btn_point")
        self.horizontalLayout.addWidget(self.btn_point)
        self.btn_equal = QtWidgets.QPushButton(self.line_1)
        self.btn_equal.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_equal.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_equal.setObjectName("btn_equal")
        self.horizontalLayout.addWidget(self.btn_equal)
        self.btn_plus = QtWidgets.QPushButton(self.line_1)
        self.btn_plus.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_plus.setMaximumSize(QtCore.QSize(95, 95))
        font = QtGui.QFont()
        font.setFamily("NFL Jacksonville Jaguars")
        font.setPointSize(20)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(20, 20, 20);\n"
"    color : rgb(100, 100, 100);\n"
"}")
        self.btn_plus.setObjectName("btn_plus")
        self.horizontalLayout.addWidget(self.btn_plus)
        self.verticalLayout_2.addWidget(self.line_1)
        self.verticalLayout.addWidget(self.screen_numbers)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuCreator = QtWidgets.QMenu(self.menuBar)
        self.menuCreator.setObjectName("menuCreator")
        MainWindow.setMenuBar(self.menuBar)
        self.actionMateus_Santos = QtWidgets.QAction(MainWindow)
        self.actionMateus_Santos.setObjectName("actionMateus_Santos")
        self.menuCreator.addAction(self.actionMateus_Santos)
        self.menuBar.addAction(self.menuCreator.menuAction())

        # 
        # FUNCTIONS
        # 

        self.btn_1.clicked.connect(self.key1)
        self.btn_2.clicked.connect(self.key2)
        self.btn_3.clicked.connect(self.key3)
        self.btn_4.clicked.connect(self.key4)
        self.btn_5.clicked.connect(self.key5)
        self.btn_6.clicked.connect(self.key6)
        self.btn_7.clicked.connect(self.key7)
        self.btn_8.clicked.connect(self.key8)
        self.btn_9.clicked.connect(self.key9)
        self.btn_bar.clicked.connect(self.keyBar)
        self.btn_mult.clicked.connect(self.keyMult)
        self.btn_minus.clicked.connect(self.keyMinus)
        self.btn_plus.clicked.connect(self.keyPlus)
        self.btn_point.clicked.connect(self.keyPoint)
        self.btn_0.clicked.connect(self.key0)
        self.btn_equal.clicked.connect(self.keyEqual)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.screen_result.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_bar.setText(_translate("MainWindow", "/"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_mult.setText(_translate("MainWindow", "x"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.menuCreator.setTitle(_translate("MainWindow", "Creator"))
        self.actionMateus_Santos.setText(_translate("MainWindow", "Mateus Santos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
