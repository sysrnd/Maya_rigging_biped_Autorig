import maya.cmds as cmds

class match():

	def __init__(self):
		self.switch_izq = 0
		self.switch_der = 0

	def main(self):

		if (cmds.window("switch_ik_fk", exists=True)):

			cmds.deleteUI("switch_ik_fk")

		switch_brazos=cmds.window('switch_ik_fk', title='Switch IK/Fk', widthHeight=(100, 100), sizeable=True, bgc=( .114, .114, .114))

		cmds.columnLayout( adjustableColumn=True )
		cmds.separator(height=15, st='none')

		cmds.rowColumnLayout()

		self. checkBoxes = cmds.checkBoxGrp(columnWidth2=[100, 100], numberOfCheckBoxes=2, l1='Izquierda', l2='Derecha')
		cmds.separator(height=25, st='none')
		self. checkBoxeskey = cmds.checkBoxGrp(columnWidth2=[100, 100], numberOfCheckBoxes=1, l1='Key Frame')

		cmds.separator(height=10, st='none')
	        
		cmds.rowColumnLayout( "PIE", numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,70), (2, 130)] )
	        
		cmds.button( label='Close', command=('cmds.deleteUI(\"' + switch_brazos + '\", window=True)'), w= 70,bgc=( .835, .530, .127), parent = "PIE")
	        
		cmds.button(label='RUN', c=self.acc0, bgc=( .835, .530, .127), parent = "PIE")

		cmds.showWindow( switch_brazos )

	def acc0(self, arg):
		var1 = cmds.checkBoxGrp(self.checkBoxes, q = 1, v1 = 1)
		var2 = cmds.checkBoxGrp(self.checkBoxes, q = 1, v2 = 1)
		var3 = cmds.checkBoxGrp(self.checkBoxeskey, q = 1, v1 = 1)

		if var1:
			var1 = 1
		else:
			var1 = 0

		if var2:
			var2 = 1
		else:
			var2 = 0

		if var3:
			var3 = 1
		else:
			var3 = 0
		self.accion(switch_izq = var1, switch_der = var2, key=var3)


	def accion(self,switch_izq,switch_der, key):

		if switch_izq == 1 or switch_der == 1:

			if switch_izq == 1 and switch_der == 1:
				var_lado = 0
			
			if switch_izq == 0 and switch_der == 1:
				var_lado = 1
			
			if switch_izq == 1 and switch_der == 0:
				var_lado = 0


			while var_lado < 2:

				lado = 'IZQ'

				if var_lado == 1:
					lado = 'DER'


				#OBTERNER VALORES Y CAMBIAR A FK (COMIENZA)

				SWITCH_IK_FK = cmds.getAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado)

				if SWITCH_IK_FK == 1:

					#Guardar ik (controles y switch) en el frame actual
					if key ==1:

						cmds.setKeyframe('DRIVER_CODO_%s' %lado, bd= 0, hi='none',cp = 0, s=0)
						cmds.setKeyframe('DRIVER_MANO_%s' %lado, bd= 0, hi='none',cp = 0, s=0)
						cmds.setKeyframe('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, bd= 0, hi='none',cp = 0, s=0)
						tiempo = cmds.currentTime( query=True )

					PX = cmds.getAttr('LOC_HOMBRO_%s_FK.rx' %lado)
					PY = cmds.getAttr('LOC_HOMBRO_%s_FK.ry' %lado)
					PZ = cmds.getAttr('LOC_HOMBRO_%s_FK.rz' %lado)

					cmds.rotate( PX, PY, PZ,  'DRIVER_HOMBRO_%s_FK' %lado)


					PX = cmds.getAttr('LOC_CODO_%s_FK.rx' %lado)
					PY = cmds.getAttr('LOC_CODO_%s_FK.ry' %lado)
					PZ = cmds.getAttr('LOC_CODO_%s_FK.rz' %lado)

					cmds.rotate( PX, PY, PZ,  'DRIVER_CODO_%s_FK' %lado)


					PX = cmds.getAttr('LOC_MANO_%s_FK.rx' %lado)
					PY = cmds.getAttr('LOC_MANO_%s_FK.ry' %lado)
					PZ = cmds.getAttr('LOC_MANO_%s_FK.rz' %lado)

					cmds.rotate( PX, PY, PZ,  'DRIVER_MANO_%s_FK' %lado)

					CODO = cmds.getAttr('DRIVER_MANO_%s.CORRECION_CODO' %lado)

					cmds.setAttr('DRIVER_MANO_%s_FK.CORRECION_CODO' %lado, CODO)


					cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 0)

					#Guardar fk (controles y switch) en el siguiente frame
					if key ==1:
						tiempo = tiempo+1
						cmds.setKeyframe('DRIVER_HOMBRO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0, t=tiempo)
						cmds.setKeyframe('DRIVER_CODO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0, t=tiempo)
						cmds.setKeyframe('DRIVER_MANO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0, t=tiempo)
						cmds.setKeyframe('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, bd= 0, hi='none',cp = 0, s=0, t=tiempo)

				#OBTERNER VALORES Y CAMBIAR A FK (TERMINA)


				#OBTERNER VALORES Y CAMBIAR A IK (COMIENZA)

				else:

					#Guardar fk (controles y switch) en el frame actual
					if key ==1:
						cmds.setKeyframe('DRIVER_HOMBRO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0)
						cmds.setKeyframe('DRIVER_CODO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0)
						cmds.setKeyframe('DRIVER_MANO_%s_FK' %lado, bd= 0, hi='none',cp = 0, s=0)
						cmds.setKeyframe('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, bd= 0, hi='none',cp = 0, s=0)
						tiempo = cmds.currentTime( query=True )

					PX = cmds.getAttr('LOC_CODO_%s_IK.tx' %lado)
					PY = cmds.getAttr('LOC_CODO_%s_IK.ty' %lado)
					PZ = cmds.getAttr('LOC_CODO_%s_IK.tz' %lado)
					PZ -= 0.01
					cmds.move( PX, PY, PZ, 'DRIVER_CODO_%s' %lado)



					PX = cmds.getAttr('LOC_MANO_%s_IK.tx' %lado)
					PY = cmds.getAttr('LOC_MANO_%s_IK.ty' %lado)
					PZ = cmds.getAttr('LOC_MANO_%s_IK.tz' %lado)

					cmds.move( PX, PY, PZ,  'DRIVER_MANO_%s' %lado)

					PX = cmds.getAttr('LOC_MANO_%s_IK.rx' %lado)
					PY = cmds.getAttr('LOC_MANO_%s_IK.ry' %lado)
					PZ = cmds.getAttr('LOC_MANO_%s_IK.rz' %lado)

					cmds.rotate( PX, PY, PZ,  'DRIVER_MANO_%s' %lado)


					CODO = cmds.getAttr('DRIVER_MANO_%s_FK.CORRECION_CODO' %lado)

					cmds.setAttr('DRIVER_MANO_%s.CORRECION_CODO' %lado, CODO)


					cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 1)

					#Guardar ik (controles y switch) en el siguiente frame
					if key ==1:
						tiempo = tiempo+1
						cmds.setKeyframe('DRIVER_CODO_%s' %lado, bd= 0, hi='none',cp = 0, s=0 ,t=tiempo)
						cmds.setKeyframe('DRIVER_MANO_%s' %lado, bd= 0, hi='none',cp = 0, s=0 ,t=tiempo)
						cmds.setKeyframe('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, bd= 0, hi='none',cp = 0, s=0,t=tiempo)

				#OBTERNER VALORES Y CAMBIAR A IK (TERMINA)


				var_lado = var_lado+1

				if switch_der == 0:
					var_lado = var_lado+1

				cmds.headsUpMessage( '--- !!!!  MATCH LISTO  !!!! ---' )

				pass

		else:
			cmds.headsUpMessage( '--- Debes selecionar alguna opcion TONTO!!!! ---' )


ander_class=match()
ander_class.main()

