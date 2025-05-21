from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6 import uic
from Transactions.Directory_Transactions import Transaction
import Commons
import sys
from FThread import TransactionPerformer

class RedApp(QMainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.ui = uic.load_ui.loadUi(r"C:\Users\fevzi\Downloads\pages\red_ui.ui", self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())

        # Store the corresponding lineEdit to the openFileDialog button
        self.matchDict:dict[QPushButton, QLineEdit] = {
            self.btn_openDialog_address :   self.lineEdit_address
        }

        self.btn_openDialog_address.clicked.connect(self.openFileDialog)

        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_address
        ]

        self.btn_delete.clicked.connect(self.run)
    
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
            self._parent.functionStack.append("R.E.D. operation")
            address = self.lineEdit_address.text()
            inSymlink = self.checkBox_deleteObjectsInSymlinks.isChecked()
            recursive = self.checkBox_recursive.isChecked()

            # create a transaction object
            transaction = Transaction()

            # call function for delete operation
            self.transactionPerformer.addToTransactionQueue(transaction.remove_empty_directories,
                                                            obj_addr=address,
                                                            in_symlink_ok=inSymlink,
                                                            recursive=recursive)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RedApp()
    window.show()
    sys.exit(app.exec())


# END