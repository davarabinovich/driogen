
from sys import argv
from random import randint
from PyQt6.QtWidgets import QApplication

from lib.app_supervisor.app_supervisor_qt import *
from ui_logic.ui_logic import *
from ui.MainWin import *
from file_processor.file_reader import *
from file_processor.file_writer import *


EXTENSION = '.dprj'


class MainWin(MainWinQt):
    def __init__(self, ui: Ui_MainWin):
        super().__init__(ui)
        self._ui.lineEdit.setVisible(False)
        # self.new = self._ui.actionNew.triggered
        self._ui.actionNew.triggered.connect(self.new)
        self._ui.lineEdit.textChanged.connect(self.edit)
        self._ui.actionSave.triggered.connect(self.save)
        self._ui.actionOpen.triggered.connect(self.load)

    def resizeEvent(self, a0: Optional[QtGui.QResizeEvent]) -> None:
        pass


class ContentGui(ContentGuiQt):
    def __init__(self, parent: MainWin):
        super().__init__(parent)
        self._data: SupervisedData | None = None

    def create_content(self):
        self._data = SupervisedData('Test data object name', randint(0, 125))
        self.parent._ui.lineEdit.setVisible(True)

    def set_content(self, content: SupervisedData):
        self._data = content

    def get_content(self) -> SupervisedData:
        return self._data


def main():
    app = QApplication(argv)
    ui = Ui_MainWin()
    main_win = MainWin(ui)
    content_gui = ContentGui(main_win)

    AppSupervisorQt(main_win, SupervisedData, content_gui, EXTENSION, argv, write, read)

    main_win.show()
    app.exec()
    exit()


TEST_CONTENT = '''<mxfile host="Electron" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/28.0.6 Chrome/138.0.7204.100 Electron/37.2.3 Safari/537.36" version="28.0.6" pages="3">
  <diagram id="oeTdnU0xfzHf7-I6OooS" name="Architectural Diagram">
    <mxGraphModel dx="3565" dy="2105" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="xuHbROfH0oEkT6LFa74m-93" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;absoluteArcSize=1;arcSize=36;strokeColor=none;opacity=75;" vertex="1" parent="1">
          <mxGeometry x="760" y="460" width="40" height="310" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''

if __name__ == '__main__':
    main()
