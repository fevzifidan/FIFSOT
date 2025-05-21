from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import Qt
from Transactions.Directory_Transactions import Transaction
import Commons
import sys
from os import path
from FThread import TransactionPerformer

class DeleteApp(QMainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        fileDir = path.dirname(path.abspath(__file__))
        ui_file = path.join(fileDir, "delete_ui.ui")
        self.ui = uic.load_ui.loadUi(ui_file, self)
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
            self._parent.functionStack.append("Delete operation")
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

            # create a transaction object
            transaction = Transaction()

            # set conditions
            transaction.setCond(extension=extension, name_startswith=nameStartswith, contains=nameContains,
                                excl_startswith=excludeNameStartswith, excl_contains=excludeNameContains,
                                case_insensitive=caseInsensitive, filterOnlyForFiles=True)
            
            # call function for delete operation
            self.transactionPerformer.addToTransactionQueue(transaction.delete,
                                                            obj_addr=address,
                                                            in_symlink_ok=inSymlink, follow_symlinks=followSymlinks,
                                                            only_content=onlyContent, recursive=recursive,
                                                            forcePermissions=forcePermissions)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeleteApp()
    window.show()
    sys.exit(app.exec())


# END