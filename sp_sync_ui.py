# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sp_sync_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SPsync(object):
    def setupUi(self, SPsync):
        if not SPsync.objectName():
            SPsync.setObjectName(u"SPsync")
        SPsync.setEnabled(True)
        SPsync.resize(366, 158)
        self.verticalLayout = QVBoxLayout(SPsync)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.file_path = QLineEdit(SPsync)
        self.file_path.setObjectName(u"file_path")

        self.horizontalLayout.addWidget(self.file_path)

        self.file_select = QPushButton(SPsync)
        self.file_select.setObjectName(u"file_select")

        self.horizontalLayout.addWidget(self.file_select)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.select_preset = QComboBox(SPsync)
        self.select_preset.addItem("")
        self.select_preset.setObjectName(u"select_preset")

        self.verticalLayout_2.addWidget(self.select_preset)

        self.auto_sync = QCheckBox(SPsync)
        self.auto_sync.setObjectName(u"auto_sync")
        self.auto_sync.setChecked(True)

        self.verticalLayout_2.addWidget(self.auto_sync)

        self.sync_button = QPushButton(SPsync)
        self.sync_button.setObjectName(u"sync_button")

        self.verticalLayout_2.addWidget(self.sync_button)

        self.view_sync = QCheckBox(SPsync)
        self.view_sync.setObjectName(u"view_sync")

        self.verticalLayout_2.addWidget(self.view_sync)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(SPsync)

        QMetaObject.connectSlotsByName(SPsync)
    # setupUi

    def retranslateUi(self, SPsync):
        SPsync.setWindowTitle(QCoreApplication.translate("SPsync", u"SPsync", None))
        self.file_select.setText(QCoreApplication.translate("SPsync", u"\u9009\u62e9", None))
        self.select_preset.setItemText(0, QCoreApplication.translate("SPsync", u"\u9ed8\u8ba4(\u5206\u901a\u9053\u8f93\u51fa)", None))

        self.auto_sync.setText(QCoreApplication.translate("SPsync", u"\u8f93\u51fa\u8d34\u56fe\u81ea\u52a8\u540c\u6b65\u5230\u5f15\u64ce", None))
        self.sync_button.setText(QCoreApplication.translate("SPsync", u"SYNC", None))
        self.view_sync.setText(QCoreApplication.translate("SPsync", u"\u89c6\u53e3\u540c\u6b65", None))
    # retranslateUi

