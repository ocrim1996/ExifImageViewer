# Exif and Image Viewer
## General Introduction to Exif
[![MIT License](https://img.shields.io/badge/License-MIT-blueviolet)](https://opensource.org/licenses/mit-license.php)
[![Platform](https://img.shields.io/badge/OS-Ubuntu%20v.20.04-red)](https://www.ubuntu-it.org/download)
[![Library](https://img.shields.io/badge/Pyqt5-5.15.1-informational)](https://pypi.org/project/PyQt5/)
[![Library](https://img.shields.io/badge/Pilllow-8.0.1-informational)](https://pypi.org/project/Pillow/)

**Exchangeable image file format**, also known as **Exif**, is a standard the defines specific information related to an image or other media captured by digital cameras (including smartphones or tablets). This information is also know as “metadata”.
It is capable of storing such important data as:
- Camera model;
- Image orientation;
- Shuttered speed;
- Focal Length;
- ISO speed information;
- Camera exposure;
- White balance;
- Date / time the image was captured;
- and even GPS location.

The only file formats that can handle EXIF are **JPEG** and **TIFF** (regarding pictures), which means that you often cannot read the data from other image formats such as GIF and PNG.
EXIF data is embedded in the physical file, and specific tools that are capable of reading this information must be used to view it.

## Goal of the Project

In this project the goal is to have an image viewer and for each image to have the possibility to extract the exif data. Images can also be rotated clockwise or counterclockwise. Furthermore, if an image contains exif data relating to GPS information, it can be geolocated on Google Maps.

## Project Implementation

The project is built using **Python** and pattern **MVC** (**Model-View-Controller**). In particular, PyQt5 was used to develop the GUI, with the help of Qt Designer.

### The Model
The model is implemented in the Python file `ExifImageModel.py` through the homonymous class `ExifImageModel`. The model encapsulates the fundamental data for the application. It provides methods for obtaining, setting, modifying and evolving the state.
Some operations it deals with are:
- Manage the list of images;
- Extract general details;
- Extract Exif details;
- Get the coordinate string.

### The GUI (Graphic User Interface)
The GUI includes all the graphic components (such as buttons, labels, lists) and is divided into two parts:
- the one relating to the main page that deals with displaying the image and managing various operations (in `ImageViewer.py`).
- the one related to the widget that shows the general details and the exif details in two separate tabs (in `ExifViewer.py`).

The graphical interface is built through the **Qt Designer** development environment, generating the two files `Ui_ImageViewer.py` and `Ui_ExifViewer.py`, which are then used in the respective classes `ImageViewer` and `ExifViewer`.

### The Controller
To instantiate and start using all these components it is necessary to run the script inside the `main.py` file which technically contains the Controller code.

## How the Project Looks

### ExifViewer
ExifViewer is the main page that appears when you run the project. Its appearance is as follows:

<p align="center">
  <img src="/Readme_Documents/ImageViewer_Empty.png" alt="ImageViewer Empty" width="50%"/>
</p>

There are 6 buttons, but in the initial state the only one enabled is "**Add Image**" which allows you to add an image to the project via a FileDialog.


When the images are loaded, all buttons are enabled (except "**Remove Item**" which is activated only when you click on an image in the list).

<p float="left" align="center">
  <img src="/Readme_Documents/ImageViewer_with_Image.png" alt="ImageViewer with Image" width="45%" />
  <img src="/Readme_Documents/ImageViewer_with_Selected_Image.png" alt="ImageViewer with Selected Image" width="45%" /> 
</p>

**Each button** performs an operation:
- **Add Image** —> adds an image to the project, inserting it in the list of images and updating the view with the last image inserted;
- **Left Rotate** —> Rotates the image 90 degrees counterclockwise;
- **Right Rotate** —> Rotates the image 90 degrees clockwise;
- **Geo Location** —> If the image contains GPS information, it opens Google Maps by geolocating the image on the map;
- **Clear List** —> Removes all images from the list returning to the initial state;
- **Remove Item** —> Removes only the selected item (button enabled only when you click on an image in the list)
- **Get Info** —> Opens the widget tab showing the general details and exif details of the selected image.

### ExifViewer
ExifViewer is a widget with two tabs:
- The first tab shows a list of all the general details of the selected image.
- The second tab shows the exif details of the selected image.

<p float="left" align="center">
  <img src="/Readme_Documents/ExifViewer_General_Details.png" alt="General Details" width="45%" />
  <img src="/Readme_Documents/ExifViewer_Exif_Details.png" alt="Exif Details" width="45%" /> 
</p>

## Run the Project

To run the project just run the **main.py** file. To test the project you can select the images uploaded to this repository in the `TestImages` folder.
```sh
$ python3 main.py
```

## Functionalities

The application allows you to view images like .jpeg, tiff etc... The imported image is displayed on the main page, with the list of all imported images alongside. The window can be resized by obtaining a relative resizing of the selected image. It is possible to change the displayed image by simply clicking on another image in the list on the side. The image can also be rotated 90 degrees either left (counterclockwise) or right (clockwise). In addition, if the image contains GPS information, the image can be geolocated via Google Maps with the relative "**Geo Location**" button.

## Use Cases Examples
These are two examples of a use cases:

<p align="center">
  <img src="/Readme_Documents/Use_Case_Example.gif" alt="Use Case Example"/>
</p>

> View an image, resize the window, rotate the image, open the exif tab and delete the images.

<br /> 
<br />  
  
<p align="center">
  <img src="/Readme_Documents/Geolocation_Example.gif" alt="Geolocation Example"/>
</p>

> Geolocate an image on the map using Google Maps.

## Libraries Needed
To run the code you need the following libraries:

Library | Version
------------- | -------------
**PyQt5**  | >= 5.15.1
**Pillow** | >= 8.0.1 

The code has been tested with Ubuntu 20.04 and MacOS Catalina (version 10.15.2).

## License
MIT License. See [LICENSE](LICENSE) file for further information.

