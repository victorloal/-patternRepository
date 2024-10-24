from PyQt5 import QtWidgets, QtCore
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogNewDomain import Ui_NewDomain
from logic.UI.ui_messageBoxManager import MessageBoxManager


class NewDomain(QtWidgets.QDialog, Ui_NewDomain):
    """
    A dialog for creating or editing a new domain.

    This dialog allows users to manage domains, including adding, editing, and deleting requirements.
    """

    def __init__(self, parent=None, edit=False):
        """
        Initializes the NewDomain dialog.

        Args:
            parent (QWidget, optional): The parent widget of the dialog.
            edit (bool, optional): Flag indicating if the dialog is for editing an existing domain.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        
        if edit:
            self.setWindowTitle("Edit Domain")
            self.le_nameDomain.setVisible(False)
            self.cb_domains.setVisible(True)
            self.pb_deleteDomain.setVisible(False)
        else:
            self.cb_domains.setVisible(False)
            self.le_nameDomain.setVisible(True)
            self.pb_deleteDomain.setVisible(False)
        
        self.init_ui()
    
    def deleteDomain(self, data={}):
        """
        Prepares the dialog for deleting a domain.

        Args:
            data (dict): Existing domain data to display in the combo box.
        """
        self.cb_domains.clear()
        self.cb_domains.addItems(list(data.keys()))
        self.setWindowTitle("Eliminar Dominio")
        self.le_nameDomain.setVisible(False)
        self.cb_domains.setVisible(True)
        self.lw_requirements.setVisible(False)
        self.pb_add.setVisible(False)
        self.pb_deleteRequirements.setVisible(False)
        self.pb_save.setVisible(False)
        self.pb_cancel.setVisible(False)
        self.lb_requisitos.setVisible(False)
        self.pb_edit.setVisible(False)
        self.cb_requirements.setVisible(False)
        self.pb_deleteDomain.setVisible(True)
        
        self.adjustSize()

    def editDomain(self, data={}):
        """
        Prepares the dialog for editing an existing domain.

        Args:
            data (dict): Existing domain data to display in the combo box.
        """
        self.cb_domains.clear()
        self.cb_domains.addItems(list(data.keys()))
        
    def listRequirementsInEdit(self):
        """
        Lists requirements associated with the currently selected domain in edit mode.
        """
        requirements = []
        data = self.patternRepository.get_domains()
        for requirement in data[self.cb_domains.currentText()]:
            requirements.append(requirement)
        self.lw_requirements.clear()
        self.lw_requirements.addItems(requirements)
        
    def init_ui(self):
        """
        Initializes the UI elements and connects signals to their respective slots.
        """
        self.listRequirements()
        self.pb_add.clicked.connect(self.add_requirement)
        self.pb_deleteRequirements.clicked.connect(self.delete_requirement)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_save.clicked.connect(self.save) 
        self.cb_domains.currentIndexChanged.connect(self.listRequirementsInEdit)
        self.pb_edit.clicked.connect(self.edit_requirement)
        self.pb_deleteDomain.clicked.connect(self.delete_domain)
        
    def edit_requirement(self):
        """
        Allows editing of a selected requirement in the list.
        """
        if self.lw_requirements.currentItem() is None:
            self.messageManager.show_critical_message(self, "Error", "Seleccione un requerimiento")
        else:
            current_item = self.lw_requirements.currentItem()
            if current_item.flags() & QtCore.Qt.ItemIsEditable:
                self.lw_requirements.editItem(current_item)
            else:
                current_item.setFlags(current_item.flags() | QtCore.Qt.ItemIsEditable)
            if self.patternRepository.verifyRequirement(current_item.text()):
                self.messageManager.show_critical_message(self, "Error", "El requerimiento está en la información de un patrón")
            else:
                self.lw_requirements.editItem(current_item)

    def delete_domain(self):
        """
        Deletes the currently selected domain and displays an appropriate message.
        """
        domainName = self.cb_domains.currentText()
        valor = self.patternRepository.delete_domain(domainName)
        if valor[0]:
            self.patternRepository.delete_domain(domainName)
            self.accept()
        else:
            self.messageManager.show_critical_message(self, "Error", valor[1])
        
    def add_requirement(self):
        """
        Adds the selected requirement from the combo box to the list.
        """
        self.lw_requirements.addItem(self.cb_requirements.currentText())
       
    def delete_requirement(self):
        """
        Deletes the currently selected requirement from the list if it is not associated with a pattern.
        """
        #optener el nombre del dominio
        dominio= self.cb_domains.currentText()
        if dominio == "":
            dominio = self.le_nameDomain.text()
        result = self.messageManager.show_question_message(self, "Warning", "Esta seguro de eliminar este requerimiento?","Eliminar","Cancelar")
        if not result:
            result, menssage = self.patternRepository.delete_requirement(dominio, self.lw_requirements.currentItem().text())
        if  not result:
            self.messageManager.show_critical_message(self, "Error", "No es posible eliminar el requerimiento," + menssage)
        else:
            self.lw_requirements.takeItem(self.lw_requirements.currentRow())
     
    def listRequirements(self):
        """
        Populates the requirements combo box with available requirements from the repository.
        """
        self.cb_requirements.clear()
        requirements = self.patternRepository.get_requirements()
        self.cb_requirements.addItems(requirements) 

    def save(self):
        """
        Validates and saves the domain data to the repository.
        """
        if self.verify():
            domainName = self.le_nameDomain.text().lower()
            if domainName == "":
                domainName = self.cb_domains.currentText()
            
            requirements = [self.lw_requirements.item(i).text().lower() for i in range(self.lw_requirements.count())]
            
            self.patternRepository.add_domain(domainName, requirements)
            self.accept()
            
    def verify(self):
        """
        Validates the input fields in the dialog.

        Returns:
            bool: True if all fields are valid, False otherwise.
        """
        def validate_widget(widget, textWidget, empty_value, style_valid="border: 1px solid green;", style_invalid="border: 1px solid red;"):
            if textWidget == empty_value:
                widget.setStyleSheet(style_invalid)
                return False
            else:
                widget.setStyleSheet(style_valid)
                return True

        vali = True
        domains = self.patternRepository.get_domains()
        if self.le_nameDomain.text() is  None and self.cb_domains.currentText() not in domains.keys():
            self.le_nameDomain.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.le_nameDomain.setStyleSheet("border: 1px solid green;")
            vali2 = validate_widget(self.le_nameDomain, self.le_nameDomain.text(), "")
            vali3 = self.cb_domains.currentText() in domains.keys()
            vali = vali2 or vali3
        if self.lw_requirements.count() == 0:
            self.lw_requirements.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.lw_requirements.setStyleSheet("border: 1px solid green;")
        return vali
    
