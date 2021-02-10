import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QTreeWidgetItem)
from Ui_ExifViewer import Ui_ExifViewer


class ExifViewer(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_ExifViewer()
        self.ui.setupUi(self)
        self.center_on_screen()

    # Sets the reference to the model and sets general details into widget.
    def tab_general_details_ui(self, model):
        self.model = model
        self.model.clear_general_details()
        self.model.extract_general_details(self.model.current_image)
        general_details = self.model.get_general_details()

        # If there are general details on current image, call fill_widget function.
        if general_details:
            self.fill_widget(self.ui.general_details_data, general_details)

        # If general details on current image are empty.
        else:
            self.ui.general_details_data.clear()
            self.ui.message = QTreeWidgetItem(self.ui.general_details_data)
            self.ui.message.setText(0, "No General Details available for this image")
            self.ui.message.setTextAlignment(0, Qt.AlignCenter)

    # Sets the reference to the model and sets exif details into widget.
    def tab_exif_details_ui(self, model):
        self.model = model
        self.model.clear_exif_details()
        self.model.extract_exif_details(self.model.current_image)
        exif_details = self.model.get_exif_details()

        # If there are exif details on current image, call fill_widget function.
        if exif_details:
            self.ui.exif_details_data.clear()
            self.fill_widget(self.ui.exif_details_data, exif_details)

        # If exif details on current image are empty.
        else:
            self.ui.exif_details_data.clear()
            self.ui.message = QTreeWidgetItem(self.ui.exif_details_data)
            self.ui.message.setText(0, "No Exif Details available for this image")
            self.ui.message.setTextAlignment(0, Qt.AlignCenter)

    # Fills the widget by calling the fill_item() function inside it
    def fill_widget(self, widget, value):
        self.widget = widget
        self.widget.clear()
        self.fill_item(self.widget.invisibleRootItem(), value)

    # Fills the widget with values of General Details or Exif Details.
    def fill_item(self, item, value):
        item.setExpanded(True)
        if type(value) is dict:
            for key, val in value.items():
                child = QTreeWidgetItem()
                child.setText(0, str(key))
                item.addChild(child)
                self.fill_item(child, val)
        elif type(value) is list:
            for val in value:
                child = QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:
                    child.setText(0, '[dict]')
                    self.fill_item(child, val)
                elif type(val) is list:
                    child.setText(0, '[list]')
                    self.fill_item(child, val)
                else:
                    child.setText(0, str(val))
                    child.setExpanded(True)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(value))
            item.addChild(child)

    # Places the window that opens in the center of the screen
    def center_on_screen(self):
        frame_gm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(
            PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        center_point = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())
