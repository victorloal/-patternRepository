import sys
from PyQt5 import QtWidgets
from logic.UI.home import Home

if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    main_window = Home()
    main_window.show()
    sys.exit(app.exec_())


    
    
    
    
    
    
      