from PyQt5 import  QtWidgets
from logic.pattern_repository import PatternRepository
from ui_generated.ui_dialogEditRequirement import Ui_Dialog
from ui_generated.ui_messageBoxManager import MessageBoxManager


class NewRequirement(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.showNormal()
        self.init_ui()
        
    def init_ui(self):
        self.pb_cancel.clicked.connect(self.close)
        
    def ui_new(self,flat):
        if flat:
            self.pb_edit.setVisible(False)
            
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pb_new.sizePolicy().hasHeightForWidth())
            self.pb_new.setSizePolicy(sizePolicy)
        

        