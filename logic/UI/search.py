from PyQt5 import QtCore, QtGui, QtWidgets
from logic.pattern_repository import PatternRepository
from logic.UI.ui_messageBoxManager import MessageBoxManager
from ui_generated.ui_dialogSearch import Ui_Search

class Search(QtWidgets.QDialog, Ui_Search):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.patternRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.init_ui()
        
    def init_ui(self):
        self.pb_buscar.clicked.connect(self.search)
        self.pb_crearPatron.clicked.connect(self.close)  # Assuming it should close the dialog
        self.pb_verPatron.clicked.connect(self.accept)  # Accept action

    def search(self):
        search_text = self.le_datos.text()
        search_by_name = self.cb_nombre.isChecked()
        search_by_roles = self.cb_roles.isChecked()
        search_by_dominio = self.cb_dominio.isChecked()
        
        if not (search_by_name or search_by_roles or search_by_dominio):
            self.messageManager.show_critical_message(self,"Error", "Please select at least one search criteria.")
            return

        results = self.patternRepository.search(search_text, search_by_name, search_by_roles, search_by_dominio)
        self.display_results(results)

    def display_results(self, results):
        self.tw_listaPatrones.setRowCount(0)  # Clear previous results
        for result in results:
            row_position = self.tw_listaPatrones.rowCount()
            self.tw_listaPatrones.insertRow(row_position)
            self.tw_listaPatrones.setItem(row_position, 0, QtWidgets.QTableWidgetItem(result['Name']))
            self.tw_listaPatrones.setItem(row_position, 1, QtWidgets.QTableWidgetItem(result['Description']))

        