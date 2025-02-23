from PyQt6.QtWidgets import QMenu, QPushButton, QWidget
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QIcon
from ui_files import resources_rc


class TitleBarPopUpMenu():
    def __init__(self, parent=None):

        self.menu = QMenu(parent=parent)

        self.menu.setStyleSheet("""
                                QMenu {
                                    color:#FFFFFF;
                                    background-color:#101524;
                                    font:12px;
                                }

                                QMenu::item {
                                    background-color:transparent;
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
        
        self.actionGitHub = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/github_blue.png"), "GitHub")
        self.actionSeparator = self.menu.addSeparator()
        self.actionHelp = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/help_blue.png"), "Help")
        self.actionAbout = self.menu.addAction(QIcon(":/yeniÖnek/fifsot_icons/info_blue.png"), "About")

    def show_menu(self, button:QPushButton, widget:QWidget):
        btn_pos = button.mapToGlobal(QPoint(0, 0)).x()
        widget_pos = widget.mapToGlobal(QPoint(0, widget.height())).y()
        pos = QPoint()
        pos.setX(btn_pos)
        pos.setY(widget_pos + 1)
        self.menu.exec(pos)


# END