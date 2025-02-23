from PyQt6.QtWidgets import QMenu, QPushButton, QWidget
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QIcon
from ui_files import resources_rc


class AddTransactionPopUpMenu():
    def __init__(self, parent=None, func=None):

        self.menu = QMenu(parent=parent)

        self.menu.setStyleSheet("""
                                QMenu QWidget {
                                    background-color:transparent;
                                }
                                QMenu {
                                    color:#FFFFFF;
                                    background-color:#202124;
                                    font:12px;
                                    border:1px solid #202124;
                                }

                                QMenu::item {
                                    background-color:transparent;
                                    border:1px solid transparent;
                                    height:30px;
                                    width:150px;
                                }

                                QMenu::item:selected {
                                    background-color:#555555;
                                }

                                QMenu::separator {
                                    background-color:#808080;
                                    height:1px;
                                    margin-top:5px;
                                    margin-bottom:5px;
                                }
                                """)
        
        self.actionCopy = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/copy_files.png"), "Copy")
        self.actionCount = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/count_1.png"), "Count")
        self.actionCreateArchive = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/archive_1_blue.png"), "Create Archive")
        self.actionDelete = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/delete.png"), "Delete")
        self.actionRED = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/remove_directory.png"), "R.E.D.")
        self.actionRename = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/rename.png"), "Rename")

        if func is not None:
            actionList = [self.actionCopy, self.actionCount, self.actionCreateArchive,
                          self.actionDelete, self.actionRED, self.actionRename]
            
            for action in actionList:
                action.triggered.connect(func)


    def show_menu(self, button:QPushButton, widget:QWidget):
        btn_pos = button.mapToGlobal(QPoint(0, 0)).x()
        widget_pos = widget.mapToGlobal(QPoint(0, widget.height())).y()
        pos = QPoint()
        pos.setX(btn_pos - int(self.menu.sizeHint().width()/4))
        pos.setY(widget_pos - widget.height() - self.menu.sizeHint().height() - 1)
        self.menu.exec(pos)


# END