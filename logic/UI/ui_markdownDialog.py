import sys
import os
import markdown2
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QTextBrowser, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

class MarkdownDialog(QDialog):
    """
    A dialog for displaying Markdown files as HTML.

    This dialog allows users to select Markdown files from a specified directory,
    convert them to HTML, and display the content in a QTextBrowser.
    """
    
    def __init__(self,directory):
        """
        Initializes the MarkdownDialog.

        Sets up the UI components including a QTextBrowser to display HTML content,
        a QListWidget to list Markdown files, and a close button.
        """
        super().__init__()
        self.directory = directory
        self.setWindowTitle("Diálogo de Markdown")
        self.resize(1300, 700)  
        layout = QVBoxLayout()
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True) 
        layout.addWidget(self.text_browser)
        self.file_list_widget = QListWidget()
        self.file_list_widget.setMaximumHeight(80)  
        self.load_markdown_files()  
        self.file_list_widget.itemClicked.connect(self.display_markdown_file)  
        layout.addWidget(self.file_list_widget)
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.accept)  
        layout.addWidget(close_button)

        self.setLayout(layout)

    def load_markdown_files(self):
        """
        Loads Markdown files from the "./resources" directory into the QListWidget.

        This method checks if the resources directory exists and lists all 
        Markdown files (with .md extension) found within it.
        """
        resource_dir = "./resources/"+self.directory
        if os.path.exists(resource_dir):
            for file_name in os.listdir(resource_dir):
                if file_name.endswith(".md"):
                    item = QListWidgetItem(file_name)
                    self.file_list_widget.addItem(item)

    def display_markdown_file(self, item):
        """
        Displays the content of the selected Markdown file in the QTextBrowser.

        Args:
            item (QListWidgetItem): The item clicked in the QListWidget representing a Markdown file.
        """
        file_name = item.text()
        file_path = os.path.join("./resources/"+self.directory, file_name)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
            html_content = markdown2.markdown(markdown_content)
            html_content = self.adjust_image_paths(html_content, file_path)
            self.text_browser.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo: {e}")

    def adjust_image_paths(self, html_content, markdown_file_path):
        """
        Adjusts the image paths in the HTML content based on the location of the Markdown file.

        Args:
            html_content (str): The HTML content derived from the Markdown.
            markdown_file_path (str): The path to the original Markdown file.

        Returns:
            str: The modified HTML content with adjusted image paths.
        """
        
        base_dir = os.path.dirname(markdown_file_path)
        import re
        def replace_image_path(match):
            img_src = match.group(1)
            if not img_src.startswith(('http://', 'https://')):
                
                img_path = os.path.join(base_dir, img_src)
                return f'src="{img_path}"'
            return f'src="{img_src}"'

        html_content = re.sub(r'src="([^"]*?)"', replace_image_path, html_content)
        return html_content

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MarkdownDialog("Informacion del programa")
    dialog.exec_()
