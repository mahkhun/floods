import sys
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from floods_home import Ui_FloodsHome
from floods_form import Ui_FloodsForm


class FloodsMainInterface(object):

    def __init__(self):
        self.open_home_ui()


    def open_home_ui(self):
        self.home_ui = FloodsHomeInterface()
        self.home_ui.show()
        self.home_ui.open_form_signal.connect(self.open_form_ui)


    def open_form_ui(self):
        self.form_ui = FloodsFormInterface()
        self.form_ui.show()
        self.form_ui.cancel_form_signal.connect(self.open_home_ui)


class FloodsHomeInterface(qtw.QWidget):

    open_form_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_FloodsHome()
        self.ui.setupUi(self)

        self.ui.quit_button.clicked.connect(sys.exit)
        self.ui.create_button.clicked.connect(self.open_form_window)


    def open_form_window(self):
        self.close()
        self.open_form_signal.emit()


class FloodsFormInterface(qtw.QWidget):

    cancel_form_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_FloodsForm()
        self.ui.setupUi(self)

        self.ui.cancel_button.clicked.connect(self.cancel_form)
        self.ui.image_browse_button.clicked.connect(self.browse_files)


    def cancel_form(self):
        self.close()
        self.cancel_form_signal.emit()


    def browse_files(self):
        file_name = qtw.QFileDialog.getOpenFileName(self, "Select Image", str(Path.home()))
        self.ui.image_lineedit.setText(file_name[0])
        print(file_name)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = FloodsMainInterface()
    sys.exit(app.exec_())
