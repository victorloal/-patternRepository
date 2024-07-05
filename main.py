import sys
from PyQt5 import QtWidgets
from interfacesPy.Busqueda import Ui_BusquedaPatron

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    BusquedaPatron = QtWidgets.QMainWindow()
    ui = Ui_BusquedaPatron()
    ui.setupUi(BusquedaPatron)
    BusquedaPatron.show()
    sys.exit(app.exec_())