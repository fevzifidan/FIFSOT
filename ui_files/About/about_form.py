# Form implementation generated from reading ui file 'pages\about_ui.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from ui_files import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        MainWindow.resize(430, 447)
        MainWindow.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton[objectName=\"btn_visit_github\"] {\n"
"    border-radius:10px;\n"
"    color:#FFFFFF;\n"
"    background-color:#40E0D0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color:#555555;\n"
"}\n"
"\n"
"QPushButton[objectName=\"btn_close_window\"]{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_white.png\");\n"
"}\n"
"\n"
"QPushButton[objectName=\"btn_close_window\"]:hover{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_red.png\");\n"
"}\n"
"\n"
"QPushButton[objectName=\"btn_close_window\"]:pressed{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_white.png\");\n"
"}\n"
"\n"
"QLabel {\n"
"    color:#FFFFFF;\n"
"}\n"
"\n"
"QLabel[objectName=\"lbl_about_fifsot\"]{\n"
"    font:24px;\n"
"}\n"
"\n"
"QLabel[objectName=\"lbl_text\"]{\n"
"    font:12px;\n"
"}\n"
"\n"
"QLabel[objectName=\"lbl_version_header\"]{\n"
"    font:18px;\n"
"    color:#99FFFF;\n"
"}\n"
"\n"
"QLabel[objectName=\"lbl_version\"]{\n"
"    font:12px;\n"
"}\n"
"\n"
"QLabel[objectName=\"lbl_note\"]{\n"
"    font:18px;\n"
"    color:#99FFFF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color:#555555;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_note = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_note.setMinimumSize(QtCore.QSize(382, 20))
        self.lbl_note.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_note.setWordWrap(True)
        self.lbl_note.setIndent(16)
        self.lbl_note.setObjectName("lbl_note")
        self.gridLayout.addWidget(self.lbl_note, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.widget_btn_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_btn_container.setMinimumSize(QtCore.QSize(430, 50))
        self.widget_btn_container.setStyleSheet("QWidget[objectName=\"widget_btn_container\"]{\n"
"    background-color:#101524;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#40E0D0;\n"
"}")
        self.widget_btn_container.setObjectName("widget_btn_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_btn_container)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_close = QtWidgets.QPushButton(parent=self.widget_btn_container)
        self.btn_close.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_close.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.gridLayout.addWidget(self.widget_btn_container, 13, 0, 1, 1)
        self.lbl_version_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_version_header.setMinimumSize(QtCore.QSize(382, 20))
        self.lbl_version_header.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_version_header.setWordWrap(True)
        self.lbl_version_header.setIndent(16)
        self.lbl_version_header.setObjectName("lbl_version_header")
        self.gridLayout.addWidget(self.lbl_version_header, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        self.widget_frame = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_frame.setMinimumSize(QtCore.QSize(0, 42))
        self.widget_frame.setMaximumSize(QtCore.QSize(16777215, 42))
        self.widget_frame.setStyleSheet("QWidget[objectName=\"widget_frame\"]{\n"
"    background-color:#101524;\n"
"    border: 1px solid #101524;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:none;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:none;\n"
"    color:#FFFFFF;\n"
"}")
        self.widget_frame.setObjectName("widget_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_titlebar_icon = QtWidgets.QLabel(parent=self.widget_frame)
        self.lbl_titlebar_icon.setMinimumSize(QtCore.QSize(24, 24))
        self.lbl_titlebar_icon.setMaximumSize(QtCore.QSize(24, 24))
        self.lbl_titlebar_icon.setText("")
        self.lbl_titlebar_icon.setPixmap(QtGui.QPixmap(":/yeniÖnek/fifsot_icons/F_Icon_1.png"))
        self.lbl_titlebar_icon.setScaledContents(True)
        self.lbl_titlebar_icon.setObjectName("lbl_titlebar_icon")
        self.horizontalLayout.addWidget(self.lbl_titlebar_icon)
        self.lbl_titlebar_text = QtWidgets.QLabel(parent=self.widget_frame)
        self.lbl_titlebar_text.setObjectName("lbl_titlebar_text")
        self.horizontalLayout.addWidget(self.lbl_titlebar_text)
        spacerItem3 = QtWidgets.QSpacerItem(342, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_close_window = QtWidgets.QPushButton(parent=self.widget_frame)
        self.btn_close_window.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_close_window.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_close_window.setText("")
        self.btn_close_window.setObjectName("btn_close_window")
        self.horizontalLayout.addWidget(self.btn_close_window)
        self.gridLayout.addWidget(self.widget_frame, 0, 0, 1, 1)
        self.lbl_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_text.setFont(font)
        self.lbl_text.setWordWrap(True)
        self.lbl_text.setIndent(16)
        self.lbl_text.setObjectName("lbl_text")
        self.gridLayout.addWidget(self.lbl_text, 10, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.lbl_header_icon = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_header_icon.setMinimumSize(QtCore.QSize(32, 32))
        self.lbl_header_icon.setMaximumSize(QtCore.QSize(32, 32))
        self.lbl_header_icon.setText("")
        self.lbl_header_icon.setPixmap(QtGui.QPixmap(":/yeniÖnek/fifsot_icons/info_blue.png"))
        self.lbl_header_icon.setScaledContents(True)
        self.lbl_header_icon.setObjectName("lbl_header_icon")
        self.horizontalLayout_3.addWidget(self.lbl_header_icon)
        self.lbl_about_fifsot = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_about_fifsot.setMinimumSize(QtCore.QSize(170, 20))
        self.lbl_about_fifsot.setMaximumSize(QtCore.QSize(170, 20))
        self.lbl_about_fifsot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_about_fifsot.setWordWrap(True)
        self.lbl_about_fifsot.setIndent(8)
        self.lbl_about_fifsot.setObjectName("lbl_about_fifsot")
        self.horizontalLayout_3.addWidget(self.lbl_about_fifsot)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem6, 11, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem8, 7, 0, 1, 1)
        self.lbl_version = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_version.setMinimumSize(QtCore.QSize(382, 20))
        self.lbl_version.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_version.setFont(font)
        self.lbl_version.setWordWrap(True)
        self.lbl_version.setIndent(16)
        self.lbl_version.setObjectName("lbl_version")
        self.gridLayout.addWidget(self.lbl_version, 6, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(100, 0))
        self.widget.setStyleSheet("QPushButton {\n"
"    color:#000000;\n"
"    background-color:#40E0D0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color:#555555;\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_visit_github = QtWidgets.QPushButton(parent=self.widget)
        self.btn_visit_github.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_visit_github.setMaximumSize(QtCore.QSize(16777215, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/yeniÖnek/fifsot_icons/github_black.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_visit_github.setIcon(icon)
        self.btn_visit_github.setObjectName("btn_visit_github")
        self.gridLayout_2.addWidget(self.btn_visit_github, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.gridLayout.addLayout(self.horizontalLayout_4, 12, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AboutWindow"))
        self.lbl_note.setText(_translate("MainWindow", "Note:"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
        self.lbl_version_header.setText(_translate("MainWindow", "Version:"))
        self.lbl_titlebar_text.setText(_translate("MainWindow", "About"))
        self.lbl_text.setText(_translate("MainWindow", "Check the GitHub page for features, warnings, terms of use, and upcoming updates. Always make sure to follow the terms and warnings. Details are available on GitHub."))
        self.lbl_about_fifsot.setText(_translate("MainWindow", "About FIFSOT"))
        self.lbl_version.setText(_translate("MainWindow", "v1.0.0 - Beta"))
        self.btn_visit_github.setText(_translate("MainWindow", "Visit GitHub"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
