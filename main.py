import sys
from turtle import onclick
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# 导入my_win.py中内容
from control_degee import *
import cv2
import sys

# 创建mainWin类并传入Ui_MainWindow
class mainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)
        # self.horizontalSlider.
        self.horizontalSlider.valueChanged.connect(self.getslidervalue)
        self.horizontalSlider_2.valueChanged.connect(self.getslidervalue2)
        self.horizontalSlider_3.valueChanged.connect(self.getslidervalue3)
        self.horizontalSlider_4.valueChanged.connect(self.getslidervalue4)
        self.horizontalSlider_5.valueChanged.connect(self.getslidervalue5)
        self.horizontalSlider_6.valueChanged.connect(self.getslidervalue6)
        self.horizontalSlider_7.valueChanged.connect(self.getslidervalue7)
        self.horizontalSlider_8.valueChanged.connect(self.getslidervalue8)
        self.horizontalSlider_9.valueChanged.connect(self.getslidervalue9)
        self.spinBox.valueChanged.connect(self.getspinboxchange)
        self.spinBox_2.valueChanged.connect(self.getspinboxchange_2)
        self.spinBox_3.valueChanged.connect(self.getspinboxchange_3)
        self.spinBox_4.valueChanged.connect(self.getspinboxchange_4)
        self.spinBox_5.valueChanged.connect(self.getspinboxchange_5)
        self.spinBox_6.valueChanged.connect(self.getspinboxchange_6)
        self.spinBox_7.valueChanged.connect(self.getspinboxchange_7)
        self.spinBox_8.valueChanged.connect(self.getspinboxchange_8)
        self.spinBox_9.valueChanged.connect(self.getspinboxchange_9)

        self.pushButton.clicked.connect(self.init_pos)
        self.pushButton_2.clicked.connect(self.send_data)
        self.checkBox.clicked.connect(self.on_instantaction_click)
        self.init()
    
    def init(self):
        self.spinBox.setValue(self.horizontalSlider.value())
        self.spinBox_2.setValue(self.horizontalSlider_2.value())
        self.spinBox_3.setValue(self.horizontalSlider_3.value())
        self.spinBox_4.setValue(self.horizontalSlider_4.value())
        self.spinBox_5.setValue(self.horizontalSlider_5.value())
        self.spinBox_6.setValue(self.horizontalSlider_6.value())
        self.spinBox_7.setValue(self.horizontalSlider_7.value())
        self.spinBox_8.setValue(self.horizontalSlider_8.value())
        self.spinBox_9.setValue(self.horizontalSlider_9.value())
        self.degee = [  self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value(),
                        self.horizontalSlider_4.value(),self.horizontalSlider_5.value(),self.horizontalSlider_6.value(),
                        self.horizontalSlider_7.value(),self.horizontalSlider_8.value(),self.horizontalSlider_9.value()
                     ]
    
    def getslidervalue(self):
        # print(self.horizontalSlider.value())
        self.spinBox.setValue(self.horizontalSlider.value())
        self.degee[0] = self.horizontalSlider.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getslidervalue2(self):
        # print(self.horizontalSlider.value())
        self.spinBox_2.setValue(self.horizontalSlider_2.value())
        self.degee[1] = self.horizontalSlider_2.value()
        if self.checkBox.isChecked():
            print(self.degee)
    
    def getslidervalue3(self):
        # print(self.horizontalSlider.value())
        self.spinBox_3.setValue(self.horizontalSlider_3.value())
        self.degee[2] = self.horizontalSlider_3.value()
        if self.checkBox.isChecked():
            print(self.degee)
    
    def getslidervalue4(self):
        # print(self.horizontalSlider.value())
        self.spinBox_4.setValue(self.horizontalSlider_4.value())
        self.degee[3] = self.horizontalSlider_4.value()
        if self.checkBox.isChecked():
            print(self.degee)
    
    def getslidervalue5(self):
        # print(self.horizontalSlider.value())
        self.spinBox_5.setValue(self.horizontalSlider_5.value())
        self.degee[4] = self.horizontalSlider_5.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getslidervalue6(self):
        # print(self.horizontalSlider.value())
        self.spinBox_6.setValue(self.horizontalSlider_6.value())
        self.degee[5] = self.horizontalSlider_6.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getslidervalue7(self):
        # print(self.horizontalSlider.value())
        self.spinBox_7.setValue(self.horizontalSlider_7.value())
        self.degee[6] = self.horizontalSlider_7.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getslidervalue8(self):
        # print(self.horizontalSlider.value())
        self.spinBox_8.setValue(self.horizontalSlider_8.value())
        self.degee[7] = self.horizontalSlider_8.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getslidervalue9(self):
        # print(self.horizontalSlider.value())
        self.spinBox_9.setValue(self.horizontalSlider_9.value())
        self.degee[8] = self.horizontalSlider_9.value()
        if self.checkBox.isChecked():
            print(self.degee)

    def getspinboxchange(self):
        self.horizontalSlider.setValue(self.spinBox.value())
    
    def getspinboxchange_2(self):
        self.horizontalSlider_2.setValue(self.spinBox_2.value())
    
    def getspinboxchange_3(self):
        self.horizontalSlider_3.setValue(self.spinBox_3.value())
    
    def getspinboxchange_4(self):
        self.horizontalSlider_4.setValue(self.spinBox_4.value())
    
    def getspinboxchange_5(self):
        self.horizontalSlider_5.setValue(self.spinBox_5.value())
    
    def getspinboxchange_6(self):
        self.horizontalSlider_6.setValue(self.spinBox_6.value())

    def getspinboxchange_7(self):
        self.horizontalSlider_7.setValue(self.spinBox_7.value())

    def getspinboxchange_8(self):
        self.horizontalSlider_8.setValue(self.spinBox_8.value())

    def getspinboxchange_9(self):
        self.horizontalSlider_9.setValue(self.spinBox_9.value())

    def init_pos(self):
        self.horizontalSlider.setValue(2048)
        self.horizontalSlider_2.setValue(2048)
        self.horizontalSlider_3.setValue(2048)
        self.horizontalSlider_4.setValue(2048)
        self.horizontalSlider_5.setValue(2048)
        self.horizontalSlider_6.setValue(2048)
        self.horizontalSlider_7.setValue(2048)
        self.horizontalSlider_8.setValue(2048)
        self.horizontalSlider_9.setValue(2048)
        print(self.degee)

    def send_data(self):
        print(self.degee)
    def on_instantaction_click(self):
        pass
        # if self.checkBox.isChecked():
        #     print(1)
        # else:
        #     print(2)
    

if __name__ == '__main__':
    # 下面是使用PyQt5的固定用法
    app = QApplication(sys.argv)
    
    main_win = mainWin()
    while(1):
        main_win.show()
        main_win.update()
        sys.exit(app.exec_())

