# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../interfaces/Requisitos de Dominio asociados a la Solución Especifica.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json
from PyQt5 import QtCore, QtGui, QtWidgets
from interfacesPy.NuevoDomino import Ui_NuevoDominio as nd


class Ui_RequisitosdeDominio(object):
    def setupUi(self, RequisitosdeDominio):
        self.RequisitosdeDominio = RequisitosdeDominio
        self.RequisitosdeDominio.setObjectName("RequisitosdeDominio")
        self.RequisitosdeDominio.resize(673, 399)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RequisitosdeDominio.sizePolicy().hasHeightForWidth())
        self.RequisitosdeDominio.setSizePolicy(sizePolicy)
        self.RequisitosdeDominio.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(self.RequisitosdeDominio)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_dominioAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_dominioAceptar.setObjectName("pb_dominioAceptar")
        self.gridLayout.addWidget(self.pb_dominioAceptar, 6, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_dominios = QtWidgets.QComboBox(self.centralwidget)
        self.cb_dominios.setObjectName("cb_dominios")
        self.verticalLayout.addWidget(self.cb_dominios)
        self.lw_dominios = QtWidgets.QListWidget(self.centralwidget)
        self.lw_dominios.setObjectName("lw_dominios")
        self.verticalLayout.addWidget(self.lw_dominios)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_eliminarDominio = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_eliminarDominio.sizePolicy().hasHeightForWidth())
        self.pb_eliminarDominio.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_eliminarDominio.setIcon(icon)
        self.pb_eliminarDominio.setObjectName("pb_eliminarDominio")
        self.horizontalLayout.addWidget(self.pb_eliminarDominio)
        self.pb_crearDominio = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_crearDominio.setIcon(icon)
        self.pb_crearDominio.setObjectName("pb_crearDominio")
        self.horizontalLayout.addWidget(self.pb_crearDominio)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.pb_dominioQuitar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_dominioQuitar.setObjectName("pb_dominioQuitar")
        self.gridLayout.addWidget(self.pb_dominioQuitar, 6, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
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
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 6, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 2, 1, 1, 1)
        self.pb_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cancelar.setObjectName("pb_cancelar")
        self.gridLayout.addWidget(self.pb_cancelar, 7, 0, 1, 1)
        self.pb_aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_aceptar.setObjectName("pb_aceptar")
        self.gridLayout.addWidget(self.pb_aceptar, 7, 3, 1, 1)
        self.lb_requisitosDominioAsociados = QtWidgets.QLabel(self.centralwidget)
        self.lb_requisitosDominioAsociados.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitosDominioAsociados.setObjectName("lb_requisitosDominioAsociados")
        self.gridLayout.addWidget(self.lb_requisitosDominioAsociados, 0, 3, 1, 1)
        self.lw_dominiosAsociados = QtWidgets.QListWidget(self.centralwidget)
        self.lw_dominiosAsociados.setObjectName("lw_dominiosAsociados")
        self.gridLayout.addWidget(self.lw_dominiosAsociados, 2, 3, 1, 1)
        self.lb_requisitoDominio = QtWidgets.QLabel(self.centralwidget)
        self.lb_requisitoDominio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitoDominio.setObjectName("lb_requisitoDominio")
        self.gridLayout.addWidget(self.lb_requisitoDominio, 0, 0, 1, 1)
        self.RequisitosdeDominio.setCentralWidget(self.centralwidget)
        self.cb_dominios.addItem("Seleccionar Dominio")



        self.optenerRuta()
        self.listarDominios()
        self.cb_dominios.currentIndexChanged.connect(self.listarRequisitos)
        self.pb_crearDominio.clicked.connect(self.crearDominio)
        self.pb_eliminarDominio.clicked.connect(self.eliminarDominio)
        self.pb_dominioAceptar.clicked.connect(self.dominioAceptar)
        self.pb_dominioQuitar.clicked.connect(self.dominioQuitar)
        self.pb_aceptar.clicked.connect(self.cancelar)
        self.pb_cancelar.clicked.connect(self.cancelar)
    
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.RequisitosdeDominio)

    def crearDominio(self):
        self.NuevoDominio = QtWidgets.QDialog()
        self.ui_arbol_patrones = nd()
        self.ui_arbol_patrones.setupUi(self.NuevoDominio)
        self.NuevoDominio.show()
    
    def eliminarDominio(self):
        pass
    
    def optenerRuta(self):
        with open("conf.json", "r") as file:
            data = json.load(file)
            self.file = data["repositorio"]
   
               
    def listarDominios(self):
        with open(f"{self.file}/Dominios.json") as file:
            data = file.read()
            data = json.loads(data)
            data = data["Dominios"]
            for dominio in data:
                self.cb_dominios.addItem(dominio)
                
    def listarRequisitos(self):
        with open(f"{self.file}/Dominios.json") as file:
            data = file.read()
            data = json.loads(data)
            data = data["Dominios"]
            self.lw_dominios.clear()
            try:  
                data = data[self.cb_dominios.currentText()]
                for requisito in data:
                    self.lw_dominios.addItem(requisito)
                
            except: 
                pass
                
    def dominioAceptar(self):
        try:
            with open("data.json", "r+") as file:
                # Cargar el contenido del archivo JSON
                data = json.load(file)
                # A ñadir el dominio a la lista de dominios asociados con repetición
                # ver si el dominio ya está en la lista
                if self.cb_dominios.currentText() not in data["Dominios"]:
                    data["Dominios"].append(self.cb_dominios.currentText())
                data["RequisitosRelacionados"].append(self.lw_dominios.currentItem().text())
                # Volver al inicio del archivo para sobreescribir el contenido
                file.seek(0)
                # Guardar los cambios
                json.dump(data, file, indent=4)
            #Agregar el dominio seleccionado a la lista de dominios asociados
            self.lw_dominiosAsociados.addItem(f"{self.cb_dominios.currentText()} : {self.lw_dominios.currentItem().text()}")
        except FileNotFoundError:
            print("El archivo data.json no se encuentra.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            
        file.close()
    
    def dominioQuitar(self):
        try:
            
            with open("data.json", "r+") as file:
                # Cargar el contenido del archivo JSON
                data = json.load(file)
                # Quitar el dominio de la lista de dominios asociados
                dominio_seleccionado = self.lw_dominiosAsociados.currentItem().text().split(" : ")[0]
                if dominio_seleccionado in data["Dominios"]:
                    data["Dominios"].remove(dominio_seleccionado)
                requisito_seleccionado = self.lw_dominiosAsociados.currentItem().text().split(" : ")[1]
                if requisito_seleccionado in data["RequisitosRelacionados"]:
                    data["RequisitosRelacionados"].remove(requisito_seleccionado)
                # Volver al inicio del archivo para sobreescribir el contenido
                file.seek(0) 
                # Truncar el archivo para eliminar el contenido restante
                file.truncate()
                # Guardar los cambios
                json.dump(data, file, indent=4)
            
            #Quitar el dominio seleccionado de la lista de dominios asociados
            self.lw_dominiosAsociados.takeItem(self.lw_dominiosAsociados.currentRow())
        except FileNotFoundError:
            print("El archivo data.json no se encuentra.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
    
        file.close()
        
        
    
    def cancelar(self):
        self.RequisitosdeDominio.close()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.RequisitosdeDominio.setWindowTitle(_translate("RequisitosdeDominio", "Requisitos de Dominio asociados a la Solución Especifica"))
        self.pb_dominioAceptar.setText(_translate("RequisitosdeDominio", ">>"))
        self.pb_eliminarDominio.setText(_translate("RequisitosdeDominio", "Eliminar"))
        self.pb_crearDominio.setText(_translate("RequisitosdeDominio", "Crear nuevo"))
        self.pb_dominioQuitar.setText(_translate("RequisitosdeDominio", "<<"))
        self.pb_cancelar.setText(_translate("RequisitosdeDominio", "Cancelar"))
        self.pb_aceptar.setText(_translate("RequisitosdeDominio", "Aceptar"))
        self.lb_requisitosDominioAsociados.setText(_translate("RequisitosdeDominio", "Requisitos de Dominio asociados"))
        self.lb_requisitoDominio.setText(_translate("RequisitosdeDominio", "Requisitos de Dominio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RequisitosdeDominio = QtWidgets.QMainWindow()
    ui = Ui_RequisitosdeDominio()
    ui.setupUi(RequisitosdeDominio)
    RequisitosdeDominio.show()
    sys.exit(app.exec_())
