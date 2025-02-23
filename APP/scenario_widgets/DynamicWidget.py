from PyQt6.QtWidgets import QLineEdit, QCheckBox, QRadioButton, QComboBox, QSpinBox, QLabel, QWidget
from FThread import TransactionPerformer


class DynamicWidget:
    transactionPerformer = TransactionPerformer()

    def __init__(self):
        # self.transactionPerformer = TransactionPerformer(self)
        pass
    
    @staticmethod
    def setTransactionPerformer(transactionPerformer:TransactionPerformer):
        DynamicWidget.transactionPerformer = transactionPerformer

    def getWidget(self, parent=None):
        if parent is not None:
            self.widget.setParent(parent)
        
        return self.widget
    
    def prepare(self, transactionType:str, recordDict:dict|None = None):
        try:
            self.lbl_tempID.setText("None")
        except AttributeError:
            pass
        except Exception as e:
            print(e)
        
        if recordDict is not None:
            self.loadWidget(recordDict)
    
    def getValue(self, item:QLineEdit|QCheckBox|QRadioButton|QComboBox|QSpinBox|QLabel):
        if isinstance(item, QLineEdit): return item.text()
        elif isinstance(item, QCheckBox): return item.isChecked()
        elif isinstance(item, QRadioButton): return item.isChecked()
        elif isinstance(item, QComboBox): return item.currentText()
        elif isinstance(item, QSpinBox): return item.value()
        elif isinstance(item, QLabel): return item.text()
        else: return None
    
    def setValue(self, item:QLineEdit|QCheckBox|QRadioButton|QComboBox|QSpinBox|QLabel, value:any) -> bool:
        if isinstance(item, QLineEdit): item.setText(value)
        elif isinstance(item, QCheckBox): item.setChecked(value)
        elif isinstance(item, QRadioButton): item.setChecked(value)
        elif isinstance(item, QComboBox): item.setCurrentText(value)
        elif isinstance(item, QSpinBox): item.setValue(int(value))
        elif isinstance(item, QLabel): item.setText(value)
        else: return False

        return True
    
    def dump(self) -> dict:
        self.recordDict:dict = dict()
        widgetAtHand = self.getWidget()

        for child in widgetAtHand.children():
            if child.parent() != widgetAtHand:
                # Explain with an example:
                # A QComboBox or QSpinBox can also have a QLineEdit inside.
                # To get the real QLineEdits, check also child's parent.
                # If it belongs to another parent rather than widgetAtHand,
                # then ignore it for this turn. Otherwise, evaluate
                # it.
                continue

            elif isinstance(child, (QLineEdit, QCheckBox, QRadioButton, QComboBox, QSpinBox, QLabel)):
                self.recordDict[child.objectName()] = self.getValue(child)
        
        return self.recordDict
    
    def loadWidget(self, recordDict:dict[str,any]):
        widgetAtHand = self.getWidget()
        for item, value in recordDict.items():
            for child in widgetAtHand.findChildren(QWidget):
                if child.parent() != widgetAtHand:
                    continue

                if child.objectName() != item:
                    continue

                else:
                    ret = self.setValue(child, value)
                    if not ret:
                        print(f"Invalid in loadWidget: item -> {type(item)} | value -> {value} - {type(value)}")
    
    def getTransactionPerformer(self):
        # return self.transactionPerformer
        return DynamicWidget.transactionPerformer


# END