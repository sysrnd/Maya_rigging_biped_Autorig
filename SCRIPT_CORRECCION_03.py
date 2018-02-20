
import maya.cmds as cmds
import maya.mel as mel

def mainCorrection():

	lados = ['DER', 'IZQ']

	for lado in lados:

		#CORRECION SWITCH RODILLA (COMIENZA)

		cmds.group('DRIVER_RODILLA_%s' %lado, n='GRP_DRIVER_RODILLA_%s' %lado)

		cmds.group('GRP_DRIVER_RODILLA_%s' %lado, n='GRP_PRC_DRIVER_RODILLA_%s' %lado)

		cmds.select('DRIVER_RODILLA_%s' %lado)
		#cmds.select('DRIVER_PIE_%s' %lado)

		cmds.addAttr(longName='SWITCH_RODILLA_%s' %lado, attributeType='enum', enumName='NONE:FOOT:MIDDLE', k=True)

		cmds.parentConstraint( 'DRIVER_PIE_%s' %lado, 'GRP_DRIVER_RODILLA_%s' %lado, mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_RODILLA_%s' %lado)

		cmds.parentConstraint( 'DRIVER_ROOT', 'GRP_PRC_DRIVER_RODILLA_%s' %lado, mo=1, name = 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s' %lado)


		cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
		cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 0)

		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))

		cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 1 )
		#cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 1 )


		cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 1)

		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))

		cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 2 )
		#cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 2 )

		cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
		cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 1)

		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
		#cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))


		cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 0 )
		#cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 0 )

	cmds.setAttr( 'DRIVER_HOMBRO_IZQ_FK.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_HOMBRO_IZQ_FK.overrideColor', 6 )

	cmds.setAttr( 'DRIVER_HOMBRO_DER_FK.overrideEnabled', 1 )
	cmds.setAttr( 'DRIVER_HOMBRO_DER_FK.overrideColor', 13 )


	#CORRECION SWITCH CABEZA (COMIENZA)

	cmds.spaceLocator(n='LOC_CABEZA')

	cmds.pointConstraint( 'DRIVER_CABEZA', 'LOC_CABEZA', name = 'POINT_CONSTRAIN_CABEZA')

	cmds.parent('DRIVER_CABEZA', w=True)

	cmds.group('DRIVER_CABEZA', n='GRP_DRIVER_CABEZA')

	PX = cmds.getAttr('LOC_CABEZA.tx')
	PY = cmds.getAttr('LOC_CABEZA.ty')
	PZ = cmds.getAttr('LOC_CABEZA.tz')

	cmds.move(PX, PY, PZ, "GRP_DRIVER_CABEZA.scalePivot","GRP_DRIVER_CABEZA.rotatePivot", absolute=True)

	cmds.delete('LOC_CABEZA')

	cmds.parent( 'GRP_DRIVER_CABEZA', 'MOVE_ALL')

	cmds.parentConstraint( 'DRIVER_COLUMNA_TOP', 'GRP_DRIVER_CABEZA', mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_CABEZA_TRANSLATE')

	cmds.parentConstraint( 'DRIVER_COLUMNA_TOP', 'GRP_DRIVER_CABEZA', mo=1, st=["x","z","y"], name = 'PARENT_CONSTRAIN_CABEZA_ROTATE')

	cmds.parentConstraint( 'MOVE_ALL', 'GRP_DRIVER_CABEZA', mo=1, st=["x","z","y"])

	cmds.select('DRIVER_CABEZA')

	cmds.addAttr(longName='SWITCH_CABEZA_FOLLOW', defaultValue=0, minValue=0, maxValue=1, k=True)

	cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', 0)

	cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', 1)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

	cmds.setAttr( 'DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW' , 1 )
	cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', 1)
	cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', 0)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

	cmds.setAttr( 'DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW' , 0 )

	#CORRECION SWITCH CABEZA (TERMINA)

