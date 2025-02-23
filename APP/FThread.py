from PyQt6.QtCore import QThread, pyqtSignal
from Customs import CustomMessageBox
from Transactions.package import Errors
import time

class TransactionPerformer(QThread):
    numberOfTransactions = pyqtSignal(int)
    isWorking = pyqtSignal(bool)
    transactionQueue = list()

    lastResult = pyqtSignal(object)
    info = pyqtSignal(str)
    warning = pyqtSignal(str)
    error = pyqtSignal(str)

    alreadyCalled:bool = False

    def __init__(self, _parent=None):
        self._parent = _parent
        return super().__init__()

    def addToTransactionQueue(self, func, *args, **kwargs):
        self.transactionQueue.append((func, args, kwargs))

        self.numberOfTransactions.emit(len(self.transactionQueue))
        
        if not self.alreadyCalled:
            self.alreadyCalled = True
            self.start()
        else:
            pass

    def run(self):
        if not self.transactionQueue:
            self.isWorking.emit(False)
            self.alreadyCalled = False
            return
        
        self.numberOfTransactions.emit(len(self.transactionQueue))
        self.isWorking.emit(True)

        self.transaction = self.transactionQueue[0]
        self.func, self.args, self.kwargs = self.transaction
        
        try:
            ret = self.func(*self.args, **self.kwargs)
            self.lastResult.emit(ret)
        except Errors.CompletedProcessWithMissingItems as e:
            self.info.emit(str(e))
        except Errors.ProcessAborted as e:
            self.error.emit(str(e))
        except Exception as e:
            self.warning.emit(str(e))
            print(e)
            print(self.kwargs)
        finally:
            self.transactionQueue.pop(0)

        self.run()


# END