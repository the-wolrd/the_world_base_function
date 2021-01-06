import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# import your Qt Designer UI googleing
from baseOfUi import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # self.setWindowFlag(Qt.FramelessWindowHint) #cunstom top bar
        # self.setAttribute(Qt.WA_TranslucentBackground) #cunstom top bar
        # def moveWindow(event): #cunstom top bar
        #     if event.buttons() == Qt.LeftButton:
        #         try:
        #             self.move(self.pos() + event.globalPos() - self.dragPos)
        #             self.dragPos = event.globalPos()
        #             event.accept()
        #         except:
        #             pass
        # self.ui.top_bar.mouseMoveEvent = moveWindow #cunstom top bar
    # def mousePressEvent(self, event): #cunstom top bar
    #     self.dragPos = event.globalPos()
    def btn1(self):
        print("버튼이다")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())