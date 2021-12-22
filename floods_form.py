# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floods_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FloodsForm(object):
    def setupUi(self, FloodsForm):
        FloodsForm.setObjectName("FloodsForm")
        FloodsForm.resize(1000, 600)
        FloodsForm.setMinimumSize(QtCore.QSize(1000, 600))
        FloodsForm.setMaximumSize(QtCore.QSize(1000, 600))
        self.horizontalLayout = QtWidgets.QHBoxLayout(FloodsForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.floods_data_frame = QtWidgets.QFrame(FloodsForm)
        self.floods_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.floods_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.floods_data_frame.setObjectName("floods_data_frame")
        self.date_frame = QtWidgets.QFrame(self.floods_data_frame)
        self.date_frame.setGeometry(QtCore.QRect(40, 20, 401, 91))
        self.date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_frame.setObjectName("date_frame")
        self.date_title_label = QtWidgets.QLabel(self.date_frame)
        self.date_title_label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.date_title_label.setStyleSheet("font-size: 10pt;")
        self.date_title_label.setObjectName("date_title_label")
        self.date_description_label = QtWidgets.QLabel(self.date_frame)
        self.date_description_label.setGeometry(QtCore.QRect(10, 30, 371, 16))
        self.date_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.date_description_label.setObjectName("date_description_label")
        self.date_lineedit = QtWidgets.QLineEdit(self.date_frame)
        self.date_lineedit.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.date_lineedit.setInputMask("")
        self.date_lineedit.setText("")
        self.date_lineedit.setObjectName("date_lineedit")
        self.location_frame = QtWidgets.QFrame(self.floods_data_frame)
        self.location_frame.setGeometry(QtCore.QRect(40, 120, 401, 151))
        self.location_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.location_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.location_frame.setObjectName("location_frame")
        self.location_title_label = QtWidgets.QLabel(self.location_frame)
        self.location_title_label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.location_title_label.setStyleSheet("font-size: 10pt;")
        self.location_title_label.setObjectName("location_title_label")
        self.location_description_label = QtWidgets.QLabel(self.location_frame)
        self.location_description_label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.location_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.location_description_label.setObjectName("location_description_label")
        self.cityprovince_lineedit = QtWidgets.QLineEdit(self.location_frame)
        self.cityprovince_lineedit.setGeometry(QtCore.QRect(10, 120, 381, 22))
        self.cityprovince_lineedit.setObjectName("cityprovince_lineedit")
        self.region_combobox = QtWidgets.QComboBox(self.location_frame)
        self.region_combobox.setGeometry(QtCore.QRect(10, 70, 381, 22))
        self.region_combobox.setObjectName("region_combobox")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_combobox.addItem("")
        self.region_label = QtWidgets.QLabel(self.location_frame)
        self.region_label.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.region_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.region_label.setObjectName("region_label")
        self.cityprovince_label = QtWidgets.QLabel(self.location_frame)
        self.cityprovince_label.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.cityprovince_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.cityprovince_label.setObjectName("cityprovince_label")
        self.infrastructure_frame = QtWidgets.QFrame(self.floods_data_frame)
        self.infrastructure_frame.setGeometry(QtCore.QRect(40, 280, 401, 91))
        self.infrastructure_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infrastructure_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infrastructure_frame.setObjectName("infrastructure_frame")
        self.infrastructure_title_label = QtWidgets.QLabel(self.infrastructure_frame)
        self.infrastructure_title_label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.infrastructure_title_label.setStyleSheet("font-size: 10pt;")
        self.infrastructure_title_label.setObjectName("infrastructure_title_label")
        self.infrastructure_description_label = QtWidgets.QLabel(self.infrastructure_frame)
        self.infrastructure_description_label.setGeometry(QtCore.QRect(10, 30, 371, 16))
        self.infrastructure_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.infrastructure_description_label.setObjectName("infrastructure_description_label")
        self.infrastructure_lineedit = QtWidgets.QLineEdit(self.infrastructure_frame)
        self.infrastructure_lineedit.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.infrastructure_lineedit.setObjectName("infrastructure_lineedit")
        self.damage_frame = QtWidgets.QFrame(self.floods_data_frame)
        self.damage_frame.setGeometry(QtCore.QRect(40, 380, 401, 91))
        self.damage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.damage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.damage_frame.setObjectName("damage_frame")
        self.damage_title_label = QtWidgets.QLabel(self.damage_frame)
        self.damage_title_label.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.damage_title_label.setStyleSheet("font-size: 10pt;")
        self.damage_title_label.setObjectName("damage_title_label")
        self.damage_description_label = QtWidgets.QLabel(self.damage_frame)
        self.damage_description_label.setGeometry(QtCore.QRect(10, 30, 381, 16))
        self.damage_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.damage_description_label.setObjectName("damage_description_label")
        self.damage_lineedit = QtWidgets.QLineEdit(self.damage_frame)
        self.damage_lineedit.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.damage_lineedit.setObjectName("damage_lineedit")
        self.waterlevel_frame = QtWidgets.QFrame(self.floods_data_frame)
        self.waterlevel_frame.setGeometry(QtCore.QRect(40, 480, 401, 91))
        self.waterlevel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.waterlevel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.waterlevel_frame.setObjectName("waterlevel_frame")
        self.waterlevel_title_label = QtWidgets.QLabel(self.waterlevel_frame)
        self.waterlevel_title_label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.waterlevel_title_label.setStyleSheet("font-size: 10pt;")
        self.waterlevel_title_label.setObjectName("waterlevel_title_label")
        self.waterlevel_description_label = QtWidgets.QLabel(self.waterlevel_frame)
        self.waterlevel_description_label.setGeometry(QtCore.QRect(10, 30, 381, 16))
        self.waterlevel_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.waterlevel_description_label.setObjectName("waterlevel_description_label")
        self.waterlevel_lineedit = QtWidgets.QLineEdit(self.waterlevel_frame)
        self.waterlevel_lineedit.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.waterlevel_lineedit.setObjectName("waterlevel_lineedit")
        self.horizontalLayout.addWidget(self.floods_data_frame)
        self.floods_image_frame = QtWidgets.QFrame(FloodsForm)
        self.floods_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.floods_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.floods_image_frame.setObjectName("floods_image_frame")
        self.imageholder = QtWidgets.QLabel(self.floods_image_frame)
        self.imageholder.setGeometry(QtCore.QRect(40, 20, 401, 311))
        self.imageholder.setObjectName("imageholder")
        self.image_frame = QtWidgets.QFrame(self.floods_image_frame)
        self.image_frame.setGeometry(QtCore.QRect(40, 360, 401, 121))
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image_title_label = QtWidgets.QLabel(self.image_frame)
        self.image_title_label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.image_title_label.setStyleSheet("font-size: 10pt;")
        self.image_title_label.setObjectName("image_title_label")
        self.image_description_label = QtWidgets.QLabel(self.image_frame)
        self.image_description_label.setGeometry(QtCore.QRect(10, 30, 281, 16))
        self.image_description_label.setStyleSheet("font-size: 8pt;\n"
"font-style: italic;")
        self.image_description_label.setObjectName("image_description_label")
        self.image_lineedit = QtWidgets.QLineEdit(self.image_frame)
        self.image_lineedit.setGeometry(QtCore.QRect(10, 50, 381, 22))
        self.image_lineedit.setObjectName("image_lineedit")
        self.image_browse_button = QtWidgets.QPushButton(self.image_frame)
        self.image_browse_button.setGeometry(QtCore.QRect(120, 80, 141, 28))
        self.image_browse_button.setObjectName("image_browse_button")
        self.navigation_frame = QtWidgets.QFrame(self.floods_image_frame)
        self.navigation_frame.setGeometry(QtCore.QRect(50, 490, 381, 71))
        self.navigation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation_frame.setObjectName("navigation_frame")
        self.cancel_button = QtWidgets.QPushButton(self.navigation_frame)
        self.cancel_button.setGeometry(QtCore.QRect(20, 20, 141, 28))
        self.cancel_button.setObjectName("cancel_button")
        self.submit_button = QtWidgets.QPushButton(self.navigation_frame)
        self.submit_button.setGeometry(QtCore.QRect(220, 20, 141, 28))
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout.addWidget(self.floods_image_frame)

        self.retranslateUi(FloodsForm)
        QtCore.QMetaObject.connectSlotsByName(FloodsForm)

    def retranslateUi(self, FloodsForm):
        _translate = QtCore.QCoreApplication.translate
        FloodsForm.setWindowTitle(_translate("FloodsForm", "Floods | Form"))
        self.date_title_label.setText(_translate("FloodsForm", "Date"))
        self.date_description_label.setText(_translate("FloodsForm", "The date of when the image of the area was taken."))
        self.date_lineedit.setPlaceholderText(_translate("FloodsForm", "e.g. 2001-03-14 13:10:32 (YYYY-MM-DD HH:MM:SS)"))
        self.location_title_label.setText(_translate("FloodsForm", "Location"))
        self.location_description_label.setText(_translate("FloodsForm", "The main location of the area."))
        self.cityprovince_lineedit.setPlaceholderText(_translate("FloodsForm", "e.g. Quezon City, Iloilo, Agusan del Norte"))
        self.region_combobox.setItemText(0, _translate("FloodsForm", "Select a Region"))
        self.region_combobox.setItemText(1, _translate("FloodsForm", "National Capital Region (NCR)"))
        self.region_combobox.setItemText(2, _translate("FloodsForm", "Cordillera Administrative Region (CAR)"))
        self.region_combobox.setItemText(3, _translate("FloodsForm", "Ilocos Region (Region I)"))
        self.region_combobox.setItemText(4, _translate("FloodsForm", "Cagayan Valley (Region II)"))
        self.region_combobox.setItemText(5, _translate("FloodsForm", "Central Luzon (Region III)"))
        self.region_combobox.setItemText(6, _translate("FloodsForm", "Calabarzon (Region IV-A)"))
        self.region_combobox.setItemText(7, _translate("FloodsForm", "Southwestern Tagalog Region (MIMAROPA)"))
        self.region_combobox.setItemText(8, _translate("FloodsForm", "Bicol Region (Region V)"))
        self.region_combobox.setItemText(9, _translate("FloodsForm", "Western Visayas (Region VI)"))
        self.region_combobox.setItemText(10, _translate("FloodsForm", "Central Visayas (Region VII)"))
        self.region_combobox.setItemText(11, _translate("FloodsForm", "Eastern Visayas (Region VIII)"))
        self.region_combobox.setItemText(12, _translate("FloodsForm", "Zamboanga Peninsula (Region IX)"))
        self.region_combobox.setItemText(13, _translate("FloodsForm", "Northern Mindanao (Region X)"))
        self.region_combobox.setItemText(14, _translate("FloodsForm", "Davao Region (Region XI)"))
        self.region_combobox.setItemText(15, _translate("FloodsForm", "Soccsksargen (Region XII)"))
        self.region_combobox.setItemText(16, _translate("FloodsForm", "Caraga (Region XIII)"))
        self.region_combobox.setItemText(17, _translate("FloodsForm", "Bangsamoro (BARMM)"))
        self.region_label.setText(_translate("FloodsForm", "Region"))
        self.cityprovince_label.setText(_translate("FloodsForm", "City/Province"))
        self.infrastructure_title_label.setText(_translate("FloodsForm", "Type of Infrastructure"))
        self.infrastructure_description_label.setText(_translate("FloodsForm", "The main infrastrure found in the area."))
        self.infrastructure_lineedit.setPlaceholderText(_translate("FloodsForm", "e.g. Roads, Highways, Streets, Buildings, Trees, Terminals"))
        self.damage_title_label.setText(_translate("FloodsForm", "Extent of Damage"))
        self.damage_description_label.setText(_translate("FloodsForm", "The main damaged infrastructure in the area."))
        self.damage_lineedit.setPlaceholderText(_translate("FloodsForm", "e.g. Damaged Roads, Damaged Buildings"))
        self.waterlevel_title_label.setText(_translate("FloodsForm", "Water Level"))
        self.waterlevel_description_label.setText(_translate("FloodsForm", "The highest estimated water level in the area in meters (m)."))
        self.waterlevel_lineedit.setPlaceholderText(_translate("FloodsForm", "e.g. 5.00m, 6.27m, 11.90m"))
        self.imageholder.setText(_translate("FloodsForm", "Insert Image Here"))
        self.image_title_label.setText(_translate("FloodsForm", "Image"))
        self.image_description_label.setText(_translate("FloodsForm", "The clear image of the area."))
        self.image_browse_button.setText(_translate("FloodsForm", "Browse Files"))
        self.cancel_button.setText(_translate("FloodsForm", "Cancel"))
        self.submit_button.setText(_translate("FloodsForm", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FloodsForm = QtWidgets.QWidget()
    ui = Ui_FloodsForm()
    ui.setupUi(FloodsForm)
    FloodsForm.show()
    sys.exit(app.exec_())
