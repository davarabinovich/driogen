from lib.app_supervisor.app_supervisor_qt import *
from gen.main_win_plot import *


class MainWin(MainWinQt):
    def __init__(self):
        super().__init__(Ui_MainWin())
        self._ui.actionNew.triggered.connect(self.new)
        self._ui.actionSave.triggered.connect(self.save)
        self._ui.actionOpen.triggered.connect(self.load)

    def resizeEvent(self, a0: Optional[QtGui.QResizeEvent]) -> None:
        pass
