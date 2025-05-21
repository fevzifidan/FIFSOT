from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import Qt
import Commons
from Transactions.Directory_Transactions import Transaction
import sys
from FThread import TransactionPerformer

class CountApp(QMainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.ui = uic.load_ui.loadUi(r"C:\Users\fevzi\Downloads\pages\count_ui.ui", self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())
        
        # Store the corresponding lineEdit to the openFileDialog button
        self.matchDict:dict[QPushButton, QLineEdit] = {
            self.btn_openDialog_address: self.lineEdit_address
        }

        self.btn_openDialog_address.clicked.connect(self.openFileDialog)

        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_address
        ]

        self.btn_count.clicked.connect(self.run)
    
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
            self._parent.functionStack.append("Count operation")
            # params
            address = self.lineEdit_address.text()
            onlyFiles = self.checkBox_onlyFiles.isChecked()
            recursive = self.checkBox_recursive.isChecked()
            followSymlinks = self.checkBox_followSymlinks.isChecked()

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
                                case_insensitive=caseInsensitive, filterOnlyForFiles=onlyFiles)
            
            # call count function
            self.transactionPerformer.addToTransactionQueue(transaction.count,
                                                            addr=address, only_files=onlyFiles,
                                                            recursive=recursive,
                                                            follow_symlinks=followSymlinks)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountApp()
    window.show()
    sys.exit(app.exec())


# END