from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import os.path
import time


# Returns a human readable string representation of bytes.
def human_readable_size(n_bytes, units=None):
    if units is None:
        units = [' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
    return str(n_bytes) + units[0] if n_bytes < 1024 else human_readable_size(n_bytes >> 10, units[1:])


class ExifImageModel:

    # Initializes the Model.
    def __init__(self, name=None):

        # The current image displayed in ImageViewer.
        self.current_image = name

        # List of images.
        self.image_list = []

        # Dictionary to contain exif details.
        self.exif_details = {}

        # Dictionary to contain general details.
        self.general_details = {}

    # Updates the Model, the parameter "name" indicates the name of current image.
    def update_model(self, name):
        self.current_image = name
        print("\n")
        print("• The Current Image is: " + str(self.current_image))

    # Inserts an image in the list and before inserting it, checks if it is not already in the list.
    def insert_image_in_list(self, image):
        for i in self.image_list:
            if i == image:
                return
        self.image_list.append(image)

    # Returns element of list at a specific position. Where "image_position" indicates the position of image in list.
    def get_element(self, image_position):
        current_element = self.image_list[image_position]
        self.update_model(current_element)

    # Clears the image list.
    def clear_list(self):
        self.image_list.clear()

    # Removes an image from the list at a specific position and updates the model.
    def remove_item(self, image_position):

        # If image removed is the displayed image && not in first position && the list contains more than only one elem.
        if self.image_list[image_position] == self.current_image and image_position != 0 and len(self.image_list) != 1:
            # Updates the main image with the one above.
            self.update_model(self.image_list[image_position - 1])

        # If image removed is the displayed image && in first position && the list contains more than only one elem.
        elif self.image_list[image_position] == self.current_image and image_position == 0 and len(
                self.image_list) != 1:
            # Updates the main image with the one below.
            self.update_model(self.image_list[image_position + 1])

        # If the list contains only one element.
        elif len(self.image_list) == 1:
            self.update_model("")

        for i, v in enumerate(self.image_list):
            if i == image_position:
                self.image_list.pop(i)

    # Returns the list of images.
    def get_list(self):
        return self.image_list

    # Extracts the exif details of the image, where "image" is the current image.
    def extract_exif_details(self, image):
        try:
            img = Image.open(image)

            # If the type of image is PNG, the exif details don't exist, so extracts only data associated with the image
            if img.format != "PNG":
                info = img._getexif()
            else:
                info = img.info
            for tag, value in info.items():
                decoded_data = TAGS.get(tag, tag)
                if decoded_data == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded_data = GPSTAGS.get(t, t)
                        gps_data[sub_decoded_data] = value[t]
                    self.exif_details[decoded_data] = gps_data
                else:
                    self.exif_details[decoded_data] = value
        except:
            print("• No Exif Details available for this image")

    # Returns the exif details
    def get_exif_details(self):
        return self.exif_details

    # Clears the exif details list.
    def clear_exif_details(self):
        self.exif_details.clear()

    # Extracts the general details of the image, where "image" is the current image.
    def extract_general_details(self, image):
        try:
            img = Image.open(image)
            self.general_details['File name'] = os.path.basename(img.filename)
            self.general_details['Image type'] = img.format
            self.general_details['File size'] = human_readable_size(
                os.stat(img.filename).st_size) + " (%5d bytes)" % os.stat(
                img.filename).st_size
            self.general_details['Creation date'] = time.ctime(os.path.getctime(img.filename))
            self.general_details['Modification date'] = time.ctime(os.path.getmtime(img.filename))
            self.general_details['Image size'] = img.size
            self.general_details['Color model'] = img.mode
        except:
            print("• No General Details available for this image")

    # Returns the general details
    def get_general_details(self):
        return self.general_details

    # Clears the general details list.
    def clear_general_details(self):
        self.general_details.clear()

    # Converts GPS Info from Degrees Minutes Seconds (DMS) to Decimal Degrees (DD)
    def convert_to_degree(self, value):
        degrees = float(value[0])
        minutes = float(value[1]) / 60.0
        seconds = float(value[2]) / 3600.0

        return degrees + minutes + seconds

    # Returns the coordinate string to be appended to the google maps url.
    def get_position(self):
        if 'GPSInfo' in self.exif_details:
            if self.exif_details['GPSInfo']['GPSLatitudeRef'] == 'N' and self.exif_details['GPSInfo'][
                'GPSLongitudeRef'] == 'E':
                return str(self.convert_to_degree(self.exif_details['GPSInfo']['GPSLatitude'])) + ',' + str(
                    self.convert_to_degree(self.exif_details['GPSInfo']['GPSLongitude']))

            if self.exif_details['GPSInfo']['GPSLatitudeRef'] == 'N' and self.exif_details['GPSInfo'][
                'GPSLongitudeRef'] == 'W':
                return str(self.convert_to_degree(self.exif_details['GPSInfo']['GPSLatitude'])) + ',' + str(
                    -self.convert_to_degree(self.exif_details['GPSInfo']['GPSLongitude']))

            if self.exif_details['GPSInfo']['GPSLatitudeRef'] == 'S' and self.exif_details['GPSInfo'][
                'GPSLongitudeRef'] == 'E':
                return str(-self.convert_to_degree(self.exif_details['GPSInfo']['GPSLatitude'])) + ',' + str(
                    self.convert_to_degree(self.exif_details['GPSInfo']['GPSLongitude']))

            if self.exif_details['GPSInfo']['GPSLatitudeRef'] == 'S' and self.exif_details['GPSInfo'][
                'GPSLongitudeRef'] == 'W':
                return str(-self.convert_to_degree(self.exif_details['GPSInfo']['GPSLatitude'])) + ',' + str(
                    -self.convert_to_degree(self.exif_details['GPSInfo']['GPSLongitude']))
