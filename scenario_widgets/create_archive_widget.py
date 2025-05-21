from PyQt6 import uic
from PyQt6.QtWidgets import *
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.create_archive
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Create Archive"
        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "create_archive_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        # params
        archiveAddress = self.lineEdit_archiveAddress.text()
        archiveName = self.lineEdit_archiveName.text()
        rootDirectory, baseDirectory = path.split(self.lineEdit_selectFolder.text())
        archiveFormat = self.comboBox_format.currentText()

        # create the destination path
        archiveAddress = path.join(archiveAddress, archiveName)

        # call function to create archive
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        base_name=archiveAddress, format=archiveFormat,
                                                        root_dir=rootDirectory, base_dir=baseDirectory)


if __name__ == '__main__':
    pass