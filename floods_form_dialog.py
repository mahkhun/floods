# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floods_form_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FloodsFormDialog(object):
    def setupUi(self, FloodsFormDialog):
        FloodsFormDialog.setObjectName("FloodsFormDialog")
        FloodsFormDialog.resize(795, 454)
        self.header_label = QtWidgets.QLabel(FloodsFormDialog)
        self.header_label.setGeometry(QtCore.QRect(230, 20, 351, 16))
        self.header_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;\n"
"")
        self.header_label.setObjectName("header_label")
        self.navigation_frame = QtWidgets.QFrame(FloodsFormDialog)
        self.navigation_frame.setGeometry(QtCore.QRect(170, 410, 461, 31))
        self.navigation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation_frame.setObjectName("navigation_frame")
        self.create_new_button = QtWidgets.QPushButton(self.navigation_frame)
        self.create_new_button.setGeometry(QtCore.QRect(10, 0, 211, 28))
        self.create_new_button.setObjectName("create_new_button")
        self.return_button = QtWidgets.QPushButton(self.navigation_frame)
        self.return_button.setGeometry(QtCore.QRect(240, 0, 211, 28))
        self.return_button.setObjectName("return_button")
        self.date_label = QtWidgets.QLabel(FloodsFormDialog)
        self.date_label.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.date_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.date_label.setObjectName("date_label")
        self.date_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.date_description_label.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.date_description_label.setObjectName("date_description_label")
        self.location_label = QtWidgets.QLabel(FloodsFormDialog)
        self.location_label.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.location_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.location_label.setObjectName("location_label")
        self.infrastructure_label = QtWidgets.QLabel(FloodsFormDialog)
        self.infrastructure_label.setGeometry(QtCore.QRect(10, 230, 161, 16))
        self.infrastructure_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.infrastructure_label.setObjectName("infrastructure_label")
        self.damage_label = QtWidgets.QLabel(FloodsFormDialog)
        self.damage_label.setGeometry(QtCore.QRect(10, 290, 121, 16))
        self.damage_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.damage_label.setObjectName("damage_label")
        self.region_label = QtWidgets.QLabel(FloodsFormDialog)
        self.region_label.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.region_label.setObjectName("region_label")
        self.location_label_2 = QtWidgets.QLabel(FloodsFormDialog)
        self.location_label_2.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.location_label_2.setObjectName("location_label_2")
        self.waterlevel_label = QtWidgets.QLabel(FloodsFormDialog)
        self.waterlevel_label.setGeometry(QtCore.QRect(10, 350, 91, 16))
        self.waterlevel_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.waterlevel_label.setObjectName("waterlevel_label")
        self.region_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.region_description_label.setGeometry(QtCore.QRect(10, 140, 141, 21))
        self.region_description_label.setObjectName("region_description_label")
        self.location_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.location_description_label.setGeometry(QtCore.QRect(10, 190, 141, 21))
        self.location_description_label.setObjectName("location_description_label")
        self.infrastructure_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.infrastructure_description_label.setGeometry(QtCore.QRect(10, 250, 141, 21))
        self.infrastructure_description_label.setObjectName("infrastructure_description_label")
        self.damage_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.damage_description_label.setGeometry(QtCore.QRect(10, 310, 141, 21))
        self.damage_description_label.setObjectName("damage_description_label")
        self.waterlevel_description_label = QtWidgets.QLabel(FloodsFormDialog)
        self.waterlevel_description_label.setGeometry(QtCore.QRect(10, 370, 141, 21))
        self.waterlevel_description_label.setObjectName("waterlevel_description_label")
        self.image_label = QtWidgets.QLabel(FloodsFormDialog)
        self.image_label.setGeometry(QtCore.QRect(290, 50, 51, 21))
        self.image_label.setStyleSheet("font-size: 9pt;\n"
"font-style: italic;")
        self.image_label.setObjectName("image_label")
        self.image_placeholder = QtWidgets.QLabel(FloodsFormDialog)
        self.image_placeholder.setGeometry(QtCore.QRect(290, 80, 141, 21))
        self.image_placeholder.setObjectName("image_placeholder")

        self.retranslateUi(FloodsFormDialog)
        QtCore.QMetaObject.connectSlotsByName(FloodsFormDialog)

    def retranslateUi(self, FloodsFormDialog):
        _translate = QtCore.QCoreApplication.translate
        FloodsFormDialog.setWindowTitle(_translate("FloodsFormDialog", "Floods | Form Dialog"))
        self.header_label.setText(_translate("FloodsFormDialog", "The following data has been added to the database:"))
        self.create_new_button.setText(_translate("FloodsFormDialog", "Create another New Flood Data"))
        self.return_button.setText(_translate("FloodsFormDialog", "Return Home"))
        self.date_label.setText(_translate("FloodsFormDialog", "Date"))
        self.date_description_label.setText(_translate("FloodsFormDialog", "Description: "))
        self.location_label.setText(_translate("FloodsFormDialog", "Location"))
        self.infrastructure_label.setText(_translate("FloodsFormDialog", "Type of Infrastructure"))
        self.damage_label.setText(_translate("FloodsFormDialog", "Extent of Damage"))
        self.region_label.setText(_translate("FloodsFormDialog", "Region"))
        self.location_label_2.setText(_translate("FloodsFormDialog", "City/Province"))
        self.waterlevel_label.setText(_translate("FloodsFormDialog", "Water Level"))
        self.region_description_label.setText(_translate("FloodsFormDialog", "Description: "))
        self.location_description_label.setText(_translate("FloodsFormDialog", "Description:"))
        self.infrastructure_description_label.setText(_translate("FloodsFormDialog", "Description:"))
        self.damage_description_label.setText(_translate("FloodsFormDialog", "Description:"))
        self.waterlevel_description_label.setText(_translate("FloodsFormDialog", "Description:"))
        self.image_label.setText(_translate("FloodsFormDialog", "Image"))
        self.image_placeholder.setText(_translate("FloodsFormDialog", "Insert Image Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FloodsFormDialog = QtWidgets.QDialog()
    ui = Ui_FloodsFormDialog()
    ui.setupUi(FloodsFormDialog)
    FloodsFormDialog.show()
    sys.exit(app.exec_())