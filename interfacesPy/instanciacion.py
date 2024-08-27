from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from lxml import etree

class SvgTextModifier:
    def __init__(self, svg_content):
        self.svg_content = svg_content
        self.tree = etree.fromstring(svg_content.encode('utf-8'))
        self.ns = {'svg': 'http://www.w3.org/2000/svg'}
        self.text_elements = self.tree.findall('.//svg:text', namespaces=self.ns)

    def get_texts(self):
        texts = []
        for text in self.text_elements:
            tspan_elements = text.findall('.//svg:tspan', namespaces=self.ns)
            if not tspan_elements:
                text_content = text.text.strip() if text.text else ''
                if text_content:  # Ignorar textos vacíos
                    texts.append(text_content)
            else:
                for tspan in tspan_elements:
                    tspan_content = tspan.text.strip() if tspan.text else ''
                    if tspan_content:  # Ignorar textos vacíos
                        texts.append(tspan_content)
        return list(set(texts))  # Return unique texts

    def modify_text(self, text_replacements):
        for text in self.text_elements:
            tspan_elements = text.findall('.//svg:tspan', namespaces=self.ns)
            if not tspan_elements:
                original_text = text.text.strip() if text.text else ''
                if original_text in text_replacements:
                    text.text = text_replacements[original_text]
            else:
                for tspan in tspan_elements:
                    original_text = tspan.text.strip() if tspan.text else ''
                    if original_text in text_replacements:
                        tspan.text = text_replacements[original_text]
        return etree.tostring(self.tree, encoding='unicode')
    

class Instanciacion(QDialog):
    def __init__(self, svg_content, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit SVG Text")
        self.setMinimumSize(400, 300)

        self.modifier = SvgTextModifier(svg_content)
        self.original_texts = self.modifier.get_texts()

        layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.text_entries = {}

        for text in self.original_texts:
            if text:  # Ignorar textos vacíos
                label = QLabel(text)
                line_edit = QLineEdit(text)
                self.form_layout.addRow(label, line_edit)
                self.text_entries[text] = line_edit

        save_button = QPushButton("Save As")
        save_button.clicked.connect(self.save_as)

        layout.addLayout(self.form_layout)
        layout.addWidget(save_button)

        self.setLayout(layout)
        self.modified_svg_content = svg_content

    def save_as(self):
        text_replacements = {text: entry.text().strip() for text, entry in self.text_entries.items() if text.strip()}
        print(f"Text replacements: {text_replacements}")  # Debugging line
        self.modified_svg_content = self.modifier.modify_text(text_replacements)

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save SVG File", "", "SVG Files (*.svg);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.modified_svg_content)
            print(f"File saved to {file_path}")
        self.accept()