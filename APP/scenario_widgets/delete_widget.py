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
        self.func = self.transaction.delete
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Delete"
        self.prepare(recordDict)

    def prepare(self, recordDict:dict|None = None):
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 821, 301))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_address = QLabel(self.widget)
        self.lbl_address.setObjectName(u"lbl_address")
        self.lbl_address.setMinimumSize(QSize(75, 20))
        self.lbl_address.setMaximumSize(QSize(75, 20))
        self.lbl_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_address)

        self.lineEdit_address = QLineEdit(self.widget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(430, 25))
        self.lineEdit_address.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_address)

        self.btn_openDialog_address = QPushButton(self.widget)
        self.btn_openDialog_address.setObjectName(u"btn_openDialog_address")
        self.btn_openDialog_address.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_address.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/yeni/Önek/fifsot_icons/open_file_dialog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_openDialog_address.setIcon(icon)
        self.btn_openDialog_address.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_openDialog_address)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(8, -1, -1, -1)
        self.checkBox_onlyContent = QCheckBox(self.widget)
        self.checkBox_onlyContent.setObjectName(u"checkBox_onlyContent")
        self.checkBox_onlyContent.setMinimumSize(QSize(0, 16))
        self.checkBox_onlyContent.setMaximumSize(QSize(16777215, 16))
        self.checkBox_onlyContent.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_onlyContent, 1, 0, 1, 1)

        self.checkBox_deleteObjectsInSymlinks = QCheckBox(self.widget)
        self.checkBox_deleteObjectsInSymlinks.setObjectName(u"checkBox_deleteObjectsInSymlinks")
        self.checkBox_deleteObjectsInSymlinks.setMinimumSize(QSize(0, 16))
        self.checkBox_deleteObjectsInSymlinks.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_2.addWidget(self.checkBox_deleteObjectsInSymlinks, 0, 1, 1, 1)

        self.checkBox_followSymlinks = QCheckBox(self.widget)
        self.checkBox_followSymlinks.setObjectName(u"checkBox_followSymlinks")
        self.checkBox_followSymlinks.setMinimumSize(QSize(0, 16))
        self.checkBox_followSymlinks.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_2.addWidget(self.checkBox_followSymlinks, 0, 2, 1, 1)

        self.checkBox_recursive = QCheckBox(self.widget)
        self.checkBox_recursive.setObjectName(u"checkBox_recursive")
        self.checkBox_recursive.setMinimumSize(QSize(0, 16))
        self.checkBox_recursive.setMaximumSize(QSize(16777215, 16))
        self.checkBox_recursive.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_recursive, 1, 1, 1, 1)

        self.checkBox_onlyFiles = QCheckBox(self.widget)
        self.checkBox_onlyFiles.setObjectName(u"checkBox_onlyFiles")
        self.checkBox_onlyFiles.setMinimumSize(QSize(0, 16))
        self.checkBox_onlyFiles.setMaximumSize(QSize(16777215, 16))
        self.checkBox_onlyFiles.setIconSize(QSize(16, 16))

        self.gridLayout_2.addWidget(self.checkBox_onlyFiles, 0, 0, 1, 1)

        self.checkBox_forcePermission = QCheckBox(self.widget)
        self.checkBox_forcePermission.setObjectName(u"checkBox_forcePermission")
        self.checkBox_forcePermission.setMinimumSize(QSize(0, 16))
        self.checkBox_forcePermission.setMaximumSize(QSize(16777215, 16))
        self.checkBox_forcePermission.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_forcePermission, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.lbl_conditions = QLabel(self.widget)
        self.lbl_conditions.setObjectName(u"lbl_conditions")
        self.lbl_conditions.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_conditions)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_extension = QLabel(self.widget)
        self.lbl_extension.setObjectName(u"lbl_extension")
        self.lbl_extension.setMinimumSize(QSize(105, 20))
        self.lbl_extension.setMaximumSize(QSize(16777215, 20))
        self.lbl_extension.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_extension)

        self.lineEdit_extension = QLineEdit(self.widget)
        self.lineEdit_extension.setObjectName(u"lineEdit_extension")
        self.lineEdit_extension.setMinimumSize(QSize(204, 25))
        self.lineEdit_extension.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_extension.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_extension)

        self.lbl_excludeNameStartswith = QLabel(self.widget)
        self.lbl_excludeNameStartswith.setObjectName(u"lbl_excludeNameStartswith")
        self.lbl_excludeNameStartswith.setMinimumSize(QSize(145, 20))
        self.lbl_excludeNameStartswith.setMaximumSize(QSize(16777215, 20))
        self.lbl_excludeNameStartswith.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_excludeNameStartswith)

        self.lineEdit_excludeNameStartswith = QLineEdit(self.widget)
        self.lineEdit_excludeNameStartswith.setObjectName(u"lineEdit_excludeNameStartswith")
        self.lineEdit_excludeNameStartswith.setMinimumSize(QSize(204, 25))
        self.lineEdit_excludeNameStartswith.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_excludeNameStartswith.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_excludeNameStartswith)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_nameStartswith = QLabel(self.widget)
        self.lbl_nameStartswith.setObjectName(u"lbl_nameStartswith")
        self.lbl_nameStartswith.setMinimumSize(QSize(105, 20))
        self.lbl_nameStartswith.setMaximumSize(QSize(16777215, 20))
        self.lbl_nameStartswith.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_nameStartswith)

        self.lineEdit_nameStartswith = QLineEdit(self.widget)
        self.lineEdit_nameStartswith.setObjectName(u"lineEdit_nameStartswith")
        self.lineEdit_nameStartswith.setMinimumSize(QSize(204, 25))
        self.lineEdit_nameStartswith.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_nameStartswith.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_nameStartswith)

        self.lbl_excludeNameContains = QLabel(self.widget)
        self.lbl_excludeNameContains.setObjectName(u"lbl_excludeNameContains")
        self.lbl_excludeNameContains.setMinimumSize(QSize(145, 20))
        self.lbl_excludeNameContains.setMaximumSize(QSize(16777215, 20))
        self.lbl_excludeNameContains.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_excludeNameContains.setIndent(2)

        self.horizontalLayout_4.addWidget(self.lbl_excludeNameContains)

        self.lineEdit_excludeNameContains = QLineEdit(self.widget)
        self.lineEdit_excludeNameContains.setObjectName(u"lineEdit_excludeNameContains")
        self.lineEdit_excludeNameContains.setMinimumSize(QSize(204, 25))
        self.lineEdit_excludeNameContains.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_excludeNameContains.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_excludeNameContains)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_nameContains = QLabel(self.widget)
        self.lbl_nameContains.setObjectName(u"lbl_nameContains")
        self.lbl_nameContains.setMinimumSize(QSize(105, 20))
        self.lbl_nameContains.setMaximumSize(QSize(16777215, 20))
        self.lbl_nameContains.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lbl_nameContains)

        self.lineEdit_nameContains = QLineEdit(self.widget)
        self.lineEdit_nameContains.setObjectName(u"lineEdit_nameContains")
        self.lineEdit_nameContains.setMinimumSize(QSize(204, 25))
        self.lineEdit_nameContains.setMaximumSize(QSize(204, 25))
        self.lineEdit_nameContains.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_nameContains)

        self.checkBox_caseInsensitive = QCheckBox(self.widget)
        self.checkBox_caseInsensitive.setObjectName(u"checkBox_caseInsensitive")
        self.checkBox_caseInsensitive.setMinimumSize(QSize(0, 20))
        self.checkBox_caseInsensitive.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_5.addWidget(self.checkBox_caseInsensitive)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi()

        self.widget.setLayout(self.gridLayout)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)

    def retranslateUi(self):
        self.lbl_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.lineEdit_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_address.setText("")
        self.checkBox_onlyContent.setText(QCoreApplication.translate("MainWindow", u"Only Content", None))
        self.checkBox_deleteObjectsInSymlinks.setText(QCoreApplication.translate("MainWindow", u"Delete Objects in Symlinks", None))
        self.checkBox_followSymlinks.setText(QCoreApplication.translate("MainWindow", u"Follow Symlinks", None))
        self.checkBox_recursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        self.checkBox_onlyFiles.setText(QCoreApplication.translate("MainWindow", u"Only Files", None))
        self.checkBox_forcePermission.setText(QCoreApplication.translate("MainWindow", u"Force Permissions", None))
        self.lbl_conditions.setText(QCoreApplication.translate("MainWindow", u"Conditions", None))
        self.lbl_extension.setText(QCoreApplication.translate("MainWindow", u"Extension:", None))
        self.lineEdit_extension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--All--", None))
        self.lbl_excludeNameStartswith.setText(QCoreApplication.translate("MainWindow", u"Exclude Name Startswith:", None))
        self.lineEdit_excludeNameStartswith.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--None--", None))
        self.lbl_nameStartswith.setText(QCoreApplication.translate("MainWindow", u"Name Startswith:", None))
        self.lineEdit_nameStartswith.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--All--", None))
        self.lbl_excludeNameContains.setText(QCoreApplication.translate("MainWindow", u"Exclude Name Contains:", None))
        self.lineEdit_excludeNameContains.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--None--", None))
        self.lbl_nameContains.setText(QCoreApplication.translate("MainWindow", u"Name Contains:", None))
        self.lineEdit_nameContains.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--All--", None))
        self.checkBox_caseInsensitive.setText(QCoreApplication.translate("MainWindow", u"Case Insensitive", None))
    
    def run(self):
        address = self.lineEdit_address.text()

        # params
        onlyFiles = self.checkBox_onlyFiles.isChecked()
        inSymlink = self.checkBox_deleteObjectsInSymlinks.isChecked()
        followSymlinks = self.checkBox_followSymlinks.isChecked()
        onlyContent = self.checkBox_onlyContent.isChecked()
        recursive = self.checkBox_recursive.isChecked()
        forcePermissions = self.checkBox_forcePermission.isChecked()

        # conditions
        extension = self.lineEdit_extension.text()
        nameStartswith = self.lineEdit_nameStartswith.text()
        nameContains = self.lineEdit_nameContains.text()
        excludeNameStartswith = self.lineEdit_excludeNameStartswith.text()
        excludeNameContains = self.lineEdit_excludeNameContains.text()
        caseInsensitive = self.checkBox_caseInsensitive.isChecked()

        # set conditions
        self.transaction.setCond(extension=extension, name_startswith=nameStartswith, contains=nameContains,
                                 excl_startswith=excludeNameStartswith, excl_contains=excludeNameContains,
                                 case_insensitive=caseInsensitive)
        
        # call function for delete operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        obj_addr=address, only_files=onlyFiles,
                                                        in_symlink_ok=inSymlink, follow_symlinks=followSymlinks,
                                                        only_content=onlyContent, recursive=recursive,
                                                        forcePermissions=forcePermissions)


if __name__ == '__main__':
    pass