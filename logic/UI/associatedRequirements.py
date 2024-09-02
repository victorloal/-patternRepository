from logic.pattern_repository import PatternRepository
from ui_generated.ui_associatedRequirements import Ui_AssociatedRequirements
from ui_generated.ui_customInputDialog import CustomInputDialog
from ui_generated.ui_messageBoxManager import MessageBoxManager
from PyQt5 import QtCore, QtGui, QtWidgets

class NewAssociatedRequirements(QtWidgets.QDialog, Ui_AssociatedRequirements):
    def __init__(self, parent=None, edit= False):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.pattern_repository = PatternRepository()
        self.menssageBoxManager = MessageBoxManager()
        self.customDialog = CustomInputDialog()
        self.requirements = []
        self.init_ui()
        
    def init_ui(self):
        self.listDomains()
        self.listRequirements()
        self.domains = {}
        
        self.pb_deleteRequirements.clicked.connect(self.delete_requirements)
        self.pb_newRequirements.clicked.connect(self.create_new_requirement)
        self.pb_addRequirements.clicked.connect(self.add_requirement)
        self.pb_removeRequirements.clicked.connect(self.remove_requirement)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_save.clicked.connect(self.save)
        self.cb_domains.currentIndexChanged.connect(self.listRequirements)
        
        
    
    def save(self):
        self.result = []
        for i in range(self.lw_associatedRequirements.count()):
            self.result.append(self.lw_associatedRequirements.item(i).text())
        self.AssociatedRequirements.accept()
        
    def get_result(self):
        # Return the selected domains and associated requirements
        return self.domains, self.result
    
    def set_result(self, domains, requirements):
        # Set the selected domains and associated requirements
        self.domains = domains
        self.lw_associatedRequirements.addItems(requirements)
    
    def listDomains(self):
        domains = self.pattern_repository.get_domains()
        for dominio in domains["Domains"].keys():
            self.cb_domains.addItem(dominio)
            
    def listRequirements(self):
        self.lw_domains.clear()
        domains = self.pattern_repository.get_domains()
        for requisito in domains["Domains"][self.cb_domains.currentText()]:
            self.lw_domains.addItem(requisito)
            
        pass
    
    def delete_requirements(self):
        # Remove selected items from lw_domains
        selected_items = self.lw_domains.selectedItems()
        for item in selected_items:
            result = self.menssageBoxManager.show_question_message(self.AssociatedRequirements, "Warning", "esta seguro de eliminar este requerimiento?","Eliminar","Cancelar")   
            if result:
                self.pattern_repository.delete_requirement(self.cb_domains.currentText(), item.text())
                self.lw_domains.takeItem(self.lw_domains.row(item))
    
    def create_new_requirement(self):
        # Show dialog to create new requirement
        self.customDialog.update_dialog(
            title="Nuevo Requisito",
            label_text="Ingrese el nombre del requisito:",
            input_text="",  # No default input text
            ok_button_text="Crear",
            cancel_button_text="Cancelar"
        )
        
        user_input = self.customDialog.get_input()
        if user_input:
            # Add the new requirement to the appropriate domain
            self.pattern_repository.append_requirement(self.cb_domains.currentText(), user_input)
            self.listRequirements()
    
    def add_requirement(self):
        # Add selected requirement from lw_domains to lw_associatedRequirements
        selected_items = self.lw_domains.selectedItems()
        if not self.verifyItem(selected_items):
            for item in selected_items:
                self.lw_associatedRequirements.addItem(item.text())
                self.domains[item.text()] = self.cb_domains.currentText()
            
    def verifyItem(self, selected_items):
        # Flag to determine if any duplicate items are found
        duplicate_found = False

        # Iterate over selected items
        for item in selected_items:
            # Check if the item already exists in lw_associatedRequirements
            for i in range(self.lw_associatedRequirements.count()):
                if item.text() == self.lw_associatedRequirements.item(i).text():
                    duplicate_found = True
                    break
            
            if duplicate_found:
                break
        
        # Show message if duplicates are found
        if duplicate_found:
            #prueba todos los elementos de la lista
            self.menssageBoxManager.show_info_message(self.AssociatedRequirements, "Warning", "Duplicate items are not allowed.")
        return duplicate_found
    
    def remove_requirement(self):
        # Remove selected associated requirement from lw_associatedRequirements
        selected_items = self.lw_associatedRequirements.selectedItems()
        for item in selected_items:
            self.lw_associatedRequirements.takeItem(self.lw_associatedRequirements.row(item))
            self.domains.pop(item.text())
