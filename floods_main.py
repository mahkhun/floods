import re
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
from floods_form_dialog import Ui_FloodsFormDialog

with open("regions-cities.json") as f:
    regions_cities = json.load(f)

with open("db-tablenames.json") as f:
    db_tablenames = json.load(f)
    inverse_db_tablenames = {value: key for key, value in db_tablenames.items()}

class FloodsMainInterface(object):

    def __init__(self) -> None:
        self.show_home_ui()


    def show_home_ui(self) -> None:
        """ Displays the FloodsHome window. """
        self.home_ui = FloodsHomeInterface()
        self.home_ui.show()
        self.home_ui.open_form_signal.connect(self.show_form_ui)
        self.home_ui.open_selection_signal.connect(self.show_selection_ui)


    def show_form_ui(self) -> None:
        """ Displays the FloodsForm window. """
        self.form_ui = FloodsFormInterface()
        self.form_ui.show()
        self.form_ui.cancel_form_signal.connect(self.show_home_ui)
        self.form_ui.accomplished_form_signal.connect(self.show_form_dialog_ui)

    
    def show_form_dialog_ui(self, data_dict) -> None:
        """ Displays the FloodsForm dialog window. """
        # insert data in floodsformdialog for proper init
        self.form_dialog_ui = FloodsFormDialog(data_dict)
        self.form_dialog_ui.show()
        self.form_dialog_ui.return_home_signal.connect(self.show_home_ui)
        self.form_dialog_ui.create_new_signal.connect(self.show_form_ui)


    def show_selection_ui(self) -> None:
        """ Displays the FloodsSelection window. """
        self.selection_ui = FloodsSelectionInterface()
        self.selection_ui.show()
        self.selection_ui.close_selection_signal.connect(self.show_home_ui)
        

class FloodsHomeInterface(qtw.QWidget, Ui_FloodsHome):

    open_form_signal = qtc.pyqtSignal()
    open_selection_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_button.clicked.connect(sys.exit)
        self.create_button.clicked.connect(self.open_form_window)
        self.view_button.clicked.connect(self.open_selection_window)


    def open_form_window(self) -> None:
        """ Opens the FloodsForm window and closes the FloodsHome window. """
        self.close()
        self.open_form_signal.emit()

    def open_selection_window(self) -> None:
        """ Opens the FloodsSelection window and closes the FloodsHome window. """
        self.close()
        self.open_selection_signal.emit()


class FloodsFormInterface(qtw.QWidget, Ui_FloodsForm):

    cancel_form_signal = qtc.pyqtSignal()
    accomplished_form_signal = qtc.pyqtSignal(dict)
    valid = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.region_combobox.addItem("Select a region", ["Select a region first!"])

        for region, cities in regions_cities.items():
            self.region_combobox.addItem(region, cities)

        self.region_combobox.currentIndexChanged.connect(self.update_location_combobox)
        self.update_location_combobox(self.region_combobox.currentIndex())

        self.date_lineedit.textChanged.connect(self.check_form)
        self.region_combobox.activated.connect(self.check_form)
        self.location_combobox.activated.connect(self.check_form)
        self.infrastructure_lineedit.textChanged.connect(self.check_form)
        self.damage_lineedit.textChanged.connect(self.check_form)
        self.waterlevel_lineedit.textChanged.connect(self.check_form)
        self.image_lineedit.textChanged.connect(self.check_form)

        self.cancel_button.clicked.connect(self.close_form)
        self.image_browse_button.clicked.connect(self.browse_files)
        self.submit_button.clicked.connect(self.submit_form)



    def close_form(self) -> None:
        """ Closes the FloodsForm window. """
        self.close()
        self.cancel_form_signal.emit()        


    def accomplished_form(self, data_dict) -> None:
        """ Shows the FloodsFormDialog window. """
        self.close()
        self.accomplished_form_signal.emit(data_dict)


    def update_location_combobox(self, index) -> None:
        """ Updates the location combobox with the location associated with the region selected in the region combobox. """
        self.location_combobox.clear()
        locations = self.region_combobox.itemData(index)
        if locations:
            self.location_combobox.addItems(locations)


    def browse_files(self) -> None:
        """ Allows the user to browse files. """
        file_name = qtw.QFileDialog.getOpenFileName(self, "Select Image File", str(Path.home()))
        self.image_lineedit.setText(file_name[0])


    def check_form(self) -> None:
        """ Checks if the information proided by the user on the form is valid. """
        self.valid = True

        # Validates the date
        date_text = self.date_lineedit.text()
        if not date_text:
            # No date is provided
            self.date_status_label.setText("No date provided!")
            self.date_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        elif not re.search(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", date_text):
            # Provided date is not on the proper format
            self.date_status_label.setText("Date provided is in improper format!")
            self.date_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            # The data is provided and is on the proper format
            self.date_status_label.setText("Date is provided!")
            self.date_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates the region
        region_text = self.region_combobox.currentText()
        if region_text == "Select a region":
            # Region is empty
            self.region_status_label.setText("No region selected!")
            self.region_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            # A region is selected
            self.region_status_label.setText("Region is provided!")
            self.region_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates the city/province
        cityprovince_text = self.location_combobox.currentText()
        if cityprovince_text == "Select a region first!":
            self.cityprovince_status_label.setText("No city/province selected!")
            self.cityprovince_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            self.cityprovince_status_label.setText("City/provice is provided!")
            self.cityprovince_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates the infrastructure description
        infrastructure_text = self.infrastructure_lineedit.text()
        if not infrastructure_text: 
            self.infrastructure_status_label.setText("No infrastructure provided!")
            self.infrastructure_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            self.infrastructure_status_label.setText("Infrastructure is provided!")
            self.infrastructure_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates the damage description
        damage_text = self.damage_lineedit.text()
        if not damage_text:
            self.damage_status_label.setText("No extent of damage is provided!")
            self.damage_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            self.damage_status_label.setText("Extent of damage is provided!")
            self.damage_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates the water level
        water_level_text = self.waterlevel_lineedit.text()
        if not water_level_text:
            self.waterlevel_status_label.setText("No water level is provided!")
            self.valid = False
            self.waterlevel_status_label.setStyleSheet(r"color: red; font-style: italic")
        elif not re.search(r"^\d{0,}\.\d{2,}$", water_level_text):
            self.waterlevel_status_label.setText("Water level provided is in improper format!")
            self.waterlevel_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            self.waterlevel_status_label.setText("Water level is provided!")
            self.waterlevel_status_label.setStyleSheet(r"color: green; font-style: italic")


        # Validates image path
        image_path = self.image_lineedit.text()
        if not image_path:
            self.image_status_label.setText("No image file path is provided!")
            self.image_status_label.setStyleSheet(r"color: red; font-style: italic")
            self.valid = False
        else:
            self.image_status_label.setText("Image file path is provided!")
            self.image_status_label.setStyleSheet(r"color: green; font-style: italic")

        
    def submit_form(self) -> None:
        """ Gathers data about floods. """
        if self.valid:
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
                self.accomplished_form(form_dict)
            

class FloodsFormDialog(qtw.QDialog, Ui_FloodsFormDialog):

    create_new_signal = qtc.pyqtSignal()
    return_home_signal = qtc.pyqtSignal()


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.update_descriptions(args[0])
        self.return_button.clicked.connect(self.close_form_dialog)
        self.create_new_button.clicked.connect(self.create_new_form)


    def update_descriptions(self, data_dict) -> None:
        """ Updates the description displayed in the FloodsFormDialog window. """
        desc = "Description: {}"
        self.date_description_label.setText(desc.format(data_dict["date"]))
        self.region_description_label.setText(desc.format(data_dict["region"]))
        self.location_description_label.setText(desc.format(data_dict["city/province"]))
        self.infrastructure_description_label.setText(desc.format(data_dict["type of infrastructure"]))
        self.damage_description_label.setText(desc.format(data_dict["extent of damage"]))
        self.waterlevel_description_label.setText(desc.format(data_dict["water level"]))
        # - image update here

    
    def create_new_form(self) -> None:
        """ Closes the FloodsFormDialog window and emits create_new_signal to signify opening another new FloodsForm window. """
        self.close()
        self.create_new_signal.emit()


    def close_form_dialog(self) -> None:
        """ Closes the FloodsFormDialog window and emits the return_home_signal to signify to return in the FloodsHome window."""
        self.close()
        self.return_home_signal.emit()


class FloodsSelectionInterface(qtw.QWidget, Ui_FloodsSelection):

    close_selection_signal = qtc.pyqtSignal()
    region_combobox_change_signal = qtc.pyqtSignal(str, int)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Initializes and sets up the FloodsSelection window.
        self.setupUi(self)

        # Updates the region combobox based on the tables found in floods_data.db.
        self.update_region_combobox()

        # Forms a connection between region combobox and location combobox.
        self.region_combobox.activated.connect(self.handle_region_combobox_activation)
        self.region_combobox_change_signal.connect(self.update_location_combobox)

        # Update the location combobox according to the current index of the region combobox.
        self.update_location_combobox(self.region_combobox.currentText(), self.region_combobox.currentIndex())

        # Forms a conection between location combobox and date combobox.
        self.location_combobox.currentIndexChanged.connect(self.update_date_combobox)

        # Update the date combobox according to the current index of the location combobox.
        self.update_date_combobox(self.location_combobox.currentIndex())

        # Forms a connection to the cancel button, causing the FloodsSelection window to close when clicked.
        self.cancel_button.clicked.connect(self.close_selection)


    # Temporary function
    def handle_region_combobox_activation(self) -> None:
        self.region_combobox_change_signal.emit(self.region_combobox.currentText(), self.region_combobox.currentIndex())


    def close_selection(self) -> None:
        """ Closes the FloodsSelection window. """
        # Closes the FloodsSelecton window.
        self.close()

        # Emits a signal showing that the FloodsSelection window is closed.
        self.close_selection_signal.emit()

        
    def update_region_combobox(self) -> None:
        """ Updates the region combobox with the tables found in floods_data.db along with the available corresponding cities."""
        # Queries a list of table names from floods_data.db.
        table_list = db.query_table("sqlite_master", "name", WHERE="type='table'")["name"]

        # Each table name in table_list will be converted to its corresponding region name.
        available_regions = [inverse_db_tablenames[table_name] for table_name in table_list]

        # Each region in available_regions will have a corresponding list where their locations based on floods_data.db will be stored.
        region_location_dict = {region:[] for region in available_regions}

        # The corresponding locations for each region in the available_regions will be stored in its respective list.
        for region in available_regions:
            location_list = sorted(list(set(db.query_table(db_tablenames[region], "location")["location"])))
            region_location_dict[region].extend(location_list) # location, yes

        # Each region and location pair will be stored in the region combobox.
        for region, location in region_location_dict.items():
            self.region_combobox.addItem(region, location)

    
    def update_location_combobox(self, region, index) -> None:
        """ Updates the location combobox with the cities/provinces associated with the current region presented in the region combobox."""
        # Clears the items stored in the location combobox.
        self.location_combobox.clear()
        
        # Gathers the respective list of locations for the current region selected in the region combobox.
        locations = self.region_combobox.itemData(index)

        # For each location in locations, its corresponding list of dates will be added to the location combobox.
        for location in locations:
            date_list = sorted(db.query_table(db_tablenames[region], "date", WHERE=f"location=='{location}'")["date"])
            self.location_combobox.addItem(location, date_list)


    def update_date_combobox(self, index) -> None:
        """ Updates the date combobox with the dates associated with the current city/province presented in the location combobox. """
        # Clears the items stored in the date combobox.
        self.date_combobox.clear()

        # Gathers the respective list of dates for the current location selected in the location combobox.
        dates = self.location_combobox.itemData(index)

        # The corresponding list of dates will be added to the date combobox.
        if dates:
            self.date_combobox.addItems(dates)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = FloodsMainInterface()
    sys.exit(app.exec_())
