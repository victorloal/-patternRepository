# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Dialog_EditREquirement.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_requisitoDominio = QtWidgets.QLabel(Dialog)
        self.lb_requisitoDominio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_requisitoDominio.setObjectName("lb_requisitoDominio")
        self.verticalLayout.addWidget(self.lb_requisitoDominio)
        self.cb_dominios = QtWidgets.QComboBox(Dialog)
        self.cb_dominios.setObjectName("cb_dominios")
        self.verticalLayout.addWidget(self.cb_dominios)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_delete = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_delete.sizePolicy().hasHeightForWidth())
        self.pb_delete.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("remove")
        self.pb_delete.setIcon(icon)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout_2.addWidget(self.pb_delete)
        self.pb_new = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_new.sizePolicy().hasHeightForWidth())
        self.pb_new.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("add")
        self.pb_new.setIcon(icon)
        self.pb_new.setObjectName("pb_new")
        self.horizontalLayout_2.addWidget(self.pb_new)
        self.pb_edit = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_edit.sizePolicy().hasHeightForWidth())
        self.pb_edit.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("edit")
        self.pb_edit.setIcon(icon)
        self.pb_edit.setObjectName("pb_edit")
        self.horizontalLayout_2.addWidget(self.pb_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lw_requisitos = QtWidgets.QListWidget(Dialog)
        self.lw_requisitos.setObjectName("lw_requisitos")
        self.verticalLayout.addWidget(self.lw_requisitos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_cancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout.addWidget(self.pb_cancel)
        self.pb_save = QtWidgets.QPushButton(Dialog)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout.addWidget(self.pb_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_requisitoDominio.setText(_translate("Dialog", "Requisitos de Dominio"))
        self.pb_delete.setText(_translate("Dialog", "Eliminar"))
        self.pb_new.setText(_translate("Dialog", "Crear"))
        self.pb_edit.setText(_translate("Dialog", "Editar"))
        self.pb_cancel.setText(_translate("Dialog", "Cancelar"))
        self.pb_save.setText(_translate("Dialog", "Guardar Cambios"))
