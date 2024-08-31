from PyQt5.QtWidgets import QFrame, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5 import QtWidgets

from logic.svg_text_modifier import SvgTextModifier

class Instanciacion(QFrame):
    def __init__(self, svg_content, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)  # Optional: Set the frame shape
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # Allow expanding

        self.modifier = SvgTextModifier(svg_content)
        self.original_texts = self.modifier.get_texts()

        layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.text_entries = {}

        for text in self.original_texts:
            if text:  # Ignore empty texts
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

        self.adjust_size()  # Adjust size to fit content

    def save_as(self):
        text_replacements = {text: entry.text().strip() for text, entry in self.text_entries.items() if entry.text().strip()}
        print(f"Text replacements: {text_replacements}")  # Debugging line
        self.modified_svg_content = self.modifier.modify_text(text_replacements)

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save SVG File", "", "SVG Files (*.svg);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.modified_svg_content)
            print(f"File saved to {file_path}")

    def adjust_size(self):
        # Adjust the widget size based on its content
        self.resize(self.sizeHint())  # Set size based on the hint provided by the layout