import maya.cmds as cmds


# EL WRAP DE LA CEJA  DEBE HACERSE POR EL USUARIO



cv = 0

#CREAR CLUSTER OJO DER(COMIENZA)

while cv < 12:

	cmds.select( 'DEFORM_CURV_DER.cv[%s]' %cv, visible=True )
	cmds.cluster( rel=True, name = 'CLR_CURV_OJO_DER_%s' %cv )
	

	cv = cv +1
	pass

#CREAR CLUSTER OJO DER(TERMINA)



cv = 0

#CREAR CLUSTER NARIZ(COMIENZA)

while cv < 3:

	cmds.select( 'DEFORM_CURV_NARIZ.cv[%s]' %cv, visible=True )
	cmds.cluster( rel=True, name = 'CLR_CURV_NARIZ_%s' %cv )


	cv = cv +1
	pass

#CREAR CLUSTER NARIZ(TERMINA)



cv = 0

#CREAR CLUSTER BOCA SUP(COMIENZA)

while cv < 5:

	cmds.select( 'DEFORM_CURV_BOCA_SUP.cv[%s]' %cv, visible=True )
	cmds.cluster( rel=True, name = 'CLR_CURV_BOCA_SUP_%s' %cv )


	cv = cv +1
	pass

#CREAR CLUSTER BOCA SUP(TERMINA)



cv = 0

#CREAR CLUSTER BOCA INF(COMIENZA)

while cv < 5:

	cmds.select( 'DEFORM_CURV_BOCA_INF.cv[%s]' %cv, visible=True )
	cmds.cluster( rel=True, name = 'CLR_CURV_BOCA_INF_%s' %cv )


	cv = cv +1
	pass

#CREAR CLUSTER BOCA INF(TERMINA)



#CREACION DE LOCATOR Y COLOCACION DE PIVOTE Y CURVA IZQ (COMEINZA)

cmds.select( 'DEFORM_CURV_NARIZ.cv[0]', 'DEFORM_CURV_NARIZ.cv[2]', visible=True )
cmds.cluster( rel=True, name = 'CLR_CURV_NARIZ_TEMP' )
	

cmds.spaceLocator(n='LOC_NARIZ')
cmds.pointConstraint( 'CLR_CURV_NARIZ_TEMPHandle', 'LOC_NARIZ' )


PZ = cmds.getAttr('LOC_NARIZ.tz' )
PY = cmds.getAttr('LOC_NARIZ.ty' )
PX = cmds.getAttr('LOC_NARIZ.tx' )

cmds.move(PX, PY, PZ, "CLR_CURV_NARIZ_1Handle.scalePivot","CLR_CURV_NARIZ_1Handle.rotatePivot", absolute=True)



cmds.delete('LOC_NARIZ_pointConstraint1')
cmds.pointConstraint( 'BS_WIRE', 'LOC_NARIZ' )

cmds.duplicate( 'DEFORM_CURV_DER', rr=True, n='DEFORM_CURV_IZQ')
cmds.group( 'DEFORM_CURV_IZQ', n='GRP_TEMP' )

PZ = cmds.getAttr('LOC_NARIZ.tz' )
PY = cmds.getAttr('LOC_NARIZ.ty' )
PX = cmds.getAttr('LOC_NARIZ.tx' )

cmds.move(PX, PY, PZ, "GRP_TEMP.scalePivot","GRP_TEMP.rotatePivot", absolute=True)

cmds.setAttr('GRP_TEMP.scaleX', -1)
cmds.select('GRP_TEMP')
cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1)

cmds.ungroup( 'GRP_TEMP' )
cmds.delete('CLR_CURV_NARIZ_TEMPHandle', 'LOC_NARIZ')

#CREACION DE LOCATOR Y COLOCACION DE PIVOTE Y CURVA IZQ (TERMINA)



#CREAR CLUSTERS OJO IZQ (COMIENZA)

cv = 0

while cv < 12:

	cmds.select( 'DEFORM_CURV_IZQ.cv[%s]' %cv, visible=True )
	cmds.cluster( rel=True, name = 'CLR_CURV_OJO_IZQ_%s' %cv )
	

	cv = cv +1
	pass

#CREAR CLUSTERS OJO IZQ (TERMINA)



#CONECTAR CLUSTERS A DRIVER(COMIENZA)

cmds.connectAttr( 'CEJA_DER_00.rotate', 'CLR_CURV_OJO_DER_11Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_00.translate', 'CLR_CURV_OJO_DER_11Handle.translate' )

cmds.connectAttr( 'CEJA_DER_01.rotate', 'CLR_CURV_OJO_DER_0Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_01.translate', 'CLR_CURV_OJO_DER_0Handle.translate' )

cmds.connectAttr( 'CEJA_DER_02.rotate', 'CLR_CURV_OJO_DER_1Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_02.translate', 'CLR_CURV_OJO_DER_1Handle.translate' )

cmds.connectAttr( 'CEJA_DER_03.rotate', 'CLR_CURV_OJO_DER_2Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_03.translate', 'CLR_CURV_OJO_DER_2Handle.translate' )

cmds.connectAttr( 'CEJA_DER_04.rotate', 'CLR_CURV_OJO_DER_3Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_04.translate', 'CLR_CURV_OJO_DER_3Handle.translate' )

cmds.connectAttr( 'CEJA_DER_05.rotate', 'CLR_CURV_OJO_DER_4Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_05.translate', 'CLR_CURV_OJO_DER_4Handle.translate' )

cmds.connectAttr( 'CEJA_DER_06.rotate', 'CLR_CURV_OJO_DER_5Handle.rotate' )
cmds.connectAttr( 'CEJA_DER_06.translate', 'CLR_CURV_OJO_DER_5Handle.translate' )


cmds.connectAttr( 'POMULO_DER_01.rotate', 'CLR_CURV_OJO_DER_10Handle.rotate' )
cmds.connectAttr( 'POMULO_DER_01.translate', 'CLR_CURV_OJO_DER_10Handle.translate' )

cmds.connectAttr( 'POMULO_DER_02.rotate', 'CLR_CURV_OJO_DER_9Handle.rotate' )
cmds.connectAttr( 'POMULO_DER_02.translate', 'CLR_CURV_OJO_DER_9Handle.translate' )

cmds.connectAttr( 'POMULO_DER_03.rotate', 'CLR_CURV_OJO_DER_8Handle.rotate' )
cmds.connectAttr( 'POMULO_DER_03.translate', 'CLR_CURV_OJO_DER_8Handle.translate' )

cmds.connectAttr( 'POMULO_DER_04.rotate', 'CLR_CURV_OJO_DER_7Handle.rotate' )
cmds.connectAttr( 'POMULO_DER_04.translate', 'CLR_CURV_OJO_DER_7Handle.translate' )

cmds.connectAttr( 'POMULO_DER_05.rotate', 'CLR_CURV_OJO_DER_6Handle.rotate' )
cmds.connectAttr( 'POMULO_DER_05.translate', 'CLR_CURV_OJO_DER_6Handle.translate' )



cmds.connectAttr( 'CEJA_IZQ_00.rotate', 'CLR_CURV_OJO_IZQ_11Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_00.translate', 'CLR_CURV_OJO_IZQ_11Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_01.rotate', 'CLR_CURV_OJO_IZQ_0Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_01.translate', 'CLR_CURV_OJO_IZQ_0Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_02.rotate', 'CLR_CURV_OJO_IZQ_1Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_02.translate', 'CLR_CURV_OJO_IZQ_1Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_03.rotate', 'CLR_CURV_OJO_IZQ_2Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_03.translate', 'CLR_CURV_OJO_IZQ_2Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_04.rotate', 'CLR_CURV_OJO_IZQ_3Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_04.translate', 'CLR_CURV_OJO_IZQ_3Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_05.rotate', 'CLR_CURV_OJO_IZQ_4Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_05.translate', 'CLR_CURV_OJO_IZQ_4Handle.translate' )

cmds.connectAttr( 'CEJA_IZQ_06.rotate', 'CLR_CURV_OJO_IZQ_5Handle.rotate' )
cmds.connectAttr( 'CEJA_IZQ_06.translate', 'CLR_CURV_OJO_IZQ_5Handle.translate' )


cmds.connectAttr( 'POMULO_IZQ_01.rotate', 'CLR_CURV_OJO_IZQ_10Handle.rotate' )
cmds.connectAttr( 'POMULO_IZQ_01.translate', 'CLR_CURV_OJO_IZQ_10Handle.translate' )

cmds.connectAttr( 'POMULO_IZQ_02.rotate', 'CLR_CURV_OJO_IZQ_9Handle.rotate' )
cmds.connectAttr( 'POMULO_IZQ_02.translate', 'CLR_CURV_OJO_IZQ_9Handle.translate' )

cmds.connectAttr( 'POMULO_IZQ_03.rotate', 'CLR_CURV_OJO_IZQ_8Handle.rotate' )
cmds.connectAttr( 'POMULO_IZQ_03.translate', 'CLR_CURV_OJO_IZQ_8Handle.translate' )

cmds.connectAttr( 'POMULO_IZQ_04.rotate', 'CLR_CURV_OJO_IZQ_7Handle.rotate' )
cmds.connectAttr( 'POMULO_IZQ_04.translate', 'CLR_CURV_OJO_IZQ_7Handle.translate' )

cmds.connectAttr( 'POMULO_IZQ_05.rotate', 'CLR_CURV_OJO_IZQ_6Handle.rotate' )
cmds.connectAttr( 'POMULO_IZQ_05.translate', 'CLR_CURV_OJO_IZQ_6Handle.translate' )



cmds.connectAttr( 'NARIZ_SEC_DER.rotate', 'CLR_CURV_NARIZ_0Handle.rotate' )
cmds.connectAttr( 'NARIZ_SEC_DER.translate', 'CLR_CURV_NARIZ_0Handle.translate' )


cmds.connectAttr( 'NARIZ.rotate', 'CLR_CURV_NARIZ_1Handle.rotate' )
cmds.connectAttr( 'NARIZ.translate', 'CLR_CURV_NARIZ_1Handle.translate' )

cmds.connectAttr( 'NARIZ_SEC_IZQ.rotate', 'CLR_CURV_NARIZ_2Handle.rotate' )
cmds.connectAttr( 'NARIZ_SEC_IZQ.translate', 'CLR_CURV_NARIZ_2Handle.translate' )



cmds.connectAttr( 'LABIO_SUPERIOR_ESQ_DER.rotate', 'CLR_CURV_BOCA_SUP_0Handle.rotate' )
cmds.connectAttr( 'LABIO_SUPERIOR_ESQ_DER.translate', 'CLR_CURV_BOCA_SUP_0Handle.translate' )

cmds.connectAttr( 'LABIO_SUPERIOR_DER.rotate', 'CLR_CURV_BOCA_SUP_1Handle.rotate' )
cmds.connectAttr( 'LABIO_SUPERIOR_DER.translate', 'CLR_CURV_BOCA_SUP_1Handle.translate' )

cmds.connectAttr( 'LABIO_SUPERIOR_CNT.rotate', 'CLR_CURV_BOCA_SUP_2Handle.rotate' )
cmds.connectAttr( 'LABIO_SUPERIOR_CNT.translate', 'CLR_CURV_BOCA_SUP_2Handle.translate' )

cmds.connectAttr( 'LABIO_SUPERIOR_IZQ.rotate', 'CLR_CURV_BOCA_SUP_3Handle.rotate' )
cmds.connectAttr( 'LABIO_SUPERIOR_IZQ.translate', 'CLR_CURV_BOCA_SUP_3Handle.translate' )

cmds.connectAttr( 'LABIO_SUPERIOR_ESQ_IZQ.rotate', 'CLR_CURV_BOCA_SUP_4Handle.rotate' )
cmds.connectAttr( 'LABIO_SUPERIOR_ESQ_IZQ.translate', 'CLR_CURV_BOCA_SUP_4Handle.translate' )



cmds.connectAttr( 'LABIO_INFERIOR_ESQ_DER.rotate', 'CLR_CURV_BOCA_INF_0Handle.rotate' )
cmds.connectAttr( 'LABIO_INFERIOR_ESQ_DER.translate', 'CLR_CURV_BOCA_INF_0Handle.translate' )

cmds.connectAttr( 'LABIO_INFERIOR_DER.rotate', 'CLR_CURV_BOCA_INF_1Handle.rotate' )
cmds.connectAttr( 'LABIO_INFERIOR_DER.translate', 'CLR_CURV_BOCA_INF_1Handle.translate' )

cmds.connectAttr( 'LABIO_INFERIOR_CNT.rotate', 'CLR_CURV_BOCA_INF_2Handle.rotate' )
cmds.connectAttr( 'LABIO_INFERIOR_CNT.translate', 'CLR_CURV_BOCA_INF_2Handle.translate' )

cmds.connectAttr( 'LABIO_INFERIOR_IZQ.rotate', 'CLR_CURV_BOCA_INF_3Handle.rotate' )
cmds.connectAttr( 'LABIO_INFERIOR_IZQ.translate', 'CLR_CURV_BOCA_INF_3Handle.translate' )

cmds.connectAttr( 'LABIO_INFERIOR_ESQ_IZQ.rotate', 'CLR_CURV_BOCA_INF_4Handle.rotate' )
cmds.connectAttr( 'LABIO_INFERIOR_ESQ_IZQ.translate', 'CLR_CURV_BOCA_INF_4Handle.translate' )

#CONECTAR CLUSTERS A DRIVER(TERMINA)



#CREAR WIRE (COMIENZA)

cmds.wire( 'BS_WIRE', w='DEFORM_CURV_DER', gw= False, en= 1, ce= 0, li= 0, n='WIRE_OJO_DER' )

cmds.wire( 'BS_WIRE', w='DEFORM_CURV_IZQ', gw= False, en= 1, ce= 0, li= 0, n='WIRE_OJO_IZQ')

cmds.wire( 'BS_WIRE', w='DEFORM_CURV_NARIZ', gw= False, en= 1, ce= 0, li= 0, n='WIRE_NARIZ')

cmds.wire( 'BS_WIRE', w='DEFORM_CURV_BOCA_SUP', gw= False, en= 1, ce= 0, li= 0, n='WIRE_BOCA_UP' )

cmds.wire( 'BS_WIRE', w='DEFORM_CURV_BOCA_INF', gw= False, en= 1, ce= 0, li= 0, n='WIRE_BOCA_DOWN' )

#CREAR WIRE (TERMINA)



#CREAR BLEND SHAPES (COMIENZA)

cmds.select('BS_BOCA_ABIERTA_SONRISA', 'BS_BOCA_F', 'BS_BOCA_E', 'BS_BOCA_A', 'BS_BOCA_I', 'BS_BOCA_U', 'BS_BOCA_O', 'BS_BOCA_M', 'BS_BOCA_BESO', 'BS_BOCA_CHICA',
			'BS_FELIZ', 'BS_TRISTE', 'BS_ENOJADO', 'BS_SORPRENDIDO', 'BS_CENO_ENOJADO', 'BS_PARPADO_UP_CERRADO_DER', 
			'BS_PARPADO_UP_CERRADO_IZQ', 'BS_PARPADO_DOWN_CERRADO_DER', 'BS_PARPADO_DOWN_CERRADO_IZQ', 'BS_CACHETE_INFLADO_IZQ', 
			'BS_CACHETE_INFLADO_DER', 'BS_CEJAS_ENOJADAS', 'BS_CEJAS_TRISTES', 'BS_BOCA_SMIRK_DER', 'BS_BOCA_SMIRK_IZQ', 'BS_STRETCH',
			'BS_SQUASH', 'BS_VACIO1', 'BS_VACIO2', 'BS_VACIO3', 'BS_VACIO4', 'BS_WIRE', 
			'BS_ROOT')

cmds.blendShape(n='BLEND_GENERAL')


#cmds.select('MD_CEJAS_WRAP', 'MD_CEJAS')

cmds.blendShape(n='BLEND_CEJAS')


cmds.select('BS_ROOT', 'MD_CABEZA')

cmds.blendShape(n='BLEND_ROOT')


cmds.setAttr('BLEND_GENERAL.BS_WIRE', 1)
#cmds.setAttr('BLEND_CEJAS.MD_CEJAS_WRAP', 1)
cmds.setAttr('BLEND_ROOT.BS_ROOT', 1)

#CREAR BLEND SHAPES (TERMINA)



#CONECTA BLEND SHAPES A CONTROLES (COMIENZA)

cmds.connectAttr( 'DRIVER_CARA.BS_TRISTE', 'BLEND_GENERAL.BS_TRISTE' )
cmds.connectAttr( 'DRIVER_CARA.BS_ENOJADO', 'BLEND_GENERAL.BS_ENOJADO' )
cmds.connectAttr( 'DRIVER_CARA.BS_SORPRENDIDO', 'BLEND_GENERAL.BS_SORPRENDIDO' )
cmds.connectAttr( 'DRIVER_CARA.BS_STRETCH', 'BLEND_GENERAL.BS_STRETCH' )
cmds.connectAttr( 'DRIVER_CARA.BS_SQUASH', 'BLEND_GENERAL.BS_SQUASH' )

cmds.connectAttr( 'CEJAS.BS_CEJAS_ENOJADAS', 'BLEND_GENERAL.BS_CEJAS_ENOJADAS' )
cmds.connectAttr( 'CEJAS.BS_CEJAS_TRISTES', 'BLEND_GENERAL.BS_CEJAS_TRISTES' )

cmds.connectAttr( 'EXTRAS.BS_CENO_ENOJADO', 'BLEND_GENERAL.BS_CENO_ENOJADO' )
cmds.connectAttr( 'EXTRAS.BS_CACHETE_INFLADO_IZQ', 'BLEND_GENERAL.BS_CACHETE_INFLADO_IZQ' )
cmds.connectAttr( 'EXTRAS.BS_CACHETE_INFLADO_DER', 'BLEND_GENERAL.BS_CACHETE_INFLADO_DER' )
#cmds.connectAttr( 'EXTRAS.BS_CABEZA_SQUASH', 'BLEND_GENERAL.BS_CABEZA_SQUASH' )
#cmds.connectAttr( 'EXTRAS.BS_CABEZA_STRETCH', 'BLEND_GENERAL.BS_CABEZA_STRETCH' )
cmds.connectAttr( 'EXTRAS.BS_VACIO1', 'BLEND_GENERAL.BS_VACIO1' )
cmds.connectAttr( 'EXTRAS.BS_VACIO2', 'BLEND_GENERAL.BS_VACIO2' )
cmds.connectAttr( 'EXTRAS.BS_VACIO3', 'BLEND_GENERAL.BS_VACIO3' )
cmds.connectAttr( 'EXTRAS.BS_VACIO4', 'BLEND_GENERAL.BS_VACIO4' )


cmds.connectAttr( 'BOCA.BS_BOCA_E', 'BLEND_GENERAL.BS_BOCA_E' )
cmds.connectAttr( 'BOCA.BS_BOCA_A', 'BLEND_GENERAL.BS_BOCA_A' )
cmds.connectAttr( 'BOCA.BS_BOCA_I', 'BLEND_GENERAL.BS_BOCA_I' )
cmds.connectAttr( 'BOCA.BS_BOCA_U', 'BLEND_GENERAL.BS_BOCA_U' )
cmds.connectAttr( 'BOCA.BS_BOCA_F', 'BLEND_GENERAL.BS_BOCA_F' )
cmds.connectAttr( 'BOCA.BS_BOCA_O', 'BLEND_GENERAL.BS_BOCA_O' )
cmds.connectAttr( 'BOCA.BS_BOCA_M', 'BLEND_GENERAL.BS_BOCA_M' )
cmds.connectAttr( 'BOCA.BS_BOCA_BESO', 'BLEND_GENERAL.BS_BOCA_BESO' )
cmds.connectAttr( 'BOCA.BS_BOCA_CHICA', 'BLEND_GENERAL.BS_BOCA_CHICA' )
cmds.connectAttr( 'BOCA.BS_BOCA_SMIRK_DER', 'BLEND_GENERAL.BS_BOCA_SMIRK_DER' )
cmds.connectAttr( 'BOCA.BS_BOCA_SMIRK_IZQ', 'BLEND_GENERAL.BS_BOCA_SMIRK_IZQ' )
cmds.connectAttr( 'BOCA.BS_FELIZ', 'BLEND_GENERAL.BS_FELIZ' )
cmds.connectAttr( 'BOCA.BS_BOCA_ABIERTA_SONRISA', 'BLEND_GENERAL.BS_BOCA_ABIERTA_SONRISA' )

#CONECTA BLEND SHAPES A CONTROLES (TERMINA)



#CONECTAR BLEND SHAPES CON PARPADOS(COMIENZA)

cmds.setAttr('PARPADO_SUPERIOR_IZQ.translateY', 0)
cmds.setAttr('PARPADO_SUPERIOR_DER.translateY', 0)
cmds.setAttr('PARPADO_INFERIOR_IZQ.translateY', 0)
cmds.setAttr('PARPADO_INFERIOR_DER.translateY', 0)

cmds.setAttr('BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_DER', 0)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_IZQ', 0)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_UP_CERRADO_DER', 0)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_UP_CERRADO_IZQ', 0)

cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_UP_CERRADO_IZQ', cd='PARPADO_SUPERIOR_IZQ.translateY' )
cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_UP_CERRADO_DER', cd='PARPADO_SUPERIOR_DER.translateY' )

cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_IZQ', cd='PARPADO_INFERIOR_IZQ.translateY' )
cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_DER', cd='PARPADO_INFERIOR_DER.translateY' )


cmds.setAttr('PARPADO_SUPERIOR_IZQ.translateY', -1)
cmds.setAttr('PARPADO_SUPERIOR_DER.translateY', -1)
cmds.setAttr('PARPADO_INFERIOR_IZQ.translateY', 1)
cmds.setAttr('PARPADO_INFERIOR_DER.translateY', 1)

cmds.setAttr('BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_DER', 1)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_IZQ', 1)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_UP_CERRADO_DER', 1)
cmds.setAttr('BLEND_GENERAL.BS_PARPADO_UP_CERRADO_IZQ', 1)


cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_UP_CERRADO_IZQ', cd='PARPADO_SUPERIOR_IZQ.translateY' )
cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_UP_CERRADO_DER', cd='PARPADO_SUPERIOR_DER.translateY' )

cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_IZQ', cd='PARPADO_INFERIOR_IZQ.translateY' )
cmds.setDrivenKeyframe( 'BLEND_GENERAL.BS_PARPADO_DOWN_CERRADO_DER', cd='PARPADO_INFERIOR_DER.translateY' )


cmds.setAttr('PARPADO_SUPERIOR_IZQ.translateY', 0)
cmds.setAttr('PARPADO_SUPERIOR_DER.translateY', 0)
cmds.setAttr('PARPADO_INFERIOR_IZQ.translateY', 0)
cmds.setAttr('PARPADO_INFERIOR_DER.translateY', 0)

#CONECTAR BLEND SHAPES CON PARPADOS(TERMINA)



#AGREGAR MIEMBROS AL GRUPO NO TOCAR (COMEINZA)

cmds.editDisplayLayerMembers( 'no_tocar', 'IK_BRAZO_IZQ', 'IK_BRAZO_DER', 'IK_TALON_IZQ', 'IK_TALON_DER',
 	'IK_PIE_IZQ', 'IK_PIE_DER', 'IK_DEDOS_PIE_IZQ', 'IK_DEDOS_PIE_DER', 'CLR_CODO_IZQ_1', 'CLR_CODO_IZQ_2',
  	'CLR_CODO_DER_1', 'CLR_CODO_DER_2', 'REV_IZQ_1', 'REV_DER_1', 'CLR_RODILLA_IZQ_1', 'CLR_RODILLA_DER_1', 
  	'CLR_RODILLA_IZQ_2', 'CLR_RODILLA_DER_2', 'BS_BOCA_ABIERTA_SONRISA', 'BS_BOCA_F', 'BS_BOCA_E', 'BS_BOCA_A', 'BS_BOCA_I', 'BS_BOCA_U', 'BS_BOCA_O',
  	'BS_BOCA_M','BS_BOCA_BESO','BS_BOCA_CHICA','BS_FELIZ','BS_TRISTE','BS_ENOJADO','BS_SORPRENDIDO','BS_CENO_ENOJADO',
  	'BS_PARPADO_UP_CERRADO_DER','BS_PARPADO_UP_CERRADO_IZQ', 'BS_PARPADO_DOWN_CERRADO_DER','BS_PARPADO_DOWN_CERRADO_IZQ',
  	'BS_CACHETE_INFLADO_IZQ','BS_CACHETE_INFLADO_DER', 'BS_CEJAS_ENOJADAS','BS_CEJAS_TRISTES', 'BS_BOCA_SMIRK_DER',
  	'BS_BOCA_SMIRK_IZQ','BS_STRETCH', 'BS_SQUASH','BS_VACIO1', 'BS_VACIO2',
  	'BS_VACIO3', 'BS_VACIO4','BS_WIRE','BS_ROOT','BS_ROOTBase', 'DEFORM_CURV_DER','DEFORM_CURV_DERBaseWire', 
  	'DEFORM_CURV_IZQ','DEFORM_CURV_IZQBaseWire', 'DEFORM_CURV_NARIZ','DEFORM_CURV_NARIZBaseWire', 'DEFORM_CURV_BOCA_SUP', 
  	'DEFORM_CURV_BOCA_SUPBaseWire', 'DEFORM_CURV_BOCA_INF', 'DEFORM_CURV_BOCA_INFBaseWire', 'CLR_CURV_OJO_DER_1Handle', 
  	'CLR_CURV_OJO_DER_2Handle', 'CLR_CURV_OJO_DER_3Handle', 'CLR_CURV_OJO_DER_4Handle', 'CLR_CURV_OJO_DER_5Handle', 
  	'CLR_CURV_OJO_DER_6Handle', 'CLR_CURV_OJO_DER_7Handle', 'CLR_CURV_OJO_DER_8Handle', 'CLR_CURV_OJO_DER_9Handle', 
  	'CLR_CURV_OJO_DER_10Handle', 'CLR_CURV_OJO_DER_11Handle', 'CLR_CURV_OJO_DER_0Handle', 'CLR_CURV_OJO_IZQ_0Handle', 
  	'CLR_CURV_OJO_IZQ_1Handle', 'CLR_CURV_OJO_IZQ_2Handle', 'CLR_CURV_OJO_IZQ_3Handle', 'CLR_CURV_OJO_IZQ_4Handle', 
  	'CLR_CURV_OJO_IZQ_5Handle', 'CLR_CURV_OJO_IZQ_6Handle', 'CLR_CURV_OJO_IZQ_7Handle', 'CLR_CURV_OJO_IZQ_8Handle', 
  	'CLR_CURV_OJO_IZQ_9Handle', 'CLR_CURV_OJO_IZQ_10Handle', 'CLR_CURV_OJO_IZQ_11Handle', 'CLR_CURV_NARIZ_0Handle', 
  	'CLR_CURV_NARIZ_1Handle', 'CLR_CURV_NARIZ_2Handle', 'CLR_CURV_BOCA_SUP_0Handle', 'CLR_CURV_BOCA_SUP_1Handle', 
  	'CLR_CURV_BOCA_SUP_2Handle', 'CLR_CURV_BOCA_SUP_3Handle', 'CLR_CURV_BOCA_SUP_4Handle', 'CLR_CURV_BOCA_INF_0Handle', 
  	'CLR_CURV_BOCA_INF_1Handle', 'CLR_CURV_BOCA_INF_2Handle', 'CLR_CURV_BOCA_INF_3Handle', 'CLR_CURV_BOCA_INF_4Handle')

#AGREGAR MIEMBROS AL GRUPO NO TOCAR (COMEINZA)