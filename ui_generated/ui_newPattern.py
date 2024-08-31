# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Catalogaciondelpatron.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from logic.pattern_repository import PatternRepository
from ui_generated.ui_knowUses import Ui_KnowUses
from ui_generated.ui_messageBoxManager import MessageBoxManager
from ui_generated.ui_newDomain import Ui_NewDomain
from ui_generated.ui_associatedRequirements import Ui_AssociatedRequirements


class Ui_NewPattern(object):
    def setupUi(self, NewPattern):
        NewPattern.setObjectName("NewPattern")
        NewPattern.resize(884, 549)
        self.Catalogaciondelpatron_2 = QtWidgets.QWidget(NewPattern)
        self.Catalogaciondelpatron_2.setObjectName("Catalogaciondelpatron_2")
        self.gridLayout = QtWidgets.QGridLayout(self.Catalogaciondelpatron_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_scopeDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_scopeDia.setIcon(icon)
        self.pb_scopeDia.setCheckable(False)
        self.pb_scopeDia.setChecked(False)
        self.pb_scopeDia.setAutoRepeat(False)
        self.pb_scopeDia.setAutoExclusive(False)
        self.pb_scopeDia.setAutoDefault(False)
        self.pb_scopeDia.setDefault(False)
        self.pb_scopeDia.setFlat(False)
        self.pb_scopeDia.setObjectName("pb_scopeDia")
        self.horizontalLayout_2.addWidget(self.pb_scopeDia)
        self.lb_modeloAlcanceDia = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcanceDia.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloAlcanceDia.setObjectName("lb_modeloAlcanceDia")
        self.horizontalLayout_2.addWidget(self.lb_modeloAlcanceDia)
        self.pb_scopeSvg = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_scopeSvg.setIcon(icon)
        self.pb_scopeSvg.setObjectName("pb_scopeSvg")
        self.horizontalLayout_2.addWidget(self.pb_scopeSvg)
        self.lb_modeloAlcanceSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcanceSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloAlcanceSVG.setObjectName("lb_modeloAlcanceSVG")
        self.horizontalLayout_2.addWidget(self.lb_modeloAlcanceSVG)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 2, 1, 1)
        self.le_name = QtWidgets.QLineEdit(self.Catalogaciondelpatron_2)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 0, 2, 1, 1)
        self.tb_infoModeloEstructura = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoModeloEstructura.setIcon(icon)
        self.tb_infoModeloEstructura.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoModeloEstructura.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoModeloEstructura.setAutoRaise(True)
        self.tb_infoModeloEstructura.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoModeloEstructura.setObjectName("tb_infoModeloEstructura")
        self.gridLayout.addWidget(self.tb_infoModeloEstructura, 9, 0, 1, 1)
        self.pb_associatedRequirements = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        self.pb_associatedRequirements.setObjectName("pb_associatedRequirements")
        self.gridLayout.addWidget(self.pb_associatedRequirements, 7, 2, 1, 1)
        self.lb_nombrePatron = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_nombrePatron.setObjectName("lb_nombrePatron")
        self.gridLayout.addWidget(self.lb_nombrePatron, 0, 1, 1, 1)
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
        self.gridLayout.addWidget(self.tb_infoModeloAlcance, 8, 0, 1, 1)
        self.lb_usosConocidos = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_usosConocidos.setObjectName("lb_usosConocidos")
        self.gridLayout.addWidget(self.lb_usosConocidos, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pb_templateDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_templateDia.setIcon(icon)
        self.pb_templateDia.setCheckable(False)
        self.pb_templateDia.setChecked(False)
        self.pb_templateDia.setAutoRepeat(False)
        self.pb_templateDia.setAutoExclusive(False)
        self.pb_templateDia.setAutoDefault(False)
        self.pb_templateDia.setDefault(False)
        self.pb_templateDia.setFlat(False)
        self.pb_templateDia.setObjectName("pb_templateDia")
        self.horizontalLayout_6.addWidget(self.pb_templateDia)
        self.lb_TemplateDIA = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_TemplateDIA.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_TemplateDIA.setObjectName("lb_TemplateDIA")
        self.horizontalLayout_6.addWidget(self.lb_TemplateDIA)
        self.pb_templatesvg = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_templatesvg.setIcon(icon)
        self.pb_templatesvg.setCheckable(False)
        self.pb_templatesvg.setChecked(False)
        self.pb_templatesvg.setAutoRepeat(False)
        self.pb_templatesvg.setAutoExclusive(False)
        self.pb_templatesvg.setAutoDefault(False)
        self.pb_templatesvg.setDefault(False)
        self.pb_templatesvg.setFlat(False)
        self.pb_templatesvg.setObjectName("pb_templatesvg")
        self.horizontalLayout_6.addWidget(self.pb_templatesvg)
        self.lb_ModeloComportamientoSVG_2 = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_ModeloComportamientoSVG_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ModeloComportamientoSVG_2.setObjectName("lb_ModeloComportamientoSVG_2")
        self.horizontalLayout_6.addWidget(self.lb_ModeloComportamientoSVG_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 2, 1, 1)
        self.tb_infoModeloComportamiento = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoModeloComportamiento.setIcon(icon)
        self.tb_infoModeloComportamiento.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoModeloComportamiento.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoModeloComportamiento.setAutoRaise(True)
        self.tb_infoModeloComportamiento.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoModeloComportamiento.setObjectName("tb_infoModeloComportamiento")
        self.gridLayout.addWidget(self.tb_infoModeloComportamiento, 10, 0, 1, 1)
        self.pb_uses = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        self.pb_uses.setObjectName("pb_uses")
        self.gridLayout.addWidget(self.pb_uses, 6, 2, 1, 1)
        self.pb_cancel = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_cancel.setIcon(icon)
        self.pb_cancel.setFlat(False)
        self.pb_cancel.setObjectName("pb_cancel")
        self.gridLayout.addWidget(self.pb_cancel, 12, 1, 1, 1)
        self.lb_modeloEstructura = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructura.setObjectName("lb_modeloEstructura")
        self.gridLayout.addWidget(self.lb_modeloEstructura, 9, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_structurDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_structurDia.setIcon(icon)
        self.pb_structurDia.setObjectName("pb_structurDia")
        self.horizontalLayout_4.addWidget(self.pb_structurDia)
        self.lb_modeloEstructuraDIA = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructuraDIA.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloEstructuraDIA.setObjectName("lb_modeloEstructuraDIA")
        self.horizontalLayout_4.addWidget(self.lb_modeloEstructuraDIA)
        self.pb_structurSvg = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_structurSvg.setIcon(icon)
        self.pb_structurSvg.setCheckable(False)
        self.pb_structurSvg.setChecked(False)
        self.pb_structurSvg.setAutoRepeat(False)
        self.pb_structurSvg.setAutoExclusive(False)
        self.pb_structurSvg.setAutoDefault(False)
        self.pb_structurSvg.setDefault(False)
        self.pb_structurSvg.setFlat(False)
        self.pb_structurSvg.setObjectName("pb_structurSvg")
        self.horizontalLayout_4.addWidget(self.pb_structurSvg)
        self.lb_modeloEstructuraSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloEstructuraSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_modeloEstructuraSVG.setObjectName("lb_modeloEstructuraSVG")
        self.horizontalLayout_4.addWidget(self.lb_modeloEstructuraSVG)
        self.gridLayout.addLayout(self.horizontalLayout_4, 9, 2, 1, 1)
        self.tb_infoRequisitosDominio = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        self.tb_infoRequisitosDominio.setEnabled(True)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoRequisitosDominio.setIcon(icon)
        self.tb_infoRequisitosDominio.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoRequisitosDominio.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoRequisitosDominio.setAutoRaise(True)
        self.tb_infoRequisitosDominio.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoRequisitosDominio.setObjectName("tb_infoRequisitosDominio")
        self.gridLayout.addWidget(self.tb_infoRequisitosDominio, 7, 0, 1, 1)
        self.lb_modeloAlcance = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloAlcance.setObjectName("lb_modeloAlcance")
        self.gridLayout.addWidget(self.lb_modeloAlcance, 8, 1, 1, 1)
        self.te_description = QtWidgets.QTextEdit(self.Catalogaciondelpatron_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_description.sizePolicy().hasHeightForWidth())
        self.te_description.setSizePolicy(sizePolicy)
        self.te_description.setObjectName("te_description")
        self.gridLayout.addWidget(self.te_description, 4, 2, 1, 1)
        self.lb_descripcion = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_descripcion.setObjectName("lb_descripcion")
        self.gridLayout.addWidget(self.lb_descripcion, 4, 1, 1, 1)
        self.lb_dominio = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_dominio.setObjectName("lb_dominio")
        self.gridLayout.addWidget(self.lb_dominio, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_Domain = QtWidgets.QComboBox(self.Catalogaciondelpatron_2)
        self.cb_Domain.setObjectName("cb_Domain")
        self.horizontalLayout.addWidget(self.cb_Domain)
        self.pb_newDomain = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_newDomain.sizePolicy().hasHeightForWidth())
        self.pb_newDomain.setSizePolicy(sizePolicy)
        self.pb_newDomain.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_newDomain.setIcon(icon)
        self.pb_newDomain.setAutoDefault(False)
        self.pb_newDomain.setDefault(False)
        self.pb_newDomain.setFlat(True)
        self.pb_newDomain.setObjectName("pb_newDomain")
        self.horizontalLayout.addWidget(self.pb_newDomain)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.lb_requisitosDominioRelacionados = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_requisitosDominioRelacionados.setObjectName("lb_requisitosDominioRelacionados")
        self.gridLayout.addWidget(self.lb_requisitosDominioRelacionados, 7, 1, 1, 1)
        self.lb_Template = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_Template.setObjectName("lb_Template")
        self.gridLayout.addWidget(self.lb_Template, 11, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_behaviorSvg = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_behaviorSvg.setIcon(icon)
        self.pb_behaviorSvg.setCheckable(False)
        self.pb_behaviorSvg.setChecked(False)
        self.pb_behaviorSvg.setAutoRepeat(False)
        self.pb_behaviorSvg.setAutoExclusive(False)
        self.pb_behaviorSvg.setAutoDefault(False)
        self.pb_behaviorSvg.setDefault(False)
        self.pb_behaviorSvg.setFlat(False)
        self.pb_behaviorSvg.setObjectName("pb_behaviorSvg")
        self.horizontalLayout_5.addWidget(self.pb_behaviorSvg)
        self.lb_ModeloComportamientoDIA = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_ModeloComportamientoDIA.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ModeloComportamientoDIA.setObjectName("lb_ModeloComportamientoDIA")
        self.horizontalLayout_5.addWidget(self.lb_ModeloComportamientoDIA)
        self.pb_behaviorDia = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pb_behaviorDia.setIcon(icon)
        self.pb_behaviorDia.setCheckable(False)
        self.pb_behaviorDia.setChecked(False)
        self.pb_behaviorDia.setAutoRepeat(False)
        self.pb_behaviorDia.setAutoExclusive(False)
        self.pb_behaviorDia.setAutoDefault(False)
        self.pb_behaviorDia.setDefault(False)
        self.pb_behaviorDia.setFlat(False)
        self.pb_behaviorDia.setObjectName("pb_behaviorDia")
        self.horizontalLayout_5.addWidget(self.pb_behaviorDia)
        self.lb_ModeloComportamientoSVG = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_ModeloComportamientoSVG.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ModeloComportamientoSVG.setObjectName("lb_ModeloComportamientoSVG")
        self.horizontalLayout_5.addWidget(self.lb_ModeloComportamientoSVG)
        self.gridLayout.addLayout(self.horizontalLayout_5, 10, 2, 1, 1)
        self.pb_save = QtWidgets.QPushButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pb_save.setIcon(icon)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout.addWidget(self.pb_save, 12, 2, 1, 1)
        self.tb_infoTemplate = QtWidgets.QToolButton(self.Catalogaciondelpatron_2)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.tb_infoTemplate.setIcon(icon)
        self.tb_infoTemplate.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tb_infoTemplate.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_infoTemplate.setAutoRaise(True)
        self.tb_infoTemplate.setArrowType(QtCore.Qt.NoArrow)
        self.tb_infoTemplate.setObjectName("tb_infoTemplate")
        self.gridLayout.addWidget(self.tb_infoTemplate, 11, 0, 1, 1)
        self.lb_modeloComportamiento = QtWidgets.QLabel(self.Catalogaciondelpatron_2)
        self.lb_modeloComportamiento.setObjectName("lb_modeloComportamiento")
        self.gridLayout.addWidget(self.lb_modeloComportamiento, 10, 1, 1, 1)
        NewPattern.setCentralWidget(self.Catalogaciondelpatron_2)

        self.retranslateUi(NewPattern)
        QtCore.QMetaObject.connectSlotsByName(NewPattern)
        
        
        #=================================================================
        self.uses = []
        self.domains = {}
        self.requirements = []
        self.patternsRepository = PatternRepository()
        self.messageManager = MessageBoxManager()
        self.listDomains()
        self.pb_cancel.clicked.connect(NewPattern.close)
        self.pb_newDomain.clicked.connect(self.openNewDomainDialog)
        self.pb_associatedRequirements.clicked.connect(self.openAssociatedRequirementsDialog)
        self.pb_uses.clicked.connect(self.openKnownUsesDialog)
        self.pb_save.clicked.connect(self.save)
        
        self.pb_scopeDia.clicked.connect(lambda: self.uploadModel(self.lb_modeloAlcanceDia,".dia"))
        self.pb_scopeSvg.clicked.connect(lambda: self.uploadModel(self.lb_modeloAlcanceSVG,".svg"))
        self.pb_structurDia.clicked.connect(lambda: self.uploadModel(self.lb_modeloEstructuraDIA,".dia"))
        self.pb_structurSvg.clicked.connect(lambda: self.uploadModel(self.lb_modeloEstructuraSVG,".svg"))
        self.pb_behaviorDia.clicked.connect(lambda: self.uploadModel(self.lb_ModeloComportamientoDIA,".dia"))
        self.pb_behaviorSvg.clicked.connect(lambda: self.uploadModel(self.lb_ModeloComportamientoSVG,".svg"))
        self.pb_templateDia.clicked.connect(lambda: self.uploadModel(self.lb_TemplateDIA,".dia"))
        self.pb_templatesvg.clicked.connect(lambda: self.uploadModel(self.lb_ModeloComportamientoSVG_2,".svg"))
        
    def listDomains(self):
        self.cb_Domain.clear()
        domains = self.patternsRepository.get_domains()
        domain_keys = list(domains["Domains"].keys())

        # Agregar solo si no existe
        for key in domain_keys:
            if key not in [self.cb_Domain.itemText(i) for i in range(self.cb_Domain.count())]:
                self.cb_Domain.addItem(key)
            
    def uploadModel(self, label, tipo_archivo):
        """
        Carga un archivo y actualiza el QLabel especificado con el nombre del archivo.
        
        :param label: QLabel a actualizar.
        :param tipo_archivo: Tipo de archivo aceptado, como ".dia" o ".svg".
        """
        file_name = self.openFileDialog()
        if file_name:
            if file_name.endswith(tipo_archivo):
                label.setText(file_name)
            else:
                self.messageManager.show_critical_message(None, "Error", f"El archivo seleccionado no es un archivo {tipo_archivo}.")

        
    def openFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
            
            
        
    def openKnownUsesDialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = Ui_KnowUses()
            ui.setupUi(dialog)
            ui.retranslateUi(dialog)
            ui.setUses(self.uses)
            dialog.show()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                # Get updated data from the dialog if it was accepted
                self.uses = ui.getUses() 
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")
            
    def openAssociatedRequirementsDialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = Ui_AssociatedRequirements()
            ui.setupUi(dialog)
            ui.retranslateUi(dialog)
            ui.set_result(self.domains, self.requirements)
            dialog.show()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                # Get updated data from the dialog if it was accepted
                self.domains, self.requirements = ui.get_result() 
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")
            
    def openNewDomainDialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = Ui_NewDomain()
            ui.setupUi(dialog)
            ui.retranslateUi(dialog)
            dialog.show()
            dialog.exec_()  # Correctly call exec_() on QDialog instance
        except Exception as e:
            print(f"Error al abrir el diálogo: {e}")

        
        
    def save(self):
        if self.verify():
            data = {}
            data["Name"] = self.le_name.text().lower()
            data["Domains"] = []
            data["Domains"].append(self.cb_Domain.currentText().lower())
            self.domains["1"] = self.cb_Domain.currentText().lower()
            data["Description"] = self.te_description.toPlainText().lower()
            data["RelatedPatterns"] = self.realatedPatterns()
            data["Uses"] = self.uses
            data["Requirements"] = self.requirements
            #eliminar los duplicados   
            self.domains = list(dict.fromkeys(self.domains.values()))
            self.domains.remove(self.cb_Domain.currentText().lower())
            for i in range(len(self.domains)):
                data["Domains"].append(self.domains[i].lower())
            
            print(data)
            image_path = {}
            
            image_path["behaviorModelDia"] = self.lb_ModeloComportamientoDIA.text()
            image_path["scopeModelDia"] = self.lb_modeloAlcanceDia.text()
            image_path["structureModelDia"] = self.lb_modeloEstructuraDIA.text()
            image_path["templateDia"] = self.lb_TemplateDIA.text()
            image_path["behaviorModelSVG"] = self.lb_ModeloComportamientoSVG.text()
            image_path["scopeModelSVG"] = self.lb_modeloAlcanceSVG.text()
            image_path["structureModelSVG"] = self.lb_modeloEstructuraSVG.text()
            image_path["templateSVG"] = self.lb_ModeloComportamientoSVG_2.text()
            
            self.patternsRepository.new_pattern(data, image_path)
            
            #madar a guardar los archivos
    def realatedPatterns(self):
        #obtener los nombres de los patrones relacionados
        result = []
        domains = self.patternsRepository.get_domains()
        for domain in domains["DomainsWithPatterns"].keys():
            if  domain in self.domains.values():
                for pattern in domains["DomainsWithPatterns"][domain]:
                    if pattern not in result:
                        print(pattern)
                        result.append(pattern)
                    
        uses = self.patternsRepository.get_knowUses()
        for use in uses["Uses"]:
            if use in self.uses:
                for pattern in uses["Uses"][use]:
                    if pattern not in result:
                        print(pattern)
                        result.append(pattern)
        
        #eliminar los duplicados
        return result
        
    def verify(self):
        def validate_widget(widget,textWidget, empty_value, style_valid="border: 1px solid green;", style_invalid="border: 1px solid red;"):
            if textWidget == empty_value:
                widget.setStyleSheet(style_invalid)
                return False
            else:
                widget.setStyleSheet(style_valid)
                return True

        vali = True
        # Verificar datos
        vali &= validate_widget(self.le_name,self.le_name.text(), "")
        vali &= validate_widget(self.cb_Domain,self.cb_Domain.currentText(), "Dominio Principal")
        vali &= validate_widget(self.te_description, self.te_description.toPlainText(), "")
        
        # Verificar archivos
        file_checks = [
            (self.lb_modeloAlcanceDia, "<...>.dia"),
            (self.lb_modeloAlcanceSVG, "<...>.svg"),
            (self.lb_modeloEstructuraDIA, "<...>.dia"),
            (self.lb_modeloEstructuraSVG, "<...>.svg"),
            (self.lb_ModeloComportamientoDIA, "<...>.dia"),
            (self.lb_ModeloComportamientoSVG, "<...>.svg"),
            (self.lb_TemplateDIA, "<...>.dia"),
            (self.lb_ModeloComportamientoSVG_2, "<...>.svg")
        ]
        
        for label, empty_value in file_checks:
            vali &= validate_widget(label,label.text(), empty_value)

        return vali
        
    def retranslateUi(self, NewPattern):
        _translate = QtCore.QCoreApplication.translate
        NewPattern.setWindowTitle(_translate("NewPattern", "MainWindow"))
        self.pb_scopeDia.setText(_translate("NewPattern", "Subir Modelo"))
        self.lb_modeloAlcanceDia.setText(_translate("NewPattern", "<...>.dia"))
        self.pb_scopeSvg.setText(_translate("NewPattern", "Subir Imagen"))
        self.lb_modeloAlcanceSVG.setText(_translate("NewPattern", "<...>.svg"))
        self.le_name.setPlaceholderText(_translate("NewPattern", "Ingrese el nombre"))
        self.tb_infoModeloEstructura.setText(_translate("NewPattern", "..."))
        self.pb_associatedRequirements.setText(_translate("NewPattern", "Añadir requisitos de dominio"))
        self.lb_nombrePatron.setText(_translate("NewPattern", "Nombre del Patron"))
        self.tb_infoUsosConocidos.setText(_translate("NewPattern", "..."))
        self.tb_infoModeloAlcance.setText(_translate("NewPattern", "..."))
        self.lb_usosConocidos.setText(_translate("NewPattern", "Usos Conocidos"))
        self.pb_templateDia.setText(_translate("NewPattern", "Subir Modelo"))
        self.lb_TemplateDIA.setText(_translate("NewPattern", "<...>.dia"))
        self.pb_templatesvg.setText(_translate("NewPattern", "Subir Imagen"))
        self.lb_ModeloComportamientoSVG_2.setText(_translate("NewPattern", "<...>.svg"))
        self.tb_infoModeloComportamiento.setText(_translate("NewPattern", "..."))
        self.pb_uses.setText(_translate("NewPattern", "Añadir usos conocidos del patron"))
        self.pb_cancel.setText(_translate("NewPattern", "Cancelar"))
        self.lb_modeloEstructura.setText(_translate("NewPattern", "Modelo de Estructura "))
        self.pb_structurDia.setText(_translate("NewPattern", "Subir Modelo"))
        self.lb_modeloEstructuraDIA.setText(_translate("NewPattern", "<...>.dia"))
        self.pb_structurSvg.setText(_translate("NewPattern", "Subir Imagen"))
        self.lb_modeloEstructuraSVG.setText(_translate("NewPattern", "<...>.svg"))
        self.tb_infoRequisitosDominio.setText(_translate("NewPattern", "..."))
        self.lb_modeloAlcance.setText(_translate("NewPattern", "Modelo de Alcance"))
        self.te_description.setHtml(_translate("NewPattern", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_description.setPlaceholderText(_translate("NewPattern", "Descripcion que abarque lo mas relevante del patron"))
        self.lb_descripcion.setText(_translate("NewPattern", "Descripción"))
        self.lb_dominio.setText(_translate("NewPattern", "Dominio Principal"))
        self.lb_requisitosDominioRelacionados.setText(_translate("NewPattern", "Requisitos de Dominio Relacionados"))
        self.lb_Template.setText(_translate("NewPattern", "Template"))
        self.pb_behaviorSvg.setText(_translate("NewPattern", "Subir Modelo"))
        self.lb_ModeloComportamientoDIA.setText(_translate("NewPattern", "<...>.dia"))
        self.pb_behaviorDia.setText(_translate("NewPattern", "Subir Imagen"))
        self.lb_ModeloComportamientoSVG.setText(_translate("NewPattern", "<...>.svg"))
        self.pb_save.setText(_translate("NewPattern", "Guardar"))
        self.tb_infoTemplate.setText(_translate("NewPattern", "..."))
        self.lb_modeloComportamiento.setText(_translate("NewPattern", "Modelo de Comportamiento"))
