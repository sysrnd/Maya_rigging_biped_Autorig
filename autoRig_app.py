"""
StandAlone pyqt4

"""
import sys
import platform
from Modules.Qt  import QtCore, QtGui, QtWidgets

import Rigging.Maya_rigging_biped_Autorig.autorig_UI.autorig_Window_qt5
reload(Rigging.Maya_rigging_biped_Autorig.autorig_UI.autorig_Window_qt5)
from Rigging.Maya_rigging_biped_Autorig.autorig_UI.autorig_Window_qt5 import Ui_AutoRig_window

import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_Bridge
reload(Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_Bridge)
from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_Bridge import BridgeActions
#Por ventana que hayas disenado


class MyApplication(QtWidgets.QMainWindow, Ui_AutoRig_window):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
	
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()
	window = MyApplication()
	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	interfaceMacho = BridgeActions(window_interface=window)
	window.show()

	try:
		sys.exit(app.exec_())
	except:
		"error al intentar salir"


