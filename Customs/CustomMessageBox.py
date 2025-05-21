from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon

def _CreateInformativeMessageBox(obj, windowTitle:str, text:str, icon):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(windowTitle)
    msgBox.setWindowIcon(QIcon(":/yeniÖnek/fifsot_icons/F_Icon_1.png"))
    msgBox.setText(text)
    msgBox.setIcon(icon)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    return msgBox

def _CreateResultNotifierMessageBox(obj, windowTitle:str, text:str, iconPixmap:QPixmap):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(windowTitle)
    msgBox.setWindowIcon(QIcon(":/yeniÖnek/fifsot_icons/F_Icon_1.png"))
    msgBox.setText(text)
    iconPixmap = iconPixmap.scaled(QSize(48,48), Qt.AspectRatioMode.IgnoreAspectRatio)
    msgBox.setIconPixmap(iconPixmap)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
    return msgBox

def Information(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Information
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Warning(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Warning
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Error(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Critical
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Successful(obj, reload:bool|None = None):
    # Reload is not used anymore and will be deprecated.
    title = "Successul"
    text = "The process has been completed successfully."
    iconPixmap = QPixmap(":/yeniÖnek/fifsot_icons/completed_green_1.png")
    
    return _CreateResultNotifierMessageBox(obj, title, text, iconPixmap)

def NoResultsFound(obj):
    title = "No Results Found"
    text = "No results found."
    iconPixmap = QPixmap(":/yeniÖnek/fifsot_icons/no_results_found.png")
    return _CreateResultNotifierMessageBox(obj, title, text, iconPixmap)

def Question(obj, windowTitle:str, text:str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(windowTitle)
    msgBox.setWindowIcon(QIcon(":/yeniÖnek/fifsot_icons/F_Icon_1.png"))
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Critical)
    msgBox.addButton(QMessageBox.StandardButton.Yes)
    msgBox.addButton(QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.No)
    return msgBox


# END