from PyQt5 import QtWidgets, QtCore

class CustomInputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize with default values
        self.default_title = "Input Dialog"
        self.default_label_text = "Please enter your input:"
        self.default_input_text = ""
        self.default_ok_button_text = "OK"
        self.default_cancel_button_text = "Cancel"
        
        # Set initial values
        self.setWindowTitle(self.default_title)
        self.setModal(True)
        
        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Create label and input field
        self.label = QtWidgets.QLabel(self.default_label_text, self)
        self.layout.addWidget(self.label)
        
        self.input_field = QtWidgets.QLineEdit(self.default_input_text, self)
        self.layout.addWidget(self.input_field)
        
        # Create buttons
        self.button_box = QtWidgets.QDialogButtonBox(self)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        
        self.ok_button = self.button_box.addButton(self.default_ok_button_text, QtWidgets.QDialogButtonBox.AcceptRole)
        self.cancel_button = self.button_box.addButton(self.default_cancel_button_text, QtWidgets.QDialogButtonBox.RejectRole)
        
        self.layout.addWidget(self.button_box)
        
        # Connect buttons to methods
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def update_dialog(self, title=None, label_text=None, input_text=None, ok_button_text=None, cancel_button_text=None):
        """
        Update the dialog's title, label text, input field text, and button texts.
        """
        if title is not None:
            self.setWindowTitle(title)
        if label_text is not None:
            self.label.setText(label_text)
        if input_text is not None:  # Allow setting empty text
            self.input_field.setText(input_text)
        if ok_button_text is not None:
            self.ok_button.setText(ok_button_text)
        if cancel_button_text is not None:
            self.cancel_button.setText(cancel_button_text)

    def get_input(self):
        """
        Show the dialog and return the text from the input field if the dialog was accepted.
        """
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.input_field.text()
        return None