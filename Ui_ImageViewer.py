# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer):
        ImageViewer.setObjectName("ImageViewer")
        ImageViewer.resize(711, 633)
        ImageViewer.setMinimumSize(QtCore.QSize(711, 633))
        ImageViewer.setStyleSheet("background-color: #c3fdff;")
        ImageViewer.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.get_info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_info_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_info_btn.sizePolicy().hasHeightForWidth())
        self.get_info_btn.setSizePolicy(sizePolicy)
        self.get_info_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.get_info_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.get_info_btn.setStyleSheet("QPushButton{\n"
"background-color: #eeeeee;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #aeaeae;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get_info_btn.setIcon(icon)
        self.get_info_btn.setIconSize(QtCore.QSize(24, 24))
        self.get_info_btn.setObjectName("get_info_btn")
        self.gridLayout.addWidget(self.get_info_btn, 2, 9, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 6)
        self.image_size_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.image_size_lineEdit.setSizePolicy(sizePolicy)
        self.image_size_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.image_size_lineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.image_size_lineEdit.setStyleSheet("border: 1px solid #c3fdff;\n"
"border-radius: 4px;")
        self.image_size_lineEdit.setText("")
        self.image_size_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.image_size_lineEdit.setReadOnly(True)
        self.image_size_lineEdit.setObjectName("image_size_lineEdit")
        self.gridLayout.addWidget(self.image_size_lineEdit, 2, 3, 1, 1)
        self.left_rotate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_rotate_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_rotate_btn.sizePolicy().hasHeightForWidth())
        self.left_rotate_btn.setSizePolicy(sizePolicy)
        self.left_rotate_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.left_rotate_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.left_rotate_btn.setStyleSheet("QPushButton{\n"
"background-color: #eeeeee;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #aeaeae;\n"
"}")
        self.left_rotate_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/left_rotate_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_rotate_btn.setIcon(icon1)
        self.left_rotate_btn.setIconSize(QtCore.QSize(30, 30))
        self.left_rotate_btn.setObjectName("left_rotate_btn")
        self.gridLayout.addWidget(self.left_rotate_btn, 0, 9, 1, 1)
        self.right_rotate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_rotate_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_rotate_btn.sizePolicy().hasHeightForWidth())
        self.right_rotate_btn.setSizePolicy(sizePolicy)
        self.right_rotate_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.right_rotate_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.right_rotate_btn.setStyleSheet("QPushButton{\n"
"background-color: #eeeeee;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #aeaeae;\n"
"}")
        self.right_rotate_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/right_rotate_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_rotate_btn.setIcon(icon2)
        self.right_rotate_btn.setIconSize(QtCore.QSize(30, 30))
        self.right_rotate_btn.setObjectName("right_rotate_btn")
        self.gridLayout.addWidget(self.right_rotate_btn, 0, 10, 1, 1)
        self.clear_list_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_list_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_list_btn.sizePolicy().hasHeightForWidth())
        self.clear_list_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear_list_btn.setFont(font)
        self.clear_list_btn.setStyleSheet("QPushButton{\n"
"background-color: #ef9a9a;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ffcccb;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #ba6b6c;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_list_btn.setIcon(icon3)
        self.clear_list_btn.setIconSize(QtCore.QSize(24, 24))
        self.clear_list_btn.setObjectName("clear_list_btn")
        self.gridLayout.addWidget(self.clear_list_btn, 0, 0, 1, 1)
        self.image_viewer_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_viewer_list.sizePolicy().hasHeightForWidth())
        self.image_viewer_list.setSizePolicy(sizePolicy)
        self.image_viewer_list.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.image_viewer_list.setFont(font)
        self.image_viewer_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_viewer_list.setStyleSheet("background-color: #eeffff;\n"
"border: 1px solid gray;\n"
"border-radius: 8px;")
        self.image_viewer_list.setLineWidth(0)
        self.image_viewer_list.setMidLineWidth(0)
        self.image_viewer_list.setIconSize(QtCore.QSize(110, 110))
        self.image_viewer_list.setSelectionRectVisible(False)
        self.image_viewer_list.setItemAlignment(QtCore.Qt.AlignHCenter)
        self.image_viewer_list.setObjectName("image_viewer_list")
        self.gridLayout.addWidget(self.image_viewer_list, 1, 0, 2, 2)
        self.remove_item_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_item_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_item_btn.sizePolicy().hasHeightForWidth())
        self.remove_item_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_item_btn.setFont(font)
        self.remove_item_btn.setStyleSheet("QPushButton{\n"
"background-color: #eeeeee;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #aeaeae;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/remove_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_item_btn.setIcon(icon4)
        self.remove_item_btn.setIconSize(QtCore.QSize(24, 24))
        self.remove_item_btn.setObjectName("remove_item_btn")
        self.gridLayout.addWidget(self.remove_item_btn, 0, 1, 1, 1)
        self.geo_location_btn = QtWidgets.QPushButton(self.centralwidget)
        self.geo_location_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geo_location_btn.sizePolicy().hasHeightForWidth())
        self.geo_location_btn.setSizePolicy(sizePolicy)
        self.geo_location_btn.setStyleSheet("QPushButton{\n"
"background-color: #66bb6a;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #98ee99;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #338a3e;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/location_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geo_location_btn.setIcon(icon5)
        self.geo_location_btn.setIconSize(QtCore.QSize(24, 24))
        self.geo_location_btn.setObjectName("geo_location_btn")
        self.gridLayout.addWidget(self.geo_location_btn, 0, 8, 1, 1)
        self.image_viewer = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_viewer.sizePolicy().hasHeightForWidth())
        self.image_viewer.setSizePolicy(sizePolicy)
        self.image_viewer.setMinimumSize(QtCore.QSize(522, 522))
        self.image_viewer.setStyleSheet("border: 2px solid black;\n"
"border-radius: 8px;")
        self.image_viewer.setText("")
        self.image_viewer.setScaledContents(False)
        self.image_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.image_viewer.setObjectName("image_viewer")
        self.gridLayout.addWidget(self.image_viewer, 1, 2, 1, 9)
        self.add_image_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_image_btn.sizePolicy().hasHeightForWidth())
        self.add_image_btn.setSizePolicy(sizePolicy)
        self.add_image_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.add_image_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_image_btn.setFont(font)
        self.add_image_btn.setStyleSheet("QPushButton{\n"
"background-color: #2196f3;\n"
"border-radius: 8px;\n"
"border: 1.5px solid;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #6ec6ff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #0069c0;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/image_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_image_btn.setIcon(icon6)
        self.add_image_btn.setIconSize(QtCore.QSize(24, 24))
        self.add_image_btn.setObjectName("add_image_btn")
        self.gridLayout.addWidget(self.add_image_btn, 2, 10, 1, 1)
        self.image_size_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.image_size_label.setFont(font)
        self.image_size_label.setObjectName("image_size_label")
        self.gridLayout.addWidget(self.image_size_label, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        ImageViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImageViewer)
        self.image_viewer_list.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "Image Viewer"))
        self.get_info_btn.setText(_translate("ImageViewer", " Get\n"
" Info"))
        self.image_size_lineEdit.setPlaceholderText(_translate("ImageViewer", "width x height"))
        self.clear_list_btn.setText(_translate("ImageViewer", "Clear\n"
" List"))
        self.remove_item_btn.setText(_translate("ImageViewer", "Remove \n"
"   Item"))
        self.geo_location_btn.setText(_translate("ImageViewer", "    Geo\n"
"Location"))
        self.add_image_btn.setText(_translate("ImageViewer", "   Add\n"
" Image"))
        self.image_size_label.setText(_translate("ImageViewer", "Current Size:"))
