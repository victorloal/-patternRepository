from PyQt5 import QtCore, QtGui, QtWidgets
from logic.pattern_repository import PatternRepository
from logic.UI.ui_messageBoxManager import MessageBoxManager
from ui_generated.ui_dialogKnowUses import Ui_KnowUses

class KnowUses(QtWidgets.QDialog, Ui_KnowUses):
    """
    A dialog for managing known uses.

    This dialog allows users to add or remove known uses associated with a pattern.
    """

    def __init__(self, parent=None):
        """
        Initializes the KnowUses dialog.

        Args:
            parent (QWidget, optional): The parent widget of the dialog.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.menssageManager = MessageBoxManager()
        self.listUses()
        self.init_ui()
        
    def init_ui(self):
        """
        Initializes the UI elements and connects signals to their respective slots.
        """
        self.pb_addUse.clicked.connect(self.addUse)
        self.pb_removeUse.clicked.connect(self.removeUse)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_save.clicked.connect(self.save)
    
    def setUses(self, uses):
        """
        Sets the initial list of uses in the dialog.

        Args:
            uses (list): A list of known uses to display.
        """
        if uses:
            for use in uses:
                self.lw_uses.addItem(use)
                
    def getUses(self):
        """
        Retrieves the current list of uses from the dialog.

        Returns:
            list: A list of known uses.
        """
        uses = []
        for i in range(self.lw_uses.count()):
            uses.append(self.lw_uses.item(i).text())
        return uses
            
    def save(self):
        """
        Saves the current list of uses if valid and closes the dialog.
        """
        uses = []
        for i in range(self.lw_uses.count()):
            uses.append(self.lw_uses.item(i).text())
            
        if self.valid():
            self.accept()
        
    def valid(self):
        """
        Validates the input in the dialog.

        Returns:
            bool: True if valid, False otherwise.
        """
        if self.lw_uses.count() == 0:
            self.lw_uses.setStyleSheet("border: 1px solid red;")
            self.menssageManager.show_critical_message(self, 'Error', 'Debe ingresar al menos un uso')
            return False
        return True
    
    def listUses(self):
        """
        Populates the combo box with known uses from the repository.
        """
        uses = self.patternRepository.get_knowUses()
        for use in uses.keys():
            self.cb_uses.addItem(use)
            
    def addUse(self):
        """
        Adds the selected use from the combo box to the list of known uses.
        """
        for i in range(self.lw_uses.count()):
            if self.cb_uses.currentText() == self.lw_uses.item(i).text():
                self.menssageManager.show_info_message(self, 'Info', 'El uso ya se encuentra en la lista')
                return
        self.lw_uses.addItem(self.cb_uses.currentText())

    def removeUse(self):
        """
        Removes the currently selected use from the list of known uses.
        """
        self.lw_uses.takeItem(self.lw_uses.currentRow())
