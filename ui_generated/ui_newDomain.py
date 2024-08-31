from PyQt5 import QtCore, QtGui, QtWidgets
from logic.pattern_repository import PatternRepository

class Ui_NewDomain(object):
    def setupUi(self, NewDomain):
        self.NewDomain = NewDomain
        NewDomain.setObjectName("NewDomain")
        NewDomain.resize(422, 334)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewDomain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lb_nuevoDominio = QtWidgets.QLabel(NewDomain)
        self.lb_nuevoDominio.setObjectName("lb_nuevoDominio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_nuevoDominio)
        self.le_nameDomain = QtWidgets.QLineEdit(NewDomain)
        self.le_nameDomain.setObjectName("le_nameDomain")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_nameDomain)
        self.verticalLayout.addLayout(self.formLayout)
        self.lb_requisitos = QtWidgets.QLabel(NewDomain)
        self.lb_requisitos.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitos.setObjectName("lb_requisitos")
        self.verticalLayout.addWidget(self.lb_requisitos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_requirements = QtWidgets.QComboBox(NewDomain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_requirements.sizePolicy().hasHeightForWidth())
        self.cb_requirements.setSizePolicy(sizePolicy)
        self.cb_requirements.setEditable(True)
        self.cb_requirements.setDuplicatesEnabled(False)
        self.cb_requirements.setFrame(True)
        self.cb_requirements.setObjectName("cb_requirements")
        self.horizontalLayout.addWidget(self.cb_requirements)
        self.pb_add = QtWidgets.QPushButton(NewDomain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pb_add.setIcon(icon)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lw_requirements = QtWidgets.QListWidget(NewDomain)
        self.lw_requirements.setObjectName("lw_requirements")
        self.verticalLayout.addWidget(self.lw_requirements)
        self.pb_deleteRequirements = QtWidgets.QPushButton(NewDomain)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pb_deleteRequirements.setIcon(icon)
        self.pb_deleteRequirements.setObjectName("pb_deleteRequirements")
        self.verticalLayout.addWidget(self.pb_deleteRequirements)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_cancel = QtWidgets.QPushButton(NewDomain)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.pb_cancel.setIcon(icon)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_save = QtWidgets.QPushButton(NewDomain)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pb_save.setIcon(icon)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout_2.addWidget(self.pb_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(NewDomain)
        QtCore.QMetaObject.connectSlotsByName(NewDomain)
        self.patternRepository = PatternRepository()
        
        # ================== Eventos ==================
        self.listRequirements()
        self.pb_add.clicked.connect(self.add_requirement)
        self.pb_deleteRequirements.clicked.connect(self.delete_requirement)
        self.pb_cancel.clicked.connect(NewDomain.close)  # Corrected
        self.pb_save.clicked.connect(self.save)  # Corrected
    
    def add_requirement(self):
        self.lw_requirements.addItem(self.cb_requirements.currentText())
        
    def delete_requirement(self):
        self.lw_requirements.takeItem(self.lw_requirements.currentRow())
        
    def listRequirements(self):
        self.cb_requirements.clear()
        requirements = self.patternRepository.get_requirements()
        self.cb_requirements.addItems(requirements)  # Uncommented

    def save(self):
        if self.verify():
            domainName = self.le_nameDomain.text()
            requirements = [self.lw_requirements.item(i).text() for i in range(self.lw_requirements.count())]
            
            self.patternRepository.add_domain(domainName,requirements)
            #cerrar el dialogo
            self.pb_cancel.click() 
        
    def verify(self):
        def validate_widget(widget, textWidget, empty_value, style_valid="border: 1px solid green;", style_invalid="border: 1px solid red;"):
            if textWidget == empty_value:
                widget.setStyleSheet(style_invalid)
                return False
            else:
                widget.setStyleSheet(style_valid)
                return True

        vali = True
        # Verificar datos
        domains = self.patternRepository.get_domains()
        print(self.le_nameDomain.text() in domains["Domains"].keys())
        if self.le_nameDomain.text() in domains["Domains"].keys():
            self.le_nameDomain.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.le_nameDomain.setStyleSheet("border: 1px solid green;")
            vali &= validate_widget(self.le_nameDomain, self.le_nameDomain.text(), "")
        if self.lw_requirements.count() == 0:
            self.lw_requirements.setStyleSheet("border: 1px solid red;")
            vali = False
        else:
            self.lw_requirements.setStyleSheet("border: 1px solid green;")

        return vali
    
    def retranslateUi(self, NewDomain):
        _translate = QtCore.QCoreApplication.translate
        NewDomain.setWindowTitle(_translate("NewDomain", "Dialog"))
        self.lb_nuevoDominio.setText(_translate("NewDomain", "Nuevo Dominio"))
        self.lb_requisitos.setText(_translate("NewDomain", "Requisitos"))
        self.cb_requirements.setCurrentText(_translate("NewDomain", "Nuevo Requisito"))
        self.cb_requirements.setPlaceholderText(_translate("NewDomain", "Nuevo requisito"))
        self.pb_add.setText(_translate("NewDomain", "Adicionar"))
        self.pb_deleteRequirements.setText(_translate("NewDomain", "Eliminar Requisito"))
        self.pb_cancel.setText(_translate("NewDomain", "Cancelar"))
        self.pb_save.setText(_translate("NewDomain", "Guardar"))
