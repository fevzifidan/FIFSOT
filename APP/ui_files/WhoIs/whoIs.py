from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from ui_files.WhoIs.whoIs_form import Ui_MainWindow
from Customs import CustomMessageBox
from Transactions.Directory_Transactions import Transaction
from FThread import TransactionPerformer
from PyQt6.QtGui import QMovie
import Commons
import sys
from os import path
from ui_files import resources_rc

class WhoIsApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, transactionPerformer:TransactionPerformer=None):
        super().__init__()
        self.setupUi(self)

        self._parent = parent
        self.transactionPerformer = transactionPerformer

        self.transactionPerformer.lastResult.connect(self.signalHandler)
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

        self.btn_detect.clicked.connect(self.detect)
        self.btn_terminate.clicked.connect(self.terminate)

        # Initialize movie object
        self.movie = None
        
        # Connect currentChanged signal to relevant function
        self.stackedWidget.currentChanged.connect(self.pageChanged)

        # set initial page of stackedWidget
        self.stackedWidget.setCurrentIndex(0)

        # Do not show terminate button until detection completed
        self.setButtons(False)

        self.lineEdit_address.textChanged.connect(self.addressChangedEvent)
    
    def mousePressEvent(self, event):
        return Commons.mousePressEvent(self, event)
    
    def mouseMoveEvent(self, event):
        return Commons.mouseMoveEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        return Commons.mouseReleaseEvent(self, event)
    
    def closeEvent(self, event):
        # Set the current page an arbitrary page different
        # from loading page in order to properly delete QMovie
        # object from memory
        self.stackedWidget.setCurrentIndex(0)

        self._parent.setEnabled(True)

        self.close()
        
        self.deleteLater()
    
    def openFileDialog(self):
        Commons.openFileDialog(self)
    
    def setButtons(self, value:bool) -> None:
        self.btn_terminate.setVisible(value)
        self.lbl_not_recommended.setVisible(value)
    
    def addressChangedEvent(self):
        self.stackedWidget.setCurrentIndex(0)
        self.setButtons(False)
    
    def playLoadingGif(self):
        if not self.movie:
            self.movie = QMovie(":/yeniÖnek/fifsot_icons/loading_gif_1.gif")
            self.lbl_loading_icon.setMovie(self.movie)
            self.movie.setSpeed(250)
            self.movie.start()
    
    def pageChanged(self):
        if self.movie:
            self.movie.stop()
            self.lbl_loading_icon.setMovie(None)
            self.movie = None

        if self.sender().currentWidget() == self.page_start:
            self.setButtons(False)
            self.lineEdit_address.clear()
            self.lineEdit_address.setFocus()
            self.btn_detect.setEnabled(True)
        
        elif self.sender().currentWidget() == self.page_loading:
            self.playLoadingGif()
            self.btn_detect.setEnabled(False)

        elif self.sender().currentWidget() == self.page_info:
            self.btn_detect.setEnabled(True)        

    
    def detect(self):
        if not Commons.checkCompulsoryInputs(self):
            return False
        
        address = self.lineEdit_address.text()
        transaction = Transaction()
        self.transactionPerformer.addToTransactionQueue(transaction.detectFileHolder,
                                                        file_path=address)
        self.stackedWidget.setCurrentWidget(self.page_loading)
    
    def signalHandler(self, value):
        # This signal contains the result for process information
        # coming from detect function

        # We filter irrelevant signals
        # Here is for dict and None type signals. If another signal
        # comes, ignore it.
        if isinstance(value, bool): return

        elif value:
            name, _id = value[path.normpath(self.lineEdit_address.text())]

            self.stackedWidget.setCurrentWidget(self.page_info)

            self.lbl_process_name.setText(name)
            self.lbl_process_id.setText(str(_id))

            self.setButtons(True)
        
        else:
            self.stackedWidget.setCurrentIndex(0)
            CustomMessageBox.NoResultsFound(self).exec()
    
    def terminate(self):
        if not Commons.checkCompulsoryInputs(self):
            return False
        
        else:
            address = self.lineEdit_address.text()

            # create a transaction object
            transaction = Transaction()

            # call function for rename operation
            try:
                self.transactionPerformer.addToTransactionQueue(transaction.terminateProcess,
                                                                int(self.lbl_process_id.text()),
                                                                address)
            
            except Exception as e:
                CustomMessageBox.Warning(self, "Error", f"{str(e)}").exec()
            
            else:
                CustomMessageBox.Information(self, "Transaction Successful",
                                             "The transaction was completed successfully.").exec()
            
            finally:
                self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WhoIsApp()
    window.show()
    sys.exit(app.exec())


# END