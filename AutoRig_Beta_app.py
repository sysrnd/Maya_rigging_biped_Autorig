import maya.cmds as cmds
import maya.mel as mel
import os
import Utils.os_Find_Env.findEnv_app as findEnv
#HUESOS CREAR CADENA DEL ROOT HACIA ARRIBA, HE IR ACOMPLETANDO LA CADENA HACIA ABAJO , LA MANO DE IZQUIERDA A DERECHA Y NO OLVIDAR EL REVERESE


def autoRigAnderPte1(*args):
	cmds.button('startBtn', e=True, en=False)
	cmds.text('falangina', e=True, en=True)
	cmds.floatSlider('falanginaSlider', e=True, en=True)
	cmds.text('falangeta', e=True, en=True)
	cmds.floatSlider('falangetaSlider', e=True, en=True)
	cmds.button('finishBtn', e=True, en=True)
	#cmds.button('facialBtn', e=True, en=True)

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


	#ACOMODAR DRIVER(TERMINA)

def autoRigAnderPte2(*args):

	cmds.text('falangina', e=True, en=False)
	cmds.floatSlider('falanginaSlider', e=True, en=False)
	cmds.text('falangeta', e=True, en=False)
	cmds.floatSlider('falangetaSlider', e=True, en=False)
	cmds.button('finishBtn', e=True, en=False)
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
	#cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 
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

def windowSlider():
	'''
	mainWindow
	'''
	MKF_autoRig = "MKF_autoRig"
	windowSize = (500, 500)
	if (cmds.window(MKF_autoRig , exists=True)):
		cmds.deleteUI(MKF_autoRig)
	cmds.window(MKF_autoRig, title= MKF_autoRig, widthHeight=(windowSize[0], windowSize[1]))
	cmds.columnLayout( adjustableColumn=True )
	cmds.columnLayout( "mainColumn", adjustableColumn=True )
	cmds.button('importRigBtn', label='Import Rig', parent = "mainColumn", c=importRig, en=True)
	cmds.separator( height=5, style='in')
	cmds.button('startBtn', label='Start AutoRig', parent = "mainColumn", c=autoRigAnderPte1, en=True)
	cmds.separator( height=10, style='in')
	falanginaText = cmds.text('falangina', label='falangina', align='center', en=False)
	cmds.floatSlider('falanginaSlider', min=-180, max=180, value=0, step=1, dc=falangina, en=False)
	cmds.separator( height=10, style='in')
	falangetaText = cmds.text('falangeta', label='falangeta', align='center', en=False)
	cmds.floatSlider('falangetaSlider', min=-180, max=180, value=0, step=1, dc=falangeta, en=False)
	cmds.separator( height=15, style='none')
	cmds.button('finishBtn', label='Finish orienting', parent = "mainColumn", c=autoRigAnderPte2, en=False)
	cmds.separator( height=5, style='in')
	cmds.button('upgradesBtn',label='Rig Upgrades', parent = "mainColumn", c=rigUpgrades)
	cmds.separator( height=5, style='in')
	cmds.button('facialBtn',label='Facial rig', parent = "mainColumn", c=facialRig)


	cmds.showWindow()

def falangeta(*args):
	'''
	deals with thumb constraints
	'''
	value = cmds.floatSlider('falangetaSlider', q=True, v=True)
	cmds.setAttr('GRP_DRIVER_THUMB_IZQ_3' + '.rotateX', value)
	#cmds.setAttr('GRP_DRIVER_THUMB_DER_3' + '.rotateX', (value - 180))

def falangina(*args):
	'''
	deals with thumb constraints
	'''
	value = cmds.floatSlider('falanginaSlider', q=True, v=True)

	cmds.setAttr('GRP_DRIVER_THUMB_IZQ_2' + '.rotateX', value)
	#cmds.setAttr('GRP_DRIVER_THUMB_DER_2' + '.rotateX', (value - 180))



def rigUpgrades(*args):
	
	#import Rigging.Maya_rigging_biped_Autorig.SCRIPT_CORRECCION_03
	#reload(Rigging.Maya_rigging_biped_Autorig.SCRIPT_CORRECCION_03)

	#import Rigging.Maya_rigging_biped_Autorig.updateClavicleSwitch
	#reload(Rigging.Maya_rigging_biped_Autorig.updateClavicleSwitch)

	import Rigging.Maya_rigging_biped_Autorig.fix_ThumbOrientation
	reload(Rigging.Maya_rigging_biped_Autorig.fix_ThumbOrientation)

	#import Rigging.MKF_Autorig.Autorig_v05_23102017.Rig_update2_00
	#reload(Rigging.MKF_Autorig.Autorig_v05_23102017.Rig_update2_00)

	cmds.button('upgradesBtn', e=True, en=False)

def facialRig(*args):


	import Rigging.MKF_Autorig.Autorig_v05_23102017.wrapCejas
	reload(Rigging.MKF_Autorig.Autorig_v05_23102017.wrapCejas)

	import Rigging.MKF_Autorig.Autorig_v05_23102017.RIGG_FACIAL_03
	reload(Rigging.MKF_Autorig.Autorig_v05_23102017.RIGG_FACIAL_03) 

	cmds.button('facialBtn', e=True, en=False)

def importRig(*args):
	'''
	namespace=':' to delete namespaces
	'''
	file = findEnv.findEnvVar_('MAYA_SCRIPT_PATH', 'Scripts', 'MKF', 'RND')

	cmds.file(file + '/Rigging/Maya_rigging_biped_Autorig/RIGG_BASE.ma', type='mayaAscii', ignoreVersion=True, ra=True, mergeNamespacesOnClash=True, namespace= ':', pr=True, i=True)
windowSlider()
