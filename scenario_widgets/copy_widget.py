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
        self.func = self.transaction.copy
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Copy"
        self.prepare(recordDict)
    
    def prepare(self, recordDict:dict|None = None):
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 50, 698, 421))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_source = QLabel(self.widget)
        self.lbl_source.setObjectName(u"lbl_source")
        self.lbl_source.setMinimumSize(QSize(75, 20))
        self.lbl_source.setMaximumSize(QSize(75, 20))
        self.lbl_source.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_source)

        self.lineEdit_source = QLineEdit(self.widget)
        self.lineEdit_source.setObjectName(u"lineEdit_source")
        self.lineEdit_source.setMinimumSize(QSize(430, 25))
        self.lineEdit_source.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_source)

        self.btn_openDialog_source = QPushButton(self.widget)
        self.btn_openDialog_source.setObjectName(u"btn_openDialog_source")
        self.btn_openDialog_source.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_source.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/yeniÖnek/fifsot_icons/open_file_dialog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_openDialog_source.setIcon(icon)
        self.btn_openDialog_source.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_openDialog_source)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_destination = QLabel(self.widget)
        self.lbl_destination.setObjectName(u"lbl_destination")
        self.lbl_destination.setMinimumSize(QSize(75, 20))
        self.lbl_destination.setMaximumSize(QSize(75, 20))
        self.lbl_destination.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_destination)

        self.lineEdit_destination = QLineEdit(self.widget)
        self.lineEdit_destination.setObjectName(u"lineEdit_destination")
        self.lineEdit_destination.setMinimumSize(QSize(430, 25))
        self.lineEdit_destination.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_destination)

        self.btn_openDialog_destination = QPushButton(self.widget)
        self.btn_openDialog_destination.setObjectName(u"btn_openDialog_destination")
        self.btn_openDialog_destination.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_destination.setMaximumSize(QSize(20, 20))
        self.btn_openDialog_destination.setIcon(icon)
        self.btn_openDialog_destination.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_openDialog_destination)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_name = QLabel(self.widget)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setMinimumSize(QSize(75, 20))
        self.lbl_name.setMaximumSize(QSize(75, 20))
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lbl_name)

        self.lineEdit_name = QLineEdit(self.widget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(430, 25))
        self.lineEdit_name.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_name)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(8, -1, -1, -1)
        self.checkBox_symlinks = QCheckBox(self.widget)
        self.checkBox_symlinks.setObjectName(u"checkBox_symlinks")
        self.checkBox_symlinks.setMinimumSize(QSize(0, 16))
        self.checkBox_symlinks.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.checkBox_symlinks, 1, 0, 1, 1)

        self.checkBox_mergeContentOnly = QCheckBox(self.widget)
        self.checkBox_mergeContentOnly.setObjectName(u"checkBox_mergeContentOnly")
        self.checkBox_mergeContentOnly.setMinimumSize(QSize(0, 16))
        self.checkBox_mergeContentOnly.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.checkBox_mergeContentOnly, 0, 1, 1, 1)

        self.checkBox_skipExistingOnes = QCheckBox(self.widget)
        self.checkBox_skipExistingOnes.setObjectName(u"checkBox_skipExistingOnes")
        self.checkBox_skipExistingOnes.setMinimumSize(QSize(0, 16))
        self.checkBox_skipExistingOnes.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.checkBox_skipExistingOnes, 0, 2, 1, 1)

        self.checkBox_copyMetaData = QCheckBox(self.widget)
        self.checkBox_copyMetaData.setObjectName(u"checkBox_copyMetaData")
        self.checkBox_copyMetaData.setMinimumSize(QSize(0, 16))
        self.checkBox_copyMetaData.setMaximumSize(QSize(16777215, 16))
        self.checkBox_copyMetaData.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_copyMetaData, 1, 1, 1, 1)

        self.checkBox_onlyFiles = QCheckBox(self.widget)
        self.checkBox_onlyFiles.setObjectName(u"checkBox_onlyFiles")
        self.checkBox_onlyFiles.setMinimumSize(QSize(0, 16))
        self.checkBox_onlyFiles.setMaximumSize(QSize(16777215, 16))
        self.checkBox_onlyFiles.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.checkBox_onlyFiles, 0, 0, 1, 1)

        self.checkBox_recursive = QCheckBox(self.widget)
        self.checkBox_recursive.setObjectName(u"checkBox_recursive")
        self.checkBox_recursive.setMinimumSize(QSize(0, 16))
        self.checkBox_recursive.setMaximumSize(QSize(16777215, 16))
        self.checkBox_recursive.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_recursive, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_keepAsTemp = QCheckBox(self.widget)
        self.checkBox_keepAsTemp.setObjectName(u"checkBox_keepAsTemp")
        self.checkBox_keepAsTemp.setMinimumSize(QSize(100, 20))
        self.checkBox_keepAsTemp.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_6.addWidget(self.checkBox_keepAsTemp)

        self.lbl_tempID = QLabel(self.widget)
        self.lbl_tempID.setObjectName(u"lbl_tempID")
        self.lbl_tempID.setMinimumSize(QSize(200, 20))
        self.lbl_tempID.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.lbl_tempID)

        self.btn_copyTempID = QPushButton(self.widget)
        self.btn_copyTempID.setObjectName(u"btn_copyTempID")
        self.btn_copyTempID.setMinimumSize(QSize(16, 16))
        self.btn_copyTempID.setMaximumSize(QSize(16, 16))
        self.btn_copyTempID.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.btn_copyTempID)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi()

        self.widget.setLayout(self.gridLayout_2)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)

    def retranslateUi(self):
        self.lbl_source.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.lineEdit_source.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_source.setText("")
        self.lbl_destination.setText(QCoreApplication.translate("MainWindow", u"Destination:", None))
        self.lineEdit_destination.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_destination.setText("")
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Optional, depends on your destination.--", None))
        self.checkBox_symlinks.setText(QCoreApplication.translate("MainWindow", u"Symlinks", None))
        self.checkBox_mergeContentOnly.setText(QCoreApplication.translate("MainWindow", u"Merge Content Only", None))
        self.checkBox_skipExistingOnes.setText(QCoreApplication.translate("MainWindow", u"Skip Existing Ones", None))
        self.checkBox_copyMetaData.setText(QCoreApplication.translate("MainWindow", u"Copy Meta Data", None))
        self.checkBox_onlyFiles.setText(QCoreApplication.translate("MainWindow", u"Only Files", None))
        self.checkBox_recursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
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
        self.checkBox_keepAsTemp.setText(QCoreApplication.translate("MainWindow", u"Keep as Temp", None))
        self.lbl_tempID.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_copyTempID.setText("")
    
    def run(self):
        source = self.lineEdit_source.text()
        destination = self.lineEdit_destination.text()
        name = self.lineEdit_name.text()

        if name:
            destination = path.join(destination, name)
        
        # params
        onlyFiles = self.checkBox_onlyFiles.isChecked()
        mergeContentOnly = self.checkBox_mergeContentOnly.isChecked()
        skipExistingOnes = self.checkBox_skipExistingOnes.isChecked()
        symlinks = self.checkBox_symlinks.isChecked()
        copyMetaData = self.checkBox_copyMetaData.isChecked()
        recursive = self.checkBox_recursive.isChecked()

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
        
        # call copy function
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        src=source, dest=destination,
                                                        only_files=onlyFiles,
                                                        merge_content_only=mergeContentOnly,
                                                        skip_existing_ones=skipExistingOnes,
                                                        symlinks=symlinks, copyMetaData=copyMetaData,
                                                        recursive=recursive)


if __name__ == '__main__':
    pass