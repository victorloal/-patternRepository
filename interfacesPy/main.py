import sys
from PyQt5 import QtWidgets
from Busqueda import Ui_MainWindow
from CatalogacionPatrones import Ui_Catalogaciondelpatron

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui_busqueda = Ui_MainWindow()
        self.ui_catalogacion = Ui_Catalogaciondelpatron()
        
        self.ui_busqueda.setupUi(self)
        self.show()

    def closeEvent(self, event):
        self.next_window()

    def next_window(self):
        self.new_window = QtWidgets.QMainWindow()
        self.ui_catalogacion.setupUi(self.new_window)
        self.new_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())