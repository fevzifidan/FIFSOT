from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from ui_files.CreateArchive.create_archive_form import Ui_MainWindow
from Transactions.Directory_Transactions import Transaction
from Customs import CustomMessageBox
import Commons
import sys
from os import path
from FThread import TransactionPerformer

class ArchiveApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.setupUi(self)

        self._parent = parent
        self.transactionPerformer = transactionPerformer
        self.btn_close_window.clicked.connect(lambda: self.close())

        self.matchDict:dict[QPushButton, QLineEdit] = {
            self.btn_openDialog_archiveAddress      :       self.lineEdit_archiveAddress,
            self.btn_openDialog_rootDirectory       :       self.lineEdit_rootDirectory,
            self.btn_openDialog_baseDirectory       :       self.lineEdit_baseDirectory
        }

        for btn, _ in self.matchDict.items():
            btn.clicked.connect(self.openFileDialog)
        
        # Store compulsory input(s)
        self.compulsoryInputs:list[QLineEdit] = [
            self.lineEdit_archiveAddress, self.lineEdit_archiveName,
            self.lineEdit_rootDirectory
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
            self._parent.functionStack.append("Archive creation")
            # params
            archiveAddress = self.lineEdit_archiveAddress.text()
            archiveName = self.lineEdit_archiveName.text()
            rootDirectory = self.lineEdit_rootDirectory.text()
            baseDirectory = self.lineEdit_baseDirectory.text()
            archiveFormat = self.comboBox_format.currentText()

            # create the destination path
            archiveAddress = path.join(archiveAddress, archiveName)

            # arrange base directory if specified
            if baseDirectory:
                # When it is selected via the dialog, the path of baseDirectory
                # that is common with rootDirectory should be deleted.
                commonPath = path.commonpath([rootDirectory, baseDirectory])
                baseDirectory = path.relpath(baseDirectory, commonPath)

            # create a transaction object
            transaction = Transaction()

            # call function to create archive
            self.transactionPerformer.addToTransactionQueue(transaction.create_archive,
                                                            base_name=archiveAddress, format=archiveFormat,
                                                            root_dir=rootDirectory, base_dir=baseDirectory)
            
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArchiveApp()
    window.show()
    sys.exit(app.exec())


# END