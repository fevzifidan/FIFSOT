from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from ui_files.CreateSymlink.create_symlink_form import Ui_MainWindow
from Transactions.Directory_Transactions import Transaction
from Customs import CustomMessageBox
import Commons
import sys
from os import path
from FThread import TransactionPerformer

class SymlinkApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.setupUi(self)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())

        # Store the corresponding lineEdit to each openFileDialog button
        self.matchDict:dict[QPushButton, QLineEdit] = {
            self.btn_openDialog_source      :   self.lineEdit_source,
            self.btn_openDialog_destination :   self.lineEdit_destination
        }

        for btn, _ in self.matchDict.items():
            btn.clicked.connect(self.openFileDialog)
        
        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_source, self.lineEdit_destination, self.lineEdit_name
        ]

        self.btn_create.clicked.connect(self.run)
    
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
            self._parent.functionStack.append("Symlink creation")
            # params
            source = self.lineEdit_source.text()
            destination = self.lineEdit_destination.text()
            name = self.lineEdit_name.text()
            
            # create destination by combining
            # dir path and desired name
            destination = path.join(destination, name)

            # create transaction object
            transaction = Transaction()

            # call function to create symlink
            self.transactionPerformer.addToTransactionQueue(transaction.create_symlink,
                                                            src=source, dest=destination)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SymlinkApp()
    window.show()
    sys.exit(app.exec())


# END