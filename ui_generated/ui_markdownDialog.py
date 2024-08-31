import sys
import os
import markdown2
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QTextBrowser, QFileDialog
from PyQt5.QtCore import Qt

class MarkdownDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diálogo de Markdown")
        self.resize(600, 400)  # Tamaño inicial de la ventana

        # Layout principal del diálogo
        layout = QVBoxLayout()

        # Crear un QTextBrowser para mostrar el contenido HTML
        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser)

        # Botón para abrir el archivo Markdown
        open_button = QPushButton("Abrir archivo Markdown")
        open_button.clicked.connect(self.open_markdown_file)
        layout.addWidget(open_button)

        # Botón para cerrar el diálogo
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.accept)  # Cierra el diálogo al hacer clic
        layout.addWidget(close_button)

        self.setLayout(layout)

    def open_markdown_file(self):
        # Abrir un diálogo de selección de archivo
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo Markdown", "", "Markdown Files (*.md);;All Files (*)", options=options)

        if file_name:
            # Leer el archivo Markdown
            with open(file_name, 'r', encoding='utf-8') as file:
                markdown_content = file.read()

            # Convertir Markdown a HTML
            html_content = markdown2.markdown(markdown_content)

            # Ajustar rutas de imágenes en HTML
            html_content = self.adjust_image_paths(html_content, file_name)

            # Mostrar el contenido HTML en QTextBrowser
            self.text_browser.setHtml(html_content)

    def adjust_image_paths(self, html_content, markdown_file_path):
        # Obtener el directorio del archivo Markdown
        base_dir = os.path.dirname(markdown_file_path)
        
        # Reemplazar rutas relativas de imágenes en el HTML
        import re
        def replace_image_path(match):
            img_src = match.group(1)
            if not img_src.startswith(('http://', 'https://')):
                # Construir la ruta absoluta de la imagen
                img_path = os.path.join(base_dir, img_src)
                return f'src="{img_path}"'
            return f'src="{img_src}"'

        # Buscar y reemplazar rutas de imágenes
        html_content = re.sub(r'src="([^"]*?)"', replace_image_path, html_content)
        return html_content

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MarkdownDialog()
    dialog.exec_()
    