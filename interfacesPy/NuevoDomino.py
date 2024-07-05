# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../interfaces/Nuevo dominio.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NuevoDominio(object):
    def setupUi(self, NuevoDominio):
        NuevoDominio.setObjectName("NuevoDominio")
        NuevoDominio.resize(422, 334)
        self.verticalLayout = QtWidgets.QVBoxLayout(NuevoDominio)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lb_nuevoDominio = QtWidgets.QLabel(NuevoDominio)
        self.lb_nuevoDominio.setObjectName("lb_nuevoDominio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_nuevoDominio)
        self.le_nombreDominio = QtWidgets.QLineEdit(NuevoDominio)
        self.le_nombreDominio.setObjectName("le_nombreDominio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_nombreDominio)
        self.verticalLayout.addLayout(self.formLayout)
        self.lb_requisitos = QtWidgets.QLabel(NuevoDominio)
        self.lb_requisitos.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitos.setObjectName("lb_requisitos")
        self.verticalLayout.addWidget(self.lb_requisitos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_requisitos = QtWidgets.QComboBox(NuevoDominio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_requisitos.sizePolicy().hasHeightForWidth())
        self.cb_requisitos.setSizePolicy(sizePolicy)
        self.cb_requisitos.setEditable(True)
        self.cb_requisitos.setDuplicatesEnabled(False)
        self.cb_requisitos.setFrame(True)
        self.cb_requisitos.setObjectName("cb_requisitos")
        self.horizontalLayout.addWidget(self.cb_requisitos)
        self.pb_adicionar = QtWidgets.QPushButton(NuevoDominio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_adicionar.sizePolicy().hasHeightForWidth())
        self.pb_adicionar.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_adicionar.setIcon(icon)
        self.pb_adicionar.setObjectName("pb_adicionar")
        self.horizontalLayout.addWidget(self.pb_adicionar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lw_requisitos = QtWidgets.QListWidget(NuevoDominio)
        self.lw_requisitos.setObjectName("lw_requisitos")
        self.verticalLayout.addWidget(self.lw_requisitos)
        self.pb_eliminar = QtWidgets.QPushButton(NuevoDominio)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_eliminar.setIcon(icon)
        self.pb_eliminar.setObjectName("pb_eliminar")
        self.verticalLayout.addWidget(self.pb_eliminar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_cancel = QtWidgets.QPushButton(NuevoDominio)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.pb_cancel.setIcon(icon)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_save = QtWidgets.QPushButton(NuevoDominio)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pb_save.setIcon(icon)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout_2.addWidget(self.pb_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        
        self.optenerRuta()
        self.listarRequisitos()
        self.pb_adicionar.clicked.connect(self.adicionarRequisito)
        self.pb_eliminar.clicked.connect(self.eliminarRequisito)
        self.pb_cancel.clicked.connect(NuevoDominio.close)
        self.pb_save.clicked.connect(self.guardarDominio)

        self.retranslateUi(NuevoDominio)
        QtCore.QMetaObject.connectSlotsByName(NuevoDominio)
    
    def guardarDominio(self):
        dominio = self.le_nombreDominio.text()
        if dominio:
            requisitos = []
            for i in range(self.lw_requisitos.count()):
                requisitos.append(self.lw_requisitos.item(i).text())
            with open(f"{self.file}/Dominios.json", "r") as file:
                data = json.load(file)
                data["Dominios"][dominio] = requisitos
            with open(f"{self.file}/Dominios.json", "w") as file:
                json.dump(data, file)
            self.le_nombreDominio.clear()
            self.lw_requisitos.clear()
            self.listarRequisitos()
            
            
    def optenerRuta(self):
        with open("conf.json", "r") as file:
            data = json.load(file)
            self.file = data["repositorio"]
            
    def listarRequisitos(self):
        self.cb_requisitos.clear()
        with open(f"{self.file}/Dominios.json", "r") as file:
            data = json.load(file)
            self.cb_requisitos.addItem("Nuevo Requisito")
            for dominio, requisitos in data["Dominios"].items():
                #Anadir el dominio a la lista de requisitos con un icono de folder
                self.cb_requisitos.addItem(dominio)
                self.cb_requisitos.setItemIcon(self.cb_requisitos.count()-1, QtGui.QIcon.fromTheme("folder-open"))
                for requisito in requisitos:
                    self.cb_requisitos.addItem(requisito)
                    
    def eliminarRequisito(self):
        item = self.lw_requisitos.currentItem()
        if item:
            self.lw_requisitos.takeItem(self.lw_requisitos.row(item))
            
            
    def adicionarRequisito(self):
        requisito = self.cb_requisitos.currentText()
        if requisito:
            self.lw_requisitos.addItem(requisito)
            
    def retranslateUi(self, NuevoDominio):
        _translate = QtCore.QCoreApplication.translate
        NuevoDominio.setWindowTitle(_translate("NuevoDominio", "Dialog"))
        self.lb_nuevoDominio.setText(_translate("NuevoDominio", "Nuevo Dominio"))
        self.lb_requisitos.setText(_translate("NuevoDominio", "Requisitos"))
        self.cb_requisitos.setCurrentText(_translate("NuevoDominio", "Nuevo Requisito"))
        self.cb_requisitos.setPlaceholderText(_translate("NuevoDominio", "Nuevo requisito"))
        self.pb_adicionar.setText(_translate("NuevoDominio", "Adicionar"))
        self.pb_eliminar.setText(_translate("NuevoDominio", "Eliminar Requisito"))
        self.pb_cancel.setText(_translate("NuevoDominio", "Cancelar"))
        self.pb_save.setText(_translate("NuevoDominio", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NuevoDominio = QtWidgets.QDialog()
    ui = Ui_NuevoDominio()
    ui.setupUi(NuevoDominio)
    NuevoDominio.show()
    sys.exit(app.exec_())
