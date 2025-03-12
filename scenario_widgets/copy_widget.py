from PyQt6 import uic
from PyQt6.QtWidgets import *
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()
        self.transaction = Transaction()
        self.func = self.transaction.copy
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Copy"
        self.prepare(recordDict)
    
    def prepare(self, recordDict:dict|None = None):
        # Load ui
        ui_file = path.join(path.dirname(__file__), "widgets", "copy_widget.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)

        # Get main widget
        self.widget = self.ui.findChild(QWidget, "widget")

        # Get objects in main widget
        self.lineEdit_source = self.ui.findChild(QLineEdit, "lineEdit_source")
        self.lineEdit_destination = self.ui.findChild(QLineEdit, "lineEdit_destination")
        self.lineEdit_name = self.ui.findChild(QLineEdit, "lineEdit_name")

        self.checkBox_onlyFiles = self.ui.findChild(QCheckBox, "checkBox_onlyFiles")
        self.checkBox_mergeContentOnly = self.ui.findChild(QCheckBox, "checkBox_mergeContentOnly")
        self.checkBox_skipExistingOnes = self.ui.findChild(QCheckBox, "checkBox_skipExistingOnes")
        self.checkBox_symlinks = self.ui.findChild(QCheckBox, "checkBox_symlinks")
        self.checkBox_copyMetaData = self.ui.findChild(QCheckBox, "checkBox_copyMetaData")
        self.checkBox_recursive = self.ui.findChild(QCheckBox, "checkBox_recursive")

        self.lineEdit_extension = self.ui.findChild(QLineEdit, "lineEdit_extension")
        self.lineEdit_nameStartswith = self.ui.findChild(QLineEdit, "lineEdit_nameStartswith")
        self.lineEdit_nameContains = self.ui.findChild(QLineEdit, "lineEdit_nameContains")
        self.lineEdit_excludeNameStartswith = self.ui.findChild(QLineEdit, "lineEdit_excludeNameStartswith")
        self.lineEdit_excludeNameContains = self.ui.findChild(QLineEdit, "lineEdit_excludeNameContains")
        self.checkBox_caseInsensitive = self.ui.findChild(QCheckBox, "checkBox_caseInsensitive")


        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)
    
    def run(self):
        source = self.lineEdit_source.text()
        destination = self.lineEdit_destination.text()
        name = self.lineEdit_name.text()

        if name:
            destination = path.join(destination, name)
        
        # params
        onlyFiles = self.checkBox_onlyFiles.isChecked()
        mergeContentOnly = self.checkBox_mergeContentOnly.isChecked()
        skipExistingOnes = self.checkBox_skipExistingOnes.isChecked()
        symlinks = self.checkBox_symlinks.isChecked()
        copyMetaData = self.checkBox_copyMetaData.isChecked()
        recursive = self.checkBox_recursive.isChecked()

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
        
        # call copy function
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        src=source, dest=destination,
                                                        merge_content_only=mergeContentOnly,
                                                        skip_existing_ones=skipExistingOnes,
                                                        symlinks=symlinks, copyMetaData=copyMetaData,
                                                        recursive=recursive)


if __name__ == '__main__':
    pass