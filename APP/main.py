from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QMovie, QPixmap
from APP.ui_files.Main.main_form import Ui_MainWindow
from APP.Transactions.package import Controller
from APP import Commons
from APP.Customs import CustomMessageBox, TitleBarPopUpMenu
import sys
import os
import json

from APP.FThread import TransactionPerformer

from APP.ui_files.About import about
from APP.ui_files.CreateScenario import create_scenario

from APP.scenario_widgets import *
from APP.Initializer import main_initializer

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close_window.clicked.connect(lambda: QApplication.quit())

        # Initialize a transaction performer object for multithreading
        self.transactionPerformer = TransactionPerformer(_parent=self)

        DynamicWidget.DynamicWidget.setTransactionPerformer(self.transactionPerformer)

        self._drag_pos = None

        self.widget_frame.mousePressEvent = self.mousePressEvent
        self.widget_frame.mouseMoveEvent = self.mouseMoveEvent
        self.widget_frame.mouseReleaseEvent = self.mouseReleaseEvent
        
        # Set up signal-slot connections
        main_initializer.initialize(self)

        self.workingOnTransaction = False

        self.movie = None

        self.functionStack:list = list()

        self.getScenarioWidgets()
    
    def openCreateScenarioPage(self, value):
        if isinstance(value, dict):
            pass
        else:
            value = None

        self.secondWindow = create_scenario.CreateScenarioApp(self, self.transactionPerformer, value)
        self.secondWindow.show()
        self.setEnabled(False)
    
    def getScenarioWidgets(self):
        for scenarioSave in os.listdir(r"scenarios"):
            path = os.path.join("scenarios", scenarioSave)
            if os.path.isfile(path) and os.path.splitext(path)[1] == ".json":
                with open(path, "r") as save:
                    data = json.load(save)
                    name = data["name"]
                    transactionNumber = len(data["transactionObjectTypes"])

                    scenarioWidget = getattr(self, name, None)

                    if scenarioWidget is not None:
                        scenarioWidget.update(name, transactionNumber)
                    
                    else:
                        self.addWidget(name, transactionNumber)
    
    def addWidget(self, name:str, transactionNumber:int):
        runnerW = scenario_runner_widget.SimpleApp(name, transactionNumber)
        # setattr and getattr below avoid 'late binding' problem
        setattr(self, name, runnerW)
        getattr(self, name).buttonSignal.connect(self.scenarioWidgetButtonHandle)
        self.horizontalLayout_14.insertWidget(self.horizontalLayout_14.count()-1, getattr(self, name).getWidget())
    
    def scenarioWidgetButtonHandle(self, value):
        btn, name = value

        saveAddr = rf"scenarios/{name}.json"
        try:
            with open(saveAddr, "r") as saveFile:
                save = json.load(saveFile)
        except:
            getattr(self, name).deleteLater()
            return

        if btn == "menu":
            self.openCreateScenarioPage(value=save)
        
        elif btn == "run":
            scenario = create_scenario.CreateScenarioApp(self, self.transactionPerformer,save)
            scenario.run()
    
    def mousePressEvent(self, event):
        return Commons.mousePressEvent(self, event)
    
    def mouseMoveEvent(self, event):
        return Commons.mouseMoveEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        return Commons.mouseReleaseEvent(self, event)
    
    def setEnabled(self, value:bool):
        self.widget_short_menu.setEnabled(value)
        self.widget_long_menu.setEnabled(value)
        self.stackedWidget_header.setEnabled(value)
        self.widget_scenario_space.setEnabled(value)

        self.radioButton_page_1.setEnabled(value)
        self.radioButton_page_2.setEnabled(value)
        self.radioButton_page_3.setEnabled(value)
        self.radioButton_page_4.setEnabled(value)

        self.btn_menu_window.setEnabled(value)

        self.getScenarioWidgets()
    
    def setTitleBarText(self):
        if Controller.isAdmin():
            self.lbl_titlebar_text.setText(f"{self.lbl_titlebar_text.text()} - Administrator")
    
    def openWindow(self, window:QMainWindow):
        self.secondWindow = window(self, self.transactionPerformer)
        self.setEnabled(False)
        self.secondWindow.show()

    def openTitleBarMenu(self):
        menu = TitleBarPopUpMenu.TitleBarPopUpMenu(self)
        menu.actionGitHub.triggered.connect(lambda: print("GitHub triggered!"))
        menu.actionHelp.triggered.connect(lambda: print("Help triggered!"))
        menu.actionAbout.triggered.connect(lambda: self.openWindow(about.AboutApp))

        menu.show_menu(button = self.sender(), widget = self.widget_frame)
    
    def headerPageChanged(self, value):
        if not self.workingOnTransaction:
            self.lbl_status_message_2.setVisible(False)
            self.btn_terminate_transactions.setVisible(False)
        
        matches = {
            0: self.radioButton_page_1,
            1: self.radioButton_page_2,
            2: self.radioButton_page_3,
            3: self.radioButton_page_4
        }

        matches[self.sender().currentIndex()].click()
    
    def getNumberOfTransactions(self, value):
        self.lbl_status_message_2.setText(f"Waiting for {value} transactions...")
    
    def playLoadingGif(self):
        if not self.movie:
            self.movie = QMovie(":/yeniÖnek/fifsot_icons/loading_gif_2.gif")
            self.lbl_status_icon.setMovie(self.movie)
            self.movie.setSpeed(250)
            self.movie.start()
    
    def isWorkingOnTransaction(self, value):
        if value == True:
            self.workingOnTransaction = True
            self.stackedWidget_header.setCurrentIndex(3)
            self.playLoadingGif()
            self.lbl_status_header.setText("We are working on your transactions...")
            self.lbl_status_message.setText("We will let you know as we complete each transaction.")
            self.lbl_status_message_2.setVisible(True)
            self.btn_terminate_transactions.setVisible(True)
        
        else:
            self.workingOnTransaction = False
            if self.movie:
                self.movie.stop()
                self.lbl_status_icon.setMovie(None)
                self.movie = None
                self.lbl_status_icon.setPixmap(QPixmap(":/yeniÖnek/fifsot_icons/completed_blue.png"))

                self.lbl_status_header.setText("Everything is Done!")
                self.lbl_status_message.setText("You don\'t have any transactions that we are currently working on.")
                self.lbl_status_message_2.setVisible(False)
                self.btn_terminate_transactions.setVisible(False)

    def lastOutput(self, value):
        if self.functionStack:
            func = self.functionStack.pop(0)
            if value is not None:
                CustomMessageBox.Information(self, "FIFSOT", f"{func} resulted in:\n{value}").exec()
            else:
                CustomMessageBox.Information(self, "FIFSOT", f"{func} completed!").exec()
    
    def printInformation(self, msg:str):
        if self.functionStack:
            func = self.functionStack.pop(0)
            CustomMessageBox.Information(self, "FIFSOT", f"{func}:\n\n{msg}").exec()

    def printWarning(self, msg:str):
        if self.functionStack:
            func = self.functionStack.pop(0)
            CustomMessageBox.Warning(self, "FIFSOT", f"{func}:\n\n{msg}").exec()

    def printError(self, msg:str):
        if self.functionStack:
            func = self.functionStack.pop(0)
            CustomMessageBox.Error(self, "FIFSOT", f"{func}:\n\n{msg}").exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


# END