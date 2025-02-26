import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui_files import resources_rc

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
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 60, 230, 90))
        self.widget.setMinimumSize(QSize(250, 90))
        self.widget.setMaximumSize(QSize(16777215, 90))
        self.widget.setStyleSheet(u"#widget{\n"
"	border:2px solid #000000;\n"
"	border-radius:10px;\n"
"	border-color: linear-gradient(to right, #8A2BE2, #D8BFD8) 1;\n"
"	\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 130, 121, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"#lbl_header{\n"
"	font:12px;\n"
"   font-weight:bold;\n"
"}\n"
"\n"
"#btn_menu{\n"
"	icon:url(\":/yeni\u00d6nek/fifsot_icons/settings_black.png\")\n"
"}\n"
"\n"
"#btn_run{\n"
"	icon:url(\":/yeni\u00d6nek/fifsot_icons/play_black.png\")\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_header = QLabel(self.widget)
        self.lbl_header.setObjectName(u"lbl_header")
        self.lbl_header.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_header)

        self.lbl_operation_number = QLabel(self.widget)
        self.lbl_operation_number.setObjectName(u"lbl_operation_number")
        self.lbl_operation_number.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_operation_number)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_menu = QPushButton(self.widget)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(25, 25))
        self.btn_menu.setMaximumSize(QSize(25, 25))
        self.btn_menu.setIconSize(QSize(16,16))

        self.horizontalLayout.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_run = QPushButton(self.widget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setMinimumSize(QSize(25, 25))
        self.btn_run.setMaximumSize(QSize(25, 25))
        self.btn_run.setIconSize(QSize(20,20))

        self.horizontalLayout.addWidget(self.btn_run)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

    def retranslateUi(self):
        self.lbl_header.setText(QCoreApplication.translate("MainWindow", u"{}".format(self.name), None))
        self.lbl_operation_number.setText(QCoreApplication.translate("MainWindow", u"{} transactions".format(str(self.numberOfTransactions)), None))
        self.btn_menu.setText("")
        self.btn_run.setText("")
    
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