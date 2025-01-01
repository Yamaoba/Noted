import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt6 import QtWidgets
from Write import Ui_Write
from FrontPage import Ui_FrontPage
from About import Ui_Form

class MainWindow(QMainWindow, Ui_FrontPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)  # Setup the UI for the front page
        self.show()  # Show the front page window
        
        # Initialize the Write window, but don't show it yet
        self.WriteGUI = MainWrite(self)

        # Connect the buttons to their respective methods
        self.About.clicked.connect(self.gotoAbout)
        self.Write.clicked.connect(self.WriteGUI.gotoWrite)

    def gotoAbout(self):
        # Set up and show the About window
        self.AboutWindow = QWidget()
        self.AboutUi = Ui_Form()
        self.AboutUi.setupUi(self.AboutWindow)
        self.AboutWindow.show()


class MainWrite(QMainWindow, Ui_Write):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI for the Write window

        # Now that the UI is set up, connect the "Open" action to the method
        self.Open.triggered.connect(self.openFileDialog)

    def gotoWrite(self):
        # Show the Write window when the Write button is clicked
        self.show()  # Show the MainWrite window

    def openFileDialog(self):
        # Create a file dialog and configure it
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        # Execute the dialog and check if a file was selected
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Print the selected file path
                print("Selected File:", selected_files[0])
                # Optionally, you can load the file into the text editor here
                # For example:
                # with open(selected_files[0], 'r') as f:
                #     file_content = f.read()
                #     self.plainTextEdit.setPlainText(file_content)

app = QApplication(sys.argv)

window = MainWindow()  # Create the main window (front page)
window.show()  # Show the main window

sys.exit(app.exec())  # Start the application event loop
