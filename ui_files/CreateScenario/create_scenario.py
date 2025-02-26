from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from ui_files.CreateScenario.create_scenario_form import Ui_MainWindow
import Commons
from Customs.AddTransactionPopUpMenu import AddTransactionPopUpMenu
import sys
from FThread import TransactionPerformer

from scenario_widgets import *

import json

class CreateScenarioApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None, save:dict|None = None):
        super().__init__()
        self.setupUi(self)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())
        self.transactionObjects:list[QWidget] = []

        self.btn_add_transaction.clicked.connect(self.openAddTransactionPopUp)

        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_saveName
        ]

        self.btn_save.clicked.connect(self.save)

        if save is not None:
            self.loadSave(save)
    
    def loadSave(self, save:dict):
        self.name:str = save["name"]
        self.types:list = save["transactionObjectTypes"]
        self.record:list[dict] = save["records"]

        self.lineEdit_saveName.setText(self.name)

        for number, transactionObjectType in enumerate(self.types, start=0):
            self.addTransaction(transactionType=transactionObjectType, load=self.record[number])
    
    def mousePressEvent(self, event):
        return Commons.mousePressEvent(self, event)
    
    def mouseMoveEvent(self, event):
        return Commons.mouseMoveEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        return Commons.mouseReleaseEvent(self, event)
    
    def closeEvent(self, event):
        try:
            self._parent.setEnabled(True)
        except AttributeError:
            pass
        except:
            raise

        self.close()
        
        self.deleteLater()
    
    def openFileDialog(self):
        Commons.openFileDialog(self)
    
    def openAddTransactionPopUp(self):
        self.menu = AddTransactionPopUpMenu(self, self.addTransaction)
        self.menu.show_menu(button=self.btn_add_transaction, widget=self.widget_btn_container)

    def addTransaction(self, transactionType:str|None=None, load:dict|None = None):
        self.widget_header.setVisible(False)
        
        if transactionType == False:
            # From external calling, transactionType cannot be True or False;
            # but if the function has been called from signal, then it becomes
            # False
            transactionType = self.sender().text()

        if transactionType == "Copy":
            transactionObject = copy_widget.SimpleApp(load)
        elif transactionType == "Count":
            transactionObject = count_widget.SimpleApp(load)
        elif transactionType == "Create Archive":
            transactionObject = create_archive_widget.SimpleApp(load)
        elif transactionType == "Delete":
            transactionObject = delete_widget.SimpleApp(load)
        elif transactionType == "R.E.D.":
            transactionObject = red_widget.SimpleApp(load)
        elif transactionType == "Rename":
            transactionObject = rename_widget.SimpleApp(load)
        else:
            print(f"Transaction Type: {transactionType}")
        
        widget = transactionObject.getWidget()

        self.transactionObjects.append(transactionObject)

        self.addToArea(widget, transactionType)
    
    def addToArea(self, widget:QWidget, transactionType:str):
        label = QLabel(self)
        label.setTextFormat(Qt.TextFormat.MarkdownText)
        font = QFont()
        font.setPointSize(12)
        label.setFont(font)
        label.setText(f'<span style="color:#40E0D0">{transactionType}</span>')
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addWidget(label)
        self.verticalLayout_5.addWidget(widget)
        self.verticalLayout_5.addItem(spacer)
    
    def getTransactionObjectTypes(self):
        transactionObjectTypes = list()
        for obj in self.transactionObjects:
            transactionObjectTypes.append(obj.transactionType)
        return transactionObjectTypes
    
    def restartObjects(self):
        self.transactionObjects[0].restartRecord()
        self.transactionObjects.clear()

    def save(self):
        if not Commons.checkCompulsoryInputs(self):
            return False
        
        records:list[dict] = list()

        for obj in self.transactionObjects:
            records.append(obj.dump())
        
        save = {
            "name": f"{self.lineEdit_saveName.text()}",
            "transactionObjectTypes": self.getTransactionObjectTypes(),
            "records": records
        }

        json_data = json.dumps(save)

        with open(rf"scenarios/{save["name"]}.json", "w") as json_file:
            json_file.write(json_data)
        
        self.close()
    
    def run(self):
        for obj in self.transactionObjects:
            obj.run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateScenarioApp()
    window.show()
    sys.exit(app.exec())


# END