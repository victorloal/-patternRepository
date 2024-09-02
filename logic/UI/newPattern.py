from PyQt5 import QtCore, QtGui, QtWidgets
from logic.UI.newDomain import NewDomain
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogNewPAttern import Ui_NewPattern
from ui_generated.ui_knowUses import Ui_KnowUses
from ui_generated.ui_messageBoxManager import MessageBoxManager
from ui_generated.ui_newDomain import Ui_NewDomain
from ui_generated.ui_associatedRequirements import Ui_AssociatedRequirements

class NewPattern(QtWidgets.QDialog, Ui_NewPattern):
    def __init__(self, parent=None, edit= False):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.uses = []
        self.domains = {}
        self.requirements = []
        self.init_ui()
        
        
    def editPattern(self, data = {}, images = {}):
        self.le_name.setText(data["Name"])
        self.cb_Domain.setCurrentText(data["Domains"][0])
        self.uses = data["Uses"]
        self.domains = data["Domains"]
        self.requirements = data["Requirements"]
        
    def init_ui(self):
        # Conectar señales y slots
        self.listDomains()
        self.pb_cancel.clicked.connect(NewPattern.close)
        self.pb_newDomain.clicked.connect(self.openNewDomainDialog)
        self.pb_associatedRequirements.clicked.connect(self.openAssociatedRequirementsDialog)
        self.pb_uses.clicked.connect(self.openKnownUsesDialog)
        self.pb_save.clicked.connect(self.save)
        
        self.pb_scopeDia.clicked.connect(lambda: self.uploadModel(self.lb_scopeDia,".dia"))
        self.pb_scopeSvg.clicked.connect(lambda: self.uploadModel(self.lb_scopeSvg,".svg"))
        self.pb_structurDia.clicked.connect(lambda: self.uploadModel(self.lb_structurDia,".dia"))
        self.pb_structurSvg.clicked.connect(lambda: self.uploadModel(self.lb_structurSvg,".svg"))
        self.pb_behaviorDia.clicked.connect(lambda: self.uploadModel(self.lb_behaviorDia,".dia"))
        self.pb_behaviorSvg.clicked.connect(lambda: self.uploadModel(self.lb_behaviorSvg,".svg"))
        self.pb_templateDia.clicked.connect(lambda: self.uploadModel(self.lb_templateDia,".dia"))
        self.pb_templateSvg.clicked.connect(lambda: self.uploadModel(self.lb_templateSvg,".svg"))
        
    def listDomains(self):
        self.cb_Domain.clear()
        domains = self.patternRepository.get_domains()
        domain_keys = list(domains["Domains"].keys())

        # Agregar solo si no existe
        for key in domain_keys:
            if key not in [self.cb_Domain.itemText(i) for i in range(self.cb_Domain.count())]:
                self.cb_Domain.addItem(key)
            
    def uploadModel(self, label, tipo_archivo):
        """
        Carga un archivo y actualiza el QLabel especificado con el nombre del archivo.
        
        :param label: QLabel a actualizar.
        :param tipo_archivo: Tipo de archivo aceptado, como ".dia" o ".svg".
        """
        file_name = self.openFileDialog()
        if file_name:
            if file_name.endswith(tipo_archivo):
                label.setText(file_name)
            else:
                self.messageManager.show_critical_message(None, "Error", f"El archivo seleccionado no es un archivo {tipo_archivo}.")

        
    def openFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
            
            
        
    def openKnownUsesDialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = Ui_KnowUses()
            ui.setupUi(dialog)
            ui.retranslateUi(dialog)
            ui.setUses(self.uses)
            dialog.show()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                # Get updated data from the dialog if it was accepted
                self.uses = ui.getUses() 
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")
            
    def openAssociatedRequirementsDialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = Ui_AssociatedRequirements()
            ui.setupUi(dialog)
            ui.retranslateUi(dialog)
            ui.set_result(self.domains, self.requirements)
            dialog.show()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                # Get updated data from the dialog if it was accepted
                self.domains, self.requirements = ui.get_result() 
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")
            
    def openNewDomainDialog(self):
        try:
            dialog = NewDomain() # Correctly call exec_() on QDialog instance
            dialog.exec_()
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")

        
        
    def save(self):
        if self.verify():
            data = {}
            data["Name"] = self.le_name.text().lower()
            data["Domains"] = {}
            data["Domains"]["key"]=(self.cb_Domain.currentText().lower())
            data["Domains"]["value"]=(self.domains)
            data["Description"] = self.te_description.toPlainText().lower()
            data["RelatedPatterns"] = self.realatedPatterns()
            data["Uses"] = self.uses
            data["Requirements"] = self.requirements
            #eliminar los duplicados   
            
            image_path = {}
            
            image_path["behaviorModelDia"] = self.lb_behaviorDia.text()
            image_path["scopeModelDia"] = self.lb_scopeDia.text()
            image_path["structureModelDia"] = self.lb_structurDia.text()
            image_path["templateDia"] = self.lb_templateDia.text()
            image_path["behaviorModelSVG"] = self.lb_behaviorSvg.text()
            image_path["scopeModelSVG"] = self.lb_scopeSvg.text()
            image_path["structureModelSVG"] = self.lb_structurSvg.text()
            image_path["templateSVG"] = self.lb_templateSvg.text()
            
            self.patternRepository.new_pattern(data, image_path)
            
            #madar a guardar los archivos
    def realatedPatterns(self):
        #obtener los nombres de los patrones relacionados
        result = []
        domains = self.patternRepository.get_domains()
        for domain in domains["DomainsWithPatterns"].keys():
            if  domain in self.domains.values():
                for pattern in domains["DomainsWithPatterns"][domain]:
                    if pattern not in result:
                        print(pattern)
                        result.append(pattern)
                    
        uses = self.patternRepository.get_knowUses()
        for use in uses["Uses"]:
            if use in self.uses:
                for pattern in uses["Uses"][use]:
                    if pattern not in result:
                        print(pattern)
                        result.append(pattern)
        
        #eliminar los duplicados
        return result
        
    def verify(self):
        def validate_widget(widget,textWidget, empty_value, style_valid="border: 1px solid green;", style_invalid="border: 1px solid red;"):
            if textWidget == empty_value:
                widget.setStyleSheet(style_invalid)
                return False
            else:
                widget.setStyleSheet(style_valid)
                return True

        vali = True
        # Verificar datos
        vali &= validate_widget(self.le_name,self.le_name.text(), "")
        vali &= validate_widget(self.cb_Domain,self.cb_Domain.currentText(), "Dominio Principal")
        vali &= validate_widget(self.te_description, self.te_description.toPlainText(), "")
        
        # Verificar archivos
        file_checks = [
            (self.lb_scopeDia, "<...>.dia"),
            (self.lb_scopeSvg, "<...>.svg"),
            (self.lb_structurDia, "<...>.dia"),
            (self.lb_structurSvg, "<...>.svg"),
            (self.lb_behaviorDia, "<...>.dia"),
            (self.lb_behaviorSvg, "<...>.svg"),
            (self.lb_templateDia, "<...>.dia"),
            (self.lb_templateSvg, "<...>.svg")
        ]
        
        for label, empty_value in file_checks:
            vali &= validate_widget(label,label.text(), empty_value)

        return vali