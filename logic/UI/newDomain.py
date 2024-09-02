from PyQt5 import  QtWidgets
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogNewDomain import Ui_NewDomain
from ui_generated.ui_messageBoxManager import MessageBoxManager


class NewDomain(QtWidgets.QDialog, Ui_NewDomain):
    def __init__(self, parent=None, edit= False):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        if edit:
            self.setWindowTitle("Edit Domain")
            self.le_nameDomain.setVisible(False)
            self.cb_domains.setVisible(True)
        else:
            self.cb_domains.setVisible(False)
            self.le_nameDomain.setVisible(True)
        self.init_ui()
        
    def editDomain(self, data = {}):
        #cambiar le_nameDomain
        
        self.cb_domains.clear()
        self.cb_domains.addItems(list(data["Domains"].keys()))
        self.lw_requirements.clear()
        self.lw_requirements.addItems(data["Domains"][self.cb_domains.currentText()])
        self.cb_requirements.clear()
        requirements = []
        for domain in data["Domains"]:
            for requirement in data["Domains"][domain]:
                requirements.append(requirement)
        self.cb_requirements.addItems(requirements)
        
    def init_ui(self):
        self.listRequirements()
        self.pb_add.clicked.connect(self.add_requirement)
        self.pb_deleteRequirements.clicked.connect(self.delete_requirement)
        self.pb_cancel.clicked.connect(self.close)  # Corrected
        self.pb_save.clicked.connect(self.save) 
        
    def add_requirement(self):
        self.lw_requirements.addItem(self.cb_requirements.currentText())
       
    def delete_requirement(self):
        self.lw_requirements.takeItem(self.lw_requirements.currentRow())
     
    def listRequirements(self):
        self.cb_requirements.clear()
        requirements = self.patternRepository.get_requirements()
        self.cb_requirements.addItems(requirements)  # Uncommented

    def save(self):
        if self.verify():
            domainName = self.le_nameDomain.text()
            requirements = [self.lw_requirements.item(i).text() for i in range(self.lw_requirements.count())]
            
            self.patternRepository.add_domain(domainName,requirements)
            #cerrar el dialogo
            self.accept()
            
    def verify(self):
        def validate_widget(widget, textWidget, empty_value, style_valid="border: 1px solid green;", style_invalid="border: 1px solid red;"):
            if textWidget == empty_value:
                widget.setStyleSheet(style_invalid)
                return False
            else:
                widget.setStyleSheet(style_valid)
                return True

        vali = True
        # Verificar datos
        domains = self.patternRepository.get_domains()
        if self.le_nameDomain.text() in domains["Domains"].keys():
            self.le_nameDomain.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.le_nameDomain.setStyleSheet("border: 1px solid green;")
            vali &= validate_widget(self.le_nameDomain, self.le_nameDomain.text(), "")
        if self.lw_requirements.count() == 0:
            self.lw_requirements.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.lw_requirements.setStyleSheet("border: 1px solid green;")

        return vali
    
    