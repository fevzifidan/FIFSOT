from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt
import Commons
import sys

class AboutApp(QMainWindow):
    def __init__(self, parent=None, transactionPerformer=None):
        super().__init__()
        self.ui = uic.load_ui.loadUi(r"C:\Users\fevzi\Downloads\pages\about_ui.ui", self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._parent = parent
        self.btn_close_window.clicked.connect(lambda: self.close())
        self.btn_close.clicked.connect(lambda: self.close())
    
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AboutApp()
    window.show()
    sys.exit(app.exec())


# END