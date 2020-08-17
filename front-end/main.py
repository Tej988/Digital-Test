from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QButtonGroup
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

        self.setGeometry(100, 100, 1153, 600)
        self.setWindowTitle("Digital Test")

    def initUI(self):

        self.qstNo = 1

        button_font = QtGui.QFont()
        button_font.setFamily("Padauk")
        button_font.setPointSize(18)
        button_font.setBold(True)
        button_font.setWeight(75)

        self.phy_button = QtWidgets.QPushButton(self)
        self.phy_button.setGeometry(QtCore.QRect(130, 20, 131, 51))
        self.phy_button.setFont(button_font)
        self.phy_button.setText("Physics")

        self.che_button = QtWidgets.QPushButton(self)
        self.che_button.setGeometry(QtCore.QRect(280, 20, 141, 51))
        self.che_button.setFont(button_font)
        self.che_button.setText("Chemestry")

        self.math_button = QtWidgets.QPushButton(self)
        self.math_button.setGeometry(QtCore.QRect(450, 20, 151, 51))
        self.math_button.setFont(button_font)
        self.math_button.setText("Mathematics")

        qst_label_font = QtGui.QFont()
        qst_label_font.setFamily("Noto Sans CJK KR Medium")
        qst_label_font.setPointSize(14)
        qst_label_font.setWeight(50)
        self.qst_lable = QtWidgets.QLabel(self)
        self.qst_lable.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.qst_lable.setFont(qst_label_font)
        self.qst_lable.setText("Question 01")

        question_entry_font = QtGui.QFont()
        question_entry_font.setPointSize(16)
        self.qst_entry = QtWidgets.QTextEdit(self)
        self.qst_entry.setGeometry(QtCore.QRect(10, 130, 821, 70))
        self.qst_entry.setFont(question_entry_font)

        self.opt1_radio = QtWidgets.QRadioButton(self)
        self.opt1_radio.setGeometry(QtCore.QRect(40, 240, 16, 20))
        self.opt2_radio = QtWidgets.QRadioButton(self)
        self.opt2_radio.setGeometry(QtCore.QRect(40, 310, 16, 20))
        self.opt3_radio = QtWidgets.QRadioButton(self)
        self.opt3_radio.setGeometry(QtCore.QRect(40, 380, 16, 20))
        self.opt4_radio = QtWidgets.QRadioButton(self)
        self.opt4_radio.setGeometry(QtCore.QRect(40, 450, 16, 20))

        self.option=QButtonGroup()
        self.option.addButton(self.opt1_radio)
        self.option.addButton(self.opt2_radio)
        self.option.addButton(self.opt3_radio)
        self.option.addButton(self.opt4_radio)

        opt_entry_font = QtGui.QFont()
        opt_entry_font.setPointSize(14)
        self.opt1_entry = QtWidgets.QLineEdit(self)
        self.opt1_entry.setGeometry(QtCore.QRect(80, 230, 381, 41))
        self.opt1_entry.setFont(opt_entry_font)
        self.opt2_entry = QtWidgets.QLineEdit(self)
        self.opt2_entry.setGeometry(QtCore.QRect(80, 300, 381, 41))
        self.opt2_entry.setFont(opt_entry_font)
        self.opt3_entry = QtWidgets.QLineEdit(self)
        self.opt3_entry.setGeometry(QtCore.QRect(80, 370, 381, 41))
        self.opt3_entry.setFont(opt_entry_font)
        self.opt4_entry = QtWidgets.QLineEdit(self)
        self.opt4_entry.setGeometry(QtCore.QRect(80, 440, 381, 41))
        self.opt4_entry.setFont(opt_entry_font)

        button_font.setPointSize(16)
        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setGeometry(QtCore.QRect(690, 530, 91, 41))
        self.done_button.setFont(button_font)
        self.done_button.setText("Done")
        self.done_button.clicked.connect(self.done)

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setGeometry(QtCore.QRect(510, 530, 161, 41))
        self.next_button.setFont(button_font)
        self.next_button.setText("Save and next")
        self.next_button.clicked.connect(self.next)

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(370, 530, 121, 41))
        self.back_button.setFont(button_font)
        self.back_button.setText("Back")
        self.back_button.clicked.connect(self.back)


        pallet_label_font = QtGui.QFont()
        pallet_label_font.setPointSize(14)
        self.pallet_label = QtWidgets.QLabel(self)
        self.pallet_label.setGeometry(QtCore.QRect(930, 20, 201, 31))
        self.pallet_label.setFont(pallet_label_font)
        self.pallet_label.setText("Question Pallet")


        self.pallet_area = QtWidgets.QScrollArea(self)
        self.pallet_area.setGeometry(QtCore.QRect(839, 50, 311, 541))
        self.pallet_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 509))
        self.pallet_area.setWidget(self.scrollAreaWidgetContents)
        


    def next(self):
        if self.qst_entry.toPlainText() and self.opt1_entry.text() and self.opt2_entry.text() and self.opt3_entry.text() and self.opt4_entry.text() and (self.opt1_radio.isChecked() or self.opt2_radio.isChecked() or self.opt3_radio.isChecked() or self.opt4_radio.isChecked()):
            
            self.ans = 'a' if self.opt1_radio.isChecked() else 'b' if self.opt2_radio.isChecked() else 'c' if self.opt3_radio.isChecked() else 'd'
            
            self.option.setExclusive(False)
            self.opt1_radio.setChecked(False)
            self.opt2_radio.setChecked(False)
            self.opt3_radio.setChecked(False)
            self.opt4_radio.setChecked(False)
            self.option.setExclusive(True)

            self.qst_entry.clear()
            self.opt1_entry.clear()
            self.opt2_entry.clear()
            self.opt3_entry.clear()
            self.opt4_entry.clear()

            self.qstNo += 1
            print(self.qstNo)
            self.update()

        else:
            QMessageBox.about(
                self, "Title", "Please Populate all the input section")

    def back(self):
        self.qstNo -= 1
        print(self.qstNo)
        self.update()
        

    def done(self):
        QtCore.QCoreApplication.instance().quit()
        

    def update(self):
        self.qst_lable.setText("Question %02d" % (self.qstNo))
        self.back_button.setEnabled(
            True) if self.qstNo > 1 else self.back_button.setEnabled(False)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
