from PyQt6 import uic
from PyQt6.QtWidgets import *
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.rename
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Rename"

        self.prepare(recordDict)
    
    def prepare(self, recordDict:dict|None = None):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "rename_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        address = self.lineEdit_address.text()
        prefix = self.lineEdit_prefix.text()
        suffix = self.lineEdit_suffix.text()
        orderCase = self.comboBox_case.currentText()
        start = self.spinBox_start.text()
        zfill = self.spinBox_zfill.text()

        onlyFiles = self.checkBox_onlyFiles.isChecked()
        orderReversed = self.checkBox_reversed.isChecked()

        # Control and arrange prefix/suffix parameters.
        # Prefix and suffix cannot be None.
        
        if prefix is None:
            prefix = ""
        
        if suffix is None:
            suffix = ""
        
        # Arrange start and zfill parameters.
        # Start and zfill must be int.

        start = int(start)
        zfill = int(zfill)

        # call function for rename operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        address = address,
                                                        prefix=prefix,
                                                        suffix=suffix,
                                                        only_files=onlyFiles,
                                                        case=orderCase,
                                                        rev=orderReversed,
                                                        start=start,
                                                        zfill=zfill)


if __name__ == '__main__':
    pass