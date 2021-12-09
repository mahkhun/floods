import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from floods_home import Ui_FloodsHome


class FloodsHomeInterface(qtw.QWidget):

    # signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_FloodsHome()
        self.ui.setupUi(self)

        self.ui.quit_button.clicked.connect(sys.exit)

    



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = FloodsHomeInterface()
    window.show()
    sys.exit(app.exec_())
