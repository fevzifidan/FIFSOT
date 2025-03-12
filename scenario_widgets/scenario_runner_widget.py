from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QCoreApplication, QObject, pyqtSignal
from os import path

class ButtonSignal(QObject):
    buttonSignal = pyqtSignal(tuple)

class SimpleApp(QWidget):
    def __init__(self, name:str, numberOfTransactions:int):
        super().__init__()

        self.name = name
        self.numberOfTransactions = numberOfTransactions

        self.emitter = ButtonSignal()
        self.buttonSignal = self.emitter.buttonSignal

        self.prepare()

        self.btn_run.clicked.connect(self.emitRunSignal)
        self.btn_menu.clicked.connect(self.emitMenuSignal)
    
    def emitRunSignal(self):
        self.buttonSignal.emit(("run", self.name))
    
    def emitMenuSignal(self):
        self.buttonSignal.emit(("menu", self.name))

    def prepare(self):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "scenario_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # Get main widget
        self.widget = self.ui.findChild(QWidget, "widget")

        # Get objects in main widget
        self.btn_run = self.ui.findChild(QPushButton, "btn_run")
        self.btn_menu = self.ui.findChild(QPushButton, "btn_menu")
        self.lbl_header = self.ui.findChild(QLabel, "lbl_header")
        self.lbl_operation_number = self.ui.findChild(QLabel, "lbl_operation_number")

        # Set texts on objects
        self.lbl_header.setText(self.name)
        self.lbl_operation_number.setText(f"{self.numberOfTransactions} transactions")
    
    def getWidget(self):
        return self.widget
    
    def update(self, header:str|None = None, numberOfTransactions:str|None = None):
        if header is None: pass
        else: self.lbl_header.setText(QCoreApplication.translate("MainWindow", u"{}".format(header), None))

        if numberOfTransactions is None: pass
        else: self.lbl_operation_number.setText(QCoreApplication.translate("MainWindow", u"{} transactions".format(str(numberOfTransactions)), None))
    
    def run(self):
        pass

if __name__ == '__main__':
    pass