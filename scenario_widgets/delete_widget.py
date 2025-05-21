from PyQt6 import uic
from PyQt6.QtWidgets import *
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.delete
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Delete"
        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "delete_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        address = self.lineEdit_address.text()

        # params
        onlyFiles = self.checkBox_onlyFiles.isChecked()
        inSymlink = self.checkBox_deleteObjectsInSymlinks.isChecked()
        followSymlinks = self.checkBox_followSymlinks.isChecked()
        onlyContent = self.checkBox_onlyContent.isChecked()
        recursive = self.checkBox_recursive.isChecked()
        forcePermissions = self.checkBox_forcePermission.isChecked()

        # conditions
        extension = self.lineEdit_extension.text()
        nameStartswith = self.lineEdit_nameStartswith.text()
        nameContains = self.lineEdit_nameContains.text()
        excludeNameStartswith = self.lineEdit_excludeNameStartswith.text()
        excludeNameContains = self.lineEdit_excludeNameContains.text()
        caseInsensitive = self.checkBox_caseInsensitive.isChecked()

        # set conditions
        self.transaction.setCond(extension=extension, name_startswith=nameStartswith, contains=nameContains,
                                 excl_startswith=excludeNameStartswith, excl_contains=excludeNameContains,
                                 case_insensitive=caseInsensitive, filterOnlyForFiles=onlyFiles)
        
        # call function for delete operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        obj_addr=address,
                                                        in_symlink_ok=inSymlink, follow_symlinks=followSymlinks,
                                                        only_content=onlyContent, recursive=recursive,
                                                        forcePermissions=forcePermissions)


if __name__ == '__main__':
    pass