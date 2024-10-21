from PyQt5 import QtWidgets, QtGui, QtCore
from logic.UI.instantiate import Instantiate
from logic.UI.editRequirement import NewRequirement
from logic.UI.newDomain import NewDomain
from logic.UI.ui_markdownDialog import MarkdownDialog
from logic.UI.search import Search
from logic.UI.newPattern import NewPattern
from logic.UI.ui_messageBoxManager import MessageBoxManager
from logic.pattern_repository import PatternRepository
from ui_generated.ui_home import Ui_MainWindow

class Home(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Main application window that manages the interaction with patterns and domains.
    """

    def __init__(self):
        """
        Initializes the Home window and its components.
        """
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI components and connects signals to slots.
        """
        self.pb_search.clicked.connect(self.searchPattern)
        self.lw_pattern.itemClicked.connect(self.previewPattern)
        self.pb_fullScreen.clicked.connect(self.fullScreen)
        self.pb_instantiate.clicked.connect(self.instantiatePattern)
        self.new_pattern.triggered.connect(self.newPattern)
        self.new_domains.triggered.connect(self.newDomain)
        self.new_Requirements.triggered.connect(self.newRequirement)
        self.edit_domain.triggered.connect(self.editDomain)
        self.edit_pattern.triggered.connect(self.editPattern)
        self.edit_requirementsDomain.triggered.connect(self.editRequirement)
        self.help_app.triggered.connect(self.helpApp)
        self.help_contribute.triggered.connect(self.helpContribute)
        self.help_pattern.triggered.connect(self.helpPattern)
        self.help_ropository.triggered.connect(self.helpRepository)
        self.delete_pattern.triggered.connect(self.deletePattern)
        self.delete_domain.triggered.connect(self.deleteDomain)
        self.listPatterns()

    def deleteDomain(self):
        """
        Opens a dialog to delete an existing domain.
        """
        data = self.patternRepository.get_domains()
        dialog = NewDomain(self, edit=True)
        dialog.deleteDomain(data=data)
        dialog.exec_()

    def deletePattern(self):
        """
        Deletes the selected pattern after confirmation.
        """
        if not self.lw_pattern.currentItem():
            self.messageManager.show_critical_message(self, "Error", 'Seleccione un patrón para eliminar')
            return
        pattern_name = self.lw_pattern.currentItem().text()
        message = self.messageManager.show_warning_message(self, "Eliminar patrón", f"¿Está seguro de eliminar el patrón {pattern_name}?")
        if message == QtWidgets.QMessageBox.Ok:
            self.patternRepository.delete_pattern(pattern_name)
            self.listPatterns()

    def helpRepository(self):
        dialog = MarkdownDialog("Donde encontrar los patrones")
        dialog.exec_()

    def helpPattern(self):
        dialog = MarkdownDialog("Como crear nuevo Patron")
        dialog.exec_()

    def helpContribute(self):
        dialog = MarkdownDialog("Como colaborar cone le proyecto")
        dialog.exec_()

    def helpApp(self):
        dialog = MarkdownDialog("Informacion del programa")
        dialog.exec_()

    def editPattern(self):
        """
        Opens a dialog to edit the selected pattern.
        """
        if not self.lw_pattern.currentItem():
            self.messageManager.show_critical_message(self, "Error", 'Seleccione un patrón para editar')
            return
        pattern_name = self.lw_pattern.currentItem().text()
        data, images = self.patternRepository.get_pattern_data_by_name(pattern_name)
        images = self.patternRepository.get_path_images_by_name(pattern_name)
        dialog = NewPattern(self, edit=True)
        dialog.editPattern(data, images)
        dialog.exec_()

    def editRequirement(self):
        """
        Opens a dialog to edit requirements.
        """
        dialog = NewRequirement(self)
        dialog.exec_()

    def editDomain(self):
        """
        Opens a dialog to edit existing domains.
        """
        data = self.patternRepository.get_domains()
        dialog = NewDomain(self, edit=True)
        dialog.editDomain(data=data)
        dialog.exec_()

    def newRequirement(self):
        """
        Opens a dialog to create a new requirement.
        """
        dialog = NewRequirement(self)
        dialog.ui_new(True)
        dialog.exec_()

    def newDomain(self):
        """
        Opens a dialog to create a new domain.
        """
        dialog = NewDomain(self, edit=False)
        dialog.exec_()

    def listPatterns(self):
        """
        Lists all patterns in the list widget.
        """
        self.lw_pattern.clear()
        patterns = self.patternRepository._list_directories()
        for pattern in patterns:
            self.lw_pattern.addItem(pattern)


    def newPattern(self):
        """
        Opens a dialog to create a new pattern.
        """
        dialog = NewPattern(self, edit=False)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.listPatterns()

    def instantiatePattern(self):
        """
        Opens a dialog to instantiate the selected pattern.
        """
        if not self.lw_pattern.currentItem():
            self.messageManager.show_critical_message(self, "Error", 'Seleccione un patrón para instanciar')
            return
        images = {}
        data, images_dict = self.patternRepository.get_path_images_by_name(self.lw_pattern.currentItem().text())
        images['template'] = images_dict["templateSVG"]
        images["scopeModel"] = images_dict["scopeModelSVG"]
        images["structureModel"] = images_dict["structureModelSVG"]
        images["behaviorModel"] = images_dict["behaviorModelSVG"]
        pattern = self.lw_pattern.currentItem().text()
        dialog = Instantiate(images, pattern, self)
        dialog.exec_()

    def fullScreen(self):
        """
        Displays the currently selected image in full screen.
        """
        if not self.lw_pattern.currentItem():
            self.messageManager.show_critical_message(self, "Error", 'Seleccione un patrón para mostrar los modelos')
            return
        visible_label = None
        if self.lb_template.isVisible():
            visible_label = self.lb_template
        elif self.lb_scope.isVisible():
            visible_label = self.lb_scope
        elif self.lb_structure.isVisible():
            visible_label = self.lb_structure
        elif self.lb_behavior.isVisible():
            visible_label = self.lb_behavior

        if visible_label:
            self.show_image_maximized(visible_label)

    def show_image_maximized(self, label):
        """
        Displays the specified image label in a maximized view.

        Args:
            label (QLabel): The label containing the image to display.
        """
        pixmap = label.pixmap()
        if pixmap is None:
            print("No pixmap found in the visible label")
            return

        full_screen_widget = QtWidgets.QWidget()
        full_screen_widget.setWindowTitle("Maximized Image")

        layout = QtWidgets.QVBoxLayout(full_screen_widget)
        self.graphics_view = QtWidgets.QGraphicsView()
        layout.addWidget(self.graphics_view)

        scene = QtWidgets.QGraphicsScene()
        self.graphics_view.setScene(scene)
        scene.addPixmap(pixmap)

        toolbar = QtWidgets.QToolBar()
        layout.addWidget(toolbar)

        zoom_in_button = QtWidgets.QPushButton("Zoom In")
        zoom_in_button.clicked.connect(self.zoom_in)
        toolbar.addWidget(zoom_in_button)

        zoom_out_button = QtWidgets.QPushButton("Zoom Out")
        zoom_out_button.clicked.connect(self.zoom_out)
        toolbar.addWidget(zoom_out_button)

        self.graphics_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphics_view.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        self.graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        full_screen_widget.showMaximized()
        self.full_screen_widget = full_screen_widget
        self.graphics_view.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def zoom_in(self):
        """
        Zooms in on the displayed image.
        """
        self.graphics_view.scale(1.2, 1.2)

    def zoom_out(self):
        """
        Zooms out of the displayed image.
        """
        self.graphics_view.scale(1 / 1.2, 1 / 1.2)

    def previewPattern(self):
        """
        Displays details of the selected pattern.
        """
        pattern_name = self.lw_pattern.currentItem().text()
        data, images = self.patternRepository.get_path_images_by_name(pattern_name)
        self.lb_name.setText(data['Name'])
        self.lw_associatedDomains.clear()
        domains = [data['Domains']['key']] + list(data['Domains']['value'].values())
        domains = list(set(domains))
        domains.remove(data['Domains']['key'])
        self.lw_associatedDomains.addItem(data['Domains']['key'])
        for domain in domains:
            self.lw_associatedDomains.addItem(domain)
        self.lw_description.clear()
        self.lw_description.addItem(data['Description'])
        self.lw_knownUses.clear()
        for known_use in data['Uses']:
            self.lw_knownUses.addItem(known_use)
        self.lw_relatedPatterns.clear()
        for related_pattern in data['RelatedPatterns']:
            self.lw_relatedPatterns.addItem(related_pattern)
        self.lw_associatedRequirements.clear()
        for associated_requirement in data['Domains']["value"].keys():
            self.lw_associatedRequirements.addItem(associated_requirement)
        for roles in data['Rol']:
            self.lw_roles.addItem(roles)
        
        self.set_image(self.lb_template, images['templateSVG'], "No se encontró la imagen")
        self.set_image(self.lb_scope, images['scopeModelSVG'], "No se encontró la imagen")
        self.set_image(self.lb_structure, images['structureModelSVG'], "No se encontró la imagen")
        self.set_image(self.lb_behavior, images['behaviorModelSVG'], "No se encontró la imagen")

    def set_image(self, label, image_path, error_message):
        """
        Sets the specified image in the given label or displays an error message.

        Args:
            label (QLabel): The label to display the image.
            image_path (str): The path to the image.
            error_message (str): The message to display if the image cannot be loaded.
        """
        if image_path:
            label.setPixmap(image_path)
        else:
            label.setText(error_message)

    def searchPattern(self):
        """
        Searches for patterns by name based on user input.
        """
        if not self.cb_nombre_2.isChecked() and not self.cb_dominio.isChecked() and not self.cb_roles.isChecked():
            results = self.patternRepository.search_pattern_by_name(self.le_search.text())
            self.lw_pattern.clear()
            for result in results:
                self.lw_pattern.addItem(result['Name'])
        else:
            results = self.patternRepository.search(self.le_search.text(), self.cb_nombre_2.isChecked(), self.cb_roles.isChecked(), self.cb_dominio.isChecked())
