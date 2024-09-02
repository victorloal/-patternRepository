import os
from PyQt5 import QtCore, QtGui, QtWidgets
from logic.pattern_repository import PatternRepository
from ui_generated.ui_frameDatosInstanciacion import Instanciacion
from ui_generated.ui_fullScreen import Ui_instantiateWindow
from ui_generated.ui_messageBoxManager import MessageBoxManager

class instantiate(QtWidgets.QDialog, Ui_instantiateWindow):
    def __init__(self,images, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.images = images
        self.images_path = self.patternRepository.get_path_images_by_name(self.parent)
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.init_ui()
        
    def init_ui(self):
        self.set_image(self.lb_template, self.images['template'], "Error al cargar la imagen")
        self.set_image(self.lb_scope, self.images['scopeModel'], "Error al cargar la imagen")
        self.set_image(self.lb_structure, self.images['structureModel'], "Error al cargar la imagen")
        self.set_image(self.lb_behavior, self.images['behaviorModel'], "Error al cargar la imagen")
        
        self.tw_preview.currentChanged.connect(lambda index: self.change_data(self.images_path))

    def change_data(self, images):
        print("Cambio de pestaña")
        print(images)

        svg_content = None
        
        # Determina qué contenido SVG mostrar basado en la pestaña activa
        current_index = self.tw_preview.currentIndex()
        
        if current_index == 0:  # Template tab
            svg_content = images['template']
            print("Template")
        elif current_index == 1:  # Scope tab
            svg_content = images['scopeModel']
            print("Alcance")
        elif current_index == 2:  # Structure tab
            svg_content = images['structureModel']
            print("Estructura")
        elif current_index == 3:  # Behavior tab
            svg_content = images['behaviorModel']
            print("Comportamiento")
        
        # Verifica si el contenido SVG es válido
        if not svg_content or not os.path.exists(svg_content):
            print("Error al cargar el archivo")
            return

        # Carga el contenido del SVG
        svg_content = self.load_svg_from_file(svg_content)
        
        # Instancia la clase Instanciacion con el nuevo contenido
        new_frame_data = Instanciacion(svg_content)
        
        # Actualiza el layout del QDockWidget
        if self.dockWidget_2:
            dock_widget_layout = self.dockWidget_2.widget().layout()
            
            if dock_widget_layout:
                # Limpia el layout actual
                while dock_widget_layout.count():
                    item = dock_widget_layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()
                
                # Agrega el nuevo frame_data al layout
                dock_widget_layout.addWidget(new_frame_data)
            else:
                print("No se encontró el layout en dockWidget_2")
        
        # Forzar la actualización del UI
        QtWidgets.QApplication.processEvents()
        
    def load_svg_from_file(self, file_path):
        # Open the SVG file and read its content.
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
        
    def set_image(self,label, image_path, error_message):
        #verificar si la imagen es null o vacio
        if image_path:
            label.setPixmap(image_path)
        else:
            label.setText(error_message)
            
