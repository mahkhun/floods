import sys
import json
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 

import floods_database as db
from floods_home import Ui_FloodsHome
from floods_form import Ui_FloodsForm
from floods_selection import Ui_FloodsSelection

with open("regions-cities.json") as f:
    regions_cities = json.load(f)

with open("db-tablenames.json") as f:
    db_tablenames = json.load(f)
    inverse_db_tablenames = {value: key for key, value in db_tablenames.items()}

class FloodsMainInterface(object):

    def __init__(self):
        self.show_home_ui()


    def show_home_ui(self):
        """ Displays the FloodsHome window. """
        self.home_ui = FloodsHomeInterface()
        self.home_ui.show()
        self.home_ui.open_form_signal.connect(self.show_form_ui)
        self.home_ui.open_selection_signal.connect(self.show_selection_ui)


    def show_form_ui(self):
        """ Displays the FloodsForm window. """
        self.form_ui = FloodsFormInterface()
        self.form_ui.show()
        self.form_ui.close_form_signal.connect(self.show_home_ui)

    def show_selection_ui(self):
        """ Displays the FloodsSelection window. """
        self.selection_ui = FloodsSelectionInterface()
        self.selection_ui.show()
        self.selection_ui.close_selection_signal.connect(self.show_home_ui)
        

class FloodsHomeInterface(qtw.QWidget, Ui_FloodsHome):

    open_form_signal = qtc.pyqtSignal()
    open_selection_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_button.clicked.connect(sys.exit)
        self.create_button.clicked.connect(self.open_form_window)
        self.view_button.clicked.connect(self.open_selection_window)


    def open_form_window(self):
        """ Opens the FloodsForm window and closes the FloodsHome window. """
        self.close()
        self.open_form_signal.emit()

    def open_selection_window(self):
        """ Opens the FloodsSelection window and closes the FloodsHome window. """
        self.close()
        self.open_selection_signal.emit()
        


class FloodsFormInterface(qtw.QWidget, Ui_FloodsForm):

    close_form_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        for region, cities in regions_cities.items():
            self.region_combobox.addItem(region, cities)

        self.region_combobox.currentIndexChanged.connect(self.update_location_combobox)
        self.update_location_combobox(self.region_combobox.currentIndex())

        self.cancel_button.clicked.connect(self.close_form)
        self.image_browse_button.clicked.connect(self.browse_files)
        self.submit_button.clicked.connect(self.submit_form)


    def close_form(self):
        """ Closes the FloodsForm window. """
        self.close()
        self.close_form_signal.emit()        


    def update_location_combobox(self, index):
        """ Updates the location combobox with the location associated with the region selected in the region combobox. """
        self.location_combobox.clear()
        locations = self.region_combobox.itemData(index)
        if locations:
            self.location_combobox.addItems(locations)


    def browse_files(self):
        """ Allows the user to browse files. """
        file_name = qtw.QFileDialog.getOpenFileName(self, "Select Image File", str(Path.home()))
        self.image_lineedit.setText(file_name[0])


    def submit_form(self):
        """ Gathers data about floods. """
        form_dict = {
            "date": self.date_lineedit.text(),
            "region": self.region_combobox.currentText(),
            "city/province": self.location_combobox.currentText(),
            "type of infrastructure" : self.infrastructure_lineedit.text(),
            "extent of damage": self.damage_lineedit.text(),
            "water level": float(self.waterlevel_lineedit.text()),
            "image": self.image_lineedit.text()
            }
        error_status = [kv_pair[0] for kv_pair in list(filter(lambda kv_pair: not kv_pair[1], form_dict.items()))]
        if error_status:
            print(error_status)
            # Display errors, dont send
        else:
            table_name = db_tablenames[form_dict["region"]]
            # Create database
            db.create_table(table_name)
            # Insert database
            db.insert_table(
                table_name,
                form_dict["date"],
                form_dict["region"],
                form_dict["city/province"],
                form_dict["type of infrastructure"],
                form_dict["extent of damage"],
                form_dict["water level"],
                form_dict["image"]
            )
            # Show dialogue box, if submit another or return home
            self.close_form()


class FloodsSelectionInterface(qtw.QWidget, Ui_FloodsSelection):

    close_selection_signal = qtc.pyqtSignal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Update region combobox based on tables found in floods_data.db
        self.update_region_combobox()

        # Make a connection between region combobox and location combobox
        self.region_combobox.currentIndexChanged.connect(self.update_location_combobox)
        # M
        self.update_location_combobox(self.region_combobox.currentText(), self.region_combobox.currentIndex())

        # Make a conection between location combobox and date combobox
        self.location_combobox.currentIndexChanged.connect(self.update_date_combobox)
        # 
        self.update_date_combobox(self.location_combobox.currentIndex())


        self.cancel_button.clicked.connect(self.close_selection)

    def close_selection(self):
        """ Closes the FloodsSelection window. """
        self.close()
        self.close_selection_signal.emit()

        
    def update_region_combobox(self):
        """ Updates the region combobox with the tables found in floods_data.db along with the available corresponding cities."""
        table_list = db.query_table("sqlite_master", "name", WHERE="type='table'")["name"]
        available_regions = [inverse_db_tablenames[table_name] for table_name in table_list]

        region_location_dict = {region:[] for region in available_regions}
        for region in available_regions:
            location_list = sorted(list(set(db.query_table(db_tablenames[region], "location")["location"])))
            region_location_dict[region].extend(location_list) # location, yes

        for region, location in region_location_dict.items():
            self.region_combobox.addItem(region, location)

    
    def update_location_combobox(self, region, index):
        """ Updates the location combobox with the cities/provinces associated with the current region presented in the region combobox."""
        self.location_combobox.clear()
        locations = self.region_combobox.itemData(index)
        for location in locations:
            date_list = sorted(db.query_table(db_tablenames[region], "date", WHERE=f"location=='{location}'")["date"])
            self.location_combobox.addItem(location, date_list)


    def update_date_combobox(self, index):
        """ Updates the date combobox with the dates associated with the current city/province presented in the location combobox. """
        self.date_combobox.clear()
        dates = self.location_combobox.itemData(index)
        if dates:
            self.date_combobox.addItems(dates)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = FloodsMainInterface()
    sys.exit(app.exec_())
