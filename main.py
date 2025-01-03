import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

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
        self.AboutGUI = MainAbout(self)

        # Connect the buttons to their respective methods
        self.About.clicked.connect(self.AboutGUI.gotoAbout)
        self.New.clicked.connect(self.WriteGUI.gotoWrite)
        self.Open.clicked.connect(self.WriteGUI.gotoOpen)

class MainAbout(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Setup the UI for the About window
        
        # This flag will help in checking whether the About window is already open
        self.is_open = False

    def gotoAbout(self):
        if not self.is_open:
            self.AboutWindow = QWidget()
            self.AboutUi = Ui_Form()
            self.AboutUi.setupUi(self.AboutWindow)
            self.AboutWindow.show()
            self.is_open = True
        else:
            # If the About window is already open, bring it to the front
            self.AboutWindow.raise_()
            self.AboutWindow.activateWindow()

class MainWrite(QMainWindow, Ui_Write):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) # Set up the UI for the Write window
        
        self.AboutGUI = None
        
        # Now that the UI is set up, connect the "Open" action to the method
        self.Open.triggered.connect(self.OpenFileDialog)
        self.actionSave.triggered.connect(self.SaveFileDialog)
        self.actionSave_As.triggered.connect(self.SaveAsFileDialog)
        self.actionAbout.triggered.connect(self.showAboutWindow)

    def showAboutWindow(self):
        # Create the About window only when the action is triggered
        if self.AboutGUI is None:
            self.AboutGUI = MainAbout(self)  # Create only once when needed
        self.AboutGUI.gotoAbout()

    def gotoLicense(self):
        # Show the Write window when the Write button is clicked
        f = open(os.getcwd() + "/LICENSE", 'r')
        file_content = f.read()
        self.plainTextEdit.setPlainText(file_content)
        self.plainTextEdit.setReadOnly(True)
        self.setWindowTitle("LICENSE - Noted.")

    def gotoWrite(self):
        # Show the Write window when the Write button is clicked
        self.show()  # Show the MainWrite window

    def gotoOpen(self):
        # Show the Write window when the Write button is clicked
        self.show()
        self.OpenFileDialog()

    def OpenFileDialog(self):
        # Create a file dialog and configure it
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        # Execute the dialog and check if a file was selected
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                with open(selected_files[0], 'r') as f:
                    file_content = f.read()
                    name_title = os.path.basename(str(selected_files[0]))
                    self.plainTextEdit.setPlainText(file_content)
                    self.setWindowTitle(name_title + " - Noted.")
                    self.actionSave.setEnabled(True)
                    print(os.getcwd())
                    print(selected_files)
             
    def SaveFileDialog(self):
        f = open(selected_files[0], 'x')
        f.write(str(self.plainTextEdit.toPlainText()))   
        print(os.path.basename(str(selected_files[0])))
                
    def SaveAsFileDialog(self):
        # Create a file dialog and configure it
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Save File")
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        
        # Execute the dialog and check if a file was selected
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                with open(selected_files[0], 'x') as f:
                    name_title = os.path.basename(str(selected_files[0]))
                    f.write(str(self.plainTextEdit.toPlainText()))
                    self.setWindowTitle(name_title + " - Noted.")
                    self.actionSave.setEnabled(True)
                    

app = QApplication(sys.argv)

window = MainWindow()  # Create the main window (front page)
window.show()  # Show the main window

sys.exit(app.exec())  # Start the application event loop
