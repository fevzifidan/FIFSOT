from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from ui_files.Rename.rename_form import Ui_MainWindow
from Customs import CustomMessageBox
from Transactions.Directory_Transactions import Transaction
from FThread import TransactionPerformer
import Commons
import sys

class RenameApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer = None):
        super().__init__()
        self.setupUi(self)

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

        self.btn_rename.clicked.connect(self.run)
    
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
            self._parent.functionStack.append("Rename operation")
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

            # create a transaction object
            transaction = Transaction()

            # call function for rename operation
            self.transactionPerformer.addToTransactionQueue(transaction.rename,
                                                            address = address,
                                                            prefix=prefix,
                                                            suffix=suffix,
                                                            only_files=onlyFiles,
                                                            case=orderCase,
                                                            rev=orderReversed,
                                                            start=start,
                                                            zfill=zfill)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RenameApp()
    window.show()
    sys.exit(app.exec())


# END