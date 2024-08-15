# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../interfaces/Catalogaciondelpatron.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json
import os
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from interfacesPy.NuevoDomino import Ui_NuevoDominio as nd
from interfacesPy.UsosConosidos import Ui_UsosConocidos as uc
from interfacesPy.RequisitoDominio import Ui_RequisitosdeDominio as rd


class Ui_Catalogaciondelpatron(object):
    def setupUi(self, Catalogaciondelpatron):
        Catalogaciondelpatron.setObjectName("Catalogaciondelpatron")
        Catalogaciondelpatron.resize(884, 549)
        self.Catalogaciondelpatron_2 = QtWidgets.QWidget(Catalogaciondelpatron)
        self.Catalogaciondelpatron_2.setObjectName("Catalogaciondelpatron_2")
        self.gridLayout = QtWidgets.QGridLayout(self.Catalogaciondelpatron_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_usosConocidos = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        self.pb_usosConocidos.setObjectName("pb_usosConocidos")
        self.gridLayout.addWidget(self.pb_usosConocidos, 6, 2, 1, 1)
        self.lb_dominio = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_dominio.setObjectName("lb_dominio")
        self.gridLayout.addWidget(self.lb_dominio, 2, 1, 1, 1)
        self.tb_infoPatronesRelacionados = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoPatronesRelacionados.setIcon(icon)
        self.tb_infoPatronesRelacionados.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoPatronesRelacionados.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoPatronesRelacionados.setAutoRaise(True)
        self.tb_infoPatronesRelacionados.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoPatronesRelacionados.setObjectName("tb_infoPatronesRelacionados")
        self.gridLayout.addWidget(self.tb_infoPatronesRelacionados, 7, 0, 1, 1)
        self.lb_descripcion = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_descripcion.setObjectName("lb_descripcion")
        self.gridLayout.addWidget(self.lb_descripcion, 4, 1, 1, 1)
        self.le_nombre = QtWidgets.QLineEdit(self.Catalogaciondelpatron_2)
        self.le_nombre.setObjectName("le_nombre")
        self.gridLayout.addWidget(self.le_nombre, 0, 2, 1, 1)
        self.lb_patronesRelacionados = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_patronesRelacionados.setObjectName("lb_patronesRelacionados")
        self.gridLayout.addWidget(self.lb_patronesRelacionados, 7, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_Dominios = QtWidgets.QComboBox(self.Catalogaciondelpatron_2)
        self.cb_Dominios.setObjectName("cb_Dominios")
        self.horizontalLayout.addWidget(self.cb_Dominios)
        self.pb_nuevoDominio = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_nuevoDominio.sizePolicy().hasHeightForWidth())
        self.pb_nuevoDominio.setSizePolicy(sizePolicy)
        self.pb_nuevoDominio.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_nuevoDominio.setIcon(icon)
        self.pb_nuevoDominio.setAutoDefault(False)
        self.pb_nuevoDominio.setDefault(False)
        self.pb_nuevoDominio.setFlat(True)
        self.pb_nuevoDominio.setObjectName("pb_nuevoDominio")
        self.horizontalLayout.addWidget(self.pb_nuevoDominio)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.tb_infoUsosConocidos = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoUsosConocidos.setIcon(icon)
        self.tb_infoUsosConocidos.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoUsosConocidos.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoUsosConocidos.setAutoRaise(True)
        self.tb_infoUsosConocidos.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoUsosConocidos.setObjectName("tb_infoUsosConocidos")
        self.gridLayout.addWidget(self.tb_infoUsosConocidos, 6, 0, 1, 1)
        self.tb_infoModeloAlcance = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoModeloAlcance.setIcon(icon)
        self.tb_infoModeloAlcance.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoModeloAlcance.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoModeloAlcance.setAutoRaise(True)
        self.tb_infoModeloAlcance.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoModeloAlcance.setObjectName("tb_infoModeloAlcance")
        self.gridLayout.addWidget(self.tb_infoModeloAlcance, 9, 0, 1, 1)
        self.pb_requisitosDominiosRelacionados = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        self.pb_requisitosDominiosRelacionados.setObjectName("pb_requisitosDominiosRelacionados")
        self.gridLayout.addWidget(self.pb_requisitosDominiosRelacionados, 8, 2, 1, 1)
        self.tb_infoModeloComportamiento = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoModeloComportamiento.setIcon(icon)
        self.tb_infoModeloComportamiento.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoModeloComportamiento.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoModeloComportamiento.setAutoRaise(True)
        self.tb_infoModeloComportamiento.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoModeloComportamiento.setObjectName("tb_infoModeloComportamiento")
        self.gridLayout.addWidget(self.tb_infoModeloComportamiento, 11, 0, 1, 1)
        self.lb_usosConocidos = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_usosConocidos.setObjectName("lb_usosConocidos")
        self.gridLayout.addWidget(self.lb_usosConocidos, 6, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_modeloComportamientoDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloComportamientoDia.setIcon(icon)
        self.pb_modeloComportamientoDia.setCheckable(False)
        self.pb_modeloComportamientoDia.setChecked(False)
        self.pb_modeloComportamientoDia.setAutoRepeat(False)
        self.pb_modeloComportamientoDia.setAutoExclusive(False)
        self.pb_modeloComportamientoDia.setAutoDefault(False)
        self.pb_modeloComportamientoDia.setDefault(False)
        self.pb_modeloComportamientoDia.setFlat(False)
        self.pb_modeloComportamientoDia.setObjectName("pb_modeloComportamientoDia")
        self.horizontalLayout_5.addWidget(self.pb_modeloComportamientoDia)
        self.lb_modeloComportamientoDIA = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloComportamientoDIA.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloComportamientoDIA.setObjectName("lb_modeloComportamientoDIA")
        self.horizontalLayout_5.addWidget(self.lb_modeloComportamientoDIA)
        self.pb_modeloComportamientoSVG = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloComportamientoSVG.setIcon(icon)
        self.pb_modeloComportamientoSVG.setCheckable(False)
        self.pb_modeloComportamientoSVG.setChecked(False)
        self.pb_modeloComportamientoSVG.setAutoRepeat(False)
        self.pb_modeloComportamientoSVG.setAutoExclusive(False)
        self.pb_modeloComportamientoSVG.setAutoDefault(False)
        self.pb_modeloComportamientoSVG.setDefault(False)
        self.pb_modeloComportamientoSVG.setFlat(False)
        self.pb_modeloComportamientoSVG.setObjectName("pb_modeloComportamientoSVG")
        self.horizontalLayout_5.addWidget(self.pb_modeloComportamientoSVG)
        self.lb_modeloComportamientoSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloComportamientoSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloComportamientoSVG.setObjectName("lb_modeloComportamientoSVG")
        self.horizontalLayout_5.addWidget(self.lb_modeloComportamientoSVG)
        self.gridLayout.addLayout(self.horizontalLayout_5, 11, 2, 1, 1)
        self.lb_modeloEstructura = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructura.setObjectName("lb_modeloEstructura")
        self.gridLayout.addWidget(self.lb_modeloEstructura, 10, 1, 1, 1)
        self.te_descripcion = QtWidgets.QTextEdit(self.Catalogaciondelpatron_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_descripcion.sizePolicy().hasHeightForWidth())
        self.te_descripcion.setSizePolicy(sizePolicy)
        self.te_descripcion.setObjectName("te_descripcion")
        self.gridLayout.addWidget(self.te_descripcion, 4, 2, 1, 1)
        self.lb_modeloAlcance = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcance.setObjectName("lb_modeloAlcance")
        self.gridLayout.addWidget(self.lb_modeloAlcance, 9, 1, 1, 1)
        self.tb_infoRequisitosDominio = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        self.tb_infoRequisitosDominio.setEnabled(True)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoRequisitosDominio.setIcon(icon)
        self.tb_infoRequisitosDominio.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoRequisitosDominio.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoRequisitosDominio.setAutoRaise(True)
        self.tb_infoRequisitosDominio.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoRequisitosDominio.setObjectName("tb_infoRequisitosDominio")
        self.gridLayout.addWidget(self.tb_infoRequisitosDominio, 8, 0, 1, 1)
        self.pb_patronesRealcionados = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        self.pb_patronesRealcionados.setObjectName("pb_patronesRealcionados")
        self.gridLayout.addWidget(self.pb_patronesRealcionados, 7, 2, 1, 1)
        self.lb_modeloComportamiento = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloComportamiento.setObjectName("lb_modeloComportamiento")
        self.gridLayout.addWidget(self.lb_modeloComportamiento, 11, 1, 1, 1)
        self.lb_nombrePatron = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_nombrePatron.setObjectName("lb_nombrePatron")
        self.gridLayout.addWidget(self.lb_nombrePatron, 0, 1, 1, 1)
        self.lb_requisitosDominioRelacionados = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_requisitosDominioRelacionados.setObjectName("lb_requisitosDominioRelacionados")
        self.gridLayout.addWidget(self.lb_requisitosDominioRelacionados, 8, 1, 1, 1)
        self.tb_infoModeloEstructura = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoModeloEstructura.setIcon(icon)
        self.tb_infoModeloEstructura.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoModeloEstructura.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoModeloEstructura.setAutoRaise(True)
        self.tb_infoModeloEstructura.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoModeloEstructura.setObjectName("tb_infoModeloEstructura")
        self.gridLayout.addWidget(self.tb_infoModeloEstructura, 10, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_modeloEtructuraDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloEtructuraDia.setIcon(icon)
        self.pb_modeloEtructuraDia.setObjectName("pb_modeloEtructuraDia")
        self.horizontalLayout_4.addWidget(self.pb_modeloEtructuraDia)
        self.lb_modeloEstructuraDIA = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructuraDIA.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloEstructuraDIA.setObjectName("lb_modeloEstructuraDIA")
        self.horizontalLayout_4.addWidget(self.lb_modeloEstructuraDIA)
        self.pb_modeloEstructuraSVG = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloEstructuraSVG.setIcon(icon)
        self.pb_modeloEstructuraSVG.setCheckable(False)
        self.pb_modeloEstructuraSVG.setChecked(False)
        self.pb_modeloEstructuraSVG.setAutoRepeat(False)
        self.pb_modeloEstructuraSVG.setAutoExclusive(False)
        self.pb_modeloEstructuraSVG.setAutoDefault(False)
        self.pb_modeloEstructuraSVG.setDefault(False)
        self.pb_modeloEstructuraSVG.setFlat(False)
        self.pb_modeloEstructuraSVG.setObjectName("pb_modeloEstructuraSVG")
        self.horizontalLayout_4.addWidget(self.pb_modeloEstructuraSVG)
        self.lb_modeloEstructuraSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructuraSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloEstructuraSVG.setObjectName("lb_modeloEstructuraSVG")
        self.horizontalLayout_4.addWidget(self.lb_modeloEstructuraSVG)
        self.gridLayout.addLayout(self.horizontalLayout_4, 10, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_modeloAlcanceDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloAlcanceDia.setIcon(icon)
        self.pb_modeloAlcanceDia.setCheckable(False)
        self.pb_modeloAlcanceDia.setChecked(False)
        self.pb_modeloAlcanceDia.setAutoRepeat(False)
        self.pb_modeloAlcanceDia.setAutoExclusive(False)
        self.pb_modeloAlcanceDia.setAutoDefault(False)
        self.pb_modeloAlcanceDia.setDefault(False)
        self.pb_modeloAlcanceDia.setFlat(False)
        self.pb_modeloAlcanceDia.setObjectName("pb_modeloAlcanceDia")
        self.horizontalLayout_2.addWidget(self.pb_modeloAlcanceDia)
        self.lb_modeloAlcanceDia = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcanceDia.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloAlcanceDia.setObjectName("lb_modeloAlcanceDia")
        self.horizontalLayout_2.addWidget(self.lb_modeloAlcanceDia)
        self.pb_modeloAlcanceSVG = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_modeloAlcanceSVG.setIcon(icon)
        self.pb_modeloAlcanceSVG.setObjectName("pb_modeloAlcanceSVG")
        self.horizontalLayout_2.addWidget(self.pb_modeloAlcanceSVG)
        self.lb_modeloAlcanceSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcanceSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloAlcanceSVG.setObjectName("lb_modeloAlcanceSVG")
        self.horizontalLayout_2.addWidget(self.lb_modeloAlcanceSVG)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 2, 1, 1)
        self.pb_guardar = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pb_guardar.setIcon(icon)
        self.pb_guardar.setObjectName("pb_guardar")
        self.gridLayout.addWidget(self.pb_guardar, 12, 2, 1, 1)
        self.pb_cancelar = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_cancelar.setIcon(icon)
        self.pb_cancelar.setFlat(False)
        self.pb_cancelar.setObjectName("pb_cancelar")
        self.gridLayout.addWidget(self.pb_cancelar, 12, 1, 1, 1)
        Catalogaciondelpatron.setCentralWidget(self.Catalogaciondelpatron_2)

        self.optenerRuta()
        self.cargarDominios()

        # Eventos
        self.pb_cancelar.clicked.connect(Catalogaciondelpatron.close)
        self.pb_guardar.clicked.connect(self.guardar)
        self.pb_nuevoDominio.clicked.connect(self.nuevoDominio)
        self.pb_modeloAlcanceDia.clicked.connect(self.cargarModeloAlcance)
        self.pb_modeloEtructuraDia.clicked.connect(self.cargarModeloEstructuras)
        self.pb_modeloComportamientoDia.clicked.connect(self.cargarModeloComportamiento)
        self.pb_modeloAlcanceSVG.clicked.connect(self.cargarModeloAlcance)
        self.pb_modeloEstructuraSVG.clicked.connect(self.cargarModeloEstructuras)
        self.pb_modeloComportamientoSVG.clicked.connect(self.cargarModeloComportamiento)
        self.pb_patronesRealcionados.clicked.connect(self.patronesRelacionados)
        self.pb_usosConocidos.clicked.connect(self.usosConocidos)
        self.pb_requisitosDominiosRelacionados.clicked.connect(self.requisitosDominio)
                
        self.retranslateUi(Catalogaciondelpatron)
        QtCore.QMetaObject.connectSlotsByName(Catalogaciondelpatron)
    
    def optenerRuta(self):
        with open("conf.json", "r") as file:
            data = json.load(file)
            self.file = data["repositorio"]
            
    def cargarDominios(self):
        self.cb_Dominios.clear()
        with open(f"{self.file}/Dominios.json") as file:
            data = file.read()
            data = json.loads(data)
            data = data["Dominios"]
            for dominio in data:
                self.cb_Dominios.addItem(dominio)

                    
        
    def guardar(self):
        try:
            with open("data.json", "r+") as file:
                # Cargar el contenido del archivo JSON
                data = json.load(file)
                
                # Modificar los datos
                data["Nombre"] = self.le_nombre.text()
                data["Dominios"].insert(0, self.cb_Dominios.currentText())
                data["Descripcion"] = self.te_descripcion.toPlainText()
                
                # Volver al inicio del archivo para sobrescribirlo
                file.seek(0)
                
                # Escribir los datos modificados en el archivo
                json.dump(data, file, indent=4)
                
                # Truncar el archivo para asegurarse de que no queden datos antiguos
                file.truncate()
                
                
                self.crearPatron()
                self.guardarModelos()
                self.guardarUsos()
            
                # Volver al inicio del archivo para sobreescribir el contenido

        except FileNotFoundError:
            print("El archivo data.json no se encuentra.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            
    def crearPatron(self):
        try:
            #crear la carpeta del patron
            os.mkdir(f"{self.file}/{self.le_nombre.text()}")
            #crear las carpetas de los modelos
            os.mkdir(f"{self.file}/{self.le_nombre.text()}/diagramas.dia")
            os.mkdir(f"{self.file}/{self.le_nombre.text()}/diagramas.svg")
            #copia el data.json en la carpeta del patron
            print(f"{self.file}/{self.le_nombre.text()}/data.json")
            shutil.copy("data.json", f"{self.file}/{self.le_nombre.text()}/data.json")
            
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
            
            
    def guardarModelos(self):
        try:
            shutil.copy(f"{self.lb_modeloComportamientoDIA.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.dia/modeloComportamiento.dia")
            shutil.copy(f"{self.lb_modeloAlcanceDia.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.dia/modeloAlcance.dia")
            shutil.copy(f"{self.lb_modeloEstructuraDIA.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.dia/modeloEstructura.dia")
            
            shutil.copy(f"{self.lb_modeloComportamientoSVG.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.svg/modeloComportamiento.svg")
            shutil.copy(f"{self.lb_modeloAlcanceSVG.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.svg/modeloAlcance.svg")
            shutil.copy(f"{self.lb_modeloEstructuraSVG.text()}", f"{self.file}/{self.le_nombre.text()}/diagramas.svg/modeloEstructura.svg")
        except Exception as e:
            print(f"Error al guardar los modelos: {e}")
            
    def guardarUsos(self):
        #optener todos los usos de la lista lw_usos
        usos = []
        with open("data.json", "r") as file:
            data = json.load(file)
            usos = data["Usos"]
        with open(f"{self.file}/UsosConocidos.json", "r") as file:
            data = json.load(file)
            bandera = False
            for uso in usos:
                for key in data["Usos"]:
                    if uso == key:
                        bandera = True
                        data["Usos"][key].append(self.le_nombre.text())
                if not bandera:
                    data["Usos"][uso] = [self.le_nombre.text()]
        with open(f"{self.file}/UsosConocidos.json", "w") as file:
            json.dump(data, file)
    
    def nuevoDominio(self):
        self.NuevoDominio = QtWidgets.QDialog()
        self.ui_arbol_patrones = nd()
        self.ui_arbol_patrones.setupUi(self.NuevoDominio)
        self.NuevoDominio.show()
        def on_close_event(event):
            self.cargarDominios()
            event.accept()
        self.NuevoDominio.closeEvent = on_close_event
        
    def cargarModeloComportamiento(self):
        file_name = self.cargarArchivo()
        if file_name:
            #comparar la extencion del archivo
            if ".dia" in file_name:
                self.lb_modeloComportamientoDIA.setText(file_name)
            elif ".svg" in file_name:
                self.lb_modeloComportamientoSVG.setText(file_name)
            else:
                print("Archivo no soportado")

    
    def cargarModeloAlcance(self):
        file_name = self.cargarArchivo()
        if file_name:
            #comparar la extencion del archivo solo se aceptan .dia y .svg
            if ".dia" in file_name:
                self.lb_modeloAlcanceDia.setText(file_name)
            elif ".svg" in file_name:
                self.lb_modeloAlcanceSVG.setText(file_name)
            else:
                print("Archivo no soportado")
    
    def cargarModeloEstructuras(self):
        file_name = self.cargarArchivo()
        if file_name:
            if ".dia" in file_name:
                self.lb_modeloEstructuraDIA.setText(file_name)
            elif ".svg" in file_name:
                self.lb_modeloEstructuraSVG.setText(file_name)
            else:
                print("Archivo no soportado")
    
    def cargarArchivo(self):
        options = QFileDialog.Options()
        options = QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "Cargar Modelo", "", "Todos los Archivos (*);;Archivos de Texto (*.txt);;Archivos CSV (*.csv)", options=options)
        return file_name
    
    def patronesRelacionados(self):
        print("Patrones Relacionados")
        
    def usosConocidos(self):
        self.UsosConocidos = QtWidgets.QDialog()
        self.ui_arbol_patrones = uc()
        self.ui_arbol_patrones.setupUi(self.UsosConocidos)
        self.UsosConocidos.show()
        
    def requisitosDominio(self):
        self.UsosConocidos = QtWidgets.QMainWindow()
        self.ui_arbol_patrones = rd()
        self.ui_arbol_patrones.setupUi(self.UsosConocidos)
        self.UsosConocidos.show()

    def retranslateUi(self, Catalogaciondelpatron):
        _translate = QtCore.QCoreApplication.translate
        Catalogaciondelpatron.setWindowTitle(_translate("Catalogaciondelpatron", "MainWindow"))
        self.pb_usosConocidos.setText(_translate("Catalogaciondelpatron", "Añadir usos conocidos del patron"))
        self.lb_dominio.setText(_translate("Catalogaciondelpatron", "Dominio Principal"))
        self.tb_infoPatronesRelacionados.setText(_translate("Catalogaciondelpatron", "..."))
        self.lb_descripcion.setText(_translate("Catalogaciondelpatron", "Descripción"))
        self.le_nombre.setPlaceholderText(_translate("Catalogaciondelpatron", "Ingrese el nombre"))
        self.lb_patronesRelacionados.setText(_translate("Catalogaciondelpatron", "Patrones Relacionados"))
        self.tb_infoUsosConocidos.setText(_translate("Catalogaciondelpatron", "..."))
        self.tb_infoModeloAlcance.setText(_translate("Catalogaciondelpatron", "..."))
        self.pb_requisitosDominiosRelacionados.setText(_translate("Catalogaciondelpatron", "Añadir requisitos de dominio"))
        self.tb_infoModeloComportamiento.setText(_translate("Catalogaciondelpatron", "..."))
        self.lb_usosConocidos.setText(_translate("Catalogaciondelpatron", "Usos Conocidos"))
        self.pb_modeloComportamientoDia.setText(_translate("Catalogaciondelpatron", "Subir Modelo"))
        self.lb_modeloComportamientoDIA.setText(_translate("Catalogaciondelpatron", "<...>.dia"))
        self.pb_modeloComportamientoSVG.setText(_translate("Catalogaciondelpatron", "Subir Imagen"))
        self.lb_modeloComportamientoSVG.setText(_translate("Catalogaciondelpatron", "<...>.svg"))
        self.lb_modeloEstructura.setText(_translate("Catalogaciondelpatron", "Modelo de Estructura "))
        self.te_descripcion.setPlaceholderText(_translate("Catalogaciondelpatron", "Descripcion que abarque lo mas relevante del patron"))
        self.lb_modeloAlcance.setText(_translate("Catalogaciondelpatron", "Modelo de Alcance"))
        self.tb_infoRequisitosDominio.setText(_translate("Catalogaciondelpatron", "..."))
        self.pb_patronesRealcionados.setText(_translate("Catalogaciondelpatron", "Añadir patrones relacionados"))
        self.lb_modeloComportamiento.setText(_translate("Catalogaciondelpatron", "Modelo de Comportamiento"))
        self.lb_nombrePatron.setText(_translate("Catalogaciondelpatron", "Nombre del Patron"))
        self.lb_requisitosDominioRelacionados.setText(_translate("Catalogaciondelpatron", "Requisitos de Dominio Relacionados"))
        self.tb_infoModeloEstructura.setText(_translate("Catalogaciondelpatron", "..."))
        self.pb_modeloEtructuraDia.setText(_translate("Catalogaciondelpatron", "Subir Modelo"))
        self.lb_modeloEstructuraDIA.setText(_translate("Catalogaciondelpatron", "<...>.dia"))
        self.pb_modeloEstructuraSVG.setText(_translate("Catalogaciondelpatron", "Subir Imagen"))
        self.lb_modeloEstructuraSVG.setText(_translate("Catalogaciondelpatron", "<...>.svg"))
        self.pb_modeloAlcanceDia.setText(_translate("Catalogaciondelpatron", "Subir Modelo"))
        self.lb_modeloAlcanceDia.setText(_translate("Catalogaciondelpatron", "<...>.dia"))
        self.pb_modeloAlcanceSVG.setText(_translate("Catalogaciondelpatron", "Subir Imagen"))
        self.lb_modeloAlcanceSVG.setText(_translate("Catalogaciondelpatron", "<...>.svg"))
        self.pb_guardar.setText(_translate("Catalogaciondelpatron", "Guardar"))
        self.pb_cancelar.setText(_translate("Catalogaciondelpatron", "Cancelar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Catalogaciondelpatron = QtWidgets.QMainWindow()
    ui = Ui_Catalogaciondelpatron()
    ui.setupUi(Catalogaciondelpatron)
    Catalogaciondelpatron.show()
    sys.exit(app.exec_())
