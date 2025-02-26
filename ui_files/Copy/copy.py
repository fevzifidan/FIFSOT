from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from ui_files.Copy.copy_form import Ui_MainWindow
import Commons
from Transactions.Directory_Transactions import Transaction
from Customs import CustomMessageBox
import sys
from os import path
from FThread import TransactionPerformer

class CopyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.setupUi(self)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())
        
        # Store the corresponding lineEdit to each openFileDialog button
        self.matchDict:dict[QPushButton, QLineEdit] = {
            self.btn_openDialog_source:         self.lineEdit_source,
            self.btn_openDialog_destination:    self.lineEdit_destination
        }

        self.btn_openDialog_source.clicked.connect(self.openFileDialog)
        self.btn_openDialog_destination.clicked.connect(self.openFileDialog)

        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_source, self.lineEdit_destination
        ]

        self.btn_copy.clicked.connect(self.run)
    
    def mousePressEvent(self, event):
        return Commons.mousePressEvent(self, event)
    
    def mouseMoveEvent(self, event):
        return Commons.mouseMoveEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        return Commons.mouseReleaseEvent(self, event)
    
    def closeEvent(self, event):
        self._parent.setEnabled(True)

        self.close()
        
        self.deleteLater()
    
    def openFileDialog(self):
        Commons.openFileDialog(self)
    
    def run(self):
        if not Commons.checkCompulsoryInputs(self):
            return False
        
        else:
            self._parent.functionStack.append("Copy operation")
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
            
            # create a transaction object
            transaction = Transaction()

            # set conditions
            transaction.setCond(extension=extension, name_startswith=nameStartswith, contains=nameContains,
                                excl_startswith=excludeNameStartswith, excl_contains=excludeNameContains,
                                case_insensitive=caseInsensitive)
            
            # call copy function
            self.transactionPerformer.addToTransactionQueue(transaction.copy,
                                                            src=source, dest=destination,
                                                            only_files=onlyFiles,
                                                            merge_content_only=mergeContentOnly,
                                                            skip_existing_ones=skipExistingOnes,
                                                            symlinks=symlinks, copyMetaData=copyMetaData,
                                                            recursive=recursive)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CopyApp()
    window.show()
    sys.exit(app.exec())


# END