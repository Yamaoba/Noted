# Form implementation generated from reading ui file 'Write.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Write(object):
    def setupUi(self, Write):
        Write.setObjectName("Write")
        Write.resize(798, 600)
        Write.setAnimated(False)
        Write.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=Write)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextEditable|QtCore.Qt.TextInteractionFlag.TextEditorInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        Write.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Write)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(parent=self.menubar)
        self.File.setObjectName("File")
        self.Edit = QtWidgets.QMenu(parent=self.menubar)
        self.Edit.setObjectName("Edit")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Write.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentNew")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentOpen")
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=Write)
        self.actionSave.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSave")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSaveAs")
        self.actionSave_As.setIcon(icon)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::ApplicationExit")
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::HelpAbout")
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicense = QtGui.QAction(parent=Write)
        self.actionLicense.setObjectName("actionLicense")
        self.actionPrint = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::Printer")
        self.actionPrint.setIcon(icon)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPage_Setup = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentPrintPreview")
        self.actionPage_Setup.setIcon(icon)
        self.actionPage_Setup.setObjectName("actionPage_Setup")
        self.action_PrintSetup = QtGui.QAction(parent=Write)
        self.action_PrintSetup.setObjectName("action_PrintSetup")
        self.actionUndo = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditUndo")
        self.actionUndo.setIcon(icon)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditRedo")
        self.actionRedo.setIcon(icon)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditCut")
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditCopy")
        self.actionCopy.setIcon(icon)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditPaste")
        self.actionPaste.setIcon(icon)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditDelete")
        self.actionDelete.setIcon(icon)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtGui.QAction(parent=Write)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditSelectAll")
        self.actionSelect_All.setIcon(icon)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionWrap_Lines = QtGui.QAction(parent=Write)
        self.actionWrap_Lines.setCheckable(True)
        self.actionWrap_Lines.setChecked(True)
        self.actionWrap_Lines.setIconVisibleInMenu(True)
        self.actionWrap_Lines.setObjectName("actionWrap_Lines")
        self.actionFont = QtGui.QAction(parent=Write)
        self.actionFont.setObjectName("actionFont")
        self.actionOther = QtGui.QAction(parent=Write)
        self.actionOther.setObjectName("actionOther")
        self.File.addAction(self.actionNew)
        self.File.addAction(self.actionOpen)
        self.File.addAction(self.actionSave)
        self.File.addAction(self.actionSave_As)
        self.File.addSeparator()
        self.File.addAction(self.actionPrint)
        self.File.addAction(self.actionPage_Setup)
        self.File.addAction(self.action_PrintSetup)
        self.File.addSeparator()
        self.File.addAction(self.actionExit)
        self.Edit.addAction(self.actionUndo)
        self.Edit.addAction(self.actionRedo)
        self.Edit.addSeparator()
        self.Edit.addAction(self.actionCut)
        self.Edit.addAction(self.actionCopy)
        self.Edit.addAction(self.actionPaste)
        self.Edit.addAction(self.actionDelete)
        self.Edit.addSeparator()
        self.Edit.addAction(self.actionSelect_All)
        self.Edit.addSeparator()
        self.Edit.addAction(self.actionWrap_Lines)
        self.Edit.addAction(self.actionFont)
        self.Edit.addAction(self.actionOther)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Edit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Write)
        self.actionExit.triggered.connect(Write.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Write)

    def retranslateUi(self, Write):
        _translate = QtCore.QCoreApplication.translate
        Write.setWindowTitle(_translate("Write", "untitled - Noted."))
        self.File.setTitle(_translate("Write", "File"))
        self.Edit.setTitle(_translate("Write", "Edit"))
        self.menuHelp.setTitle(_translate("Write", "Help"))
        self.actionNew.setText(_translate("Write", "New"))
        self.actionNew.setToolTip(_translate("Write", "New"))
        self.actionNew.setShortcut(_translate("Write", "Ctrl+N"))
        self.actionOpen.setText(_translate("Write", "Open"))
        self.actionOpen.setToolTip(_translate("Write", "Open"))
        self.actionOpen.setShortcut(_translate("Write", "Ctrl+O"))
        self.actionSave.setText(_translate("Write", "Save"))
        self.actionSave.setToolTip(_translate("Write", "Save"))
        self.actionSave.setShortcut(_translate("Write", "Ctrl+S"))
        self.actionSave_As.setText(_translate("Write", "Save As"))
        self.actionExit.setText(_translate("Write", "Exit"))
        self.actionExit.setToolTip(_translate("Write", "Exit"))
        self.actionExit.setShortcut(_translate("Write", "Ctrl+Q"))
        self.actionAbout.setText(_translate("Write", "About Noted."))
        self.actionLicense.setText(_translate("Write", "License"))
        self.actionPrint.setText(_translate("Write", "Print"))
        self.actionPrint.setShortcut(_translate("Write", "Ctrl+P"))
        self.actionPage_Setup.setText(_translate("Write", "Page Setup"))
        self.action_PrintSetup.setText(_translate("Write", "Printer Setup"))
        self.actionUndo.setText(_translate("Write", "Undo"))
        self.actionUndo.setShortcut(_translate("Write", "Ctrl+Z"))
        self.actionRedo.setText(_translate("Write", "Redo"))
        self.actionRedo.setShortcut(_translate("Write", "Ctrl+Y"))
        self.actionCut.setText(_translate("Write", "Cut"))
        self.actionCut.setShortcut(_translate("Write", "Ctrl+X"))
        self.actionCopy.setText(_translate("Write", "Copy"))
        self.actionCopy.setShortcut(_translate("Write", "Ctrl+C"))
        self.actionPaste.setText(_translate("Write", "Paste"))
        self.actionPaste.setShortcut(_translate("Write", "Ctrl+V"))
        self.actionDelete.setText(_translate("Write", "Delete"))
        self.actionDelete.setShortcut(_translate("Write", "Del"))
        self.actionSelect_All.setText(_translate("Write", "Select All"))
        self.actionSelect_All.setShortcut(_translate("Write", "Ctrl+A"))
        self.actionWrap_Lines.setText(_translate("Write", "Wrap Lines"))
        self.actionFont.setText(_translate("Write", "Font"))
        self.actionOther.setText(_translate("Write", "Other"))
