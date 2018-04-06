from Modules.Qt import QtCore
import maya.cmds as cmds
from functools import partial


import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore
reload(Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore)
from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore import autoRig_mainCore

class BridgeActions():

    def __init__(self, window_interface):
        self.master_window = window_interface
        self.mainCore = autoRig_mainCore()

        #labels
        self.lbl_falangina = window_interface.lbl_falangina
        self.lbl_falangeta = window_interface.lbl_falangeta
        self.lbl_status = window_interface.lbl_status

        #layout
        self.lyt_horizontal_Advanced_Tab_2 = window_interface.lyt_horizontal_Advanced_Tab_2

        #sliders
        self.slider_falangina = window_interface.slider_falangina
        self.slider_falangeta = window_interface.slider_falangeta
        #btns
        self.btn_importRig = window_interface.btn_importRig
        self.btn_startAutorig = window_interface.btn_startAutorig
        self.btn_finishAutorig = window_interface.btn_finishAutorig
        self.btn_facialRig = window_interface.btn_facialRig
        self.btn_apply = window_interface.btn_apply
        self.btn_reset = window_interface.btn_reset

        #btns connections
        self.btn_importRig.clicked.connect(self.importRig)
        self.btn_reset.clicked.connect(self.resetUI)
        self.btn_startAutorig.clicked.connect(self.autoRig_pte1)
        self.btn_finishAutorig.clicked.connect(self.autoRig_pte2)
        self.btn_facialRig.clicked.connect(self.facialRig)
        '''
        self.btn_apply.clicked.connect(self.test)
        '''

        self.slider_falangina.valueChanged[int].connect(partial(self.slider, 'GRP_DRIVER_THUMB_IZQ_2'))
        self.slider_falangeta.valueChanged[int].connect(partial(self.slider, 'GRP_DRIVER_THUMB_IZQ_3'))




    def resetUI(self):

        self.btn_importRig.setDisabled(False)
        self.btn_startAutorig.setDisabled(False)
        self.btn_finishAutorig.setDisabled(False)
        self.btn_facialRig.setDisabled(False)
        self.btn_apply.setDisabled(False)

        self.lbl_status.setText('Reset UI')

    def importRig(self):
        self.btn_importRig.setDisabled(True)
        self.mainCore.importRig()
        self.lbl_status.setText('Imported Rig')

    def autoRig_pte1(self):
        import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_1 as pteUno
        pteUno.autoRigAnderPte1()

        self.btn_startAutorig.setDisabled(True)

    def autoRig_pte2(self):
        import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2 as pteDos
        pteDos.autoRigAnderPte2()


        
        import Rigging.Maya_rigging_biped_Autorig.fix_ThumbOrientation as fixThumb
        fixThumb.mainThumbs()

        import Rigging.Maya_rigging_biped_Autorig.SCRIPT_CORRECCION_03 as corr
        corr.mainCorrection()

        import Rigging.Maya_rigging_biped_Autorig.updateClavicleSwitch as clav
        clav.spaceSwitchClavicle('DRIVER_HOMBRO_IZQ_FK', 'IZQ')
        clav.spaceSwitchClavicle('DRIVER_HOMBRO_DER_FK', 'DER')

        from Rigging.Maya_rigging_biped_Autorig.Rig_update2_00 import updateRig as UpdateRig
        uRig = UpdateRig()
        uRig.mainWires(uRig.wiresList)
        uRig.mainClavicle(uRig.clavicleList)
        uRig.mainFingers(uRig.fingers)
        uRig.mainHeadSquetch()

        self.btn_finishAutorig.setDisabled(True)

    def facialRig(self):

        import Rigging.Maya_rigging_biped_Autorig.wrapCejas
        import Rigging.Maya_rigging_biped_Autorig.RIGG_FACIAL_03

        self.btn_facialRig.setDisabled(True)

    def slider(self, argumentirri, value):
        cmds.setAttr(argumentirri + '.rotateX', value)

