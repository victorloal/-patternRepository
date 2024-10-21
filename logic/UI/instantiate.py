import os
from PyQt5 import QtCore, QtGui, QtWidgets
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogInstantiate import Ui_InstantiatePatterns
from ui_generated.ui_frameDatosInstanciacion import Instanciacion
from logic.UI.ui_messageBoxManager import MessageBoxManager

class Instantiate(QtWidgets.QDialog, Ui_InstantiatePatterns):
    """
    A dialog for instantiating patterns with their respective images and SVG content.
    """

    def __init__(self, images, pattern, parent=None):
        """
        Initializes the Instantiate dialog.

        Args:
            images (dict): A dictionary containing image paths for different pattern components.
            parent (QWidget, optional): The parent widget of the dialog.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.images = images
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        pattern_data, self.images_path = self.patternRepository.get_path_images_by_name(pattern)
        self.init_ui(pattern)
        
    def init_ui(self,pattern):
        """
        Initializes the UI elements by setting images and connecting signals.
        """
        self.set_image(self.lb_template_2, self.images['template'], "Error al cargar la imagen")
        self.set_image(self.lb_scope_2, self.images['scopeModel'], "Error al cargar la imagen")
        self.set_image(self.lb_structure_2, self.images['structureModel'], "Error al cargar la imagen")
        self.set_image(self.lb_behavior_2, self.images['behaviorModel'], "Error al cargar la imagen")
        
        pattern_data,self.images_path = self.patternRepository.get_pattern_data_by_name(pattern)
        self.tw_preview_2.currentChanged.connect(lambda index: self.change_data(self.images_path))

    def change_data(self, images):
        """
        Changes the displayed SVG content based on the currently active tab in the preview widget.

        Args:
            images (dict): A dictionary of image paths to update the displayed content.
        """
        svg_content = None
        current_index = self.tw_preview_2.currentIndex()
        
        if current_index == 0:  # Template tab
            print("Tipo de images:", type(images))
            print("Contenido de images:", images)
            svg_content = images['templateSVG']
        elif current_index == 1:  # Scope tab
            svg_content = images['scopeModelSVG']
        elif current_index == 2:  # Structure tab
            svg_content = images['structureModelSVG']
        elif current_index == 3:  # Behavior tab
            svg_content = images['behaviorModelSVG']
        
        if not svg_content or not os.path.exists(svg_content):
            print("Error al cargar el archivo")
            return

        svg_content = self.load_svg_from_file(svg_content)
        new_frame_data = Instanciacion(svg_content)
        
        if self.dockWidget_2:
            dock_widget_layout = self.dockWidget_2.widget().layout()
            
            if dock_widget_layout:
                while dock_widget_layout.count():
                    item = dock_widget_layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()
                
                dock_widget_layout.addWidget(new_frame_data)
            else:
                print("No se encontró el layout en dockWidget_2")
        
        QtWidgets.QApplication.processEvents()
        
    def load_svg_from_file(self, file_path):
        """
        Loads the SVG content from the specified file.

        Args:
            file_path (str): The path to the SVG file.

        Returns:
            str: The content of the SVG file.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
        
    def set_image(self, label, image_path, error_message):
        """
        Sets an image in the specified label or shows an error message if the image path is invalid.

        Args:
            label (QLabel): The label to display the image.
            image_path (str): The path to the image.
            error_message (str): The message to display if the image cannot be loaded.
        """
        if image_path:
            label.setPixmap(image_path)
        else:
            label.setText(error_message)
