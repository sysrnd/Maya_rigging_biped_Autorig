import maya.cmds as cmds

def autoRigAnderPte2(*args):
	#FREEZE DRIVERS(COMIENZA)

	cmds.select('DRIVER_CABEZA', 'DRIVER_MANO_IZQ','DRIVER_MANO_DER','DRIVER_CODO_IZQ','DRIVER_CODO_DER',
		'DRIVER_CLAVICULA_IZQ','DRIVER_CLAVICULA_DER','DRIVER_DIENTES_TOP','DRIVER_DIENTES_BOTTOM','DRIVER_BOCA',
		'DRIVER_COLUMNA_TOP','DRIVER_COLUMNA_BOTTOM','DRIVER_COLUMNA_MIDDLE','DRIVER_ROOT','DRIVER_CINTURA',
		'DRIVER_PIE_IZQ','DRIVER_PIE_DER','DRIVER_RODILLA_IZQ','DRIVER_RODILLA_DER','MOVE_ALL','MASTER', 'DRIVER_LENGUA',
		'DRIVER_PINKY_SEC_DER','DRIVER_PINKY_SEC_IZQ', 'DRIVER_OJO_DER', 'DRIVER_OJO_DER', 'DRIVER_HEEL_DER', 'DRIVER_BALL_DER', 
		'DRIVER_TOE_DER', 'DRIVER_HEEL_IZQ', 'DRIVER_BALL_IZQ', 'DRIVER_TOE_IZQ', 'DRIVER_HOMBRO_IZQ_FK', 'DRIVER_CODO_IZQ_FK', 
		'DRIVER_MANO_IZQ_FK', 'DRIVER_HOMBRO_DER_FK', 'DRIVER_CODO_DER_FK', 'DRIVER_MANO_DER_FK','DRIVER_THUMB_IZQ_1','DRIVER_THUMB_IZQ_2',
		'DRIVER_THUMB_IZQ_3','DRIVER_INDEX_IZQ_1','DRIVER_INDEX_IZQ_2','DRIVER_INDEX_IZQ_3','DRIVER_MIDDLE_IZQ_1','DRIVER_MIDDLE_IZQ_2',
		'DRIVER_MIDDLE_IZQ_3','DRIVER_CANCEL_IZQ_1','DRIVER_CANCEL_IZQ_2','DRIVER_CANCEL_IZQ_3','DRIVER_PINKY_IZQ_1','DRIVER_PINKY_IZQ_2',
		'DRIVER_PINKY_IZQ_3','DRIVER_THUMB_DER_1','DRIVER_THUMB_DER_2','DRIVER_THUMB_DER_3','DRIVER_INDEX_DER_1','DRIVER_INDEX_DER_2',
		'DRIVER_INDEX_DER_3','DRIVER_MIDDLE_DER_1','DRIVER_MIDDLE_DER_2','DRIVER_MIDDLE_DER_3','DRIVER_CANCEL_DER_1','DRIVER_CANCEL_DER_2',
		'DRIVER_CANCEL_DER_3','DRIVER_PINKY_DER_1','DRIVER_PINKY_DER_2','DRIVER_PINKY_DER_3')
	cmds.select("DRIVER_TOE_FINGERS_IZQ")
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 
	#FREEZE DRIVERS(TERMINA)




	#POSICIONA DRIVER RODILLAS Y CODOS(COMIENZA)

	cmds.move( 2.5, 'DRIVER_RODILLA_DER', z=True )
	cmds.move( 2.5, 'DRIVER_RODILLA_IZQ', z=True )
	cmds.move( -2.5, 'DRIVER_CODO_IZQ', z=True )
	cmds.move( -2.5, 'DRIVER_CODO_DER', z=True )


	cmds.select('DRIVER_RODILLA_DER', 'DRIVER_RODILLA_IZQ','DRIVER_CODO_IZQ','DRIVER_CODO_DER', 'DRIVER_OJO_DER', 'DRIVER_OJO_IZQ')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 


	cmds.move( 4, 'DRIVER_OJO_DER', z=True )
	cmds.move( 4, 'DRIVER_OJO_IZQ', z=True )

	cmds.select('DRIVER_OJO_DER', 'DRIVER_OJO_IZQ')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 


	cmds.group( 'DRIVER_OJO_DER', 'DRIVER_OJO_IZQ' , n='GRP_TEMP' )
	cmds.pointConstraint( 'GRP_TEMP', 'DRIVER_OJOS', n='CONST_TEMP')
	cmds.delete('CONST_TEMP')
	cmds.ungroup( 'GRP_TEMP' )

	cmds.select('DRIVER_OJOS')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

	#POSICIONA DRIVER RODILLAS Y CODOS(TERMINA)



	#Crear atributos (COMIENZA)

	cmds.addAttr('DRIVER_COLUMNA_TOP', nn='SWT IK FK IZQ', longName='SWITCH_IK_FK_IZQ', defaultValue=0, minValue=0, maxValue=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_IZQ', channelBox = 0, keyable=1)

	cmds.addAttr('DRIVER_COLUMNA_TOP', nn='SWT IK FK DER', longName='SWITCH_IK_FK_DER', defaultValue=0, minValue=0, maxValue=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_DER', channelBox = 0, keyable=1)

	cmds.addAttr('DRIVER_CABEZA', nn='SWT OJOS', longName='SWITCH_OJOS', defaultValue=0, minValue=0, maxValue=1)
	cmds.setAttr('DRIVER_CABEZA.SWITCH_OJOS', channelBox = 0, keyable=1)




	cmds.addAttr('DRIVER_MANO_IZQ', nn='CORRECION CODO', longName='CORRECION_CODO', defaultValue=0)
	cmds.setAttr('DRIVER_MANO_IZQ.CORRECION_CODO', channelBox = 0, keyable=1)

	cmds.addAttr('DRIVER_MANO_DER', nn='CORRECION CODO', longName='CORRECION_CODO', defaultValue=0)
	cmds.setAttr('DRIVER_MANO_DER.CORRECION_CODO', channelBox = 0, keyable=1)


	cmds.addAttr('DRIVER_MANO_IZQ_FK', nn='CORRECION CODO', longName='CORRECION_CODO', defaultValue=0)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.CORRECION_CODO', channelBox = 0, keyable=1)

	cmds.addAttr('DRIVER_MANO_DER_FK', nn='CORRECION CODO', longName='CORRECION_CODO', defaultValue=0)
	cmds.setAttr('DRIVER_MANO_DER_FK.CORRECION_CODO', channelBox = 0, keyable=1)

	#Crear atributos (TERMINA)





	cmds.delete ('BONES_REFERENCIA')





	nombredriver = 'DRIVER_PIE_IZQ'

	lado = 'IZQ'

	#FREEZE DRIVERS(COMIENZA)

	cmds.select('DRIVER_CABEZA', 'DRIVER_MANO_IZQ','DRIVER_MANO_DER','DRIVER_CODO_IZQ','DRIVER_CODO_DER',
		'DRIVER_CLAVICULA_IZQ','DRIVER_CLAVICULA_DER','DRIVER_DIENTES_TOP','DRIVER_DIENTES_BOTTOM','DRIVER_BOCA',
		'DRIVER_COLUMNA_TOP','DRIVER_COLUMNA_BOTTOM','DRIVER_COLUMNA_MIDDLE','DRIVER_ROOT','DRIVER_CINTURA',
		'DRIVER_PIE_IZQ','DRIVER_PIE_DER','DRIVER_RODILLA_IZQ','DRIVER_RODILLA_DER','MOVE_ALL','MASTER', 'DRIVER_LENGUA',
		'DRIVER_PINKY_SEC_DER','DRIVER_PINKY_SEC_IZQ', 'DRIVER_OJO_DER', 'DRIVER_OJO_DER', 'DRIVER_HEEL_DER', 'DRIVER_BALL_DER', 
		'DRIVER_TOE_DER', 'DRIVER_HEEL_IZQ', 'DRIVER_BALL_IZQ', 'DRIVER_TOE_IZQ', 'DRIVER_HOMBRO_IZQ_FK', 'DRIVER_CODO_IZQ_FK', 
		'DRIVER_MANO_IZQ_FK', 'DRIVER_HOMBRO_DER_FK', 'DRIVER_CODO_DER_FK', 'DRIVER_MANO_DER_FK')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

	#FREEZE DRIVERS(TERMINA)




	#CREAR IK PIERNAS (COMIENZA)

	cmds.ikHandle( sj='PIERNA_%s' %lado, ee='TALON_%s' %lado, sol = 'ikRPsolver', name = 'IK_TALON_%s' %lado )

	cmds.ikHandle( sj='TALON_%s' %lado, ee='DEDOS_PIE_%s' %lado, sol = 'ikSCsolver', name = 'IK_PIE_%s' %lado )

	cmds.ikHandle( sj='DEDOS_PIE_%s' %lado, ee='PUNTA_PIE_%s' %lado, sol = 'ikSCsolver', name = 'IK_DEDOS_PIE_%s' %lado )

	#CREAR IK PIERNAS (TERMINA)




	#CONECTAR IK CON JOINTS (COMIENZA)

	cmds.pointConstraint( 'REV_%s_4' %lado, 'IK_TALON_%s' %lado, mo =1 )

	cmds.parent( 'IK_PIE_%s' %lado, 'REV_%s_3'%lado )

	cmds.parent( 'IK_DEDOS_PIE_%s' %lado, 'REV_%s_2'%lado )

	cmds.parent( 'REV_%s_1' %lado, '%s' %nombredriver)

	cmds.parent( 'DRIVER_TOE_FINGERS_%s' %lado, 'DRIVER_HEEL_%s' %lado )

	cmds.pointConstraint( 'DRIVER_TOE_FINGERS_%s' %lado, 'IK_DEDOS_PIE_%s' %lado, mo =1 )

	#CONECTAR IK CON JOINTS (TERMINA)



	#CREAR POLE VECTOR RODILLA (COMIENZA)

	cmds.poleVectorConstraint( 'DRIVER_RODILLA_%s' %lado, 'IK_TALON_%s' %lado, w =  1)

	#CREAR POLE VECTOR RODILLA (TERMINA)



	#CURVA DE REFERENCIA DE LAS RODILLAS (COMIENZA)

	cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=1, sl2=1, n = 'cuadradotemp')

	cmds.ungroup( 'cuadradotemp' )

	cmds.delete( 'rightcuadradotemp', 'leftcuadradotemp', 'bottomcuadradotemp' )

	cmds.rename('topcuadradotemp', 'CRV_REFR_RODILLA_%s' %lado)

	cmds.select( 'CRV_REFR_RODILLA_%s.cv[1]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_RODILLA_1' )

	cmds.rename('CLR_RODILLA_1Handle', 'CLR_RODILLA_%s_1' %lado)

	cmds.select( 'CRV_REFR_RODILLA_%s.cv[0]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_RODILLA_2' )

	cmds.rename('CLR_RODILLA_2Handle', 'CLR_RODILLA_%s_2' %lado)

	cmds.pointConstraint( 'RODILLA_%s' %lado, 'CLR_RODILLA_%s_1' %lado )

	cmds.pointConstraint( 'DRIVER_RODILLA_%s' %lado, 'CLR_RODILLA_%s_2' %lado )

	cmds.setAttr( 'CRV_REFR_RODILLA_%s.template' %lado, 1)

	#CURVA DE REFERENCIA DE LAS RODILLAS (TERMINA)




	#CONECTA LAS CURVAS DEL PIE(COMIENZA)

	cmds.parent( 'DRIVER_HEEL_%s' %lado, 'DRIVER_PIE_%s' %lado)
	cmds.parent( 'DRIVER_TOE_%s' %lado, 'DRIVER_HEEL_%s' %lado)
	cmds.parent( 'DRIVER_BALL_%s' %lado, 'DRIVER_TOE_%s' %lado)

	cmds.orientConstraint( 'DRIVER_HEEL_%s' %lado, 'REV_%s_1' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_BALL_%s' %lado, 'REV_%s_3' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_TOE_%s' %lado, 'REV_%s_2' %lado, mo=1 )

	#CONECTA LAS CURVAS DEL PIE(TERMINA)




	#COMIENZAN LAS MANOS

	nombredriver = 'DRIVER_MANO_IZQ'



	#CREAR CURVA DE REFERENCIA BRAZO_IK(COMIENZA)

	cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=1, sl2=1, n = 'cuadradotemp')

	cmds.ungroup( 'cuadradotemp' )

	cmds.delete( 'rightcuadradotemp', 'leftcuadradotemp', 'bottomcuadradotemp' )

	cmds.rename('topcuadradotemp', 'crv_refr_brazo_%s' %lado)

	cmds.select( 'crv_refr_brazo_%s.cv[1]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_CODO_1' )

	cmds.rename('CLR_CODO_1Handle', 'CLR_CODO_%s_1' %lado)

	cmds.select( 'crv_refr_brazo_%s.cv[0]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_CODO_2' )

	cmds.rename('CLR_CODO_2Handle', 'CLR_CODO_%s_2' %lado)

	cmds.pointConstraint( 'CODO_%s' %lado, 'CLR_CODO_%s_1' %lado )

	cmds.pointConstraint( 'DRIVER_CODO_%s' %lado, 'CLR_CODO_%s_2' %lado )

	cmds.setAttr( 'crv_refr_brazo_%s.template' %lado, 1)

	#CREAR CURVA DE REFERENCIA BRAZO_IK(TERMINA)




	#CREAR UNIONES ENTRE LOS HUESOS DE LOS BRAZOS Y SWITCH(COMIENZA)

	cmds.parentConstraint( 'HOMBRO_%s_IK' %lado, 'HOMBRO_%s' %lado, mo=1, n='PC_HOMBRO_%s_IK' %lado)
	cmds.parentConstraint( 'CODO_%s_IK' %lado, 'CODO_%s' %lado, mo=1, n='PC_CODO_%s_IK' %lado)
	cmds.parentConstraint( 'CODO_SEC_%s_IK' %lado, 'CODO_SEC_%s' %lado, mo=1, n='PC_CODO_SEC_%s_IK' %lado)
	cmds.parentConstraint( 'MANO_%s_IK' %lado, 'MANO_%s' %lado, mo=1, n='PC_MANO_%s_IK' %lado)


	cmds.parentConstraint( 'HOMBRO_%s_FK' %lado, 'HOMBRO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'CODO_%s_FK' %lado, 'CODO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'CODO_SEC_%s_FK' %lado, 'CODO_SEC_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'MANO_%s_FK' %lado, 'MANO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)



	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0'  %(lado, lado), 0 )



	cmds.setAttr( 'crv_refr_brazo_%s.visibility' %lado, 0)
	cmds.setAttr( 'HOMBRO_%s_IK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_CODO_%s.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_MANO_%s.visibility' %lado, 0)

	cmds.setAttr( 'HOMBRO_%s_FK.visibility' %lado, 1 )
	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_CODO_%s_FK.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_MANO_%s_FK.visibility' %lado, 1)




	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )


	cmds.setDrivenKeyframe( 'crv_refr_brazo_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado)
	cmds.setDrivenKeyframe( 'HOMBRO_%s_IK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )



	cmds.setAttr( 'DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 1 )



	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0'  %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0'  %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0'  %(lado, lado), 1 )

	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1'  %(lado, lado), 0 )




	cmds.setAttr( 'crv_refr_brazo_%s.visibility' %lado, 1)
	cmds.setAttr( 'HOMBRO_%s_IK.visibility' %lado, 1 )
	cmds.setAttr( 'DRIVER_CODO_%s.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_MANO_%s.visibility' %lado, 1)


	cmds.setAttr( 'HOMBRO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_CODO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_MANO_%s_FK.visibility' %lado, 0)



	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )


	cmds.setDrivenKeyframe( 'crv_refr_brazo_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado)
	cmds.setDrivenKeyframe( 'HOMBRO_%s_IK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	#CREAR UNIONES ENTRE LOS HUESOS DE LOS BRAZOS Y SWITCH(TERMINA)




	#CREAR IK DE LOS BRAZOS y curva de refrencia (COMIENZA)

	cmds.ikHandle( sj='HOMBRO_%s_IK' %lado, ee='CODO_SEC_%s_IK' %lado, sol = 'ikRPsolver', name = 'IK_BRAZO_%s' %lado )

	cmds.orientConstraint( 'DRIVER_MANO_%s' %lado, 'MANO_%s_IK' %lado, mo=1 )

	cmds.spaceLocator(n='LOC_BRAZO_%s' %lado)
	cmds.pointConstraint( 'MANO_%s_IK' %lado, 'LOC_BRAZO_%s' %lado )

	PX = cmds.getAttr('LOC_BRAZO_%s.tx' %lado)
	PY = cmds.getAttr('LOC_BRAZO_%s.ty' %lado)
	PZ = cmds.getAttr('LOC_BRAZO_%s.tz' %lado)

	cmds.move(PX, PY, PZ, "effector4.scalePivot","effector4.rotatePivot", absolute=True)

	cmds.move(PX, PY, PZ, 'IK_BRAZO_%s' %lado)

	cmds.delete('LOC_BRAZO_%s' %lado)

	cmds.poleVectorConstraint( 'DRIVER_CODO_%s' %lado, 'IK_BRAZO_%s' %lado, w=1, n='POLEA_BRAZO_%s' %lado)

	#CREAR IK DE LOS BRAZOS (TERMINA)




	#CREAR FK DE LOS BRAZOS (COMIENZA)

	cmds.orientConstraint( 'DRIVER_HOMBRO_%s_FK' %lado, 'HOMBRO_%s_FK' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_CODO_%s_FK' %lado, 'CODO_%s_FK' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_MANO_%s_FK' %lado, 'MANO_%s_FK' %lado, mo=1 )


	cmds.parent( 'DRIVER_MANO_%s_FK' %lado, 'DRIVER_CODO_%s_FK' %lado)
	cmds.parent( 'DRIVER_CODO_%s_FK' %lado, 'DRIVER_HOMBRO_%s_FK' %lado)

	#CREAR FK DE LOS BRAZOS (TERMINA)




	#CONSTRAINS DEDOS(COMIENZA)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_1' %lado, 'MANO_%s' %lado)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_2' %lado, 'DRIVER_INDEX_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_2' %lado, 'DRIVER_MIDDLE_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_2' %lado, 'DRIVER_CANCEL_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_2' %lado, 'DRIVER_PINKY_%s_1' %lado)
	#cmds.parent( 'GRP_DRIVER_THUMB_%s_2' %lado, 'DRIVER_THUMB_%s_1' %lado)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_3' %lado, 'DRIVER_INDEX_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_3' %lado, 'DRIVER_MIDDLE_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_3' %lado, 'DRIVER_CANCEL_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_3' %lado, 'DRIVER_PINKY_%s_2' %lado)
	#cmds.parent( 'GRP_DRIVER_THUMB_%s_3' %lado, 'DRIVER_THUMB_%s_2' %lado)





	cmds.select('DRIVER_INDEX_%s_1' %lado, 'DRIVER_MIDDLE_%s_1' %lado, 'DRIVER_CANCEL_%s_1' %lado, 'DRIVER_PINKY_%s_1' %lado,
		'DRIVER_THUMB_%s_1' %lado)

	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 





	cmds.orientConstraint( 'DRIVER_INDEX_%s_1' %lado, 'INDEX_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_INDEX_%s_2' %lado, 'INDEX_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_INDEX_%s_3' %lado, 'INDEX_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_1' %lado, 'MIDDLE_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_2' %lado, 'MIDDLE_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_3' %lado, 'MIDDLE_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_CANCEL_%s_1' %lado, 'CANCEL_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_CANCEL_%s_2' %lado, 'CANCEL_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_CANCEL_%s_3' %lado, 'CANCEL_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_PINKY_%s_1' %lado, 'PINKY_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_PINKY_%s_2' %lado, 'PINKY_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_PINKY_%s_3' %lado, 'PINKY_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_THUMB_%s_1' %lado, 'THUMB_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_THUMB_%s_2' %lado, 'THUMB_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_THUMB_%s_3' %lado, 'THUMB_%s_3' %lado, mo=1)

	#CONSTRAINS DEDOS(COMIENZA)




	#CONECTAR LA ROTACION SECUNDARIA DEL CODO(COMIENZA)

	cmds.connectAttr( 'DRIVER_MANO_%s.CORRECION_CODO' %lado, 'CODO_SEC_%s_IK.rotateX' %lado)

	cmds.connectAttr( 'DRIVER_MANO_%s_FK.CORRECION_CODO' %lado, 'CODO_SEC_%s_FK.rotateX' %lado)

	#CONECTAR LA ROTACION SECUNDARIA DEL CODO(COMIENZA)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_2' %lado, 'DRIVER_THUMB_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_3' %lado, 'DRIVER_THUMB_%s_2' %lado)
















	nombredriver = 'DRIVER_PIE_DER'

	lado = 'DER'




	#CREAR IK PIERNAS (COMIENZA)

	cmds.ikHandle( sj='PIERNA_%s' %lado, ee='TALON_%s' %lado, sol = 'ikRPsolver', name = 'IK_TALON_%s' %lado )

	cmds.ikHandle( sj='TALON_%s' %lado, ee='DEDOS_PIE_%s' %lado, sol = 'ikSCsolver', name = 'IK_PIE_%s' %lado )

	cmds.ikHandle( sj='DEDOS_PIE_%s' %lado, ee='PUNTA_PIE_%s' %lado, sol = 'ikSCsolver', name = 'IK_DEDOS_PIE_%s' %lado )

	#CREAR IK PIERNAS (TERMINA)




	#CONECTAR IK CON JOINTS (COMIENZA)

	cmds.pointConstraint( 'REV_%s_4' %lado, 'IK_TALON_%s' %lado, mo =1 )

	cmds.parent( 'IK_PIE_%s' %lado, 'REV_%s_3'%lado )

	cmds.parent( 'IK_DEDOS_PIE_%s' %lado, 'REV_%s_2'%lado )

	cmds.parent( 'REV_%s_1' %lado, '%s' %nombredriver)

	cmds.parent( 'DRIVER_TOE_FINGERS_%s' %lado, 'DRIVER_HEEL_%s' %lado )

	cmds.pointConstraint( 'DRIVER_TOE_FINGERS_%s' %lado, 'IK_DEDOS_PIE_%s' %lado, mo =1 )

	#CONECTAR IK CON JOINTS (TERMINA)



	#CREAR POLE VECTOR RODILLA (COMIENZA)

	cmds.poleVectorConstraint( 'DRIVER_RODILLA_%s' %lado, 'IK_TALON_%s' %lado, w =  1)

	#CREAR POLE VECTOR RODILLA (TERMINA)



	#CURVA DE REFERENCIA DE LAS RODILLAS (COMIENZA)

	cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=1, sl2=1, n = 'cuadradotemp')

	cmds.ungroup( 'cuadradotemp' )

	cmds.delete( 'rightcuadradotemp', 'leftcuadradotemp', 'bottomcuadradotemp' )

	cmds.rename('topcuadradotemp', 'CRV_REFR_RODILLA_%s' %lado)

	cmds.select( 'CRV_REFR_RODILLA_%s.cv[1]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_RODILLA_1' )

	cmds.rename('CLR_RODILLA_1Handle', 'CLR_RODILLA_%s_1' %lado)

	cmds.select( 'CRV_REFR_RODILLA_%s.cv[0]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_RODILLA_2' )

	cmds.rename('CLR_RODILLA_2Handle', 'CLR_RODILLA_%s_2' %lado)

	cmds.pointConstraint( 'RODILLA_%s' %lado, 'CLR_RODILLA_%s_1' %lado )

	cmds.pointConstraint( 'DRIVER_RODILLA_%s' %lado, 'CLR_RODILLA_%s_2' %lado )

	cmds.setAttr( 'CRV_REFR_RODILLA_%s.template' %lado, 1)

	#CURVA DE REFERENCIA DE LAS RODILLAS (TERMINA)




	#CONECTA LAS CURVAS DEL PIE(COMIENZA)

	cmds.parent( 'DRIVER_HEEL_%s' %lado, 'DRIVER_PIE_%s' %lado)
	cmds.parent( 'DRIVER_TOE_%s' %lado, 'DRIVER_HEEL_%s' %lado)
	cmds.parent( 'DRIVER_BALL_%s' %lado, 'DRIVER_TOE_%s' %lado)

	cmds.orientConstraint( 'DRIVER_HEEL_%s' %lado, 'REV_%s_1' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_BALL_%s' %lado, 'REV_%s_3' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_TOE_%s' %lado, 'REV_%s_2' %lado, mo=1 )

	#CONECTA LAS CURVAS DEL PIE(TERMINA)



	#COMIENZAN LAS MANOS

	nombredriver = 'DRIVER_MANO_DER'



	#CREAR CURVA DE REFERENCIA BRAZO_IK(COMIENZA)

	cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=1, sl2=1, n = 'cuadradotemp')

	cmds.ungroup( 'cuadradotemp' )

	cmds.delete( 'rightcuadradotemp', 'leftcuadradotemp', 'bottomcuadradotemp' )

	cmds.rename('topcuadradotemp', 'crv_refr_brazo_%s' %lado)

	cmds.select( 'crv_refr_brazo_%s.cv[1]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_CODO_1' )

	cmds.rename('CLR_CODO_1Handle', 'CLR_CODO_%s_1' %lado)

	cmds.select( 'crv_refr_brazo_%s.cv[0]' %lado, visible=True )

	cmds.cluster( rel=True, name = 'CLR_CODO_2' )

	cmds.rename('CLR_CODO_2Handle', 'CLR_CODO_%s_2' %lado)

	cmds.pointConstraint( 'CODO_%s' %lado, 'CLR_CODO_%s_1' %lado )

	cmds.pointConstraint( 'DRIVER_CODO_%s' %lado, 'CLR_CODO_%s_2' %lado )

	cmds.setAttr( 'crv_refr_brazo_%s.template' %lado, 1)

	#CREAR CURVA DE REFERENCIA BRAZO_IK(TERMINA)




	#CREAR UNIONES ENTRE LOS HUESOS DE LOS BRAZOS Y SWITCH(COMIENZA)

	cmds.parentConstraint( 'HOMBRO_%s_IK' %lado, 'HOMBRO_%s' %lado, mo=1, n='PC_HOMBRO_%s_IK' %lado)
	cmds.parentConstraint( 'CODO_%s_IK' %lado, 'CODO_%s' %lado, mo=1, n='PC_CODO_%s_IK' %lado)
	cmds.parentConstraint( 'CODO_SEC_%s_IK' %lado, 'CODO_SEC_%s' %lado, mo=1, n='PC_CODO_SEC_%s_IK' %lado)
	cmds.parentConstraint( 'MANO_%s_IK' %lado, 'MANO_%s' %lado, mo=1, n='PC_MANO_%s_IK' %lado)


	cmds.parentConstraint( 'HOMBRO_%s_FK' %lado, 'HOMBRO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'CODO_%s_FK' %lado, 'CODO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'CODO_SEC_%s_FK' %lado, 'CODO_SEC_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)
	cmds.parentConstraint( 'MANO_%s_FK' %lado, 'MANO_%s' %lado, mo=1, n='PC_HOMBRO_%s_FK' %lado)



	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0'  %(lado, lado), 0 )



	cmds.setAttr( 'crv_refr_brazo_%s.visibility' %lado, 0)
	cmds.setAttr( 'HOMBRO_%s_IK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_CODO_%s.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_MANO_%s.visibility' %lado, 0)

	cmds.setAttr( 'HOMBRO_%s_FK.visibility' %lado, 1 )
	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_CODO_%s_FK.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_MANO_%s_FK.visibility' %lado, 1)




	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )


	cmds.setDrivenKeyframe( 'crv_refr_brazo_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado)
	cmds.setDrivenKeyframe( 'HOMBRO_%s_IK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )



	cmds.setAttr( 'DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 1 )



	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0'  %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0'  %(lado, lado), 1 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0'  %(lado, lado), 1 )

	cmds.setAttr( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1'  %(lado, lado), 0 )
	cmds.setAttr( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1'  %(lado, lado), 0 )




	cmds.setAttr( 'crv_refr_brazo_%s.visibility' %lado, 1)
	cmds.setAttr( 'HOMBRO_%s_IK.visibility' %lado, 1 )
	cmds.setAttr( 'DRIVER_CODO_%s.visibility' %lado, 1)
	cmds.setAttr( 'DRIVER_MANO_%s.visibility' %lado, 1)


	cmds.setAttr( 'HOMBRO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_CODO_%s_FK.visibility' %lado, 0)
	cmds.setAttr( 'DRIVER_MANO_%s_FK.visibility' %lado, 0)



	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_IKW0' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.HOMBRO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.CODO_SEC_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'PC_HOMBRO_%s_FK.MANO_%s_FKW1' %(lado, lado), cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )


	cmds.setDrivenKeyframe( 'crv_refr_brazo_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado)
	cmds.setDrivenKeyframe( 'HOMBRO_%s_IK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	cmds.setDrivenKeyframe( 'DRIVER_HOMBRO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s_FK.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_CODO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )
	cmds.setDrivenKeyframe( 'DRIVER_MANO_%s.visibility' %lado, cd='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado )

	#CREAR UNIONES ENTRE LOS HUESOS DE LOS BRAZOS Y SWITCH(TERMINA)




	#CREAR IK DE LOS BRAZOS y curva de refrencia (COMIENZA)

	cmds.ikHandle( sj='HOMBRO_%s_IK' %lado, ee='CODO_SEC_%s_IK' %lado, sol = 'ikRPsolver', name = 'IK_BRAZO_%s' %lado )

	cmds.orientConstraint( 'DRIVER_MANO_%s' %lado, 'MANO_%s_IK' %lado, mo=1 )

	cmds.spaceLocator(n='LOC_BRAZO_%s' %lado)
	cmds.pointConstraint( 'MANO_%s_IK' %lado, 'LOC_BRAZO_%s' %lado )

	PX = cmds.getAttr('LOC_BRAZO_%s.tx' %lado)
	PY = cmds.getAttr('LOC_BRAZO_%s.ty' %lado)
	PZ = cmds.getAttr('LOC_BRAZO_%s.tz' %lado)

	cmds.move(PX, PY, PZ, "effector8.scalePivot","effector8.rotatePivot", absolute=True)

	cmds.move(PX, PY, PZ, 'IK_BRAZO_%s' %lado)

	cmds.delete('LOC_BRAZO_%s' %lado)

	cmds.poleVectorConstraint( 'DRIVER_CODO_%s' %lado, 'IK_BRAZO_%s' %lado, w=1, n='POLEA_BRAZO_%s' %lado)

	#CREAR IK DE LOS BRAZOS (TERMINA)




	#CREAR FK DE LOS BRAZOS (COMIENZA)

	cmds.orientConstraint( 'DRIVER_HOMBRO_%s_FK' %lado, 'HOMBRO_%s_FK' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_CODO_%s_FK' %lado, 'CODO_%s_FK' %lado, mo=1 )
	cmds.orientConstraint( 'DRIVER_MANO_%s_FK' %lado, 'MANO_%s_FK' %lado, mo=1 )


	cmds.parent( 'DRIVER_MANO_%s_FK' %lado, 'DRIVER_CODO_%s_FK' %lado)
	cmds.parent( 'DRIVER_CODO_%s_FK' %lado, 'DRIVER_HOMBRO_%s_FK' %lado)

	#CREAR FK DE LOS BRAZOS (TERMINA)




	#CONSTRAINS DEDOS(COMIENZA)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_1' %lado, 'MANO_%s' %lado)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_1' %lado, 'MANO_%s' %lado)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_2' %lado, 'DRIVER_INDEX_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_2' %lado, 'DRIVER_MIDDLE_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_2' %lado, 'DRIVER_CANCEL_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_2' %lado, 'DRIVER_PINKY_%s_1' %lado)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_2' %lado, 'DRIVER_THUMB_%s_1' %lado)

	cmds.parent( 'GRP_DRIVER_INDEX_%s_3' %lado, 'DRIVER_INDEX_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_MIDDLE_%s_3' %lado, 'DRIVER_MIDDLE_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_CANCEL_%s_3' %lado, 'DRIVER_CANCEL_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_PINKY_%s_3' %lado, 'DRIVER_PINKY_%s_2' %lado)
	cmds.parent( 'GRP_DRIVER_THUMB_%s_3' %lado, 'DRIVER_THUMB_%s_2' %lado)





	cmds.select('DRIVER_INDEX_%s_1' %lado, 'DRIVER_MIDDLE_%s_1' %lado, 'DRIVER_CANCEL_%s_1' %lado, 'DRIVER_PINKY_%s_1' %lado,
		'DRIVER_THUMB_%s_1' %lado)

	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 





	cmds.orientConstraint( 'DRIVER_INDEX_%s_1' %lado, 'INDEX_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_INDEX_%s_2' %lado, 'INDEX_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_INDEX_%s_3' %lado, 'INDEX_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_1' %lado, 'MIDDLE_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_2' %lado, 'MIDDLE_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_MIDDLE_%s_3' %lado, 'MIDDLE_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_CANCEL_%s_1' %lado, 'CANCEL_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_CANCEL_%s_2' %lado, 'CANCEL_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_CANCEL_%s_3' %lado, 'CANCEL_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_PINKY_%s_1' %lado, 'PINKY_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_PINKY_%s_2' %lado, 'PINKY_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_PINKY_%s_3' %lado, 'PINKY_%s_3' %lado, mo=1)

	cmds.orientConstraint( 'DRIVER_THUMB_%s_1' %lado, 'THUMB_%s_1' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_THUMB_%s_2' %lado, 'THUMB_%s_2' %lado, mo=1)
	cmds.orientConstraint( 'DRIVER_THUMB_%s_3' %lado, 'THUMB_%s_3' %lado, mo=1)

	#CONSTRAINS DEDOS(COMIENZA)




	#CONECTAR LA ROTACION SECUNDARIA DEL CODO(COMIENZA)

	cmds.connectAttr( 'DRIVER_MANO_%s.CORRECION_CODO' %lado, 'CODO_SEC_%s_IK.rotateX' %lado)

	cmds.connectAttr( 'DRIVER_MANO_%s_FK.CORRECION_CODO' %lado, 'CODO_SEC_%s_FK.rotateX' %lado)

	#CONECTAR LA ROTACION SECUNDARIA DEL CODO(COMIENZA)













	#MULTIPLY DIVIDES (COMIENZA)

	myShader = cmds.shadingNode('multiplyDivide', asShader= True, name ='MULTY_CUELLO', au =1 )
	cmds.connectAttr( 'DRIVER_CABEZA.rotateX', 'MULTY_CUELLO.input1X' )
	cmds.connectAttr( 'DRIVER_CABEZA.rotateY', 'MULTY_CUELLO.input1Y' )
	cmds.connectAttr( 'DRIVER_CABEZA.rotateZ', 'MULTY_CUELLO.input1Z' )

	cmds.connectAttr( 'MULTY_CUELLO.outputX', 'CUELLO_SEC.rotateZ' )
	cmds.connectAttr( 'MULTY_CUELLO.outputY', 'CUELLO_SEC.rotateX' )
	cmds.connectAttr( 'MULTY_CUELLO.outputZ', 'CUELLO_SEC.rotateY' )

	cmds.setAttr( 'MULTY_CUELLO.input2X', -0.35 )
	cmds.setAttr( 'MULTY_CUELLO.input2Y',  0.35 )
	cmds.setAttr( 'MULTY_CUELLO.input2Z', -0.35 )

	#MULTIPLY DIVIDES (TERMINA)



	#CREAR LAYER Y OCULTAR BASURA(COMIENZA)

	cmds.createDisplayLayer( noRecurse=True, name='no_tocar' )
	cmds.editDisplayLayerMembers( 'no_tocar', 'IK_BRAZO_IZQ', 'IK_BRAZO_DER', 'IK_TALON_IZQ', 'IK_TALON_DER',
	 	'IK_PIE_IZQ', 'IK_PIE_DER', 'IK_DEDOS_PIE_IZQ', 'IK_DEDOS_PIE_DER', 'CLR_CODO_IZQ_1', 'CLR_CODO_IZQ_2',
	  	'CLR_CODO_DER_1', 'CLR_CODO_DER_2', 'REV_IZQ_1', 'REV_DER_1', 'CLR_RODILLA_IZQ_1', 'CLR_RODILLA_DER_1', 
	  	'CLR_RODILLA_IZQ_2', 'CLR_RODILLA_DER_2')

	#CREAR LAYER Y OCULTAR BASURA(TERMINA)




	#CAMBIA COLORES OVERRIDES (COMIENZA)

	cmds.setAttr( 'MASTER.overrideEnabled', 1 )
	cmds.setAttr( 'MASTER.overrideColor', 17 )

	cmds.setAttr( 'DRIVER_OJO_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_OJO_IZQ.overrideColor', 6 )

	cmds.setAttr( 'DRIVER_OJO_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_OJO_DER.overrideColor', 13 )

	cmds.setAttr( 'DRIVER_PINKY_SEC_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_PINKY_SEC_IZQ.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_MANO_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_MANO_IZQ.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_CODO_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CODO_IZQ.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_CLAVICULA_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CLAVICULA_IZQ.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_PIE_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_PIE_IZQ.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_RODILLA_IZQ.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_RODILLA_IZQ.overrideColor', 6 )

	cmds.setAttr( 'DRIVER_CANCEL_IZQ_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CANCEL_IZQ_1.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_MIDDLE_IZQ_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_MIDDLE_IZQ_1.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_INDEX_IZQ_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_INDEX_IZQ_1.overrideColor', 6 )
	cmds.setAttr( 'DRIVER_THUMB_IZQ_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_THUMB_IZQ_1.overrideColor', 6 )



	cmds.setAttr( 'DRIVER_PINKY_SEC_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_PINKY_SEC_DER.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_MANO_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_MANO_DER.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_CODO_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CODO_DER.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_CLAVICULA_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CLAVICULA_DER.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_PIE_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_PIE_DER.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_RODILLA_DER.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_RODILLA_DER.overrideColor', 13 )

	cmds.setAttr( 'DRIVER_CANCEL_DER_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CANCEL_DER_1.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_MIDDLE_DER_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_MIDDLE_DER_1.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_INDEX_DER_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_INDEX_DER_1.overrideColor', 13 )
	cmds.setAttr( 'DRIVER_THUMB_DER_1.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_THUMB_DER_1.overrideColor', 13 )


	cmds.setAttr( 'MOVE_ALL.overrideEnabled', 1 )
	cmds.setAttr( 'MOVE_ALL.overrideColor', 18 )
	cmds.setAttr( 'DRIVER_CINTURA.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_CINTURA.overrideColor', 18 )
	cmds.setAttr( 'DRIVER_ROOT.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_ROOT.overrideColor', 17 )
	cmds.setAttr( 'DRIVER_COLUMNA_BOTTOM.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_COLUMNA_BOTTOM.overrideColor', 18 )
	cmds.setAttr( 'DRIVER_COLUMNA_TOP.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_COLUMNA_TOP.overrideColor', 17 )
	cmds.setAttr( 'DRIVER_BOCA.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_BOCA.overrideColor', 18 )
	cmds.setAttr( 'DRIVER_DIENTES_TOP.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_DIENTES_TOP.overrideColor', 18 )

	cmds.setAttr( 'ROOT.overrideEnabled', 1 )
	cmds.setAttr( 'ROOT.overrideColor', 1 )

	#CAMBIA COLORES OVERRIDES (TERMINA)




	#CREAR ATRIBUTOS PRENDIDO APAGADO CABEZA, PIERNAS ETC...(COMIENZA)

	cmds.addAttr('MASTER', longName='CUERPO', at = 'bool')
	cmds.setAttr('MASTER.CUERPO', channelBox = 1, keyable=1)
	cmds.addAttr('MASTER', longName='PIERNAS', at = 'bool')
	cmds.setAttr('MASTER.PIERNAS' , channelBox = 1, keyable=1)
	cmds.addAttr('DRIVER_CABEZA', longName='VISIBILITY_BS', at = 'bool')
	cmds.setAttr('DRIVER_CABEZA.VISIBILITY_BS' , channelBox = 1, keyable=1)

	cmds.setAttr('MASTER.CUERPO', 1)

	cmds.setAttr('MASTER.PIERNAS' , 1)


	#CREAR ATRIBUTOS PRENDIDO APAGADO CABEZA, PIERNAS ETC...(TERMINA)




	#CONECTAR ATRIBUTOS DE VISIBILIDAD CON DRIVERS(COMIENZA)

	cmds.connectAttr( 'MASTER.CUERPO' , 'DRIVER_ROOT.visibility')
	cmds.connectAttr( 'MASTER.CUERPO' , 'DRIVER_DIENTES_TOP.visibility')
	cmds.connectAttr( 'MASTER.CUERPO' , 'DRIVER_BOCA.visibility')


	cmds.connectAttr( 'MASTER.PIERNAS' , 'DRIVER_PIE_IZQ.visibility')
	cmds.connectAttr( 'MASTER.PIERNAS' , 'DRIVER_RODILLA_IZQ.visibility')
	cmds.connectAttr( 'MASTER.PIERNAS' , 'DRIVER_PIE_DER.visibility')
	cmds.connectAttr( 'MASTER.PIERNAS' , 'DRIVER_RODILLA_DER.visibility')

	cmds.connectAttr( 'DRIVER_CABEZA.VISIBILITY_BS' , 'DRIVER_CARA.visibility')

	#CONECTAR ATRIBUTOS DE VISIBILIDAD CON DRIVERS(TERMINA)




	#SWITCH OJOS FOLLOW(COMIENZA)

	cmds.parent( 'DRIVER_OJO_IZQ', 'DRIVER_OJOS')
	cmds.parent( 'DRIVER_OJO_DER', 'DRIVER_OJOS')
	cmds.parent( 'DRIVER_OJOS', 'MOVE_ALL')

	cmds.group( 'DRIVER_OJOS', n='GRP_OJOS' )

	cmds.parentConstraint( 'CABEZA_ALTA', 'GRP_OJOS', mo=1 )


	cmds.setDrivenKeyframe( 'GRP_OJOS_parentConstraint1.CABEZA_ALTAW0', cd='DRIVER_CABEZA.SWITCH_OJOS' )

	cmds.setAttr( 'DRIVER_CABEZA.SWITCH_OJOS', 1 )
	cmds.setAttr( 'GRP_OJOS_parentConstraint1.CABEZA_ALTAW0', 0 )

	cmds.setDrivenKeyframe( 'GRP_OJOS_parentConstraint1.CABEZA_ALTAW0', cd='DRIVER_CABEZA.SWITCH_OJOS' )

	#SWITCH OJOS FOLLOW(TERMINA)




	#CONSTRAINS GENEALES(COMIENZA)

	cmds.parent( 'DRIVER_HOMBRO_IZQ_FK', 'DRIVER_CLAVICULA_IZQ')
	cmds.parent( 'DRIVER_HOMBRO_DER_FK', 'DRIVER_CLAVICULA_DER')

	cmds.parent( 'DRIVER_PINKY_SEC_IZQ', 'MANO_IZQ')
	cmds.parent( 'DRIVER_PINKY_SEC_DER', 'MANO_DER')

	cmds.select('DRIVER_PINKY_SEC_IZQ', 'DRIVER_PINKY_SEC_DER')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

	cmds.parent( 'GRP_DRIVER_PINKY_IZQ_1', 'DRIVER_PINKY_SEC_IZQ')
	cmds.parent( 'GRP_DRIVER_PINKY_DER_1', 'DRIVER_PINKY_SEC_DER')

	cmds.parent( 'DRIVER_DIENTES_BOTTOM', 'DRIVER_BOCA')
	cmds.parent( 'DRIVER_BOCA', 'CABEZA')
	cmds.parent( 'DRIVER_DIENTES_TOP', 'CABEZA')
	cmds.parent( 'DRIVER_LENGUA', 'DRIVER_BOCA')
	cmds.parent( 'DRIVER_CABEZA', 'DRIVER_COLUMNA_TOP')
	cmds.parent( 'DRIVER_CLAVICULA_IZQ', 'DRIVER_COLUMNA_TOP')
	cmds.parent( 'DRIVER_CLAVICULA_DER', 'DRIVER_COLUMNA_TOP')
	cmds.parent( 'DRIVER_MANO_DER', 'MOVE_ALL')
	cmds.parent( 'DRIVER_MANO_IZQ', 'MOVE_ALL')
	cmds.parent( 'DRIVER_CODO_IZQ', 'MOVE_ALL')
	cmds.parent( 'DRIVER_CODO_DER', 'MOVE_ALL')
	cmds.parent( 'DRIVER_COLUMNA_TOP', 'DRIVER_COLUMNA_MIDDLE')
	cmds.parent( 'DRIVER_COLUMNA_MIDDLE', 'DRIVER_COLUMNA_BOTTOM')
	cmds.parent( 'DRIVER_COLUMNA_BOTTOM', 'DRIVER_ROOT')
	cmds.parent( 'DRIVER_CINTURA', 'DRIVER_ROOT')
	cmds.parent( 'DRIVER_RODILLA_DER', 'MOVE_ALL')
	cmds.parent( 'DRIVER_RODILLA_IZQ', 'MOVE_ALL')
	cmds.parent( 'DRIVER_PIE_DER', 'MOVE_ALL')
	cmds.parent( 'DRIVER_PIE_IZQ', 'MOVE_ALL')
	cmds.parent( 'DRIVER_ROOT', 'MOVE_ALL')
	cmds.parent( 'MOVE_ALL', 'MASTER')



	cmds.select('DRIVER_BOCA', 'DRIVER_DIENTES_TOP')
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 



	cmds.parent( 'IK_BRAZO_IZQ', 'MOVE_ALL')
	cmds.parent( 'IK_BRAZO_DER', 'MOVE_ALL')
	cmds.parent( 'IK_TALON_IZQ', 'MOVE_ALL')
	cmds.parent( 'IK_TALON_DER', 'MOVE_ALL')


	cmds.parent( 'ROOT', 'MOVE_ALL')

	cmds.orientConstraint( 'DRIVER_CINTURA', 'CINTURA', mo=1)
	cmds.parentConstraint( 'DRIVER_ROOT', 'ROOT', mo=1)
	cmds.orientConstraint( 'DRIVER_COLUMNA_BOTTOM', 'COLUMNA_BAJA', mo=1)
	cmds.orientConstraint( 'DRIVER_COLUMNA_MIDDLE', 'COLUMNA_MEDIA', mo=1)
	cmds.orientConstraint( 'DRIVER_COLUMNA_TOP', 'COLUMNA_ALTA', mo=1)
	cmds.orientConstraint( 'DRIVER_CABEZA', 'CUELLO', mo=1)
	cmds.orientConstraint( 'DRIVER_CLAVICULA_IZQ', 'CLAVICULA_IZQ', mo=1 )
	cmds.orientConstraint( 'DRIVER_CLAVICULA_DER', 'CLAVICULA_DER', mo=1 )
	cmds.parentConstraint( 'DRIVER_DIENTES_TOP', 'DIENTES_ARRIBA', mo=1)
	cmds.parentConstraint( 'DRIVER_DIENTES_BOTTOM', 'DIENTES_BAJA', mo=1)
	cmds.orientConstraint( 'DRIVER_BOCA', 'BOCA_1', mo=1 )
	cmds.parentConstraint( 'DRIVER_LENGUA', 'LENGUA_2', mo=1 )
	cmds.aimConstraint( 'DRIVER_OJO_IZQ', 'OJO_IZQ', mo=1 )
	cmds.aimConstraint( 'DRIVER_OJO_DER', 'OJO_DER', mo=1 )



	cmds.orientConstraint( 'DRIVER_PINKY_SEC_IZQ', 'PINKY_SEC_IZQ', mo=1)
	cmds.orientConstraint( 'DRIVER_PINKY_SEC_DER', 'PINKY_SEC_DER', mo=1)
	cmds.pointConstraint( 'DRIVER_MANO_IZQ', 'IK_BRAZO_IZQ', mo=1 )
	cmds.pointConstraint( 'DRIVER_MANO_DER', 'IK_BRAZO_DER', mo=1 )

	#CONSTRAINS GENEALES(TERMINA)





	#BLOQUEAR Y OCULTAR ATRIBUTOS(COMIENZA)

	cmds.setAttr('DRIVER_OJO_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_OJO_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_OJO_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CABEZA.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CABEZA.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_LENGUA.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_LENGUA.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_LENGUA.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_LENGUA.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_BOCA.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BOCA.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_DIENTES_TOP.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_TOP.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_TOP.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_TOP.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_DIENTES_BOTTOM.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_BOTTOM.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_BOTTOM.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_DIENTES_BOTTOM.v', channelBox = 0, keyable=0, l=1)


	cmds.setAttr('DRIVER_CLAVICULA_IZQ.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CLAVICULA_DER.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CLAVICULA_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CODO_IZQ.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CODO_DER.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MANO_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MANO_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER.v', channelBox = 0, keyable=0, l=1)



	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_SEC_DER.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_SEC_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_IZQ_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_DER_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_IZQ_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_DER_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_IZQ_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_IZQ_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PINKY_DER_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PINKY_DER_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_IZQ_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_DER_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_IZQ_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_DER_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_IZQ_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_IZQ_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CANCEL_DER_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CANCEL_DER_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_DER_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_DER_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_IZQ_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MIDDLE_DER_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MIDDLE_DER_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_IZQ_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_DER_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_IZQ_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_DER_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_IZQ_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_IZQ_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_INDEX_DER_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_INDEX_DER_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_IZQ_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_DER_1.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_1.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_IZQ_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_DER_2.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_2.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_IZQ_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_IZQ_3.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_THUMB_DER_3.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_THUMB_DER_3.v', channelBox = 0, keyable=0, l=1)




	cmds.setAttr('DRIVER_COLUMNA_TOP.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_TOP.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_MIDDLE.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_COLUMNA_BOTTOM.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_ROOT.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_ROOT.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_ROOT.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_ROOT.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CINTURA.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CINTURA.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_RODILLA_IZQ.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_RODILLA_DER.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_RODILLA_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PIE_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_PIE_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_PIE_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('MOVE_ALL.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('MOVE_ALL.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('MOVE_ALL.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('MOVE_ALL.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('MASTER.v', channelBox = 0, keyable=0, l=1)



	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_IZQ_FK.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CODO_IZQ_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_IZQ_FK.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MANO_IZQ_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_IZQ_FK.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_HOMBRO_DER_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HOMBRO_DER_FK.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_CODO_DER_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_CODO_DER_FK.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_MANO_DER_FK.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_MANO_DER_FK.v', channelBox = 0, keyable=0, l=1)


	cmds.setAttr('DRIVER_HEEL_IZQ.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_BALL_IZQ.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_TOE_IZQ.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_IZQ.v', channelBox = 0, keyable=0, l=1)


	cmds.setAttr('DRIVER_HEEL_DER.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_HEEL_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_BALL_DER.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_BALL_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_TOE_DER.tx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.ty', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.tz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_DER.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_IZQ.v', channelBox = 0, keyable=0, l=1)

	cmds.setAttr('DRIVER_TOE_FINGERS_DER.rx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.ry', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.rz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.sx', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.sy', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.sz', channelBox = 0, keyable=0, l=1)
	cmds.setAttr('DRIVER_TOE_FINGERS_DER.v', channelBox = 0, keyable=0, l=1)

	#BLOQUEAR Y OCULTAR ATRIBUTOS(TERMINA)




	#GRUPO GENERAL(COMIENZA)

	cmds.group( 'MASTER', 'CRV_REFR_RODILLA_IZQ', 'CLR_RODILLA_IZQ_1', 'CLR_RODILLA_IZQ_2', 
		'crv_refr_brazo_IZQ', 'CLR_CODO_IZQ_1', 'CLR_CODO_IZQ_2', 'CRV_REFR_RODILLA_DER', 
		'CLR_RODILLA_DER_1', 'CLR_RODILLA_DER_2', 'crv_refr_brazo_DER', 'CLR_CODO_DER_1', 
		'CLR_CODO_DER_2', 'GRP_GEO', n='GRP_RIGG' )

	#GRUPO GENERAL(TERMINA)



	#EMPARENTAMIENTO Y CREACION DE BLENDS CARA(COMIENZA)

	cmds.parent( 'DRIVER_CARA', 'MASTER')

	#EMPARENTAMIENTO Y CREACION DE BLENDS CARA(TERMINA)


	cmds.setAttr("DRIVER_CODO_IZQ_FK.rotateX", l=True)
	cmds.setAttr("DRIVER_CODO_IZQ_FK.rotateZ", l=True)
	cmds.setAttr("DRIVER_CODO_IZQ_FK.rotateX", l=True)
	cmds.setAttr("DRIVER_CODO_IZQ_FK.rotateZ", l=True)