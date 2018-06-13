import maya.cmds as cmds
from copy import deepcopy

class facial_class():
	def __init__(self):
		self.temp = 0
		
	def rigFacial(self):

		import Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2
		reload (Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2)
		from Rigging.Maya_rigging_biped_Autorig.autorig_Core.autoRig_pte_2 import autoRig_02
		pteDos = autoRig_02('nada', 'nada', 'nada')

		for geo in cmds.ls(et='mesh'):
		    if geo.find('CEJAS') != -1:
		        if geo.find('_MD') != -1:
		            cejas = cmds.listRelatives(geo, p=True)[0]

		cabeza=''
		for geo in cmds.ls(et='mesh'):
		    if geo.find('CABEZA') != -1:
		        if geo.find('_MD') != -1:
		            cabeza = cmds.listRelatives(geo, p=True)[0]
		           

		#CREAR CLUSTERS CURVAS(COMIENZA)
		cmds.group(em=True, n='GRP_DEFORMS_CURVS')
		
		lst_clr_curv_der=self.cluster_curvs(cv=12, id_curv='DEFORM_CURV_DER', name_clr='CLR_CURV_OJO_DER')
		lst_clr_parpado_der=self.cluster_curvs(cv=8, id_curv='DEFORM_CURV_PARPADO_DER', name_clr='CLR_CURV_PARPADO_DER')
		lst_clr_nariz=self.cluster_curvs(cv=3, id_curv='DEFORM_CURV_NARIZ', name_clr='CLR_CURV_NARIZ')
		lst_clr_boca_sup=self.cluster_curvs(cv=5, id_curv='DEFORM_CURV_BOCA_SUP', name_clr='CLR_CURV_BOCA_SUP')
		lst_clr_boca_inf=self.cluster_curvs(cv=5, id_curv='DEFORM_CURV_BOCA_INF', name_clr='CLR_CURV_BOCA_INF')
		lst_clr_oreja_der=self.cluster_curvs(cv=5, id_curv='DEFORM_CURV_OREJA_DER', name_clr='CLR_CURV_OREJA_DER')

		#CREACION DE LOCATOR NARIZ, RECOLOCACION DE PIVOTE CLUSTER Y DUPLICADOS DE LAS CURVAS DER A IZQ (COMEINZA)
		cmds.select( 'DEFORM_CURV_NARIZ.cv[0]', 'DEFORM_CURV_NARIZ.cv[2]', visible=True )
		cmds.cluster( rel=True, name = 'CLR_CURV_NARIZ_TEMP' )

		cmds.spaceLocator(n='LOC_NARIZ')
		cmds.pointConstraint( 'CLR_CURV_NARIZ_TEMPHandle', 'LOC_NARIZ' )

		PZ = cmds.getAttr('LOC_NARIZ.tz' )
		PY = cmds.getAttr('LOC_NARIZ.ty' )
		PX = cmds.getAttr('LOC_NARIZ.tx' )

		cmds.move(PX, PY, PZ, "CLR_CURV_NARIZ_1Handle.scalePivot","CLR_CURV_NARIZ_1Handle.rotatePivot", absolute=True)

		cmds.delete('LOC_NARIZ_pointConstraint1')
		cmds.pointConstraint( 'WIRE_BS', 'LOC_NARIZ' )

		self.mirror_curvs(info_position= 'LOC_NARIZ', obj_duplicate= 'DEFORM_CURV_DER', name_duplicate='DEFORM_CURV_IZQ')
		self.mirror_curvs(info_position= 'LOC_NARIZ', obj_duplicate= 'DEFORM_CURV_OREJA_DER', name_duplicate='DEFORM_CURV_OREJA_IZQ')
		self.mirror_curvs(info_position= 'LOC_NARIZ', obj_duplicate= 'DEFORM_CURV_PARPADO_DER', name_duplicate='DEFORM_CURV_PARPADO_IZQ')

		cmds.delete('CLR_CURV_NARIZ_TEMPHandle', 'LOC_NARIZ')

		#CREAR CLUSTERS IZQUIERDOS(COMIENZA)
		lst_clr_curv_izq=self.cluster_curvs(cv=12, id_curv='DEFORM_CURV_IZQ', name_clr='CLR_CURV_OJO_IZQ')
		lst_clr_parpado_izq=self.cluster_curvs(cv=8, id_curv='DEFORM_CURV_PARPADO_IZQ', name_clr='CLR_CURV_PARPADO_IZQ')
		lst_clr_oreja_izq=self.cluster_curvs(cv=5, id_curv='DEFORM_CURV_OREJA_IZQ', name_clr='CLR_CURV_OREJA_IZQ')

		lsts_clr_wire = {
			'curv_der': lst_clr_curv_der,
			'parpado_der': lst_clr_parpado_der,
			'clr_nariz': lst_clr_nariz,
			'boca_sup': lst_clr_boca_sup,
			'boca_inf': lst_clr_boca_inf,
			'oreja_der': lst_clr_oreja_der,
			'curv_izq': lst_clr_curv_izq,
			'parpado_izq': lst_clr_parpado_izq,
			'oreja_izq': lst_clr_oreja_izq
		}


		#CONECTAR CLUSTERS A DRIVER(COMIENZA)
		lista_01 = ['CEJA_IZQ_01.translate','CEJA_IZQ_02.translate','CEJA_IZQ_03.translate','CEJA_IZQ_04.translate','CEJA_IZQ_05.translate','CEJA_IZQ_06.translate','POMULO_IZQ_05.translate',
		'POMULO_IZQ_04.translate','POMULO_IZQ_03.translate','POMULO_IZQ_02.translate','POMULO_IZQ_01.translate','CEJA_IZQ_00.translate']
		pteDos.multi(conexion='cat', lst_01= lista_01 ,lst_02= self.add_attr(lst=lsts_clr_wire['curv_izq'], tr=1))

		lista_01 = ['CTRL_PARPADO_IZQ_UP_03.translate','CTRL_PARPADO_IZQ_UP_02.translate','CTRL_PARPADO_IZQ_UP_01.translate','CTRL_PARPADO_IZQ_UP_00.translate',
		'CTRL_PARPADO_IZQ_DWN_01.translate','CTRL_PARPADO_IZQ_DWN_02.translate','CTRL_PARPADO_IZQ_DWN_03.translate','CTRL_PARPADO_IZQ_UP_04.translate']
		pteDos.multi(conexion='cat', lst_01= lista_01 ,lst_02= self.add_attr(lst=lsts_clr_wire['parpado_izq'], tr=1))

		lista_01 = ['OREJA_TOP_IZQ','OREJA_MID_IZQ','OREJA_BOTTOM_IZQ']
		lista_02 = ['CLR_CURV_OREJA_IZQ_1Handle','CLR_CURV_OREJA_IZQ_2Handle','CLR_CURV_OREJA_IZQ_3Handle']
		pteDos.multi(conexion='cat', lst_01= self.add_attr(lst=lista_01, tr=1) ,lst_02= self.add_attr(lst=lista_02, tr=1))
		
		lista_01 = ['NARIZ_SEC_DER.translate','NARIZ.rotate','NARIZ.translate','NARIZ_SEC_IZQ.translate']
		lista_02 = ['CLR_CURV_NARIZ_0Handle.translate','CLR_CURV_NARIZ_1Handle.rotate','CLR_CURV_NARIZ_1Handle.translate','CLR_CURV_NARIZ_2Handle.translate']
		pteDos.multi(conexion='cat', lst_01= lista_01,lst_02= lista_02, ampliar_lst=1)

		lista_01 = ['LABIO_SUPERIOR_ESQ_DER.translate','LABIO_SUPERIOR_DER.translate','LABIO_SUPERIOR_CNT.translate','LABIO_SUPERIOR_IZQ.translate','LABIO_SUPERIOR_ESQ_IZQ.translate']
		pteDos.multi(conexion='cat', lst_01= lista_01,lst_02= self.add_attr(lst=lsts_clr_wire['boca_sup'], tr=1), ampliar_lst=1)

		lista_01 = ['LABIO_INFERIOR_ESQ_DER.translate','LABIO_INFERIOR_DER.translate','LABIO_INFERIOR_CNT.translate','LABIO_INFERIOR_IZQ.translate','LABIO_INFERIOR_ESQ_IZQ.translate']
		pteDos.multi(conexion='cat', lst_01= lista_01,lst_02= self.add_attr(lst=lsts_clr_wire['boca_inf'], tr=1), ampliar_lst=1)



		#CREAR WIRE (COMIENZA)
		lista_01=['DEFORM_CURV_DER','DEFORM_CURV_IZQ','DEFORM_CURV_NARIZ','DEFORM_CURV_BOCA_SUP','DEFORM_CURV_BOCA_INF','DEFORM_CURV_PARPADO_DER','DEFORM_CURV_PARPADO_IZQ',
		'DEFORM_CURV_OREJA_DER','DEFORM_CURV_OREJA_IZQ']
		lista_02=['WIRE_OJO_DER','WIRE_OJO_IZQ','WIRE_NARIZ','WIRE_BOCA_UP','WIRE_BOCA_DOWN','WIRE_PARPADO_DER','WIRE_PARPADO_IZQ','WIRE_OREJA_DER','WIRE_OREJA_IZQ']

		for i in xrange(0, len(lista_01)):
			cmds.wire( 'WIRE_BS', w=lista_01[i], gw= False, en= 1, ce= 0, li= 0, n=lista_02[i] )

		#CREAR BLEND SHAPES (COMIENZA)
		cmds.select('BOCA_SONRISA_ABIERTA_BS', 'BOCA_F_BS', 'BOCA_E_BS', 'BOCA_A_BS', 'BOCA_I_BS', 'BOCA_U_BS', 'BOCA_O_BS', 'BOCA_M_BS', 'BOCA_BESO_BS', 'BOCA_CHICA_BS','FELIZ_BS', 
			'TRISTE_BS', 'ENOJADO_BS', 'SORPRENDIDO_BS', 'CENO_ENOJADO_BS', 'PARPADO_UP_CERRADO_DER_BS', 'PARPADO_UP_CERRADO_IZQ_BS', 'PARPADO_DOWN_CERRADO_DER_BS', 
			'PARPADO_DOWN_CERRADO_IZQ_BS', 'CACHETE_INFLADO_IZQ_BS', 'CACHETE_INFLADO_DER_BS', 'CEJAS_ENOJADAS_BS', 'CEJAS_TRISTES_BS', 'BOCA_SMIRK_DER_BS', 'BOCA_SMIRK_IZQ_BS', 
			'STRETCH_BS','SQUASH_BS', 'VACIO1_BS', 'VACIO2_BS', 'VACIO3_BS', 'VACIO4_BS','VACIO5_BS', 'WIRE_BS', 'ROOT_BS')

		cmds.blendShape(n='BLEND_GENERAL')
		

		cmds.select('ROOT_BS', cabeza)

		cmds.blendShape(n='BLEND_ROOT')

		cmds.select('CEJAS_WRAP_BS',cejas)
		cmds.blendShape(n='BLEND_CEJAS')

		cmds.setAttr('BLEND_CEJAS.CEJAS_WRAP_BS', 1)
		cmds.setAttr('BLEND_GENERAL.WIRE_BS', 1)
		cmds.setAttr('BLEND_ROOT.ROOT_BS', 1)

		#CREAR BLEND SHAPES (TERMINA)

		#CONECTA BLEND SHAPES A CONTROLES (COMIENZA)
		cmds.connectAttr( 'DRIVER_CARA.BS_TRISTE', 'BLEND_GENERAL.TRISTE_BS' )
		cmds.connectAttr( 'DRIVER_CARA.BS_ENOJADO', 'BLEND_GENERAL.ENOJADO_BS' )
		cmds.connectAttr( 'DRIVER_CARA.BS_SORPRENDIDO', 'BLEND_GENERAL.SORPRENDIDO_BS' )
		cmds.connectAttr( 'DRIVER_CARA.BS_STRETCH', 'BLEND_GENERAL.STRETCH_BS' )
		cmds.connectAttr( 'DRIVER_CARA.BS_SQUASH', 'BLEND_GENERAL.SQUASH_BS' )

		cmds.connectAttr( 'CEJAS.BS_CEJAS_ENOJADAS', 'BLEND_GENERAL.CEJAS_ENOJADAS_BS' )
		cmds.connectAttr( 'CEJAS.BS_CEJAS_TRISTES', 'BLEND_GENERAL.CEJAS_TRISTES_BS' )

		cmds.connectAttr( 'EXTRAS.BS_CENO_ENOJADO', 'BLEND_GENERAL.CENO_ENOJADO_BS' )
		cmds.connectAttr( 'EXTRAS.BS_CACHETE_INFLADO_IZQ', 'BLEND_GENERAL.CACHETE_INFLADO_IZQ_BS' )
		cmds.connectAttr( 'EXTRAS.BS_CACHETE_INFLADO_DER', 'BLEND_GENERAL.CACHETE_INFLADO_DER_BS' )
		cmds.connectAttr( 'EXTRAS.BS_VACIO1', 'BLEND_GENERAL.VACIO1_BS' )
		cmds.connectAttr( 'EXTRAS.BS_VACIO2', 'BLEND_GENERAL.VACIO2_BS' )
		cmds.connectAttr( 'EXTRAS.BS_VACIO3', 'BLEND_GENERAL.VACIO3_BS' )
		cmds.connectAttr( 'EXTRAS.BS_VACIO4', 'BLEND_GENERAL.VACIO4_BS' )
		cmds.connectAttr( 'EXTRAS.BS_VACIO5', 'BLEND_GENERAL.VACIO5_BS' )


		cmds.connectAttr( 'BOCA.BS_BOCA_E', 'BLEND_GENERAL.BOCA_E_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_A', 'BLEND_GENERAL.BOCA_A_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_I', 'BLEND_GENERAL.BOCA_I_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_U', 'BLEND_GENERAL.BOCA_U_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_F', 'BLEND_GENERAL.BOCA_F_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_O', 'BLEND_GENERAL.BOCA_O_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_M', 'BLEND_GENERAL.BOCA_M_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_BESO', 'BLEND_GENERAL.BOCA_BESO_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_CHICA', 'BLEND_GENERAL.BOCA_CHICA_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_SMIRK_DER', 'BLEND_GENERAL.BOCA_SMIRK_DER_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_SMIRK_IZQ', 'BLEND_GENERAL.BOCA_SMIRK_IZQ_BS' )
		cmds.connectAttr( 'BOCA.BS_FELIZ', 'BLEND_GENERAL.FELIZ_BS' )
		cmds.connectAttr( 'BOCA.BS_BOCA_SONRISA_ABIERTA', 'BLEND_GENERAL.BOCA_SONRISA_ABIERTA_BS' )

		#CONECTA BLEND SHAPES A CONTROLES (TERMINA)

		#CONECTAR BLEND SHAPES CON PARPADOS(COMIENZA)
		lista_01=['PARPADO_SUPERIOR_IZQ','PARPADO_INFERIOR_IZQ','BLEND_GENERAL','BLEND_GENERAL']
		lista_02=['translateY','translateY','PARPADO_DOWN_CERRADO_IZQ_BS','PARPADO_UP_CERRADO_IZQ_BS']
		pteDos.multi(conexion = 'set', lst_01 = lista_01, lst_02 =lista_02, attr=0)

		lista_01_sdk=['BLEND_GENERAL','BLEND_GENERAL','BLEND_GENERAL','BLEND_GENERAL']
		lista_02_sdk=['PARPADO_UP_CERRADO_IZQ_BS','PARPADO_UP_CERRADO_DER_BS','PARPADO_DOWN_CERRADO_IZQ_BS','PARPADO_DOWN_CERRADO_DER_BS']
		lista_03_sdk=['PARPADO_SUPERIOR_IZQ.translateY','PARPADO_SUPERIOR_DER.translateY','PARPADO_INFERIOR_IZQ.translateY','PARPADO_INFERIOR_DER.translateY']
		self.multi(lst_01=lista_01_sdk, lst_02=lista_02_sdk, solv=lista_03_sdk)

		pteDos.multi(conexion = 'set', lst_01 = ['PARPADO_SUPERIOR_IZQ'], lst_02 =['translateY'], attr=-1)

		lista_01=['PARPADO_INFERIOR_IZQ','BLEND_GENERAL','BLEND_GENERAL']
		lista_02=['translateY','PARPADO_DOWN_CERRADO_IZQ_BS','PARPADO_UP_CERRADO_IZQ_BS']
		pteDos.multi(conexion = 'set', lst_01 = lista_01, lst_02 =lista_02, attr=1)

		self.multi(lst_01=lista_01_sdk, lst_02=lista_02_sdk, solv=lista_03_sdk)

		pteDos.multi(conexion = 'set', lst_01 = ['PARPADO_SUPERIOR_IZQ','PARPADO_INFERIOR_IZQ'], lst_02 =['translateY','translateY'], attr=-0)


		#AGREGAR MIEMBROS AL GRUPO NO TOCAR (COMEINZA)
		cmds.parent('GRP_BLENDSHAPES','GRP_GEO','GRP_DEFORMS_CURVS','GRP_RIGG')
		cmds.editDisplayLayerMembers( 'no_tocar','GRP_CURVS_CARA', 'GRP_DEFORMS_CURVS')


		#cmds.reorderDeformers( 'skinCluster3', 'BLEND_ROOT', 'GRP_RIGG|GRP_BLENDSHAPES|'+cabeza )


		AXIS = ['X','Y','Z']
		ATTR = ['.translate', '.rotate', '.scale']

	def cluster_curvs(self, cv, id_curv, name_clr):
		lista=[]
		for knot in xrange(0, cv):
			cmds.select(id_curv +'.cv[' +str(knot) +"]", visible=True )
			cmds.cluster( rel=True, name = name_clr+'_' +str(knot))
			lista.append(name_clr+'_' +str(knot)+'Handle')

		grupo=cmds.group(lista,n= 'GRP_'+id_curv)
		cmds.parent(grupo,'GRP_DEFORMS_CURVS')

		return lista

	def add_attr(self, lst, tr=None, rt=None):
		lista=[]

		if tr!=None:
			for i in xrange(0, len(lst)):
				lista.append(lst[i]+ '.translate') 

		if rt!=None:
			for i in xrange(0, len(lst)):
				lista.append(lst[i]+ '.rotate') 

		return lista

	def mirror_curvs(self, info_position, obj_duplicate, name_duplicate):
		cmds.duplicate( obj_duplicate, rr=True, n=name_duplicate)
		cmds.group( name_duplicate, n='GRP_TEMP' )

		PZ = cmds.getAttr(info_position+'.tz' )
		PY = cmds.getAttr(info_position+'.ty' )
		PX = cmds.getAttr(info_position+'.tx' )

		cmds.move(PX, PY, PZ, "GRP_TEMP.scalePivot","GRP_TEMP.rotatePivot", absolute=True)

		cmds.setAttr('GRP_TEMP.scaleX', -1)
		cmds.select('GRP_TEMP')
		cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1)
		cmds.ungroup( 'GRP_TEMP' )

	def multi(self, lst_01, lst_02, solv):
		for element in xrange(0, len(lst_01)):
			cmds.setDrivenKeyframe( lst_01[element]+'.'+lst_02[element], cd=solv[element] )

	def block(self):

		for geo in cmds.ls(et='nurbsCurve'):
			if geo.find('DEFORM_CURV') != -1:
				geoParent = cmds.listRelatives(geo, p=True)[0]

				for attrib in ATTR:
					for ax in AXIS:
						try:
							cmds.setAttr(geoParent  + attrib + ax, l=True, k=False, cb=False)
						except:
							pass
