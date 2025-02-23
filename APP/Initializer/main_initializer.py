from ui_files.Copy import copy
from ui_files.Count import count
from ui_files.CreateArchive import create_archive
from ui_files.CreateSymlink import create_symlink
from ui_files.Delete import delete
from ui_files.Red import red
from ui_files.Rename import rename
from ui_files.WhoIs import whoIs

from FThread import TransactionPerformer


def initialize(obj):
    obj.btn_expand_window.clicked.connect(lambda: obj.showNormal() if obj.isMaximized() else obj.showMaximized())
    obj.btn_minimize_window.clicked.connect(obj.showMinimized)

    obj.stackedWidget_header.setCurrentIndex(0)

    obj.radioButton_page_1.clicked.connect(lambda: obj.stackedWidget_header.setCurrentIndex(0))
    obj.radioButton_page_2.clicked.connect(lambda: obj.stackedWidget_header.setCurrentIndex(1))
    obj.radioButton_page_3.clicked.connect(lambda: obj.stackedWidget_header.setCurrentIndex(2))
    obj.radioButton_page_4.clicked.connect(lambda: obj.stackedWidget_header.setCurrentIndex(3))

    obj.widget_short_menu.setVisible(True)
    obj.widget_long_menu.setVisible(False)

    obj.btn_short_menu_menu.clicked.connect(lambda: (obj.widget_long_menu.setVisible(True), obj.widget_short_menu.setVisible(False)))
    obj.btn_long_menu_menu.clicked.connect(lambda: (obj.widget_short_menu.setVisible(True), obj.widget_long_menu.setVisible(False)))

    obj.btn_short_menu_copy.clicked.connect(lambda: obj.openWindow(copy.CopyApp))
    obj.btn_long_menu_copy.clicked.connect(lambda: obj.openWindow(copy.CopyApp))

    obj.btn_short_menu_delete.clicked.connect(lambda: obj.openWindow(delete.DeleteApp))
    obj.btn_long_menu_delete.clicked.connect(lambda: obj.openWindow(delete.DeleteApp))

    obj.btn_short_menu_red.clicked.connect(lambda: obj.openWindow(red.RedApp))
    obj.btn_long_menu_red.clicked.connect(lambda: obj.openWindow(red.RedApp))

    obj.btn_short_menu_rename.clicked.connect(lambda: obj.openWindow(rename.RenameApp))
    obj.btn_long_menu_rename.clicked.connect(lambda: obj.openWindow(rename.RenameApp))

    obj.btn_short_menu_count.clicked.connect(lambda: obj.openWindow(count.CountApp))
    obj.btn_long_menu_count.clicked.connect(lambda: obj.openWindow(count.CountApp))

    obj.btn_short_menu_symlinks.clicked.connect(lambda: obj.openWindow(create_symlink.SymlinkApp))
    obj.btn_long_menu_symlinks.clicked.connect(lambda: obj.openWindow(create_symlink.SymlinkApp))

    obj.btn_short_menu_whoIs.clicked.connect(lambda: obj.openWindow(whoIs.WhoIsApp))
    obj.btn_long_menu_whoIs.clicked.connect(lambda: obj.openWindow(whoIs.WhoIsApp))

    obj.btn_short_menu_archive.clicked.connect(lambda: obj.openWindow(create_archive.ArchiveApp))
    obj.btn_long_menu_archive.clicked.connect(lambda: obj.openWindow(create_archive.ArchiveApp))

    obj.btn_short_menu_scenario.clicked.connect(obj.openCreateScenarioPage)
    obj.btn_long_menu_scenario.clicked.connect(obj.openCreateScenarioPage)

    obj.stackedWidget_header.currentChanged.connect(obj.headerPageChanged)

    obj.btn_menu_window.clicked.connect(obj.openTitleBarMenu)

    # Arrange titleBarText
    obj.setTitleBarText()

    obj.transactionPerformer.isWorking.connect(obj.isWorkingOnTransaction)
    obj.transactionPerformer.lastResult.connect(obj.lastOutput)
    obj.transactionPerformer.numberOfTransactions.connect(obj.getNumberOfTransactions)

    obj.transactionPerformer.info.connect(obj.printInformation)
    obj.transactionPerformer.warning.connect(obj.printWarning)
    obj.transactionPerformer.error.connect(obj.printError)


# END