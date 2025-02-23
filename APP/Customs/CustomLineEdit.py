from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QDragEnterEvent, QDropEvent

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def text(self):
        orgnlText = super().text()

        if orgnlText == None:
            return None
        
        if orgnlText == "":
            return None
        
        if isinstance(orgnlText, str) and orgnlText.isspace():
            return None
        
        return orgnlText
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setText(file_path)
            event.acceptProposedAction()


# END