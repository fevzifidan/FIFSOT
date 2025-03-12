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

        # Get main widget
        self.widget = self.ui.findChild(QWidget, "widget")

        # Get objects in main widget
        self.lineEdit_archiveAddress = self.ui.findChild(QLineEdit, "lineEdit_archiveAddress")
        self.lineEdit_archiveName = self.ui.findChild(QLineEdit, "lineEdit_archiveName")
        self.lineEdit_rootDirectory = self.ui.findChild(QLineEdit, "lineEdit_rootDirectory")
        self.lineEdit_baseDirectory = self.ui.findChild(QLineEdit, "lineEdit_baseDirectory")
        self.comboBox_format = self.ui.findChild(QComboBox, "comboBox_format")

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        # params
        archiveAddress = self.lineEdit_archiveAddress.text()
        archiveName = self.lineEdit_archiveName.text()
        rootDirectory = self.lineEdit_rootDirectory.text()
        baseDirectory = self.lineEdit_baseDirectory.text()
        archiveFormat = self.comboBox_format.currentText()

        # create the destination path
        archiveAddress = path.join(archiveAddress, archiveName)

        # arrange base directory if specified
        if baseDirectory:
            # When it is selected via the dialog, the path of baseDirectory
            # that is common with rootDirectory should be deleted.
            commonPath = path.commonpath([rootDirectory, baseDirectory])
            baseDirectory = path.relpath(baseDirectory, commonPath)

            if baseDirectory == ".": baseDirectory = None

        # call function to create archive
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        base_name=archiveAddress, format=archiveFormat,
                                                        root_dir=rootDirectory, base_dir=baseDirectory)


if __name__ == '__main__':
    pass