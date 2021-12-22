import sys
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

import floods_database as db
from floods_home import Ui_FloodsHome
from floods_form import Ui_FloodsForm

db_name = {
    "National Capital Region (NCR)": "national_capital_region",
    "Cordillera Administrative Region (CAR)": "cordillera_administrative_region",
    "Ilocos Region (Region I)": "ilocos_region",
    "Cagayan Valley (Region II)": "cagayan_valley_region",
    "Central Luzon (Region III)": "central_luzon_region",
    "Calabarzon (Region IV-A)": "calabarzon_region",
    "Southwestern Tagalog Region (MIMAROPA)": "mimaropa_region",
    "Bicol Region (Region V)": "bicol_region",
    "Western Visayas (Region VI)": "western_visayas_region",
    "Central Visayas (Region VII)": "central_visayas_region",
    "Eastern Visayas (Region VIII)": "eastern_visayas_region",
    "Zamboanga Peninsula (Region IX)": "zamboanga_peninsula_region",
    "Northern Mindanao (Region X)": "northern_mindanao_region",
    "Davao Region (Region XI)": "davao_region",
    "Soccsksargen (Region XII)": "soccsksargen_region",
    "Caraga (Region XIII)": "caraga_region",
    "Bangsamoro (BARMM)": "bangsamoro_region"
    }

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
        self.form_ui.close_form_signal.connect(self.open_home_ui)


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

    close_form_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_FloodsForm()
        self.ui.setupUi(self)

        self.ui.cancel_button.clicked.connect(self.close_form)
        self.ui.image_browse_button.clicked.connect(self.browse_files)
        self.ui.submit_button.clicked.connect(self.submit_form)


    def close_form(self):
        self.close()
        self.close_form_signal.emit()


    def browse_files(self):
        file_name = qtw.QFileDialog.getOpenFileName(self, "Select Image File", str(Path.home()))
        self.ui.image_lineedit.setText(file_name[0])


    def submit_form(self):
        form_dict = {
            "date": self.ui.date_lineedit.text(),
            "region": self.ui.region_combobox.currentText(),
            "city/province": self.ui.cityprovince_lineedit.text(),
            "type of infrastructure" : self.ui.infrastructure_lineedit.text(),
            "extent of damage": self.ui.damage_lineedit.text(),
            "water level": float(self.ui.waterlevel_lineedit.text()),
            "image": self.ui.image_lineedit.text()
            }
        error_status = [kv_pair[0] for kv_pair in list(filter(lambda kv_pair: not kv_pair[1] or kv_pair[1] == "Select a Region", form_dict.items()))]
        if error_status:
            print(error_status)
            # Display errors, dont send
        else:
            table_name = db_name[form_dict["region"]]
            # Create database
            db.create_database(table_name)
            # Insert database
            db.insert_database(
                table_name,
                form_dict["date"],
                form_dict["region"],
                form_dict["city/province"],
                form_dict["type of infrastructure"],
                form_dict["extent of damage"],
                form_dict["water level"],
                form_dict["image"]
            )
            self.close_form()
            

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = FloodsMainInterface()
    sys.exit(app.exec_())
