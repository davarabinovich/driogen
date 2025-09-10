
from lib.app_supervisor.app_supervisor_qt import *
from src.app_logic.app_logic_if import *
from src.logic.logic_workflow import *
from src.ui.main_win.main_win import *
from src.ui.item_creation_dialog.item_creation_dialog import *


class WorkflowControllerQt(WorkflowControllerIf, ContentGuiQt):
    def __init__(self, parent: MainWin):
        super().__init__(parent)
        self._data: PrjWorkflow | None = None

    def create_content(self) -> bool:
        is_accepted: bool = self._ask_new_workflow_data()
        if is_accepted:
            content = PrjWorkflow()
            self.set_content(content)
        return is_accepted

    def set_content(self, content: PrjWorkflow):
        self._data = content

    def get_content(self) -> PrjWorkflow:
        return self._data

    @pyqtSlot()
    def handle_edition(self):
        self._data.value = self.parent()._ui.lineEdit.text()
        self.edit.emit()

    def _ask_new_workflow_data(self) -> bool:
        dialog: ItemCreationDialog = ItemCreationDialog(self.parent())
        is_accepted: bool = bool(dialog.exec())
        state = dialog.is_checked()
        return is_accepted