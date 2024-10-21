from PyQt5 import QtWidgets
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogEditRequirement import Ui_Dialog
from logic.UI.ui_messageBoxManager import MessageBoxManager


class NewRequirement(QtWidgets.QDialog, Ui_Dialog):
    """
    Clase que representa un diálogo para crear o editar requisitos.
    Hereda de QDialog y Ui_Dialog.
    """

    def __init__(self, parent=None):
        """
        Inicializa el diálogo y configura la interfaz de usuario.

        :param parent: Ventana padre del diálogo.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.init_ui()

    def init_ui(self):
        """Configura los elementos de la interfaz de usuario."""
        self.pb_cancel.clicked.connect(self.close)

    def ui_new(self, flat):
        """
        Configura el diálogo para un nuevo requisito.

        :param flat: Booleano que indica si es un nuevo requisito.
        """
        if flat:
            self.pb_edit.setVisible(False)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pb_new.sizePolicy().hasHeightForWidth())
            self.pb_new.setSizePolicy(sizePolicy)
