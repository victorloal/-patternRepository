from PyQt5 import QtWidgets
from logic.UI.editRequirement import NewRequirement
from logic.UI.newDomain import NewDomain
from logic.UI.newPattern import NewPattern
from logic.pattern_repository import PatternRepository
from ui_generated.ui_fullScreen import Ui_instantiateWindow

from ui_generated.ui_search import Ui_Dialog
from ui_generated.ui_home import Ui_MainWindow

class Home(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.patternRepository = PatternRepository()
        self.init_ui()

    def init_ui(self):
        # Conectar señales y slots
        self.pb_search.clicked.connect(self.searchPattern)
        self.pb_advancedSearch.clicked.connect(self.advancedSearch)
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
        # Inicializar la lista de patrones
        self.listPatterns()
        
    
    
    def helpRepository(self):
        pass
    
    def helpPattern(self):
        pass
    
    def helpContribute(self):
        pass
    
    def helpApp(self):
        pass
    
    
    def editPattern(self):
        
        pattern_name = self.lw_pattern.currentItem().text()
        data, images = self.patternRepository.get_pattern_data_by_name(pattern_name)
        dialog =NewPattern(self,edit=True)
        dialog.editPattern(data,images)
        dialog.exec_()
    
    def editRequirement(self):
        dialog = NewRequirement(self)
        dialog.exec_()
    
    def editDomain(self):
        data = self.patternRepository.get_domains()
        dialog = NewDomain(self,edit=True)
        dialog.editDomain(data= data)
        dialog.exec_()
    
    def newRequirement(self):
        dialog = NewRequirement(self)
        dialog.ui_new(True)
        dialog.exec_()
    
    def newDomain(self):
        dialog = NewDomain(self,edit=False)
        dialog.exec_()
        
    def listPatterns(self):
        list = self.patternRepository._list_directories()
        for i in list:
            self.lw_pattern.addItem(i)
               
    def advancedSearch(self):
        #quiero que se abra el Qdialogo ui_search.py
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.retranslateUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
    def newPattern(self):
        #quiero que se abra el Qdialogo ui_newPattern.py
        dialog =NewPattern(self,edit=False)
        dialog.exec_()
        
        # Window = QtWidgets.QMainWindow()
        # ui = Ui_NewPattern()
        # ui.setupUi(Window)
        # ui.retranslateUi(Window)
        # Window.show()
        # Window.exec_()

    def instantiatePattern(self):
        #quiero que se abra el Qdialogo ui_fullScreen.py
        data,images = self.patternRepository.get_pattern_data_by_name(self.lw_pattern.currentItem().text())
        Window = QtWidgets.QMainWindow()
        ui = Ui_instantiateWindow(images=images,parent=data['Name'])
        ui.setupUi(Window)
        ui.retranslateUi(Window)
        Window.show()
        Window.exec_()

    def fullScreen(self):
        # Mostrar la imagen actual en pantalla completa
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
        else:
            print("No visible label found")

    def show_image_maximized(self, label):
        pixmap = label.pixmap()
        if pixmap is None:
            print("No pixmap found in the visible label")
            return

        full_screen_widget = QtWidgets.QWidget()
        full_screen_widget.setWindowTitle("Maximized Image")
        layout = QtWidgets.QVBoxLayout(full_screen_widget)
        scroll_area = QtWidgets.QScrollArea(full_screen_widget)
        scroll_area.setWidgetResizable(True)
        full_screen_label = QtWidgets.QLabel()
        full_screen_label.setPixmap(pixmap)
        scroll_area.setWidget(full_screen_label)
        layout.addWidget(scroll_area)
        full_screen_widget.showMaximized()
        self.full_screen_widget = full_screen_widget
        full_screen_widget.mouseDoubleClickEvent = self.close_maximized_widget

    def close_maximized_widget(self, event):
        if self.full_screen_widget:
            self.full_screen_widget.close()
            self.full_screen_widget = None

    def previewPattern(self):
        # Mostrar la información del patrón seleccionado
        pattern_name = self.lw_pattern.currentItem().text()
        data, images = self.patternRepository.get_pattern_data_by_name(pattern_name)
        self.lb_name.setText(data['Name'])
        self.lw_associatedDomains.clear()
        dominios = []
        dominios.append(data['Domains']['key'])
        dominios.extend(data['Domains']['value'].values())
        dominios = list(set(dominios))
        dominios.remove(data['Domains']['key'])
        self.lw_associatedDomains.addItem(data['Domains']['key'])
        for domain in dominios:
            self.lw_associatedDomains.addItem(domain)
        self.lw_description.clear()
        self.lw_description.addItem(data['Description'])
        self.lw_knownUses.clear()
        for knownUse in data['Uses']:
            self.lw_knownUses.addItem(knownUse)
        self.lw_relatedPatterns.clear()
        for relatedPattern in data['RelatedPatterns']:
            self.lw_relatedPatterns.addItem(relatedPattern)
        self.lw_associatedRequirements.clear()
        for associatedRequirement in data['Requirements']:
            self.lw_associatedRequirements.addItem(associatedRequirement)

        self.set_image(self.lb_template, images['template'], "No se encontró la imagen")
        self.set_image(self.lb_scope, images['scopeModel'], "No se encontró la imagen")
        self.set_image(self.lb_structure, images['structureModel'], "No se encontró la imagen")
        self.set_image(self.lb_behavior, images['behaviorModel'], "No se encontró la imagen")

    def set_image(self, label, image_path, error_message):
        if image_path:
            label.setPixmap(image_path)
        else:
            label.setText(error_message)

    def searchPattern(self):
        results = self.patternRepository.search_pattern_by_name(self.le_search.text())
        self.lw_pattern.clear()
        for result in results:
            self.lw_pattern.addItem(result['Name'])
            
