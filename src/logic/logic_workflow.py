
import lib.forest.tree as forest
from logic_item import *


class NotPhysicalProduction(Exception):
    def __init__(self):
        super().__init__('Workflow of non-physical item cannot have production stage')


class PrjWorkflow:
    class Stage:
        def __init__(self):
            pass

    def __init__(self):
        self._forest: forest.Forest = forest.Forest()
