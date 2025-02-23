# The class 'CustomFileDialog' below is developed with the help of below answer
# https://stackoverflow.com/a/78366061


from PyQt6.QtCore import QObject, QEvent
from PyQt6.QtWidgets import QFileDialog, QListView, QTreeView, QDialogButtonBox, QAbstractItemView

class CustomFileDialog(QObject):
    def __init__(self, parent=None):
        super().__init__()
        self.dialog = QFileDialog(parent=parent)
        self.dialog.setFileMode(QFileDialog.FileMode.Directory)
        self.dialog.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        
        plist = self.dialog.findChild(QListView)
        ptree = self.dialog.findChild(QTreeView)
        
        if plist:
            plist.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            plist.viewport().installEventFilter(self)
        
        if ptree:
            ptree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            ptree.viewport().installEventFilter(self)

        pButtonBox = self.dialog.findChild(QDialogButtonBox)
        if pButtonBox:
            buttons = pButtonBox.buttons()
            for button in buttons:
                if pButtonBox.buttonRole(button) == QDialogButtonBox.ButtonRole.AcceptRole:
                    button.clicked.connect(self.onChooseButtonClicked)
        
    def onChooseButtonClicked(self):
        selected_paths = self.dialog.selectedFiles()
        self.selectedPath = selected_paths[-1]
        self.dialog.close()
    
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonRelease:
            pParent = watched.parent()
            if isinstance(watched, (QTreeView, QListView)) or isinstance(pParent, (QTreeView, QListView)):
                self.onHandleButtons()
        return False

    def onHandleButtons(self):
        pButtonBox = self.dialog.findChild(QDialogButtonBox)
        if pButtonBox:
            buttons = pButtonBox.buttons()
            for button in buttons:
                if button.isEnabled():
                    continue
                if pButtonBox.buttonRole(button) == QDialogButtonBox.ButtonRole.AcceptRole:
                    button.setEnabled(True)
                    break
    
    def exec(self) -> str|None:
        self.dialog.exec()
        return getattr(self, "selectedPath", None)


# END