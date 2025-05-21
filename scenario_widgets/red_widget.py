from PyQt6 import uic
from PyQt6.QtWidgets import *
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.remove_empty_directories
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "R.E.D."

        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "red_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        address = self.lineEdit_address.text()
        inSymlink = self.checkBox_deleteObjectsInSymlinks.isChecked()
        recursive = self.checkBox_recursive.isChecked()

        # call function for delete operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        obj_addr=address,
                                                        in_symlink_ok=inSymlink,
                                                        recursive=recursive)


if __name__ == '__main__':
    pass