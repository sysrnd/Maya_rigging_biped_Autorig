# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUSarturo/Desktop/RnD/MKF/Rigging/Maya_rigging_biped_Autorig/UI/Resources/autorig_Window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AutoRig_window(object):
    def setupUi(self, AutoRig_window):
        AutoRig_window.setObjectName(_fromUtf8("AutoRig_window"))
        AutoRig_window.setEnabled(True)
        AutoRig_window.resize(348, 305)
        AutoRig_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtGui.QWidget(AutoRig_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_tabs = QtGui.QTabWidget(self.centralwidget)
        self.widget_tabs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget_tabs.setAutoFillBackground(False)
        self.widget_tabs.setStyleSheet(_fromUtf8(""))
        self.widget_tabs.setObjectName(_fromUtf8("widget_tabs"))
        self.lyt_horizontal_Basic_tab = QtGui.QWidget()
        self.lyt_horizontal_Basic_tab.setObjectName(_fromUtf8("lyt_horizontal_Basic_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.lyt_horizontal_Basic_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lyt_vertical_basicTab = QtGui.QVBoxLayout()
        self.lyt_vertical_basicTab.setContentsMargins(10, 0, 10, -1)
        self.lyt_vertical_basicTab.setObjectName(_fromUtf8("lyt_vertical_basicTab"))
        self.btn_importRig = QtGui.QPushButton(self.lyt_horizontal_Basic_tab)
        self.btn_importRig.setObjectName(_fromUtf8("btn_importRig"))
        self.lyt_vertical_basicTab.addWidget(self.btn_importRig)
        self.btn_startAutorig = QtGui.QPushButton(self.lyt_horizontal_Basic_tab)
        self.btn_startAutorig.setObjectName(_fromUtf8("btn_startAutorig"))
        self.lyt_vertical_basicTab.addWidget(self.btn_startAutorig)
        spacerItem = QtGui.QSpacerItem(13, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.lyt_vertical_basicTab.addItem(spacerItem)
        self.lyt_horizontal_falangina = QtGui.QHBoxLayout()
        self.lyt_horizontal_falangina.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.lyt_horizontal_falangina.setSpacing(0)
        self.lyt_horizontal_falangina.setObjectName(_fromUtf8("lyt_horizontal_falangina"))
        self.lbl_falangina = QtGui.QLabel(self.lyt_horizontal_Basic_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_falangina.sizePolicy().hasHeightForWidth())
        self.lbl_falangina.setSizePolicy(sizePolicy)
        self.lbl_falangina.setObjectName(_fromUtf8("lbl_falangina"))
        self.lyt_horizontal_falangina.addWidget(self.lbl_falangina)
        self.slider_falangina = QtGui.QSlider(self.lyt_horizontal_Basic_tab)
        self.slider_falangina.setAutoFillBackground(False)
        self.slider_falangina.setMinimum(-180)
        self.slider_falangina.setMaximum(180)
        self.slider_falangina.setPageStep(20)
        self.slider_falangina.setOrientation(QtCore.Qt.Horizontal)
        self.slider_falangina.setInvertedControls(False)
        self.slider_falangina.setTickPosition(QtGui.QSlider.NoTicks)
        self.slider_falangina.setTickInterval(1)
        self.slider_falangina.setObjectName(_fromUtf8("slider_falangina"))
        self.lyt_horizontal_falangina.addWidget(self.slider_falangina)
        self.lbl_falangina_int = QtGui.QLabel(self.lyt_horizontal_Basic_tab)
        self.lbl_falangina_int.setMinimumSize(QtCore.QSize(25, 20))
        self.lbl_falangina_int.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbl_falangina_int.setFont(font)
        self.lbl_falangina_int.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_falangina_int.setObjectName(_fromUtf8("lbl_falangina_int"))
        self.lyt_horizontal_falangina.addWidget(self.lbl_falangina_int)
        self.lyt_vertical_basicTab.addLayout(self.lyt_horizontal_falangina)
        self.lyt_horizontal_falangeta = QtGui.QHBoxLayout()
        self.lyt_horizontal_falangeta.setSpacing(0)
        self.lyt_horizontal_falangeta.setObjectName(_fromUtf8("lyt_horizontal_falangeta"))
        self.lbl_falangeta = QtGui.QLabel(self.lyt_horizontal_Basic_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_falangeta.sizePolicy().hasHeightForWidth())
        self.lbl_falangeta.setSizePolicy(sizePolicy)
        self.lbl_falangeta.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbl_falangeta.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbl_falangeta.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_falangeta.setScaledContents(False)
        self.lbl_falangeta.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_falangeta.setObjectName(_fromUtf8("lbl_falangeta"))
        self.lyt_horizontal_falangeta.addWidget(self.lbl_falangeta)
        self.slider_falangeta = QtGui.QSlider(self.lyt_horizontal_Basic_tab)
        self.slider_falangeta.setMinimum(-180)
        self.slider_falangeta.setMaximum(180)
        self.slider_falangeta.setPageStep(20)
        self.slider_falangeta.setOrientation(QtCore.Qt.Horizontal)
        self.slider_falangeta.setObjectName(_fromUtf8("slider_falangeta"))
        self.lyt_horizontal_falangeta.addWidget(self.slider_falangeta)
        self.lbl_falangeta_int = QtGui.QLabel(self.lyt_horizontal_Basic_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_falangeta_int.sizePolicy().hasHeightForWidth())
        self.lbl_falangeta_int.setSizePolicy(sizePolicy)
        self.lbl_falangeta_int.setMinimumSize(QtCore.QSize(25, 20))
        self.lbl_falangeta_int.setMaximumSize(QtCore.QSize(20, 20))
        self.lbl_falangeta_int.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_falangeta_int.setObjectName(_fromUtf8("lbl_falangeta_int"))
        self.lyt_horizontal_falangeta.addWidget(self.lbl_falangeta_int)
        self.lyt_vertical_basicTab.addLayout(self.lyt_horizontal_falangeta)
        spacerItem1 = QtGui.QSpacerItem(16, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.lyt_vertical_basicTab.addItem(spacerItem1)
        self.btn_finishAutorig = QtGui.QPushButton(self.lyt_horizontal_Basic_tab)
        self.btn_finishAutorig.setObjectName(_fromUtf8("btn_finishAutorig"))
        self.lyt_vertical_basicTab.addWidget(self.btn_finishAutorig)
        self.btn_facialRig = QtGui.QPushButton(self.lyt_horizontal_Basic_tab)
        self.btn_facialRig.setObjectName(_fromUtf8("btn_facialRig"))
        self.lyt_vertical_basicTab.addWidget(self.btn_facialRig)
        self.verticalLayout_2.addLayout(self.lyt_vertical_basicTab)
        self.widget_tabs.addTab(self.lyt_horizontal_Basic_tab, _fromUtf8(""))
        self.lyt_horizontal_Advanced_Tab = QtGui.QWidget()
        self.lyt_horizontal_Advanced_Tab.setObjectName(_fromUtf8("lyt_horizontal_Advanced_Tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.lyt_horizontal_Advanced_Tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lyt_horizontal_Advanced_Tab_2 = QtGui.QVBoxLayout()
        self.lyt_horizontal_Advanced_Tab_2.setObjectName(_fromUtf8("lyt_horizontal_Advanced_Tab_2"))
        self.Apply = QtGui.QPushButton(self.lyt_horizontal_Advanced_Tab)
        self.Apply.setObjectName(_fromUtf8("Apply"))
        self.lyt_horizontal_Advanced_Tab_2.addWidget(self.Apply)
        self.verticalLayout_4.addLayout(self.lyt_horizontal_Advanced_Tab_2)
        self.widget_tabs.addTab(self.lyt_horizontal_Advanced_Tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.widget_tabs)
        self.lbl_status = QtGui.QLabel(self.centralwidget)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.verticalLayout.addWidget(self.lbl_status)
        AutoRig_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AutoRig_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        AutoRig_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AutoRig_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AutoRig_window.setStatusBar(self.statusbar)

        self.retranslateUi(AutoRig_window)
        self.widget_tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.slider_falangeta, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_falangeta_int.setNum)
        QtCore.QObject.connect(self.slider_falangina, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_falangina_int.setNum)
        QtCore.QMetaObject.connectSlotsByName(AutoRig_window)

    def retranslateUi(self, AutoRig_window):
        AutoRig_window.setWindowTitle(_translate("AutoRig_window", "MKF - AutoRig", None))
        self.btn_importRig.setText(_translate("AutoRig_window", "Import Rig", None))
        self.btn_startAutorig.setText(_translate("AutoRig_window", "Start Autorig", None))
        self.lbl_falangina.setText(_translate("AutoRig_window", "Falangina  ", None))
        self.lbl_falangina_int.setText(_translate("AutoRig_window", "0", None))
        self.lbl_falangeta.setText(_translate("AutoRig_window", "Falangeta  ", None))
        self.lbl_falangeta_int.setText(_translate("AutoRig_window", "0", None))
        self.btn_finishAutorig.setText(_translate("AutoRig_window", "Finish Autorig", None))
        self.btn_facialRig.setText(_translate("AutoRig_window", "Facial Rig", None))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.lyt_horizontal_Basic_tab), _translate("AutoRig_window", "Basic", None))
        self.Apply.setText(_translate("AutoRig_window", "Apply", None))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.lyt_horizontal_Advanced_Tab), _translate("AutoRig_window", "Advanced", None))
        self.lbl_status.setText(_translate("AutoRig_window", "//", None))

