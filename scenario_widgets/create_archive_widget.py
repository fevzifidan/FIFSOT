import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction
from os import path

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.create_archive
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Create Archive"
        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 761, 251))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_archiveAddress = QLabel(self.widget)
        self.lbl_archiveAddress.setObjectName(u"lbl_archiveAddress")
        self.lbl_archiveAddress.setMinimumSize(QSize(230, 25))
        self.lbl_archiveAddress.setMaximumSize(QSize(230, 25))
        self.lbl_archiveAddress.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_archiveAddress)

        self.lineEdit_archiveAddress = QLineEdit(self.widget)
        self.lineEdit_archiveAddress.setObjectName(u"lineEdit_archiveAddress")
        self.lineEdit_archiveAddress.setMinimumSize(QSize(280, 25))
        self.lineEdit_archiveAddress.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_archiveAddress.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_archiveAddress)

        self.btn_openDialog_archiveAddress = QPushButton(self.widget)
        self.btn_openDialog_archiveAddress.setObjectName(u"btn_openDialog_archiveAddress")
        self.btn_openDialog_archiveAddress.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_archiveAddress.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/yeniÖnek/fifsot_icons/open_file_dialog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_openDialog_archiveAddress.setIcon(icon)
        self.btn_openDialog_archiveAddress.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_openDialog_archiveAddress)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_archiveName = QLabel(self.widget)
        self.lbl_archiveName.setObjectName(u"lbl_archiveName")
        self.lbl_archiveName.setMinimumSize(QSize(230, 25))
        self.lbl_archiveName.setMaximumSize(QSize(230, 25))
        self.lbl_archiveName.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lbl_archiveName)

        self.lineEdit_archiveName = QLineEdit(self.widget)
        self.lineEdit_archiveName.setObjectName(u"lineEdit_archiveName")
        self.lineEdit_archiveName.setMinimumSize(QSize(280, 25))
        self.lineEdit_archiveName.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_archiveName.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_archiveName)

        self.horizontalSpacer_5 = QSpacerItem(26, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_rootDirectory = QLabel(self.widget)
        self.lbl_rootDirectory.setObjectName(u"lbl_rootDirectory")
        self.lbl_rootDirectory.setMinimumSize(QSize(230, 25))
        self.lbl_rootDirectory.setMaximumSize(QSize(230, 25))
        self.lbl_rootDirectory.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_rootDirectory)

        self.lineEdit_rootDirectory = QLineEdit(self.widget)
        self.lineEdit_rootDirectory.setObjectName(u"lineEdit_rootDirectory")
        self.lineEdit_rootDirectory.setMinimumSize(QSize(394, 25))
        self.lineEdit_rootDirectory.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_rootDirectory.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_rootDirectory)

        self.btn_openDialog_rootDirectory = QPushButton(self.widget)
        self.btn_openDialog_rootDirectory.setObjectName(u"btn_openDialog_rootDirectory")
        self.btn_openDialog_rootDirectory.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_rootDirectory.setMaximumSize(QSize(20, 20))
        self.btn_openDialog_rootDirectory.setIcon(icon)
        self.btn_openDialog_rootDirectory.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_openDialog_rootDirectory)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_baseDirectory = QLabel(self.widget)
        self.lbl_baseDirectory.setObjectName(u"lbl_baseDirectory")
        self.lbl_baseDirectory.setMinimumSize(QSize(230, 25))
        self.lbl_baseDirectory.setMaximumSize(QSize(230, 25))
        self.lbl_baseDirectory.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_baseDirectory)

        self.lineEdit_baseDirectory = QLineEdit(self.widget)
        self.lineEdit_baseDirectory.setObjectName(u"lineEdit_baseDirectory")
        self.lineEdit_baseDirectory.setMinimumSize(QSize(394, 25))
        self.lineEdit_baseDirectory.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_baseDirectory.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_baseDirectory)

        self.btn_openDialog_baseDirectory = QPushButton(self.widget)
        self.btn_openDialog_baseDirectory.setObjectName(u"btn_openDialog_baseDirectory")
        self.btn_openDialog_baseDirectory.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_baseDirectory.setMaximumSize(QSize(20, 20))
        self.btn_openDialog_baseDirectory.setIcon(icon)
        self.btn_openDialog_baseDirectory.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_openDialog_baseDirectory)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_format = QLabel(self.widget)
        self.lbl_format.setObjectName(u"lbl_format")
        self.lbl_format.setMinimumSize(QSize(230, 25))
        self.lbl_format.setMaximumSize(QSize(230, 25))
        self.lbl_format.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_format)

        self.comboBox_format = QComboBox(self.widget)
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.setObjectName(u"comboBox_format")
        self.comboBox_format.setMinimumSize(QSize(100, 25))
        self.comboBox_format.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_4.addWidget(self.comboBox_format)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(235, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.btn_copyResultAddress = QPushButton(self.widget)
        self.btn_copyResultAddress.setObjectName(u"btn_copyResultAddress")

        self.horizontalLayout_11.addWidget(self.btn_copyResultAddress)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_11)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi()

        self.widget.setLayout(self.gridLayout)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)

    def retranslateUi(self):
        self.lbl_archiveAddress.setText(QCoreApplication.translate("MainWindow", u"Archive Address:", None))
        self.lineEdit_archiveAddress.setText("")
        self.lineEdit_archiveAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_archiveAddress.setText("")
        self.lbl_archiveName.setText(QCoreApplication.translate("MainWindow", u"Archive Name (Without Any Extension):", None))
        self.lineEdit_archiveName.setText("")
        self.lineEdit_archiveName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Compulsory--", None))
        self.lbl_rootDirectory.setText(QCoreApplication.translate("MainWindow", u"Root Directory:", None))
        self.lineEdit_rootDirectory.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_rootDirectory.setText("")
        self.lbl_baseDirectory.setText(QCoreApplication.translate("MainWindow", u"Base Directory:", None))
        self.lineEdit_baseDirectory.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_baseDirectory.setText("")
        self.lbl_format.setText(QCoreApplication.translate("MainWindow", u"Format:", None))
        self.comboBox_format.setItemText(0, QCoreApplication.translate("MainWindow", u"zip", None))
        self.comboBox_format.setItemText(1, QCoreApplication.translate("MainWindow", u"tar", None))
        self.comboBox_format.setItemText(2, QCoreApplication.translate("MainWindow", u"gztar", None))
        self.comboBox_format.setItemText(3, QCoreApplication.translate("MainWindow", u"bztar", None))
        self.comboBox_format.setItemText(4, QCoreApplication.translate("MainWindow", u"xztar", None))

        self.btn_copyResultAddress.setText(QCoreApplication.translate("MainWindow", u"Copy Result Address", None))
    
    def run(self):
        # params
        archiveAddress = self.lineEdit_archiveAddress.text()
        archiveName = self.lineEdit_archiveName.text()
        rootDirectory = self.lineEdit_rootDirectory.text()
        baseDirectory = self.lineEdit_baseDirectory.text()
        archiveFormat = self.comboBox_format.currentText()

        # create the destination path
        archiveAddress = path.join(archiveAddress, archiveName)

        # arrange base directory if specified
        if baseDirectory:
            # When it is selected via the dialog, the path of baseDirectory
            # that is common with rootDirectory should be deleted.
            commonPath = path.commonpath([rootDirectory, baseDirectory])
            baseDirectory = path.relpath(baseDirectory, commonPath)

            if baseDirectory == ".": baseDirectory = None

        # call function to create archive
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        base_name=archiveAddress, format=archiveFormat,
                                                        root_dir=rootDirectory, base_dir=baseDirectory)


if __name__ == '__main__':
    pass