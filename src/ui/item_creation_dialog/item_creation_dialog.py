
from PyQt6.QtWidgets import QDialog
from gen.item_creation_dialog_plot import *
from src.ui.main_win.main_win import *


class ItemCreationDialog(QDialog):
    def __init__(self, parent: MainWin):
        super().__init__(parent)
        self._ui: Ui_itemCreationDialog = Ui_itemCreationDialog()
        self._ui.setupUi(self)
        self._ui.buttonBox.accepted.connect(self.accept)

    def is_checked(self):
        return self._ui.physicalPartStages._ui.materialsCheckBox.isChecked()
