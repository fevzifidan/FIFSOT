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
        self.func = self.transaction.rename
        self.transactionPerformer = self.getTransactionPerformer()

        self.transactionType = "Rename"

        self.prepare(recordDict)
    
    def prepare(self, recordDict:dict|None = None):
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 561, 251))
        self.widget.setMinimumSize(QSize(0, 251))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_address = QLabel(self.widget)
        self.lbl_address.setObjectName(u"lbl_address")
        self.lbl_address.setMinimumSize(QSize(45, 20))
        self.lbl_address.setMaximumSize(QSize(45, 20))

        self.horizontalLayout.addWidget(self.lbl_address)

        self.lineEdit_address = QLineEdit(self.widget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(400, 25))
        self.lineEdit_address.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_address)

        self.btn_openDialog_address = QPushButton(self.widget)
        self.btn_openDialog_address.setObjectName(u"btn_openDialog_address")
        self.btn_openDialog_address.setMinimumSize(QSize(20, 20))
        self.btn_openDialog_address.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/yeniÖnek/fifsot_icons/open_file_dialog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_openDialog_address.setIcon(icon)
        self.btn_openDialog_address.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_openDialog_address)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_prefix = QLabel(self.widget)
        self.lbl_prefix.setObjectName(u"lbl_prefix")
        self.lbl_prefix.setMinimumSize(QSize(45, 20))
        self.lbl_prefix.setMaximumSize(QSize(45, 20))

        self.horizontalLayout_2.addWidget(self.lbl_prefix)

        self.lineEdit_prefix = QLineEdit(self.widget)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")
        self.lineEdit_prefix.setMinimumSize(QSize(170, 25))
        self.lineEdit_prefix.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_prefix)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_suffix = QLabel(self.widget)
        self.lbl_suffix.setObjectName(u"lbl_suffix")
        self.lbl_suffix.setMinimumSize(QSize(45, 20))
        self.lbl_suffix.setMaximumSize(QSize(45, 20))

        self.horizontalLayout_3.addWidget(self.lbl_suffix)

        self.lineEdit_suffix = QLineEdit(self.widget)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")
        self.lineEdit_suffix.setMinimumSize(QSize(168, 25))
        self.lineEdit_suffix.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_suffix)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_case = QLabel(self.widget)
        self.lbl_case.setObjectName(u"lbl_case")
        self.lbl_case.setMinimumSize(QSize(45, 20))
        self.lbl_case.setMaximumSize(QSize(45, 20))

        self.horizontalLayout_4.addWidget(self.lbl_case)

        self.comboBox_case = QComboBox(self.widget)
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.comboBox_case.setObjectName(u"comboBox_case")
        self.comboBox_case.setMinimumSize(QSize(130, 25))

        self.horizontalLayout_4.addWidget(self.comboBox_case)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_start = QLabel(self.widget)
        self.lbl_start.setObjectName(u"lbl_start")
        self.lbl_start.setMinimumSize(QSize(45, 20))
        self.lbl_start.setMaximumSize(QSize(45, 20))

        self.horizontalLayout_5.addWidget(self.lbl_start)

        self.spinBox_start = QSpinBox(self.widget)
        self.spinBox_start.setObjectName(u"spinBox_start")
        self.spinBox_start.setMinimumSize(QSize(74, 25))
        self.spinBox_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_start.setMaximum(1000000)
        self.spinBox_start.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox_start)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_zfill = QLabel(self.widget)
        self.lbl_zfill.setObjectName(u"lbl_zfill")
        self.lbl_zfill.setMinimumSize(QSize(45, 20))
        self.lbl_zfill.setMaximumSize(QSize(45, 20))

        self.horizontalLayout_6.addWidget(self.lbl_zfill)

        self.spinBox_zfill = QSpinBox(self.widget)
        self.spinBox_zfill.setObjectName(u"spinBox_zfill")
        self.spinBox_zfill.setMinimumSize(QSize(74, 25))
        self.spinBox_zfill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_zfill.setMinimum(1)
        self.spinBox_zfill.setMaximum(7)

        self.horizontalLayout_6.addWidget(self.spinBox_zfill)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.checkBox_onlyFiles = QCheckBox(self.widget)
        self.checkBox_onlyFiles.setObjectName(u"checkBox_onlyFiles")
        self.checkBox_onlyFiles.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_11.addWidget(self.checkBox_onlyFiles)

        self.checkBox_reversed = QCheckBox(self.widget)
        self.checkBox_reversed.setObjectName(u"checkBox_reversed")
        self.checkBox_reversed.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_11.addWidget(self.checkBox_reversed)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_keepAsTemp = QCheckBox(self.widget)
        self.checkBox_keepAsTemp.setObjectName(u"checkBox_keepAsTemp")
        self.checkBox_keepAsTemp.setMinimumSize(QSize(100, 20))
        self.checkBox_keepAsTemp.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_10.addWidget(self.checkBox_keepAsTemp)

        self.lbl_tempID = QLabel(self.widget)
        self.lbl_tempID.setObjectName(u"lbl_tempID")
        self.lbl_tempID.setMinimumSize(QSize(320, 20))
        self.lbl_tempID.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_10.addWidget(self.lbl_tempID)

        self.btn_copyTempID = QPushButton(self.widget)
        self.btn_copyTempID.setObjectName(u"btn_copyTempID")
        self.btn_copyTempID.setMinimumSize(QSize(16, 16))
        self.btn_copyTempID.setMaximumSize(QSize(16, 16))
        self.btn_copyTempID.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.btn_copyTempID)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi()

        self.widget.setLayout(self.gridLayout)

        # After the completion of widget, let the parent make the last arrangements
        super().prepare(transactionType=self.transactionType, recordDict=recordDict)

    def retranslateUi(self):
        self.lbl_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.lineEdit_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select or drag and drop", None))
        self.btn_openDialog_address.setText("")
        self.lbl_prefix.setText(QCoreApplication.translate("MainWindow", u"Prefix:", None))
        self.lineEdit_prefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Optional--", None))
        self.lbl_suffix.setText(QCoreApplication.translate("MainWindow", u"Suffix:", None))
        self.lineEdit_suffix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Optional--", None))
        self.lbl_case.setText(QCoreApplication.translate("MainWindow", u"Case:", None))
        self.comboBox_case.setItemText(0, QCoreApplication.translate("MainWindow", u"Alphabetical", None))
        self.comboBox_case.setItemText(1, QCoreApplication.translate("MainWindow", u"Creation Time", None))
        self.comboBox_case.setItemText(2, QCoreApplication.translate("MainWindow", u"Last Modification Time", None))
        self.comboBox_case.setItemText(3, QCoreApplication.translate("MainWindow", u"Last Access Time", None))
        self.comboBox_case.setItemText(4, QCoreApplication.translate("MainWindow", u"File Size", None))

        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.lbl_zfill.setText(QCoreApplication.translate("MainWindow", u"Zfill:", None))
        self.checkBox_onlyFiles.setText(QCoreApplication.translate("MainWindow", u"Only Files", None))
        self.checkBox_reversed.setText(QCoreApplication.translate("MainWindow", u"Reversed", None))
        self.checkBox_keepAsTemp.setText(QCoreApplication.translate("MainWindow", u"Keep as Temp", None))
        self.lbl_tempID.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_copyTempID.setText("")
    
    def run(self):
        address = self.lineEdit_address.text()
        prefix = self.lineEdit_prefix.text()
        suffix = self.lineEdit_suffix.text()
        orderCase = self.comboBox_case.currentText()
        start = self.spinBox_start.text()
        zfill = self.spinBox_zfill.text()

        onlyFiles = self.checkBox_onlyFiles.isChecked()
        orderReversed = self.checkBox_reversed.isChecked()

        # Control and arrange prefix/suffix parameters.
        # Prefix and suffix cannot be None.
        
        if prefix is None:
            prefix = ""
        
        if suffix is None:
            suffix = ""
        
        # Arrange start and zfill parameters.
        # Start and zfill must be int.

        start = int(start)
        zfill = int(zfill)

        # call function for rename operation
        self.transactionPerformer.addToTransactionQueue(self.func,
                                                        address = address,
                                                        prefix=prefix,
                                                        suffix=suffix,
                                                        only_files=onlyFiles,
                                                        case=orderCase,
                                                        rev=orderReversed,
                                                        start=start,
                                                        zfill=zfill)


if __name__ == '__main__':
    pass