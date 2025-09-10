
from abc import abstractmethod
from lib.app_supervisor.app_supervisor_if import *
from src.logic.logic_workflow import *


class WorkflowControllerIf(ContentGuiIf):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data: PrjWorkflow | None = None

    def create_content(self) -> bool:
        is_accepted: bool = self._ask_new_workflow_data()
        if is_accepted:
            content = PrjWorkflow()
            self.set_content(content)
        return is_accepted

    @abstractmethod
    def set_content(self, content: PrjWorkflow):
        self._data = content

    def get_content(self) -> PrjWorkflow:
        return self._data

    @abstractmethod
    def _ask_new_workflow_data(self) -> bool:
        pass
