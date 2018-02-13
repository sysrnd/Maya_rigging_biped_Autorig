import maya.cmds as cmds
#HUESOS CREAR CADENA DEL ROOT HACIA ARRIBA, HE IR ACOMPLETANDO LA CADENA HACIA ABAJO , LA MANO DE IZQUIERDA A DERECHA Y NO OLVIDAR EL REVERSE
def autoRigAnderPte1(*args):
	#CREAR LOCATORS(COMIENZA)
	for loc in xrange(1, 54):
		cmds.spaceLocator(n= 'LOC_' + str(loc))
	#CREAR LOCATORS(TERMINA)


	#ACOMODAR LOCATORS(COMIENZA)

	cmds.pointConstraint( 'R_ROOT', 'LOC_1' )
	cmds.pointConstraint( 'R_COLUMNA_BAJA', 'LOC_2' )
	cmds.pointConstraint( 'R_COLUMNA_MEDIA', 'LOC_3' )
	cmds.pointConstraint( 'R_COLUMNA_ALTA', 'LOC_4' )
	cmds.pointConstraint( 'R_CUELLO', 'LOC_5' )
	cmds.pointConstraint( 'R_CUELLO_SEC', 'LOC_6' )
	cmds.pointConstraint( 'R_CABEZA', 'LOC_7' )
	cmds.pointConstraint( 'R_CABEZA_ALTA', 'LOC_8' )
	cmds.pointConstraint( 'R_DIENTES_ARRIBA', 'LOC_9' )
	cmds.pointConstraint( 'R_MANDIBULA', 'LOC_10' )
	cmds.pointConstraint( 'R_LENGUA_1', 'LOC_11' )
	cmds.pointConstraint( 'R_LENGUA_2', 'LOC_12' )
	cmds.pointConstraint( 'R_LENGUA_3', 'LOC_13' )
	cmds.pointConstraint( 'R_BOCA_1', 'LOC_14' )
	cmds.pointConstraint( 'R_BOCA_2', 'LOC_15' )
	cmds.pointConstraint( 'R_DIENTES_BAJA', 'LOC_16' )
	cmds.pointConstraint( 'R_CLAVICULA_IZQ', 'LOC_17' )
	cmds.pointConstraint( 'R_HOMBRO_IZQ', 'LOC_18' )
	cmds.pointConstraint( 'R_CODO_IZQ', 'LOC_19' )
	cmds.pointConstraint( 'R_CODO_SEC_IZQ', 'LOC_20' )
	cmds.pointConstraint( 'R_MANO_IZQ', 'LOC_21' )
	cmds.pointConstraint( 'R_MIDDLE_IZQ_1', 'LOC_22' )
	cmds.pointConstraint( 'R_MIDDLE_IZQ_2', 'LOC_23' )
	cmds.pointConstraint( 'R_MIDDLE_IZQ_3', 'LOC_24' )
	cmds.pointConstraint( 'R_MIDDLE_IZQ_4', 'LOC_25' )
	cmds.pointConstraint( 'R_PINKY_SEC_IZQ', 'LOC_26' )
	cmds.pointConstraint( 'R_PINKY_IZQ_1', 'LOC_27' )
	cmds.pointConstraint( 'R_PINKY_IZQ_2', 'LOC_28' )
	cmds.pointConstraint( 'R_PINKY_IZQ_3', 'LOC_29' )
	cmds.pointConstraint( 'R_PINKY_IZQ_4', 'LOC_30' )
	cmds.pointConstraint( 'R_CANCEL_IZQ_1', 'LOC_31' )
	cmds.pointConstraint( 'R_CANCEL_IZQ_2', 'LOC_32' )
	cmds.pointConstraint( 'R_CANCEL_IZQ_3', 'LOC_33' )
	cmds.pointConstraint( 'R_CANCEL_IZQ_4', 'LOC_34' )
	cmds.pointConstraint( 'R_INDEX_IZQ_1', 'LOC_35' )
	cmds.pointConstraint( 'R_INDEX_IZQ_2', 'LOC_36' )
	cmds.pointConstraint( 'R_INDEX_IZQ_3', 'LOC_37' )
	cmds.pointConstraint( 'R_INDEX_IZQ_4', 'LOC_38' )
	cmds.pointConstraint( 'R_THUMB_IZQ_1', 'LOC_39' )
	cmds.pointConstraint( 'R_THUMB_IZQ_2', 'LOC_40' )
	cmds.pointConstraint( 'R_THUMB_IZQ_3', 'LOC_41' )
	cmds.pointConstraint( 'R_THUMB_IZQ_4', 'LOC_42' )
	cmds.pointConstraint( 'R_CINTURA', 'LOC_43' )
	cmds.pointConstraint( 'R_PIERNA_IZQ', 'LOC_44' )
	cmds.pointConstraint( 'R_RODILLA_IZQ', 'LOC_45' )
	cmds.pointConstraint( 'R_TALON_IZQ', 'LOC_46' )
	cmds.pointConstraint( 'R_DEDOS_PIE_IZQ', 'LOC_47' )
	cmds.pointConstraint( 'R_PUNTA_PIE_IZQ', 'LOC_48' )
	cmds.pointConstraint( 'R_REV_IZQ_1', 'LOC_49' )
	cmds.pointConstraint( 'R_REV_IZQ_2', 'LOC_50' )
	cmds.pointConstraint( 'R_REV_IZQ_3', 'LOC_51' )
	cmds.pointConstraint( 'R_REV_IZQ_4', 'LOC_52' )
	cmds.pointConstraint( 'R_OJO_IZQ', 'LOC_53' )

	#ACOMODAR LOCATORS(TERMINA)




	#CREAR JOINTS(COMIENZA)

	cmds.select( d=True )


	PX = cmds.getAttr('LOC_1.tx')
	PY = cmds.getAttr('LOC_1.ty')
	PZ = cmds.getAttr('LOC_1.tz')
	cmds.joint( p=(PX, PY, PZ) )


	PX = cmds.getAttr('LOC_2.tx')
	PY = cmds.getAttr('LOC_2.ty')
	PZ = cmds.getAttr('LOC_2.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint1', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_3.tx')
	PY = cmds.getAttr('LOC_3.ty')
	PZ = cmds.getAttr('LOC_3.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint2', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_4.tx')
	PY = cmds.getAttr('LOC_4.ty')
	PZ = cmds.getAttr('LOC_4.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint3', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_5.tx')
	PY = cmds.getAttr('LOC_5.ty')
	PZ = cmds.getAttr('LOC_5.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint4', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_6.tx')
	PY = cmds.getAttr('LOC_6.ty')
	PZ = cmds.getAttr('LOC_6.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint5', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_7.tx')
	PY = cmds.getAttr('LOC_7.ty')
	PZ = cmds.getAttr('LOC_7.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint6', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_8.tx')
	PY = cmds.getAttr('LOC_8.ty')
	PZ = cmds.getAttr('LOC_8.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint7', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint7')



	PX = cmds.getAttr('LOC_9.tx')
	PY = cmds.getAttr('LOC_9.ty')
	PZ = cmds.getAttr('LOC_9.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint7', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint7')



	PX = cmds.getAttr('LOC_10.tx')
	PY = cmds.getAttr('LOC_10.ty')
	PZ = cmds.getAttr('LOC_10.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint7', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_11.tx')
	PY = cmds.getAttr('LOC_11.ty')
	PZ = cmds.getAttr('LOC_11.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint10', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_12.tx')
	PY = cmds.getAttr('LOC_12.ty')
	PZ = cmds.getAttr('LOC_12.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint11', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_13.tx')
	PY = cmds.getAttr('LOC_13.ty')
	PZ = cmds.getAttr('LOC_13.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint12', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint10')



	PX = cmds.getAttr('LOC_14.tx')
	PY = cmds.getAttr('LOC_14.ty')
	PZ = cmds.getAttr('LOC_14.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint10', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_15.tx')
	PY = cmds.getAttr('LOC_15.ty')
	PZ = cmds.getAttr('LOC_15.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint14', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_16.tx')
	PY = cmds.getAttr('LOC_16.ty')
	PZ = cmds.getAttr('LOC_16.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint15', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint4')



	PX = cmds.getAttr('LOC_17.tx')
	PY = cmds.getAttr('LOC_17.ty')
	PZ = cmds.getAttr('LOC_17.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint4', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_18.tx')
	PY = cmds.getAttr('LOC_18.ty')
	PZ = cmds.getAttr('LOC_18.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint17', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_19.tx')
	PY = cmds.getAttr('LOC_19.ty')
	PZ = cmds.getAttr('LOC_19.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint18', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_20.tx')
	PY = cmds.getAttr('LOC_20.ty')
	PZ = cmds.getAttr('LOC_20.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint19', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_21.tx')
	PY = cmds.getAttr('LOC_21.ty')
	PZ = cmds.getAttr('LOC_21.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint20', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_22.tx')
	PY = cmds.getAttr('LOC_22.ty')
	PZ = cmds.getAttr('LOC_22.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint21', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_23.tx')
	PY = cmds.getAttr('LOC_23.ty')
	PZ = cmds.getAttr('LOC_23.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint22', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_24.tx')
	PY = cmds.getAttr('LOC_24.ty')
	PZ = cmds.getAttr('LOC_24.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint23', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_25.tx')
	PY = cmds.getAttr('LOC_25.ty')
	PZ = cmds.getAttr('LOC_25.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint24', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint21')



	PX = cmds.getAttr('LOC_26.tx')
	PY = cmds.getAttr('LOC_26.ty')
	PZ = cmds.getAttr('LOC_26.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint21', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_27.tx')
	PY = cmds.getAttr('LOC_27.ty')
	PZ = cmds.getAttr('LOC_27.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint26', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_28.tx')
	PY = cmds.getAttr('LOC_28.ty')
	PZ = cmds.getAttr('LOC_28.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint27', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_29.tx')
	PY = cmds.getAttr('LOC_29.ty')
	PZ = cmds.getAttr('LOC_29.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint28', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_30.tx')
	PY = cmds.getAttr('LOC_30.ty')
	PZ = cmds.getAttr('LOC_30.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint29', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint21')



	PX = cmds.getAttr('LOC_31.tx')
	PY = cmds.getAttr('LOC_31.ty')
	PZ = cmds.getAttr('LOC_31.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint21', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_32.tx')
	PY = cmds.getAttr('LOC_32.ty')
	PZ = cmds.getAttr('LOC_32.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint31', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_33.tx')
	PY = cmds.getAttr('LOC_33.ty')
	PZ = cmds.getAttr('LOC_33.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint32', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_34.tx')
	PY = cmds.getAttr('LOC_34.ty')
	PZ = cmds.getAttr('LOC_34.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint33', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint21')



	PX = cmds.getAttr('LOC_35.tx')
	PY = cmds.getAttr('LOC_35.ty')
	PZ = cmds.getAttr('LOC_35.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint21', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_36.tx')
	PY = cmds.getAttr('LOC_36.ty')
	PZ = cmds.getAttr('LOC_36.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint35', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_37.tx')
	PY = cmds.getAttr('LOC_37.ty')
	PZ = cmds.getAttr('LOC_37.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint36', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_38.tx')
	PY = cmds.getAttr('LOC_38.ty')
	PZ = cmds.getAttr('LOC_38.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint37', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint21')



	PX = cmds.getAttr('LOC_39.tx')
	PY = cmds.getAttr('LOC_39.ty')
	PZ = cmds.getAttr('LOC_39.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint21', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_40.tx')
	PY = cmds.getAttr('LOC_40.ty')
	PZ = cmds.getAttr('LOC_40.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint39', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_41.tx')
	PY = cmds.getAttr('LOC_41.ty')
	PZ = cmds.getAttr('LOC_41.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint40', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_42.tx')
	PY = cmds.getAttr('LOC_42.ty')
	PZ = cmds.getAttr('LOC_42.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint41', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint1')



	PX = cmds.getAttr('LOC_43.tx')
	PY = cmds.getAttr('LOC_43.ty')
	PZ = cmds.getAttr('LOC_43.tz')
	cmds.joint( p=(PX, PY, PZ) )


	PX = cmds.getAttr('LOC_44.tx')
	PY = cmds.getAttr('LOC_44.ty')
	PZ = cmds.getAttr('LOC_44.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint43', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_45.tx')
	PY = cmds.getAttr('LOC_45.ty')
	PZ = cmds.getAttr('LOC_45.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint44', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_46.tx')
	PY = cmds.getAttr('LOC_46.ty')
	PZ = cmds.getAttr('LOC_46.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint45', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_47.tx')
	PY = cmds.getAttr('LOC_47.ty')
	PZ = cmds.getAttr('LOC_47.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint46', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_48.tx')
	PY = cmds.getAttr('LOC_48.ty')
	PZ = cmds.getAttr('LOC_48.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint47', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('R_ROOT')

	cmds.select('R_ROOT', d=1)

	PX = cmds.getAttr('LOC_49.tx')
	PY = cmds.getAttr('LOC_49.ty')
	PZ = cmds.getAttr('LOC_49.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint48', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_50.tx')
	PY = cmds.getAttr('LOC_50.ty')
	PZ = cmds.getAttr('LOC_50.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint49', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_51.tx')
	PY = cmds.getAttr('LOC_51.ty')
	PZ = cmds.getAttr('LOC_51.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint50', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_52.tx')
	PY = cmds.getAttr('LOC_52.ty')
	PZ = cmds.getAttr('LOC_52.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint51', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint8')

	PX = cmds.getAttr('LOC_53.tx')
	PY = cmds.getAttr('LOC_53.ty')
	PZ = cmds.getAttr('LOC_53.tz')
	cmds.joint( p=(PX, PY, PZ) )




	cmds.select('joint17')


	PX = cmds.getAttr('LOC_18.tx')
	PY = cmds.getAttr('LOC_18.ty')
	PZ = cmds.getAttr('LOC_18.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint17', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_19.tx')
	PY = cmds.getAttr('LOC_19.ty')
	PZ = cmds.getAttr('LOC_19.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint54', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_20.tx')
	PY = cmds.getAttr('LOC_20.ty')
	PZ = cmds.getAttr('LOC_20.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint55', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_21.tx')
	PY = cmds.getAttr('LOC_21.ty')
	PZ = cmds.getAttr('LOC_21.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint56', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_22.tx')
	PY = cmds.getAttr('LOC_22.ty')
	PZ = cmds.getAttr('LOC_22.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint57', e=True, zso=True, oj='xyz', sao = 'yup' )



	cmds.select('joint17')


	PX = cmds.getAttr('LOC_18.tx')
	PY = cmds.getAttr('LOC_18.ty')
	PZ = cmds.getAttr('LOC_18.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint17', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_19.tx')
	PY = cmds.getAttr('LOC_19.ty')
	PZ = cmds.getAttr('LOC_19.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint59', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_20.tx')
	PY = cmds.getAttr('LOC_20.ty')
	PZ = cmds.getAttr('LOC_20.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint60', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_21.tx')
	PY = cmds.getAttr('LOC_21.ty')
	PZ = cmds.getAttr('LOC_21.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint61', e=True, zso=True, oj='xyz', sao = 'yup' )

	PX = cmds.getAttr('LOC_22.tx')
	PY = cmds.getAttr('LOC_22.ty')
	PZ = cmds.getAttr('LOC_22.tz')
	cmds.joint( p=(PX, PY, PZ) )

	cmds.joint( 'joint62', e=True, zso=True, oj='xyz', sao = 'yup' )

	cmds.delete('joint58', 'joint63')


	#CREAR JOINTS(TERMINA)




	#BORRAR LOCATORS(COMIENZA)

	type = cmds.ls(type= "locator")

	cmds.select(type)

	cmds.pickWalk( direction='up' )

	cmds.delete()

	#BORRAR LOCATORS(TERMINA)




	#RENOMBRA HUESOS(COMIENZA)

	cmds.rename('joint1', 'ROOT')
	cmds.rename('joint2', 'COLUMNA_BAJA')
	cmds.rename('joint3', 'COLUMNA_MEDIA')
	cmds.rename('joint4', 'COLUMNA_ALTA')
	cmds.rename('joint5', 'CUELLO')
	cmds.rename('joint6', 'CUELLO_SEC')
	cmds.rename('joint7', 'CABEZA')
	cmds.rename('joint8', 'CABEZA_ALTA')
	cmds.rename('joint9', 'DIENTES_ARRIBA')
	cmds.rename('joint10', 'MANDIBULA')
	cmds.rename('joint11', 'LENGUA_1')
	cmds.rename('joint12', 'LENGUA_2')
	cmds.rename('joint13', 'LENGUA_3')
	cmds.rename('joint14', 'BOCA_1')
	cmds.rename('joint15', 'BOCA_2')
	cmds.rename('joint16', 'DIENTES_BAJA')
	cmds.rename('joint17', 'CLAVICULA_IZQ')
	cmds.rename('joint18', 'HOMBRO_IZQ')
	cmds.rename('joint19', 'CODO_IZQ')
	cmds.rename('joint20', 'CODO_SEC_IZQ')
	cmds.rename('joint21', 'MANO_IZQ')
	cmds.rename('joint22', 'MIDDLE_IZQ_1')
	cmds.rename('joint23', 'MIDDLE_IZQ_2')
	cmds.rename('joint24', 'MIDDLE_IZQ_3')
	cmds.rename('joint25', 'MIDDLE_IZQ_4')
	cmds.rename('joint26', 'PINKY_SEC_IZQ')
	cmds.rename('joint27', 'PINKY_IZQ_1')
	cmds.rename('joint28', 'PINKY_IZQ_2')
	cmds.rename('joint29', 'PINKY_IZQ_3')
	cmds.rename('joint30', 'PINKY_IZQ_4')
	cmds.rename('joint31', 'CANCEL_IZQ_1')
	cmds.rename('joint32', 'CANCEL_IZQ_2')
	cmds.rename('joint33', 'CANCEL_IZQ_3')
	cmds.rename('joint34', 'CANCEL_IZQ_4')
	cmds.rename('joint35', 'INDEX_IZQ_1')
	cmds.rename('joint36', 'INDEX_IZQ_2')
	cmds.rename('joint37', 'INDEX_IZQ_3')
	cmds.rename('joint38', 'INDEX_IZQ_4')
	cmds.rename('joint39', 'THUMB_IZQ_1')
	cmds.rename('joint40', 'THUMB_IZQ_2')
	cmds.rename('joint41', 'THUMB_IZQ_3')
	cmds.rename('joint42', 'THUMB_IZQ_4')
	cmds.rename('joint43', 'CINTURA')
	cmds.rename('joint44', 'PIERNA_IZQ')
	cmds.rename('joint45', 'RODILLA_IZQ')
	cmds.rename('joint46', 'TALON_IZQ')
	cmds.rename('joint47', 'DEDOS_PIE_IZQ')
	cmds.rename('joint48', 'PUNTA_PIE_IZQ')
	cmds.rename('joint49', 'REV_IZQ_1')
	cmds.rename('joint50', 'REV_IZQ_2')
	cmds.rename('joint51', 'REV_IZQ_3')
	cmds.rename('joint52', 'REV_IZQ_4')
	cmds.rename('joint53', 'OJO_IZQ')

	cmds.rename('joint54', 'HOMBRO_IZQ_IK')
	cmds.rename('joint55', 'CODO_IZQ_IK')
	cmds.rename('joint56', 'CODO_SEC_IZQ_IK')
	cmds.rename('joint57', 'MANO_IZQ_IK')

	cmds.rename('joint59', 'HOMBRO_IZQ_FK')
	cmds.rename('joint60', 'CODO_IZQ_FK')
	cmds.rename('joint61', 'CODO_SEC_IZQ_FK')
	cmds.rename('joint62', 'MANO_IZQ_FK')

	#RENOMBRA HUESOS(TERMINA)
	
	#Scale Right finger ctrls to -1 to mirrorBehaviour
	'''
	R_HandCtrls = ['DRIVER_INDEX_DER_1'
	,'DRIVER_INDEX_DER_2'
	,'DRIVER_INDEX_DER_3'
	,'DRIVER_MIDDLE_DER_1'
	,'DRIVER_MIDDLE_DER_2'
	,'DRIVER_MIDDLE_DER_3'
	,'DRIVER_CANCEL_DER_1'
	,'DRIVER_CANCEL_DER_2'
	,'DRIVER_CANCEL_DER_3'
	,'DRIVER_PINKY_DER_1'
	,'DRIVER_PINKY_DER_2'
	,'DRIVER_PINKY_DER_3'
	,'DRIVER_THUMB_DER_1'
	,'DRIVER_THUMB_DER_2'
	,'DRIVER_THUMB_DER_3']

	for ctrl in R_HandCtrls:
		cmds.setAttr(ctrl + '.scaleY', -1)
		cmds.setAttr(ctrl + '.scaleX', -1)
		if ctrl.find('THUMB') != -1:
			pass
			#cmds.setAttr(ctrl + '.rotateX', 10)
			#cmds.setAttr(ctrl + '.rotateZ', -30)
			#cmds.setAttr(ctrl + '.rotateY', 60)
	'''
	



	#REFLEJA HUESOS(COMIENZA)

	cmds.select( 'CLAVICULA_IZQ', visible=True )
	cmds.mirrorJoint(mirrorYZ=True,mirrorBehavior=True,searchReplace=('IZQ', 'DER') )

	cmds.select( 'PIERNA_IZQ', visible=True )
	cmds.mirrorJoint(mirrorYZ=True,mirrorBehavior=True,searchReplace=('IZQ', 'DER') )

	cmds.select( 'REV_IZQ_1', visible=True )
	cmds.mirrorJoint(mirrorYZ=True,mirrorBehavior=True,searchReplace=('IZQ', 'DER') )

	cmds.select( 'OJO_IZQ', visible=True )
	cmds.mirrorJoint(mirrorYZ=True,mirrorBehavior=True,searchReplace=('IZQ', 'DER') )

	#REFLEJA HUESOS(TERMINA)




	#ELIMINA HUESOS REFERENCIA (COMIENZA)

	cmds.delete( 'R_ROOT', 'R_REV_IZQ_1', 'R_REV_DER_1' )

	#ELIMINA HUESOS REFERENCIA (TERMINA)

	#ACOMODAR DRIVER(COMIENZA)

	cmds.pointConstraint( 'CINTURA', 'DRIVER_CINTURA' )
	cmds.pointConstraint( 'ROOT', 'DRIVER_ROOT' )
	cmds.pointConstraint( 'COLUMNA_BAJA', 'DRIVER_COLUMNA_BOTTOM')
	cmds.pointConstraint( 'COLUMNA_MEDIA', 'DRIVER_COLUMNA_MIDDLE' )
	cmds.pointConstraint( 'COLUMNA_ALTA', 'DRIVER_COLUMNA_TOP' )
	cmds.pointConstraint( 'CUELLO', 'DRIVER_CABEZA' )
	cmds.pointConstraint( 'CLAVICULA_IZQ', 'DRIVER_CLAVICULA_IZQ' )
	cmds.pointConstraint( 'CLAVICULA_DER', 'DRIVER_CLAVICULA_DER' )
	cmds.pointConstraint( 'MANO_IZQ', 'DRIVER_MANO_IZQ' )
	cmds.pointConstraint( 'MANO_DER', 'DRIVER_MANO_DER' )
	cmds.pointConstraint( 'DIENTES_ARRIBA', 'DRIVER_DIENTES_TOP' )
	cmds.pointConstraint( 'DIENTES_BAJA', 'DRIVER_DIENTES_BOTTOM' )
	cmds.pointConstraint( 'BOCA_1', 'DRIVER_BOCA' )
	cmds.pointConstraint( 'LENGUA_2', 'DRIVER_LENGUA' )
	cmds.pointConstraint( 'CODO_IZQ', 'DRIVER_CODO_IZQ')
	cmds.pointConstraint( 'CODO_DER', 'DRIVER_CODO_DER')
	cmds.pointConstraint( 'RODILLA_DER', 'DRIVER_RODILLA_DER')
	cmds.pointConstraint( 'RODILLA_IZQ', 'DRIVER_RODILLA_IZQ')
	cmds.pointConstraint( 'TALON_DER', 'DRIVER_PIE_DER')
	cmds.pointConstraint( 'TALON_IZQ', 'DRIVER_PIE_IZQ')
	cmds.pointConstraint( 'LENGUA_2', 'DRIVER_LENGUA')
	cmds.pointConstraint( 'PINKY_SEC_IZQ', 'DRIVER_PINKY_SEC_IZQ')
	cmds.pointConstraint( 'PINKY_SEC_DER', 'DRIVER_PINKY_SEC_DER')
	cmds.pointConstraint( 'OJO_IZQ', 'DRIVER_OJO_IZQ')
	cmds.pointConstraint( 'OJO_DER', 'DRIVER_OJO_DER')
	cmds.pointConstraint( 'REV_IZQ_1', 'DRIVER_HEEL_IZQ')
	cmds.pointConstraint( 'DEDOS_PIE_IZQ', 'DRIVER_BALL_IZQ')
	cmds.pointConstraint( 'PUNTA_PIE_IZQ', 'DRIVER_TOE_IZQ')
	cmds.pointConstraint( 'PUNTA_PIE_IZQ', 'DRIVER_TOE_FINGERS_IZQ')
	cmds.pointConstraint( 'REV_DER_1', 'DRIVER_HEEL_DER')
	cmds.pointConstraint( 'DEDOS_PIE_DER', 'DRIVER_BALL_DER')
	cmds.pointConstraint( 'PUNTA_PIE_DER', 'DRIVER_TOE_DER')
	cmds.pointConstraint( 'PUNTA_PIE_DER', 'DRIVER_TOE_FINGERS_DER')

	cmds.pointConstraint( 'HOMBRO_IZQ_FK', 'DRIVER_HOMBRO_IZQ_FK')
	cmds.pointConstraint( 'CODO_IZQ_FK', 'DRIVER_CODO_IZQ_FK')
	cmds.pointConstraint( 'MANO_IZQ_FK', 'DRIVER_MANO_IZQ_FK')
	cmds.pointConstraint( 'HOMBRO_DER_FK', 'DRIVER_HOMBRO_DER_FK')
	cmds.pointConstraint( 'CODO_DER_FK', 'DRIVER_CODO_DER_FK')
	cmds.pointConstraint( 'MANO_DER_FK', 'DRIVER_MANO_DER_FK')


	cmds.parentConstraint( 'THUMB_IZQ_1', 'GRP_DRIVER_THUMB_IZQ_1')
	cmds.parentConstraint( 'THUMB_IZQ_2', 'GRP_DRIVER_THUMB_IZQ_2')
	cmds.parentConstraint( 'THUMB_IZQ_3', 'GRP_DRIVER_THUMB_IZQ_3')
	cmds.parentConstraint( 'INDEX_IZQ_1', 'GRP_DRIVER_INDEX_IZQ_1')
	cmds.parentConstraint( 'INDEX_IZQ_2', 'GRP_DRIVER_INDEX_IZQ_2')
	cmds.parentConstraint( 'INDEX_IZQ_3', 'GRP_DRIVER_INDEX_IZQ_3')
	cmds.parentConstraint( 'MIDDLE_IZQ_1', 'GRP_DRIVER_MIDDLE_IZQ_1')
	cmds.parentConstraint( 'MIDDLE_IZQ_2', 'GRP_DRIVER_MIDDLE_IZQ_2')
	cmds.parentConstraint( 'MIDDLE_IZQ_3', 'GRP_DRIVER_MIDDLE_IZQ_3')
	cmds.parentConstraint( 'CANCEL_IZQ_1', 'GRP_DRIVER_CANCEL_IZQ_1')
	cmds.parentConstraint( 'CANCEL_IZQ_2', 'GRP_DRIVER_CANCEL_IZQ_2')
	cmds.parentConstraint( 'CANCEL_IZQ_3', 'GRP_DRIVER_CANCEL_IZQ_3')
	cmds.parentConstraint( 'PINKY_IZQ_1', 'GRP_DRIVER_PINKY_IZQ_1')
	cmds.parentConstraint( 'PINKY_IZQ_2', 'GRP_DRIVER_PINKY_IZQ_2')
	cmds.parentConstraint( 'PINKY_IZQ_3', 'GRP_DRIVER_PINKY_IZQ_3')


	cmds.parentConstraint( 'THUMB_DER_1', 'GRP_DRIVER_THUMB_DER_1')
	cmds.parentConstraint( 'THUMB_DER_2', 'GRP_DRIVER_THUMB_DER_2')
	cmds.parentConstraint( 'THUMB_DER_3', 'GRP_DRIVER_THUMB_DER_3')
	cmds.parentConstraint( 'INDEX_DER_1', 'GRP_DRIVER_INDEX_DER_1')
	cmds.parentConstraint( 'INDEX_DER_2', 'GRP_DRIVER_INDEX_DER_2')
	cmds.parentConstraint( 'INDEX_DER_3', 'GRP_DRIVER_INDEX_DER_3')
	cmds.parentConstraint( 'MIDDLE_DER_1', 'GRP_DRIVER_MIDDLE_DER_1')
	cmds.parentConstraint( 'MIDDLE_DER_2', 'GRP_DRIVER_MIDDLE_DER_2')
	cmds.parentConstraint( 'MIDDLE_DER_3', 'GRP_DRIVER_MIDDLE_DER_3')
	cmds.parentConstraint( 'CANCEL_DER_1', 'GRP_DRIVER_CANCEL_DER_1')
	cmds.parentConstraint( 'CANCEL_DER_2', 'GRP_DRIVER_CANCEL_DER_2')
	cmds.parentConstraint( 'CANCEL_DER_3', 'GRP_DRIVER_CANCEL_DER_3')
	cmds.parentConstraint( 'PINKY_DER_1', 'GRP_DRIVER_PINKY_DER_1')
	cmds.parentConstraint( 'PINKY_DER_2', 'GRP_DRIVER_PINKY_DER_2')
	cmds.parentConstraint( 'PINKY_DER_3', 'GRP_DRIVER_PINKY_DER_3')


	type = cmds.ls(type= "pointConstraint")
	cmds.delete(type)

	type = cmds.ls(type= "parentConstraint")
	cmds.delete(type)

	cmds.setAttr( 'GRP_DRIVER_THUMB_DER_1.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_THUMB_DER_2.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_THUMB_DER_3.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_INDEX_DER_1.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_INDEX_DER_2.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_INDEX_DER_3.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_MIDDLE_DER_1.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_MIDDLE_DER_2.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_MIDDLE_DER_3.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_CANCEL_DER_1.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_CANCEL_DER_2.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_CANCEL_DER_3.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_PINKY_DER_1.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_PINKY_DER_2.scaleY', -1)
	cmds.setAttr( 'GRP_DRIVER_PINKY_DER_3.scaleY', -1)

