import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon
from scenario_widgets.DynamicWidget import DynamicWidget
from Transactions.Directory_Transactions import Transaction

class SimpleApp(QWidget, DynamicWidget):
    def __init__(self, recordDict:dict|None = None):
        super().__init__()

        self.transaction = Transaction()
        self.func = self.transaction.remove_empty_directories
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "R.E.D."

        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(17, 43, 591, 81))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, -1, 25, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_address = QLabel(self.widget)
        self.lbl_address.setObjectName(u"lbl_address")
        self.lbl_address.setMinimumSize(QSize(75, 20))
        self.lbl_address.setMaximumSize(QSize(75, 20))
        self.lbl_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_address)

        self.lineEdit_address = QLineEdit(self.widget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(430, 25))
        self.lineEdit_address.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_address.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_address)

        self.btn_openDialog_address = QPushButton(self.widget)
        self.btn_openDialog_address.setObjectName(u"btn_openDialog_address")
        self.btn_openDialog_address.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_address.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/yeniÖnek/fifsot_icons/open_file_dialog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_openDialog_address.setIcon(icon)
        self.btn_openDialog_address.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_openDialog_address)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.checkBox_deleteObjectsInSymlinks = QCheckBox(self.widget)
        self.checkBox_deleteObjectsInSymlinks.setObjectName(u"checkBox_deleteObjectsInSymlinks")
        self.checkBox_deleteObjectsInSymlinks.setMinimumSize(QSize(0, 20))
        self.checkBox_deleteObjectsInSymlinks.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_4.addWidget(self.checkBox_deleteObjectsInSymlinks)

        self.checkBox_recursive = QCheckBox(self.widget)
        self.checkBox_recursive.setObjectName(u"checkBox_recursive")
        self.checkBox_recursive.setMinimumSize(QSize(0, 20))
        self.checkBox_recursive.setMaximumSize(QSize(16777215, 20))
        self.checkBox_recursive.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_recursive)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi()

        self.widget.setLayout(self.gridLayout)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)

    def retranslateUi(self):
        self.lbl_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.lineEdit_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_address.setText("")
        self.checkBox_deleteObjectsInSymlinks.setText(QCoreApplication.translate("MainWindow", u"Delete Objects in Symlinks", None))
        self.checkBox_recursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
    
    def run(self):
        address = self.lineEdit_address.text()
        inSymlink = self.checkBox_deleteObjectsInSymlinks.isChecked()
        recursive = self.checkBox_recursive.isChecked()

        # call function for delete operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        obj_addr=address,
                                                        in_symlink_ok=inSymlink,
                                                        recursive=recursive)


if __name__ == '__main__':
    pass