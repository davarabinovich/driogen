
from sys import argv
from random import randint
from PyQt6.QtWidgets import QApplication
from lib.app_supervisor.app_supervisor_qt import *

from logic.logic_workflow import *
from app_logic.app_logic_qt import *
from file_processor.file_reader import *
from file_processor.file_writer import *
from ui.main_win.main_win import *
from ui.item_creation_dialog.item_creation_dialog import *

EXTENSION = '.dprj'


def main():
    app = QApplication(argv)
    main_win = MainWin()
    content_gui = WorkflowControllerQt(main_win)

    supervisor = AppSupervisorQt(main_win, PrjWorkflow, content_gui, EXTENSION, argv, write, read)

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
