# Form implementation generated from reading ui file 'pages\rename_ui.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from ui_files import resources_rc

from Customs.CustomLineEdit import CustomLineEdit
QtWidgets.QLineEdit = CustomLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        MainWindow.resize(698, 320)
        MainWindow.setMinimumSize(QtCore.QSize(698, 320))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 338))
        MainWindow.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"    color:#F0F0F0;\n"
"    font:bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color:#555555;\n"
"    border:1px solid #555555;\n"
"    border-radius:10px;\n"
"    padding-left:10px;\n"
"    color:#F0F0F0;\n"
"}\n"
"\n"
"QCheckBox{\n"
"    color:#F0F0F0;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image:url(\":/yeniÖnek/fifsot_icons/checked_square.png\");\n"
"    width:16px;\n"
"    height:16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image:url(\":/yeniÖnek/fifsot_icons/square.png\");\n"
"    width:16px;\n"
"    height:16px;\n"
"}\n"
"\n"
"#rename_header{\n"
"    color:#40E0D0;\n"
"    font:24px;\n"
"    padding:0px;\n"
"}\n"
"\n"
"#comboBox_case{\n"
"    background-color:#555555;\n"
"    color:#F0F0F0;\n"
"    border-radius:10px;\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"#comboBox_case QAbstractItemView::item{\n"
"    min-height:30px;\n"
"}\n"
"\n"
"#comboBox_case::drop-down{\n"
"    border:none;\n"
"}\n"
"\n"
"#comboBox_case::down-arrow{\n"
"    background-color:transparent;\n"
"    image:url(\":/yeniÖnek/fifsot_icons/down_arrow_blue.png\");\n"
"    width:12px;\n"
"    height:12px;\n"
"    padding-right:5px;\n"
"}\n"
"\n"
"#comboBox_case::down-arrow:on{\n"
"    background-color:transparent;\n"
"    image:url(\":/yeniÖnek/fifsot_icons/up_arrow_blue.png\");\n"
"    width:12px;\n"
"    height:12px;\n"
"    padding-right:5px;\n"
"}\n"
"\n"
"#comboBox_case QListView{\n"
"    background-color:#555555;\n"
"    selection-color:#000000;\n"
"    selection-background-color:#40E0D0;\n"
"    color:#F0F0F0;\n"
"    padding:5px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    background-color:#555555;\n"
"    color:#F0F0F0;\n"
"}\n"
"\n"
"QSpinBox:up-button{\n"
"    subcontrol-position:right;\n"
"    width:12px;\n"
"    height:12px;\n"
"    image:url(\":/yeniÖnek/fifsot_icons/up_arrow_white.png\");\n"
"}\n"
"\n"
"QSpinBox:up-button:hover{\n"
"    image:url(\":/yeniÖnek/fifsot_icons/up_arrow_blue.png\");\n"
"}\n"
"\n"
"QSpinBox:down-button{\n"
"    subcontrol-position:left;\n"
"    width:12px;\n"
"    height:12px;\n"
"    image:url(\":/yeniÖnek/fifsot_icons/down_arrow_white.png\");\n"
"}\n"
"\n"
"QSpinBox:down-button:hover{\n"
"    subcontrol-position:left;\n"
"    width:12px;\n"
"    height:12px;\n"
"    image:url(\":/yeniÖnek/fifsot_icons/down_arrow_blue.png\");\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color:#101524;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_frame = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_frame.setMinimumSize(QtCore.QSize(0, 42))
        self.widget_frame.setMaximumSize(QtCore.QSize(16777215, 42))
        self.widget_frame.setStyleSheet("QWidget[objectName=\"widget_frame\"]{\n"
"    background-color:#3B3B3B;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:none;\n"
"    border-radius:0px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:none;\n"
"    color:#FFFFFF;\n"
"}\n"
"\n"
"#lbl_titlebar_text{\n"
"    font:12px;\n"
"}\n"
"\n"
"#btn_close_window{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_white.png\");\n"
"}\n"
"\n"
"#btn_close_window:hover{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_red.png\");\n"
"}\n"
"\n"
"#btn_close_window:pressed{\n"
"    icon:url(\":/yeniÖnek/fifsot_icons/close_1_white.png\");\n"
"}")
        self.widget_frame.setObjectName("widget_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_titlebar_icon = QtWidgets.QLabel(parent=self.widget_frame)
        self.lbl_titlebar_icon.setMinimumSize(QtCore.QSize(24, 24))
        self.lbl_titlebar_icon.setMaximumSize(QtCore.QSize(24, 24))
        self.lbl_titlebar_icon.setText("")
        self.lbl_titlebar_icon.setPixmap(QtGui.QPixmap(":/yeniÖnek/fifsot_icons/F_Icon_1.png"))
        self.lbl_titlebar_icon.setScaledContents(True)
        self.lbl_titlebar_icon.setObjectName("lbl_titlebar_icon")
        self.horizontalLayout_7.addWidget(self.lbl_titlebar_icon)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.lbl_titlebar_text = QtWidgets.QLabel(parent=self.widget_frame)
        self.lbl_titlebar_text.setMinimumSize(QtCore.QSize(0, 24))
        self.lbl_titlebar_text.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lbl_titlebar_text.setObjectName("lbl_titlebar_text")
        self.horizontalLayout_7.addWidget(self.lbl_titlebar_text)
        spacerItem1 = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btn_close_window = QtWidgets.QPushButton(parent=self.widget_frame)
        self.btn_close_window.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_close_window.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_close_window.setText("")
        self.btn_close_window.setObjectName("btn_close_window")
        self.horizontalLayout_7.addWidget(self.btn_close_window)
        self.verticalLayout_2.addWidget(self.widget_frame)
        self.rename_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.rename_header.setMinimumSize(QtCore.QSize(590, 35))
        self.rename_header.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rename_header.setFont(font)
        self.rename_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rename_header.setObjectName("rename_header")
        self.verticalLayout_2.addWidget(self.rename_header)
        self.rename_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.rename_text.setMinimumSize(QtCore.QSize(590, 50))
        self.rename_text.setMaximumSize(QtCore.QSize(16777215, 50))
        self.rename_text.setWordWrap(True)
        self.rename_text.setIndent(16)
        self.rename_text.setObjectName("rename_text")
        self.verticalLayout_2.addWidget(self.rename_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_address = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_address.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_address.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_address.setObjectName("lbl_address")
        self.horizontalLayout.addWidget(self.lbl_address)
        self.lineEdit_address = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_address.setMinimumSize(QtCore.QSize(400, 25))
        self.lineEdit_address.setClearButtonEnabled(True)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.horizontalLayout.addWidget(self.lineEdit_address)
        self.btn_openDialog_address = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_openDialog_address.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_openDialog_address.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_openDialog_address.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/yeniÖnek/fifsot_icons/open_file_dialog.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_openDialog_address.setIcon(icon)
        self.btn_openDialog_address.setIconSize(QtCore.QSize(20, 20))
        self.btn_openDialog_address.setObjectName("btn_openDialog_address")
        self.horizontalLayout.addWidget(self.btn_openDialog_address)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_prefix = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_prefix.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_prefix.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_prefix.setObjectName("lbl_prefix")
        self.horizontalLayout_2.addWidget(self.lbl_prefix)
        self.lineEdit_prefix = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_prefix.setMinimumSize(QtCore.QSize(170, 25))
        self.lineEdit_prefix.setClearButtonEnabled(True)
        self.lineEdit_prefix.setObjectName("lineEdit_prefix")
        self.horizontalLayout_2.addWidget(self.lineEdit_prefix)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_suffix = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_suffix.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_suffix.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_suffix.setObjectName("lbl_suffix")
        self.horizontalLayout_3.addWidget(self.lbl_suffix)
        self.lineEdit_suffix = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_suffix.setMinimumSize(QtCore.QSize(168, 25))
        self.lineEdit_suffix.setClearButtonEnabled(True)
        self.lineEdit_suffix.setObjectName("lineEdit_suffix")
        self.horizontalLayout_3.addWidget(self.lineEdit_suffix)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_case = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_case.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_case.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_case.setObjectName("lbl_case")
        self.horizontalLayout_4.addWidget(self.lbl_case)
        self.comboBox_case = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_case.setMinimumSize(QtCore.QSize(130, 25))
        self.comboBox_case.setObjectName("comboBox_case")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_case)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_start = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_start.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_start.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_start.setObjectName("lbl_start")
        self.horizontalLayout_5.addWidget(self.lbl_start)
        self.spinBox_start = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_start.setMinimumSize(QtCore.QSize(74, 25))
        self.spinBox_start.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_start.setMaximum(1000000)
        self.spinBox_start.setProperty("value", 1)
        self.spinBox_start.setObjectName("spinBox_start")
        self.horizontalLayout_5.addWidget(self.spinBox_start)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_zfill = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_zfill.setMinimumSize(QtCore.QSize(45, 20))
        self.lbl_zfill.setMaximumSize(QtCore.QSize(45, 20))
        self.lbl_zfill.setObjectName("lbl_zfill")
        self.horizontalLayout_6.addWidget(self.lbl_zfill)
        self.spinBox_zfill = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_zfill.setMinimumSize(QtCore.QSize(74, 25))
        self.spinBox_zfill.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_zfill.setMinimum(1)
        self.spinBox_zfill.setMaximum(7)
        self.spinBox_zfill.setObjectName("spinBox_zfill")
        self.horizontalLayout_6.addWidget(self.spinBox_zfill)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.checkBox_onlyFiles = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_onlyFiles.setMinimumSize(QtCore.QSize(100, 25))
        self.checkBox_onlyFiles.setObjectName("checkBox_onlyFiles")
        self.horizontalLayout_10.addWidget(self.checkBox_onlyFiles)
        self.checkBox_reversed = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_reversed.setMinimumSize(QtCore.QSize(100, 25))
        self.checkBox_reversed.setObjectName("checkBox_reversed")
        self.horizontalLayout_10.addWidget(self.checkBox_reversed)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widget_btn_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_btn_container.setMinimumSize(QtCore.QSize(430, 50))
        self.widget_btn_container.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_btn_container.setStyleSheet("QWidget[objectName=\"widget_btn_container\"]{\n"
"    background-color:#3B3B3B;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#40E0D0;\n"
"    border:2px solid #40E0D0;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:2px solid #2BA699;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color:#555555;\n"
"}")
        self.widget_btn_container.setObjectName("widget_btn_container")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_btn_container)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.btn_rename = QtWidgets.QPushButton(parent=self.widget_btn_container)
        self.btn_rename.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_rename.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_rename.setObjectName("btn_rename")
        self.horizontalLayout_11.addWidget(self.btn_rename)
        self.verticalLayout_2.addWidget(self.widget_btn_container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenameWindow"))
        self.lbl_titlebar_text.setText(_translate("MainWindow", "Rename"))
        self.rename_header.setText(_translate("MainWindow", "Rename"))
        self.rename_text.setText(_translate("MainWindow", "Do you need to name your files according to a specific name pattern and criteria at once? Just describe the pattern and we will do the rest."))
        self.lbl_address.setText(_translate("MainWindow", "Address:"))
        self.lineEdit_address.setPlaceholderText(_translate("MainWindow", "Select or drag and drop"))
        self.lbl_prefix.setText(_translate("MainWindow", "Prefix:"))
        self.lineEdit_prefix.setPlaceholderText(_translate("MainWindow", "--Optional--"))
        self.lbl_suffix.setText(_translate("MainWindow", "Suffix:"))
        self.lineEdit_suffix.setPlaceholderText(_translate("MainWindow", "--Optional--"))
        self.lbl_case.setText(_translate("MainWindow", "Case:"))
        self.comboBox_case.setItemText(0, _translate("MainWindow", "Alphabetical"))
        self.comboBox_case.setItemText(1, _translate("MainWindow", "Creation Time"))
        self.comboBox_case.setItemText(2, _translate("MainWindow", "Last Modification Time"))
        self.comboBox_case.setItemText(3, _translate("MainWindow", "Last Access Time"))
        self.comboBox_case.setItemText(4, _translate("MainWindow", "File Size"))
        self.lbl_start.setText(_translate("MainWindow", "Start:"))
        self.lbl_zfill.setText(_translate("MainWindow", "Zfill:"))
        self.checkBox_onlyFiles.setText(_translate("MainWindow", "Only Files"))
        self.checkBox_reversed.setText(_translate("MainWindow", "Reversed"))
        self.btn_rename.setText(_translate("MainWindow", "Rename Now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
