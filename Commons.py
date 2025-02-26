from PyQt6.QtCore import Qt
from Customs.CustomFileDialog import CustomFileDialog
from Customs import CustomMessageBox
from FThread import TransactionPerformer


def mousePressEvent(obj, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if obj.childAt(event.position().toPoint()) == obj.widget_frame:
                try:
                    obj.drag_pos = event.globalPosition().toPoint() - obj.frameGeometry().topLeft()
                    event.accept()
                except:
                    return

def mouseMoveEvent(obj, event):
    if event.buttons() == Qt.MouseButton.LeftButton:
        if obj.childAt(event.position().toPoint()) == obj.widget_frame:
            try:
                obj.move(event.globalPosition().toPoint() - obj.drag_pos)
                event.accept()
            except:
                return

def mouseReleaseEvent(obj, event):
    obj.drag_pos = None
    event.accept()

def openFileDialog(obj):
    dialog = CustomFileDialog(obj)
    res = dialog.exec()
    
    obj.matchDict[obj.sender()].setText(res)

def checkCompulsoryInputs(obj):
    inputList = obj.compulsoryInputs

    for lineEdit in inputList:
        if lineEdit.text() == None:
            CustomMessageBox.Warning(obj, "Missing Information", "All mandatory fields must be filled in!").exec()
            return False
    
    return True


# END