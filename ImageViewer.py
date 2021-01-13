import webbrowser

import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QFileDialog, QMessageBox, QMainWindow)
from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtWidgets import (QListWidgetItem)
from PyQt5.QtGui import (QPixmap, QTransform, QIcon, QImage)
from PIL import Image
from Ui_ImageViewer import Ui_ImageViewer
from ExifImageModel import ExifImageModel
from ExifViewer import ExifViewer


class ImageViewer(QMainWindow):

    def __init__(self):
        super().__init__()

        # UI Initialization
        self.ui = Ui_ImageViewer()
        self.ui.setupUi(self)

        # Instantiates an object of type ExifView
        self.exif_viewer = ExifViewer()

        # Instantiates the model of type ExifImageModel
        self._model = ExifImageModel()

        # Some Parameters
        self.rotation_degree = 0
        self.isRotated = False
        self.hasGPSInfo = False

        # Set the "click event" on the list images.
        self.ui.image_viewer_list.itemClicked.connect(self.upload_image_view)
        self.ui.image_viewer_list.itemClicked.connect(self.activate_remove_item_button)

        # Connect buttons to functions
        self.ui.add_image_btn.clicked.connect(self.add_image)
        self.ui.get_info_btn.clicked.connect(self.get_info)
        self.ui.clear_list_btn.clicked.connect(self.clear_list)
        self.ui.remove_item_btn.clicked.connect(self.remove_item)
        self.ui.left_rotate_btn.clicked.connect(self.left_rotate)
        self.ui.right_rotate_btn.clicked.connect(self.right_rotate)
        self.ui.geo_location_btn.clicked.connect(self.open_google_map)

    # Opens the widget to visualize General Details and Exif Details.
    def get_info(self):
        self.exif_viewer.tab_general_details_ui(self._model)
        self.exif_viewer.tab_exif_details_ui(self._model)
        self.exif_viewer.show()

    # Opens a File Dialog to choose the image to upload, then updates the model, fills and populate image list.
    def add_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Images (*.jpg *.jpeg *.png *.JPG *.PNG)",
                                                  options=options)

        # Checks (with bool()) if the file is a real image with a picture or only a saved file as .jpg/.jpeg/.png.
        # Also checks that the image to insert is not already in the list.
        self._model.general_details.clear()
        self._model.extract_general_details(filename)
        general_details = self._model.get_general_details()
        if filename and bool(general_details) and filename not in self._model.image_list:
            self.enable_buttons()
            self.ui.remove_item_btn.setEnabled(False)

            self._model.update_model(filename)
            self._model.insert_image_in_list(filename)

            if self.isRotated:
                self.isRotated = False

            self.update_image_view()
            self.populate_image_list()

        elif filename in self._model.image_list:
            QMessageBox.about(self, "Duplicated Image", "Image already in the list")
        else:
            QMessageBox.about(self, "Image Error", "No image selected")

    # Updates the view of image in the main page.
    def update_image_view(self):
        if self._model.current_image and not self.isRotated:
            self.qpix = QPixmap(self._model.current_image)
            width = self.ui.image_viewer.width() - 40
            height = self.ui.image_viewer.height() - 40
            self.ui.image_viewer.setPixmap(
                self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            # To print the image size.
            image_width = self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio,
                                           Qt.SmoothTransformation).width()
            image_height = self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio,
                                            Qt.SmoothTransformation).height()
            print("• Image Size: " + str(image_width) + "px " + "X " + str(image_height) + "px")

            image_size_str = str(str(image_width) + ' x ' + str(image_height))
            self.ui.image_size_lineEdit.setText(image_size_str)

        elif self._model.current_image and self.isRotated:
            width = self.ui.image_viewer.width() - 40
            height = self.ui.image_viewer.height() - 40
            self.ui.image_viewer.setPixmap(
                self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            # To print the image size.
            image_width = self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio,
                                           Qt.SmoothTransformation).width()
            image_height = self.qpix.scaled(QSize(max(width, 512), max(height, 512)), Qt.KeepAspectRatio,
                                            Qt.SmoothTransformation).height()
            print("• Image Size: " + str(image_width) + "px " + "X " + str(image_height) + "px")

            image_size_str = str(str(image_width) + ' x ' + str(image_height))
            self.ui.image_size_lineEdit.setText(image_size_str)

        elif not self._model.current_image:
            self.qpix = QPixmap()
            self.ui.image_viewer.setPixmap(self.qpix)
            self.ui.image_size_lineEdit.setText('')
            self.ui.get_info_btn.setEnabled(False)
            self.ui.left_rotate_btn.setEnabled(False)
            self.ui.right_rotate_btn.setEnabled(False)

    # Resizes the image size when the page is resized.
    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.update_image_view()

    # Rotates the displayed image 90 degrees to the left and updates the image view (Counterclockwise)
    def left_rotate(self):
        self.isRotated = True
        self.rotation_degree -= 90

        transform = QTransform().rotate(self.rotation_degree)
        self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)

        self.update_image_view()
        self.rotation_degree = 0

    # Rotates the displayed image 90 degrees to the right and updates the image view (Clockwise)
    def right_rotate(self):
        self.isRotated = True
        self.rotation_degree += 90

        transform = QTransform().rotate(self.rotation_degree)
        self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)

        self.update_image_view()
        self.rotation_degree = 0

    # Populates the image list.
    def populate_image_list(self):
        # In case we're repopulating the image list, clear the image list.
        self.ui.image_viewer_list.clear()

        # Creates a list item for each image file, setting the tooltip and icon.
        for image in self._model.get_list():
            picture = Image.open(image)
            picture.thumbnail((72, 72), Image.ANTIALIAS)
            icon = QIcon(QPixmap.fromImage(QImage(picture.filename)))

            # Inserts the image in list
            item = QListWidgetItem(self.ui.image_viewer_list)
            item.setToolTip(image)
            item.setIcon(icon)

    # If click on a image in the list, that image will displayed in the image viewer.
    def upload_image_view(self):
        if self.isRotated:
            self.isRotated = False
        self.current_item = self.ui.image_viewer_list.currentRow()
        self._model.get_element(self.current_item)  # Get image from model
        self.update_image_view()
        if not self.ui.get_info_btn.isEnabled():
            self.ui.get_info_btn.setEnabled(True)
            self.ui.left_rotate_btn.setEnabled(True)
            self.ui.right_rotate_btn.setEnabled(True)

    # Clears the list and updates the model.
    def clear_list(self):
        self._model.clear_list()
        self._model.update_model("")
        self.ui.image_viewer_list.clear()
        self.update_image_view()
        self.disable_buttons()

    # Disables all buttons.
    def disable_buttons(self):
        self.ui.get_info_btn.setEnabled(False)
        self.ui.left_rotate_btn.setEnabled(False)
        self.ui.right_rotate_btn.setEnabled(False)
        self.ui.clear_list_btn.setEnabled(False)
        self.ui.remove_item_btn.setEnabled(False)
        self.ui.geo_location_btn.setEnabled(False)

    # Enables all buttons except the one to remove a single item.
    def enable_buttons(self):
        self.ui.get_info_btn.setEnabled(True)
        self.ui.left_rotate_btn.setEnabled(True)
        self.ui.right_rotate_btn.setEnabled(True)
        self.ui.clear_list_btn.setEnabled(True)
        self.ui.geo_location_btn.setEnabled(True)

    # Activates the button to remove a single item from the image list.
    def activate_remove_item_button(self):
        self.ui.remove_item_btn.setEnabled(True)
        self.current_item = self.ui.image_viewer_list.currentRow()

    # Removes a selected item from image list and call model to remove the image.
    def remove_item(self):
        self._model.remove_item(self.current_item)
        self.ui.image_viewer_list.takeItem(self.current_item)
        if self.current_item == 0 and not self._model.image_list:
            self._model.update_model("")
            self.disable_buttons()
        elif self.current_item != 0:
            self.current_item = self.current_item - 1
            self.ui.image_viewer_list.setCurrentRow(self.current_item)

        # Set isRotated to False to enter the correct condition of the update_image_view( ) function.
        self.isRotated = False
        self.update_image_view()

    # Opens Google Maps in the location where the photo was taken.
    def open_google_map(self):
        self._model.clear_exif_details()
        self._model.clear_general_details()
        self._model.extract_general_details(self._model.current_image)
        self._model.extract_exif_details(self._model.current_image)
        position = self._model.get_position()
        if position:
            webbrowser.open_new("https://www.google.com/maps/search/?api=1&query=" + str(position))
        else:
            QMessageBox.about(self, "GPS Error", "This image hasn't GPS Info")

    # Places the window that opens in the center of the screen
    def center_on_screen(self):
        frame_gm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(
            PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        center_point = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())
