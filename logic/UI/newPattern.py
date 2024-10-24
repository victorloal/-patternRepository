import os
from PyQt5 import QtCore, QtGui, QtWidgets
from logic.UI.associatedRequirements import NewAssociatedRequirements
from logic.UI.knowUses import KnowUses
from logic.UI.newDomain import NewDomain
from logic.pattern_repository import PatternRepository
from logic.svg_text_modifier import SvgTextModifier
from ui_generated.ui_dialogNewPattern import Ui_NewPattern
from logic.UI.ui_messageBoxManager import MessageBoxManager

class NewPattern(QtWidgets.QDialog, Ui_NewPattern):
    """
    A dialog for creating or editing a new pattern.

    This dialog allows users to input pattern details, select associated domains, and upload related files.
    """

    def __init__(self, parent=None, edit=False):
        """
        Initializes the NewPattern dialog.

        Args:
            parent (QWidget, optional): The parent widget of the dialog.
            edit (bool, optional): Flag indicating if the dialog is for editing an existing pattern.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.uses = []
        self.domains = {}
        self.requirements = []
        self.init_ui()

    def editPattern(self, data={}, images={}):
        """
        Fills the dialog fields with existing pattern data for editing.

        Args:
            data (dict): Existing pattern data.
            images (dict): Paths to related images.
        """
        self.le_name.setText(data["Name"])
        self.cb_Domain.setCurrentText(data["Domains"]["key"])
        self.te_description.setText(data["Description"])
        self.uses = data["Uses"]
        self.domains = data["Domains"]["value"]
        self.requirements = data["Domains"]["value"].keys()
        
        self.lb_behaviorSvg.setText(images["behaviorModelSVG"])
        self.lb_scopeSvg.setText(images["scopeModelSVG"])
        self.lb_structurSvg.setText(images["structureModelSVG"])
        self.lb_templateSvg.setText(images["templateSVG"])
        
        self.lb_behaviorDia.setText(images["behaviorModelDIA"])
        self.lb_scopeDia.setText(images["scopeModelDIA"])
        self.lb_structurDia.setText(images["structureModelDIA"])
        self.lb_templateDia.setText(images["templateDIA"])

    def init_ui(self):
        """
        Initializes the UI elements and connects signals to their respective slots.
        """
        self.listDomains()
        self.pb_cancel.clicked.connect(NewPattern.close)
        self.pb_newDomain.clicked.connect(self.openNewDomainDialog)
        self.pb_associatedRequirements.clicked.connect(self.openAssociatedRequirementsDialog)
        self.pb_uses.clicked.connect(self.openKnownUsesDialog)
        self.pb_save.clicked.connect(self.save)
        
        self.pb_scopeDia.clicked.connect(lambda: self.uploadModel(self.lb_scopeDia, ".dia"))
        self.pb_scopeSvg.clicked.connect(lambda: self.uploadModel(self.lb_scopeSvg, ".svg"))
        self.pb_structurDia.clicked.connect(lambda: self.uploadModel(self.lb_structurDia, ".dia"))
        self.pb_structurSvg.clicked.connect(lambda: self.uploadModel(self.lb_structurSvg, ".svg"))
        self.pb_behaviorDia.clicked.connect(lambda: self.uploadModel(self.lb_behaviorDia, ".dia"))
        self.pb_behaviorSvg.clicked.connect(lambda: self.uploadModel(self.lb_behaviorSvg, ".svg"))
        self.pb_templateDia.clicked.connect(lambda: self.uploadModel(self.lb_templateDia, ".dia"))
        self.pb_templateSvg.clicked.connect(lambda: self.uploadModel(self.lb_templateSvg, ".svg"))

    def listDomains(self):
        """
        Populates the domain combo box with available domains from the repository.
        """
        self.cb_Domain.clear()
        domains = self.patternRepository.get_domains()
        domain_keys = list(domains.keys())

        for key in domain_keys:
            if key not in [self.cb_Domain.itemText(i) for i in range(self.cb_Domain.count())]:
                self.cb_Domain.addItem(key)

    def uploadModel(self, label, tipo_archivo):
        """
        Loads a file and updates the specified QLabel with the file name.

        Args:
            label (QLabel): QLabel to update.
            tipo_archivo (str): Accepted file type (e.g., ".dia" or ".svg").
        """
        file_name = self.openFileDialog()
        if file_name:
            if file_name.endswith(tipo_archivo):
                label.setText(file_name)
            else:
                self.messageManager.show_critical_message(None, "Error", f"The selected file is not a {tipo_archivo} file.")

    def openFileDialog(self):
        """
        Opens a file dialog to select a file.

        Returns:
            str or None: The selected file path or None if canceled.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

    def openKnownUsesDialog(self):
        """
        Opens the dialog to manage known uses and updates the uses if accepted.
        """
        try:
            dialog = KnowUses(self)
            dialog.setUses(self.uses)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.uses = dialog.getUses()
        except Exception as e:
            print(f"Error opening the dialog: {e}")

    def openAssociatedRequirementsDialog(self):
        """
        Opens the dialog to manage associated requirements and updates the domains and requirements if accepted.
        """
        try:
            dialog = NewAssociatedRequirements(self)
            dialog.set_result(self.domains, self.requirements)
            dialog.show()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.domains, self.requirements = dialog.get_result()
        except Exception as e:
            print(f"Error opening the dialog: {e}")

    def openNewDomainDialog(self):
        """
        Opens the dialog to create a new domain and refreshes the domain list if accepted.
        """
        try:
            dialog = NewDomain()
            dialog.exec_()
            if dialog.result() == QtWidgets.QDialog.Accepted:
                self.listDomains()
        except Exception as e:
            print(f"Error opening the dialog: {e}")

    def save(self):
        """
        Validates and saves the pattern data to the repository.
        """
        if self.verify():
            data = {}
            data["Name"] = self.le_name.text().lower()
            data["Domains"] = {}
            data["Domains"]["key"] = self.cb_Domain.currentText().lower()
            data["Domains"]["value"] = self.domains
            domains = [self.cb_Domain.currentText().lower()] + list(self.domains.values())
            self.patternRepository.add_pattern_to_domain(domains, self.le_name.text().lower())
            data["Description"] = self.te_description.toPlainText().lower()
            data["RelatedPatterns"] = self.realatedPatterns(data["Domains"])
            data["Uses"] = self.uses
            
            image_path = {}
            image_path["behaviorModelSVG"] = self.lb_behaviorSvg.text()
            image_path["scopeModelSVG"] = self.lb_scopeSvg.text()
            image_path["structureModelSVG"] = self.lb_structurSvg.text()
            image_path["templateSVG"] = self.lb_templateSvg.text()
            
            data["Rol"] = []
            for key in image_path.keys():
                if image_path[key]:
                    svg_content = self.load_svg_from_file(image_path[key])
                    if not svg_content or not os.path.exists(image_path[key]):
                        print("Error loading the file")
                        return
                    svgTextModifier = SvgTextModifier(svg_content)
                    text = svgTextModifier.get_texts()
                    for i in text:
                        if 'rol' in i.lower():
                            self.patternRepository.add_roles(i, self.le_name.text().lower())
                            data["Rol"].append(i.lower())
                            
            data["Rol"] = list(set(data["Rol"]))        
            
            image_path["behaviorModelDia"] = self.lb_behaviorDia.text()
            image_path["scopeModelDia"] = self.lb_scopeDia.text()
            image_path["structureModelDia"] = self.lb_structurDia.text()
            image_path["templateDia"] = self.lb_templateDia.text()
            
            self.patternRepository.new_pattern(data, image_path)
            self.saveUses()
            self.accept()



    def load_svg_from_file(self, file_path):
        """
        Opens the SVG file and reads its content.

        Args:
            file_path (str): Path to the SVG file.

        Returns:
            str: Content of the SVG file.
        """
        with open(file_path, 'r') as file:
            return file.read()

    def saveUses(self):
        """
        Saves the uses related to the pattern to the repository.
        """
        self.patternRepository.add_uses(self.le_name.text().lower(), self.uses)

    def realatedPatterns(self, domains):
        """
        Retrieves related pattern names based on the specified domains and uses.

        Args:
            domains (dict): Dictionary of domain data.

        Returns:
            list: List of related pattern names.
        """
        result = []
        domainsPatern = []
        for domain in domains["value"].values():
            domainsPatern.append(domain)
        domainsPatern.append(self.cb_Domain.currentText().lower())
        domains = self.patternRepository.get_domainsWhitPatterns()
        for domain in domains.keys():
            if domain in domainsPatern:
                for pattern in domains[domain]:
                    if pattern not in result:
                        result.append(pattern)
                    
        uses = self.patternRepository.get_knowUses()
        for use in uses:
            if use in self.uses:
                for pattern in uses[use]:
                    if pattern not in result:
                        result.append(pattern)
        self.patternRepository.update_all_relatedPatterns(result, self.le_name.text().lower())
        return result

    def updateRealtedPatterns(self, pattern):
        """
        Updates related patterns by adding the current pattern to their list of related patterns.

        Args:
            pattern (str): The name of the pattern to update.
        """
        data, images = self.patternRepository.get_pattern_data_by_name(pattern)
        patterns = list(set(data["RelatedPatterns"]))
        if data:
            data["RelatedPatterns"].append(self.le_name.text().lower())
            data["RelatedPatterns"] = list(set(data["RelatedPatterns"]))
            
            for pattern in patterns:
                self.patternRepository.update_data(pattern, data["RelatedPatterns"], "RelatedPatterns")

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
        vali &= validate_widget(self.le_name, self.le_name.text(), "")
        vali &= validate_widget(self.cb_Domain, self.cb_Domain.currentText(), "Dominio Principal")
        vali &= validate_widget(self.te_description, self.te_description.toPlainText(), "")
        
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
            vali &= validate_widget(label, label.text(), empty_value)

        return vali
