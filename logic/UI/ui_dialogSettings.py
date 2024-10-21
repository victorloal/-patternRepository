import sys
from PyQt5 import QtWidgets, QtGui,QtCore

class SelectDirectoryDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seleccionar Ruta del Repositorio de Patrones")
        self.setWindowIcon(QtGui.QIcon("path/to/icon.png"))  # Reemplaza con la ruta a tu icono
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setModal(True)
        

        # Crear un layout
        layout = QtWidgets.QVBoxLayout()

        # Crear un label con el mensaje
        self.label = QtWidgets.QLabel("Seleccione la ruta del repositorio de patrones:")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label)

        # Crear un botón para abrir el diálogo de selección de directorio
        self.select_button = QtWidgets.QPushButton("Seleccionar Directorio")
        self.select_button.clicked.connect(self.open_directory_dialog)
        
        layout.addWidget(self.select_button)

        # Crear un layout horizontal para los botones de Aceptar y Cancelar
        button_layout = QtWidgets.QHBoxLayout()

        # Crear un botón de aceptar
        self.accept_button = QtWidgets.QPushButton("Aceptar")
        self.accept_button.clicked.connect(self.accept)
        
        button_layout.addWidget(self.accept_button)

        # Crear un botón de cancelar
        self.cancel_button = QtWidgets.QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.selected_directory = None
        
        #ajustar el tamaño
        self.adjustSize()

    

    def open_directory_dialog(self):
        # Abrir el diálogo para seleccionar un directorio
        self.selected_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar Directorio")
        if self.selected_directory:
            self.label.setText(f"Directorio seleccionado: {self.selected_directory}")

    def get_selected_directory(self):
        return self.selected_directory


