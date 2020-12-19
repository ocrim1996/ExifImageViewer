import sys
from ImageViewer import ImageViewer
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ImageViewer()
    window.center_on_screen()
    window.show()
    sys.exit(app.exec_())
