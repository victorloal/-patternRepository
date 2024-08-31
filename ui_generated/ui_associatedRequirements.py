# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Dialogo_associatedRequirements.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from logic.pattern_repository import PatternRepository
from ui_generated.ui_customInputDialog import CustomInputDialog
from ui_generated.ui_messageBoxManager import MessageBoxManager


class Ui_AssociatedRequirements(object):
    def setupUi(self, AssociatedRequirements):
        self.AssociatedRequirements = AssociatedRequirements
        AssociatedRequirements.setObjectName("AssociatedRequirements")
        AssociatedRequirements.resize(461, 300)
        self.gridLayout = QtWidgets.QGridLayout(AssociatedRequirements)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_requisitoDominio = QtWidgets.QLabel(AssociatedRequirements)
        self.lb_requisitoDominio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitoDominio.setObjectName("lb_requisitoDominio")
        self.gridLayout.addWidget(self.lb_requisitoDominio, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(AssociatedRequirements)
        self.line_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.lb_requisitosDominioAsociados = QtWidgets.QLabel(AssociatedRequirements)
        self.lb_requisitosDominioAsociados.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitosDominioAsociados.setObjectName("lb_requisitosDominioAsociados")
        self.gridLayout.addWidget(self.lb_requisitosDominioAsociados, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_domains = QtWidgets.QComboBox(AssociatedRequirements)
        self.cb_domains.setObjectName("cb_domains")
        self.verticalLayout.addWidget(self.cb_domains)
        self.lw_domains = QtWidgets.QListWidget(AssociatedRequirements)
        self.lw_domains.setObjectName("lw_domains")
        self.verticalLayout.addWidget(self.lw_domains)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_deleteRequirements = QtWidgets.QPushButton(AssociatedRequirements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_deleteRequirements.sizePolicy().hasHeightForWidth())
        self.pb_deleteRequirements.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_deleteRequirements.setIcon(icon)
        self.pb_deleteRequirements.setObjectName("pb_deleteRequirements")
        self.horizontalLayout.addWidget(self.pb_deleteRequirements)
        self.pb_newRequirements = QtWidgets.QPushButton(AssociatedRequirements)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_newRequirements.setIcon(icon)
        self.pb_newRequirements.setObjectName("pb_newRequirements")
        self.horizontalLayout.addWidget(self.pb_newRequirements)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(AssociatedRequirements)
        self.line_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 1, 1, 1)
        self.lw_associatedRequirements = QtWidgets.QListWidget(AssociatedRequirements)
        self.lw_associatedRequirements.setObjectName("lw_associatedRequirements")
        self.gridLayout.addWidget(self.lw_associatedRequirements, 1, 2, 1, 1)
        self.pb_addRequirements = QtWidgets.QPushButton(AssociatedRequirements)
        self.pb_addRequirements.setObjectName("pb_addRequirements")
        self.gridLayout.addWidget(self.pb_addRequirements, 2, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(AssociatedRequirements)
        self.line_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 1, 1, 1)
        self.pb_removeRequirements = QtWidgets.QPushButton(AssociatedRequirements)
        self.pb_removeRequirements.setObjectName("pb_removeRequirements")
        self.gridLayout.addWidget(self.pb_removeRequirements, 2, 2, 1, 1)
        self.pb_cancel = QtWidgets.QPushButton(AssociatedRequirements)
        self.pb_cancel.setObjectName("pb_cancel")
        self.gridLayout.addWidget(self.pb_cancel, 3, 0, 1, 1)
        self.pb_save = QtWidgets.QPushButton(AssociatedRequirements)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout.addWidget(self.pb_save, 3, 2, 1, 1)

        self.retranslateUi(AssociatedRequirements)
        QtCore.QMetaObject.connectSlotsByName(AssociatedRequirements)
        #  =======================================================================
        self.pattern_repository = PatternRepository()
        self.menssageBoxManager = MessageBoxManager()
        self.customDialog = CustomInputDialog()
        self.listDomains()
        self.listRequirements()
        self.domains = {}
        
        self.pb_deleteRequirements.clicked.connect(self.delete_requirements)
        self.pb_newRequirements.clicked.connect(self.create_new_requirement)
        self.pb_addRequirements.clicked.connect(self.add_requirement)
        self.pb_removeRequirements.clicked.connect(self.remove_requirement)
        self.pb_cancel.clicked.connect(AssociatedRequirements.close)
        self.pb_save.clicked.connect(self.save)
        self.cb_domains.currentIndexChanged.connect(self.listRequirements)
        
    def save(self):
        self.result = []
        for i in range(self.lw_associatedRequirements.count()):
            self.result.append(self.lw_associatedRequirements.item(i).text())
        self.AssociatedRequirements.accept()
        
    def get_result(self):
        # Return the selected domains and associated requirements
        return self.domains, self.result
    
    def set_result(self, domains, requirements):
        # Set the selected domains and associated requirements
        self.domains = domains
        self.lw_associatedRequirements.addItems(requirements)
    
    def listDomains(self):
        domains = self.pattern_repository.get_domains()
        for dominio in domains["Domains"].keys():
            self.cb_domains.addItem(dominio)
            
    def listRequirements(self):
        self.lw_domains.clear()
        domains = self.pattern_repository.get_domains()
        for requisito in domains["Domains"][self.cb_domains.currentText()]:
            self.lw_domains.addItem(requisito)
            
        pass
    
    def delete_requirements(self):
        # Remove selected items from lw_domains
        selected_items = self.lw_domains.selectedItems()
        for item in selected_items:
            result = self.menssageBoxManager.show_question_message(self.AssociatedRequirements, "Warning", "esta seguro de eliminar este requerimiento?","Eliminar","Cancelar")   
            if result:
                self.pattern_repository.delete_requirement(self.cb_domains.currentText(), item.text())
                self.lw_domains.takeItem(self.lw_domains.row(item))
    
    def create_new_requirement(self):
        # Show dialog to create new requirement
        self.customDialog.update_dialog(
            title="Nuevo Requisito",
            label_text="Ingrese el nombre del requisito:",
            input_text="",  # No default input text
            ok_button_text="Crear",
            cancel_button_text="Cancelar"
        )
        
        user_input = self.customDialog.get_input()
        if user_input:
            # Add the new requirement to the appropriate domain
            self.pattern_repository.append_requirement(self.cb_domains.currentText(), user_input)
            self.listRequirements()
    
    def add_requirement(self):
        # Add selected requirement from lw_domains to lw_associatedRequirements
        selected_items = self.lw_domains.selectedItems()
        if not self.verifyItem(selected_items):
            for item in selected_items:
                self.lw_associatedRequirements.addItem(item.text())
                self.domains[item.text()] = self.cb_domains.currentText()
            
    def verifyItem(self, selected_items):
        # Flag to determine if any duplicate items are found
        duplicate_found = False

        # Iterate over selected items
        for item in selected_items:
            # Check if the item already exists in lw_associatedRequirements
            for i in range(self.lw_associatedRequirements.count()):
                if item.text() == self.lw_associatedRequirements.item(i).text():
                    duplicate_found = True
                    break
            
            if duplicate_found:
                break
        
        # Show message if duplicates are found
        if duplicate_found:
            #prueba todos los elementos de la lista
            self.menssageBoxManager.show_info_message(self.AssociatedRequirements, "Warning", "Duplicate items are not allowed.")
        return duplicate_found
    
    def remove_requirement(self):
        # Remove selected associated requirement from lw_associatedRequirements
        selected_items = self.lw_associatedRequirements.selectedItems()
        for item in selected_items:
            self.lw_associatedRequirements.takeItem(self.lw_associatedRequirements.row(item))
            self.domains.pop(item.text())

    def retranslateUi(self, AssociatedRequirements):
        _translate = QtCore.QCoreApplication.translate
        AssociatedRequirements.setWindowTitle(_translate("AssociatedRequirements", "Dialog"))
        self.lb_requisitoDominio.setText(_translate("AssociatedRequirements", "Requisitos de Dominio"))
        self.lb_requisitosDominioAsociados.setText(_translate("AssociatedRequirements", "Requisitos de Dominio asociados"))
        self.pb_deleteRequirements.setText(_translate("AssociatedRequirements", "Eliminar"))
        self.pb_newRequirements.setText(_translate("AssociatedRequirements", "Crear nuevo"))
        self.pb_addRequirements.setText(_translate("AssociatedRequirements", ">>"))
        self.pb_removeRequirements.setText(_translate("AssociatedRequirements", "<<"))
        self.pb_cancel.setText(_translate("AssociatedRequirements", "Cancelar"))
        self.pb_save.setText(_translate("AssociatedRequirements", "Aceptar"))
