
from PyQt6.QtWidgets import QWidget
from gen.physical_part_stages_plot import *


class PhysicalPartStages(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self._ui: Ui_physicalPartStages = Ui_physicalPartStages()
        self._ui.setupUi(self)
