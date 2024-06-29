import sys

from PyQt5 import QtWidgets
import interfacesPy.CatalogacionPatrones as cp

class Main:
    def __init__(self):
        self.catalogacion = cp.CatalogacionPatrones()

    def run(self):
        self.catalogacion.run()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.run()
    sys.exit(app.exec_())