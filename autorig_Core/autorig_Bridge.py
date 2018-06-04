from Modules.Qt import QtCore
import maya.cmds as cmds
from functools import partial


import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore
reload(Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore)
from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autorig_MainCore import autoRig_mainCore

import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_1 
reload (Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_1)
from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_1 import autoRig_01

class BridgeActions():

    def __init__(self, window_interface):

        #Listado de drivers
        self.lst_drivers = ['DRIVER_CINTURA','DRIVER_ROOT','DRIVER_COLUMNA_BOTTOM','DRIVER_COLUMNA_MIDDLE','DRIVER_COLUMNA_TOP','GRP_DRIVER_CABEZA','DRIVER_CLAVICULA_IZQ',
        'DRIVER_CLAVICULA_DER','DRIVER_MANO_IZQ','DRIVER_MANO_DER','DRIVER_DIENTES_TOP','DRIVER_DIENTES_BOTTOM','DRIVER_BOCA','DRIVER_LENGUA','DRIVER_CODO_IZQ',
        'DRIVER_CODO_DER','DRIVER_RODILLA_DER','DRIVER_RODILLA_IZQ','DRIVER_PIE_DER','DRIVER_PIE_IZQ','DRIVER_PINKY_SEC_IZQ','DRIVER_PINKY_SEC_DER',
        'DRIVER_OJO_IZQ','DRIVER_OJO_DER','DRIVER_HEEL_IZQ','DRIVER_BALL_IZQ','DRIVER_TOE_IZQ','DRIVER_TOE_FINGERS_IZQ','DRIVER_HEEL_DER','DRIVER_BALL_DER',
        'DRIVER_TOE_DER','DRIVER_TOE_FINGERS_DER','DRIVER_HOMBRO_IZQ_FK','DRIVER_CODO_IZQ_FK','DRIVER_MANO_IZQ_FK','DRIVER_HOMBRO_DER_FK','DRIVER_CODO_DER_FK',
        'DRIVER_MANO_DER_FK', 'GRP_DRIVER_CUELLO','GRP_DRIVER_SOMBRERO','GRP_DRIVER_LENTES','DRIVER_BUSTO_IZQ','DRIVER_BUSTO_DER']

        #Lista de grupos dedos
        self.lst_grupos_dedos = ['GRP_DRIVER_THUMB_IZQ_1','GRP_DRIVER_THUMB_IZQ_2','GRP_DRIVER_THUMB_IZQ_3','GRP_DRIVER_INDEX_IZQ_1','GRP_DRIVER_INDEX_IZQ_2','GRP_DRIVER_INDEX_IZQ_3',
        'GRP_DRIVER_MIDDLE_IZQ_1','GRP_DRIVER_MIDDLE_IZQ_2','GRP_DRIVER_MIDDLE_IZQ_3','GRP_DRIVER_CANCEL_IZQ_1','GRP_DRIVER_CANCEL_IZQ_2','GRP_DRIVER_CANCEL_IZQ_3',
        'GRP_DRIVER_PINKY_IZQ_1','GRP_DRIVER_PINKY_IZQ_2','GRP_DRIVER_PINKY_IZQ_3']
        

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


        self.radialHombre = window_interface.rdo_hombre_2
        self.radialMujer = window_interface.rdo_mujer_2

        self.pteUno = autoRig_01(self.radialHombre, self.lst_drivers, self.lst_grupos_dedos)

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

        self.pteUno.principal()

        self.btn_startAutorig.setDisabled(True)

    def autoRig_pte2(self):
        import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2
        reload (Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2)
        from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2 import autoRig_02
        pteDos = autoRig_02(self.lst_drivers, self.lst_grupos_dedos, self.radialHombre)
        pteDos.principal()

        
        import Rigging.Maya_rigging_biped_Autorig.fix_ThumbOrientation as fixThumb
        fixThumb.mainThumbs()

        from Rigging.Maya_rigging_biped_Autorig.Rig_update2_00 import updateRig as UpdateRig
        uRig = UpdateRig()
        uRig.mainClavicle(uRig.clavicleList)
        uRig.mainFingers(uRig.fingers)
        #uRig.mainHeadSquetch()

        
        
        self.btn_finishAutorig.setDisabled(True)

    def facialRig(self):

        import Rigging.Maya_rigging_biped_Autorig.wrapCejas as wrap
        wrap.rename()

        import Rigging.Maya_rigging_biped_Autorig.autorig_Core.RIGG_FACIAL
        reload (Rigging.Maya_rigging_biped_Autorig.autorig_Core.RIGG_FACIAL)
        from Rigging.Maya_rigging_biped_Autorig.autorig_Core.RIGG_FACIAL import facial_class
        pteTres = facial_class()
        pteTres.rigFacial()

        self.btn_facialRig.setDisabled(True)

    def slider(self, argumentirri, value):
        cmds.setAttr(argumentirri + '.rotateX', value)

