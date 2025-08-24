
from sys import argv
from typing import Optional
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.MainWin import *


EXTENSION = '.dprj'


class AppSupervisor(QObject):
    def __init__(self, main_win: QMainWindow):
        super().__init__(None)
        self._main_win = main_win

    @pyqtSlot()
    def receive_save_as_action(self):
        pass

    needToSave = pyqtSignal(str, name='needToSave')

    @pyqtSlot()
    def receive_create_new(self):
        file_url_tuple = QFileDialog.getSaveFileUrl(self._main_win,
                                                    caption='Save Workflow Project',
                                                    filter='Project (*{extension})'.format(extension=EXTENSION))
        if file_url_tuple[0].isEmpty():
            return False
        file_path: str = file_url_tuple[0].toString().removeprefix('file:///')
        if not file_path.endswith(EXTENSION):
            file_path += EXTENSION

        self.needToSave.emit(file_path)
        return True


class MainWin(QMainWindow):
    def __init__(self, ui: Ui_MainWin):
        super().__init__()
        self._ui = ui
        self._ui.setupUi(self)

    def resizeEvent(self, a0: Optional[QtGui.QResizeEvent]) -> None:
        pass

    def closeEvent(self, a0: Optional[QtGui.QCloseEvent]) -> None:
        pass


def main():
    app = QApplication(argv)
    ui = Ui_MainWin()
    win = MainWin(ui)

    app_supervisor = AppSupervisor(win)
    ui.menuFile.triggered.connect(app_supervisor.receive_create_new)
    app_supervisor.needToSave.connect(save)

    win.show()
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


@pyqtSlot(str)
def save(file_path: str):
    file = open(file_path, 'w')
    file.write(TEST_CONTENT)
    file.close()


if __name__ == '__main__':
    main()
