# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../interfaces/Vista Previa del patron.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from interfacesPy.instanciacion import Instanciacion



class Ui_VistaPrevia(object):
    def setupUi(self, VistaPrevia,ruta):
        self.VistaPrevia = VistaPrevia
        VistaPrevia.setObjectName("VistaPrevia")
        VistaPrevia.resize(768, 517)
        self.centralwidget = QtWidgets.QWidget(VistaPrevia)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_template = QtWidgets.QLabel(self.tab)
        self.lb_template.setText("")
        self.lb_template.setObjectName("lb_template")
        self.horizontalLayout_2.addWidget(self.lb_template)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_vistaAlcance = QtWidgets.QLabel(self.tab_2)
        self.lb_vistaAlcance.setText("")
        self.lb_vistaAlcance.setObjectName("lb_vistaAlcance")
        self.horizontalLayout_3.addWidget(self.lb_vistaAlcance)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_vistaEstructura = QtWidgets.QLabel(self.tab_3)
        self.lb_vistaEstructura.setText("")
        self.lb_vistaEstructura.setObjectName("lb_vistaEstructura")
        self.horizontalLayout_4.addWidget(self.lb_vistaEstructura)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_vistaComportamiento = QtWidgets.QLabel(self.tab_4)
        self.lb_vistaComportamiento.setText("")
        self.lb_vistaComportamiento.setObjectName("lb_vistaComportamiento")
        self.horizontalLayout_5.addWidget(self.lb_vistaComportamiento)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_aceptar.setObjectName("pb_aceptar")
        self.horizontalLayout.addWidget(self.pb_aceptar)
        self.pb_instaciarPatron = QtWidgets.QPushButton(self.centralwidget)
        self.pb_instaciarPatron.setObjectName("pb_instaciarPatron")
        self.horizontalLayout.addWidget(self.pb_instaciarPatron)
        self.verticalLayout.addLayout(self.horizontalLayout)
        VistaPrevia.setCentralWidget(self.centralwidget)
        
        self.svg_paths = {
            self.lb_template: f"{ruta}/diagramas.svg/template.svg",
            self.lb_vistaAlcance: f"{ruta}/diagramas.svg/modeloAlcance.svg",
            self.lb_vistaEstructura: f"{ruta}/diagramas.svg/modeloEstructura.svg",
            self.lb_vistaComportamiento: f"{ruta}/diagramas.svg/modeloComportamiento.svg"
        }
        
        self.mostrarModelo(ruta)
        
        self.retranslateUi(VistaPrevia)
        
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(VistaPrevia)
        
        
        self.pb_instaciarPatron.clicked.connect(self.on_instanciar_patron)
        
    def on_instanciar_patron(self):
        #ver en que label esta visible
        if self.lb_template.isVisible():
            
            svg_path = self.lb_template
            print("Template")
        elif self.lb_vistaAlcance.isVisible():
            print("Alcance")
            svg_path = self.svg_paths[self.lb_vistaAlcance]
        elif self.lb_vistaEstructura.isVisible():
            svg_path = self.svg_paths[self.lb_vistaEstructura]
            print("Estructura")
        elif self.lb_vistaComportamiento.isVisible():
            svg_path = self.svg_paths[self.lb_vistaComportamiento]
            print("Comportamiento")
            
        
        
        if not os.path.exists(svg_path):
            print("Error: SVG file does not exist at the specified path.")
            return

        svg_content = self.load_svg_from_file(svg_path)

        # Ensure that 'self' is a QMainWindow instance when passed as the parent
        dialog = Instanciacion(svg_content, self.VistaPrevia)  # Pass the main window instance here
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            modified_svg_content = dialog.modified_svg_content
            print("Modified SVG Content:")
            print(modified_svg_content)

    def load_svg_from_file(self, file_path):
        # Open the SVG file and read its content.
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
        
    def mostrarModelo(self, ruta):
        # Define las rutas a los archivos SVG
        ruta_Template = f"{ruta}/diagramas.svg/template.svg"
        ruta_Alcance = f"{ruta}/diagramas.svg/modeloAlcance.svg"
        ruta_Comportamiento = f"{ruta}/diagramas.svg/modeloComportamiento.svg"
        ruta_Estructura = f"{ruta}/diagramas.svg/modeloEstructura.svg"
        
        # Crea un QPixmap para cada SVG
        pixmap_Alcance = QtGui.QPixmap(768, 517)
        pixmap_Alcance.fill(QtGui.QColor(0, 0, 0, 0))
        pixmap_Template = QtGui.QPixmap(768, 517)
        pixmap_Template.fill(QtGui.QColor(0, 0, 0, 0))
        pixmap_Comportamiento = QtGui.QPixmap(768, 517)
        pixmap_Comportamiento.fill(QtGui.QColor(0, 0, 0, 0))
        pixmap_Estructura = QtGui.QPixmap(768, 517)
        pixmap_Estructura.fill(QtGui.QColor(0, 0, 0, 0))
        
        # Crea un QPainter para cada QPixmap
        painter_Alcance = QtGui.QPainter(pixmap_Alcance)
        painter_Template = QtGui.QPainter(pixmap_Template)
        painter_Comportamiento = QtGui.QPainter(pixmap_Comportamiento)
        painter_Estructura = QtGui.QPainter(pixmap_Estructura)
        
        # Renderiza cada SVG en su respectivo QPixmap
        svg_Alcance = QtSvg.QSvgRenderer(ruta_Alcance)
        svg_Template = QtSvg.QSvgRenderer(ruta_Template)
        svg_Comportamiento = QtSvg.QSvgRenderer(ruta_Comportamiento)
        svg_Estructura = QtSvg.QSvgRenderer(ruta_Estructura)
        
        svg_Alcance.render(painter_Alcance)
        svg_Template.render(painter_Template)
        svg_Comportamiento.render(painter_Comportamiento)
        svg_Estructura.render(painter_Estructura)
        
        # Termina el pintado en cada QPixmap
        painter_Alcance.end()
        painter_Template.end()
        painter_Comportamiento.end()
        painter_Estructura.end()
        
        # Configura los QLabel para mostrar cada imagen
        self.lb_vistaAlcance.setPixmap(pixmap_Alcance)
        self.lb_vistaAlcance.show()
        self.lb_template.setPixmap(pixmap_Template)
        self.lb_template.show()
        self.lb_vistaComportamiento.setPixmap(pixmap_Comportamiento)
        self.lb_vistaComportamiento.show()
        self.lb_vistaEstructura.setPixmap(pixmap_Estructura)
        self.lb_vistaEstructura.show()
        
    
    def retranslateUi(self, VistaPrevia):
        _translate = QtCore.QCoreApplication.translate
        VistaPrevia.setWindowTitle(_translate("VistaPrevia", "Vista Previa del patron"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VistaPrevia", "Template"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VistaPrevia", "Vista de Alcance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VistaPrevia", "Vista de Estructura"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("VistaPrevia", "Vista de Comportamiento"))
        self.pb_aceptar.setText(_translate("VistaPrevia", "Aceptar"))
        self.pb_instaciarPatron.setText(_translate("VistaPrevia", "Instanciar Patron"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VistaPrevia = QtWidgets.QMainWindow()
    ui = Ui_VistaPrevia()
    ui.setupUi(VistaPrevia)
    VistaPrevia.show()
    sys.exit(app.exec_())
