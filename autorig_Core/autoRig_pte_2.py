import maya.cmds as cmds
from copy import deepcopy

class autoRig_02():

	def __init__(self,lst_drivers, lst_grupos_dedos, sexo):

		self.sex = sexo
		self.lst_drivers= lst_drivers
		self.lst_grupos_dedos = lst_grupos_dedos
		self.lst_drivers_faltantes = ['DRIVER_THUMB_IZQ_1','DRIVER_THUMB_IZQ_2','DRIVER_THUMB_IZQ_3','DRIVER_INDEX_IZQ_1','DRIVER_INDEX_IZQ_2','DRIVER_INDEX_IZQ_3','DRIVER_MIDDLE_IZQ_1',
		'DRIVER_MIDDLE_IZQ_2','DRIVER_MIDDLE_IZQ_3','DRIVER_CANCEL_IZQ_1','DRIVER_CANCEL_IZQ_2','DRIVER_CANCEL_IZQ_3','DRIVER_PINKY_IZQ_1','DRIVER_PINKY_IZQ_2','DRIVER_PINKY_IZQ_3', 
		'MOVE_ALL', 'MASTER', 'DRIVER_OJOS', 'DRIVER_CABEZA','DRIVER_CUELLO']

	def principal(self):

		#Si el personaje es femenino
		if self.sex.isChecked():
			try:
				self.lst_drivers.remove('DRIVER_BUSTO_IZQ')
				self.lst_drivers.remove('DRIVER_BUSTO_DER')
			except Exception as e:
				pass
		else:
			pass


		#Prende todas las curvas de la escena
		for curva in cmds.ls(et='nurbsCurve'):
		    curvaParent = cmds.listRelatives(curva, p=True)[0]
		    try:
		        cmds.setAttr(curvaParent + '.visibility', 1)
		    
		    except Exception as e:
		        pass

		#Agrega los drivers faltantes a la lista de drivers
		for agregar in xrange(0 ,len(self.lst_drivers_faltantes)):

			self.lst_drivers.append(self.lst_drivers_faltantes[agregar])

			if self.lst_drivers_faltantes[agregar].find('IZQ') != -1:
				self.lst_drivers.append(self.lst_drivers_faltantes[agregar].replace('IZQ', 'DER'))

		self.freeze(obj = self.lst_drivers)
	
		#REACOMODA DRIVER RODILLAS, CODOS Y DRIVER OJOS
		lst_poleas_drivers = ['DRIVER_RODILLA_DER','DRIVER_RODILLA_IZQ','DRIVER_CODO_IZQ','DRIVER_CODO_DER', 'DRIVER_OJO_DER', 'DRIVER_OJO_IZQ']
		lst_poleas_valores = ['2.5','2.5','-2.5','-2.5','4','4']

		for valores in xrange(0, len(lst_poleas_drivers)):
			cmds.move( lst_poleas_valores[valores], lst_poleas_drivers[valores], z=True )

		cmds.group( 'DRIVER_OJO_DER', 'DRIVER_OJO_IZQ' , n='GRP_TEMP' )
		cmds.pointConstraint( 'GRP_TEMP', 'DRIVER_OJOS', n='CONST_TEMP')
		cmds.delete('CONST_TEMP')
		cmds.ungroup( 'GRP_TEMP' )

		self.multi(conexion = 'poc', lst_01 = ['OJO_IZQ'], lst_02=['OJO_IZQ_REFERENCIA'], lst_03=['CONST_TEMP_OJO_IZQ'], offset=0)
		cmds.delete('CONST_TEMP_OJO_IZQ','CONST_TEMP_OJO_DER')
		self.multi(conexion='p', lst_01= ['OJO_IZQ_REFERENCIA'],lst_02=['OJO_IZQ'])
		self.freeze(obj = ['OJO_IZQ_REFERENCIA','OJO_DER_REFERENCIA'])

		self.freeze(obj = self.lst_drivers)

		self.multi(conexion = 'p', lst_01 = ['DRIVER_OJO_IZQ','DRIVER_OJOS'], lst_02 =['DRIVER_OJOS','MOVE_ALL'])

		cmds.group( 'DRIVER_OJOS', n='GRP_DRIVER_OJOS' )

		#CREAR IK PIERNAS
		self.multi(conexion = 'ik', lst_01 = ['PIERNA_IZQ'], lst_02 =['TALON_IZQ'], solver = 'RP')
		self.multi(conexion = 'ik', lst_01 = ['TALON_IZQ','DEDOS_PIE_IZQ'], lst_02 =['DEDOS_PIE_IZQ','PUNTA_PIE_IZQ_INUTIL'], solver = 'SC')

		# Crear parents entre los ik y los huesos de rev, ademas crea los parent de los propios drivers del pie
		# Crear pointConstraint entre lo ik y los drivers del pie
		# Crea los constrains orients de los pies
		# Crear los pol vectors de las rodillas
		lista_01 = ['IK_DEDOS_PIE_IZQ_SC','IK_PUNTA_PIE_IZQ_INUTIL_SC','REV_IZQ_1','DRIVER_TOE_FINGERS_IZQ','DRIVER_HEEL_IZQ','DRIVER_TOE_IZQ','DRIVER_BALL_IZQ']
		lista_02 = ['REV_IZQ_3','REV_IZQ_2','DRIVER_PIE_IZQ','DRIVER_HEEL_IZQ','DRIVER_PIE_IZQ','DRIVER_HEEL_IZQ','DRIVER_TOE_IZQ']
		self.multi(conexion = 'p', lst_01 = lista_01, lst_02 =lista_02)

		self.multi(conexion = 'poc', lst_01 = ['REV_IZQ_4','DRIVER_TOE_FINGERS_IZQ'], lst_02 =['IK_TALON_IZQ_RP','IK_PUNTA_PIE_IZQ_INUTIL_SC'])

		self.multi(conexion = 'or', lst_01 = ['DRIVER_HEEL_IZQ','DRIVER_BALL_IZQ','DRIVER_TOE_IZQ'], lst_02 =['REV_IZQ_1','REV_IZQ_3','REV_IZQ_2'])

		self.multi(conexion = 'pvc', lst_01 = ['DRIVER_RODILLA_IZQ'], lst_02 =['IK_TALON_IZQ_RP'])

		# Acomoda las curvas de referencia de las rodillas Y BRAZOS IK
		self.multi(conexion='poc',lst_01=['RODILLA_IZQ','DRIVER_RODILLA_IZQ','CODO_IZQ','DRIVER_CODO_IZQ'],lst_02=['CLR_RODILLA_IZQ_1','CLR_RODILLA_IZQ_2','CLR_CODO_IZQ_1','CLR_CODO_IZQ_2'],offset = 0)

		#CREAR UNIONES ENTRE LOS HUESOS DE LOS BRAZOS Y SWITCH(COMIENZA)
		lista_01 = ['HOMBRO_IZQ_IK','CODO_IZQ_IK','CODO_SEC_IZQ_IK','MANO_IZQ_IK','HOMBRO_IZQ_FK','CODO_IZQ_FK','CODO_SEC_IZQ_FK','MANO_IZQ_FK']
		lista_02 = ['HOMBRO_IZQ','CODO_IZQ','CODO_SEC_IZQ','MANO_IZQ','HOMBRO_IZQ','CODO_IZQ','CODO_SEC_IZQ','MANO_IZQ']
		lista_03 = ['PC_HOMBRO_IZQ_IK','PC_CODO_IZQ_IK','PC_CODO_SEC_IZQ_IK','PC_MANO_IZQ_IK','PC_HOMBRO_IZQ_IK_FK','PC_CODO_IZQ_IK_FK',
		'PC_CODO_SEC_IZQ_IK_FK','PC_MANO_IZQ_IK_FK']
		self.multi(conexion = 'pac', lst_01 = lista_01, lst_02 =lista_02, lst_03 = lista_03)


		lista_01_IK_FK= ['PC_HOMBRO_IZQ_IK_FK','PC_CODO_IZQ_IK_FK','PC_CODO_SEC_IZQ_IK_FK','PC_MANO_IZQ_IK_FK','crv_refr_brazo_IZQ','HOMBRO_IZQ_IK',
		'DRIVER_CODO_IZQ','DRIVER_MANO_IZQ']
		lista_02_IK_FK= ['HOMBRO_IZQ_IKW0','CODO_IZQ_IKW0','CODO_SEC_IZQ_IKW0','MANO_IZQ_IKW0','visibility','visibility','visibility','visibility']

		lista_01_FKW= ['PC_HOMBRO_IZQ_IK_FK','PC_CODO_IZQ_IK_FK','PC_CODO_SEC_IZQ_IK_FK','PC_MANO_IZQ_IK_FK']
		lista_02_FKW= ['HOMBRO_IZQ_FKW1','CODO_IZQ_FKW1','CODO_SEC_IZQ_FKW1','MANO_IZQ_FKW1']
		
		lista_01_FK= ['HOMBRO_IZQ_FK','DRIVER_HOMBRO_IZQ_FK','DRIVER_CODO_IZQ_FK','DRIVER_MANO_IZQ_FK']
		lista_02_FK= ['visibility','visibility','visibility','visibility']

		#Cambia los atributos de visibilidad de los IK a '0', y los FK a '1', tambien apaga los constrains de los huesos IK
		self.multi(conexion = 'set', lst_01 = lista_01_IK_FK, lst_02 =lista_02_IK_FK, attr=0)
		self.multi(conexion = 'set', lst_01 = lista_01_FK, lst_02 =lista_02_FK, attr=1)

		#Crea los set Driven Key de visibilidad hacia los switch de DRIVER_COLUMNA_TOP.SWITCH_IK_FK_(IZQ_DER)
		self.multi(conexion = 'sdk', lst_01 = lista_01_IK_FK, lst_02 =lista_02_IK_FK, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_')
		self.multi(conexion = 'sdk', lst_01 = lista_01_FKW, lst_02 =lista_02_FKW, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_') 
		self.multi(conexion = 'sdk', lst_01 = lista_01_FK, lst_02 =lista_02_FK, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_')

		#Cambia los atributos SWITCH_IK_FK_IZQ de DRIVER_COLUMNA_TOP a 1
		self.multi(conexion = 'set', lst_01 = ['DRIVER_COLUMNA_TOP'], lst_02 =['SWITCH_IK_FK_IZQ'], attr=1)

		#Cambia los atributos de visibilidad de los IK a '1', y los FK a '0', tambien apaga los constrains de los huesos FK
		self.multi(conexion = 'set', lst_01 = lista_01_IK_FK, lst_02 =lista_02_IK_FK, attr=1)
		self.multi(conexion = 'set', lst_01 = lista_01_FKW, lst_02 =lista_02_FKW, attr=0)
		self.multi(conexion = 'set', lst_01 = lista_01_FK, lst_02 =lista_02_FK, attr=0)

		#Crea los set Driven Key de visibilidad hacia los switch de DRIVER_COLUMNA_TOP.SWITCH_IK_FK_(IZQ_DER)
		self.multi(conexion = 'sdk', lst_01 = lista_01_IK_FK, lst_02 =lista_02_IK_FK, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_')
		self.multi(conexion = 'sdk', lst_01 = lista_01_FKW, lst_02 =lista_02_FKW, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_')
		self.multi(conexion = 'sdk', lst_01 = lista_01_FK, lst_02 =lista_02_FK, solver='DRIVER_COLUMNA_TOP.SWITCH_IK_FK_')


		#CREAR IK BRAZOS, (COMIENZAN BRAZOS)
		for i in [0, 1]:
			if i == 0:
				lado = 'IZQ'
				effector = 'effector7'

			else:
				lado = 'DER'
				effector = 'effector8'

			#CREAR IK DE LOS BRAZOS
			cmds.ikHandle( sj='HOMBRO_%s_IK' %lado, ee='CODO_SEC_%s_IK' %lado, sol = 'ikRPsolver', name = 'IK_BRAZO_%s' %lado )

			cmds.parentConstraint( 'DRIVER_MANO_%s' %lado, 'MANO_%s_IK' %lado, mo=1, st=["x","z","y"])

			cmds.spaceLocator(n='LOC_BRAZO_%s' %lado)
			cmds.pointConstraint( 'MANO_%s_IK' %lado, 'LOC_BRAZO_%s' %lado )

			PX = cmds.getAttr('LOC_BRAZO_%s.tx' %lado)
			PY = cmds.getAttr('LOC_BRAZO_%s.ty' %lado)
			PZ = cmds.getAttr('LOC_BRAZO_%s.tz' %lado)

			cmds.move(PX, PY, PZ, effector + ".scalePivot", effector + ".rotatePivot", absolute=True)

			cmds.move(PX, PY, PZ, 'IK_BRAZO_%s' %lado)

			cmds.delete('LOC_BRAZO_%s' %lado)

			cmds.poleVectorConstraint( 'DRIVER_CODO_%s' %lado, 'IK_BRAZO_%s' %lado, w=1, n='POLEA_BRAZO_%s' %lado)


		#CREAR FK DE LOS BRAZOS (COMIENZA)
		self.multi(conexion = 'pac', lst_01 = ['DRIVER_HOMBRO_IZQ_FK','DRIVER_CODO_IZQ_FK','DRIVER_MANO_IZQ_FK'], lst_02 =['HOMBRO_IZQ_FK','CODO_IZQ_FK','MANO_IZQ_FK'], sint =["x","z","y"])

		#Emparentar drivers de los dedos 
		lista_01 = ['DRIVER_MANO_IZQ_FK','DRIVER_CODO_IZQ_FK','GRP_DRIVER_INDEX_IZQ_1','GRP_DRIVER_MIDDLE_IZQ_1','GRP_DRIVER_CANCEL_IZQ_1','GRP_DRIVER_PINKY_IZQ_1','GRP_DRIVER_THUMB_IZQ_1',
		'GRP_DRIVER_INDEX_IZQ_2','GRP_DRIVER_MIDDLE_IZQ_2','GRP_DRIVER_CANCEL_IZQ_2','GRP_DRIVER_PINKY_IZQ_2','GRP_DRIVER_THUMB_IZQ_2','GRP_DRIVER_INDEX_IZQ_3','GRP_DRIVER_MIDDLE_IZQ_3',
		'GRP_DRIVER_CANCEL_IZQ_3','GRP_DRIVER_PINKY_IZQ_3','GRP_DRIVER_THUMB_IZQ_3']
		lista_02 = ['DRIVER_CODO_IZQ_FK','DRIVER_HOMBRO_IZQ_FK','MANO_IZQ','MANO_IZQ','MANO_IZQ','MANO_IZQ','MANO_IZQ','DRIVER_INDEX_IZQ_1','DRIVER_MIDDLE_IZQ_1','DRIVER_CANCEL_IZQ_1',
		'DRIVER_PINKY_IZQ_1','DRIVER_THUMB_IZQ_1','DRIVER_INDEX_IZQ_2','DRIVER_MIDDLE_IZQ_2','DRIVER_CANCEL_IZQ_2','DRIVER_PINKY_IZQ_2','DRIVER_THUMB_IZQ_2']
		self.multi(conexion = 'p', lst_01 = lista_01, lst_02 =lista_02)


		cmds.select('DRIVER_INDEX_IZQ_1', 'DRIVER_MIDDLE_IZQ_1', 'DRIVER_CANCEL_IZQ_1', 'DRIVER_PINKY_IZQ_1','DRIVER_THUMB_IZQ_1','DRIVER_INDEX_DER_1', 'DRIVER_MIDDLE_DER_1', 
			'DRIVER_CANCEL_DER_1', 'DRIVER_PINKY_DER_1','DRIVER_THUMB_DER_1')
		cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

		#Orient Constrain dedos
		lista_01 = ['DRIVER_INDEX_IZQ_1','DRIVER_INDEX_IZQ_2','DRIVER_INDEX_IZQ_3','DRIVER_MIDDLE_IZQ_1','DRIVER_MIDDLE_IZQ_2','DRIVER_MIDDLE_IZQ_3','DRIVER_CANCEL_IZQ_1',
		'DRIVER_CANCEL_IZQ_2','DRIVER_CANCEL_IZQ_3','DRIVER_PINKY_IZQ_1','DRIVER_PINKY_IZQ_2','DRIVER_PINKY_IZQ_3','DRIVER_THUMB_IZQ_1','DRIVER_THUMB_IZQ_2','DRIVER_THUMB_IZQ_3']
		lista_02 = ['INDEX_IZQ_1','INDEX_IZQ_2','INDEX_IZQ_3','MIDDLE_IZQ_1','MIDDLE_IZQ_2','MIDDLE_IZQ_3','CANCEL_IZQ_1','CANCEL_IZQ_2','CANCEL_IZQ_3','PINKY_IZQ_1','PINKY_IZQ_2',
		'PINKY_IZQ_3','THUMB_IZQ_1','THUMB_IZQ_2','THUMB_IZQ_3']
		self.multi(conexion = 'or', lst_01 = lista_01, lst_02 =lista_02)


		#CONECTAR LA ROTACION SECUNDARIA DEL CODO
		self.multi(conexion = 'cat', lst_01 = ['DRIVER_MANO_IZQ.CORRECION_CODO'], lst_02 =['CODO_SEC_IZQ_IK.rotateX'])
		self.multi(conexion = 'cat', lst_01 = ['DRIVER_MANO_IZQ_FK.CORRECION_CODO'], lst_02 =['CODO_SEC_IZQ_FK.rotateX'])

		#(TERMINAN BRAZOS)


		#CONECTAR ATRIBUTOS DE VISIBILIDAD CON DRIVERS
		lista_01 = ['MASTER.CUERPO','MASTER.CUERPO','MASTER.CUERPO','MASTER.PIERNAS','MASTER.PIERNAS','DRIVER_CABEZA.VISIBILITY_BS','DRIVER_CABEZA.LENTES_VISIBILIDAD','DRIVER_CABEZA.SOMBRERO_VISIBILIDAD']
		lista_02 = ['DRIVER_ROOT.visibility','DRIVER_DIENTES_TOP.visibility','DRIVER_BOCA.visibility','DRIVER_PIE_IZQ.visibility','DRIVER_RODILLA_IZQ.visibility','DRIVER_CARA.visibility','DRIVER_LENTES.visibility','DRIVER_SOMBRERO.visibility']
		self.multi(conexion = 'cat', lst_01 = lista_01, lst_02 =lista_02)

		#CONSTRAINS GENEALES
		self.multi(conexion = 'p', lst_01=['DRIVER_PINKY_SEC_IZQ','DRIVER_DIENTES_TOP','DRIVER_BOCA','GRP_DRIVER_SOMBRERO','GRP_DRIVER_LENTES','GRP_DRIVER_CARA'], lst_02=['MANO_IZQ','CABEZA','CABEZA','MOVE_ALL','MOVE_ALL','MASTER'])

		cmds.select('DRIVER_PINKY_SEC_IZQ', 'DRIVER_PINKY_SEC_DER','DRIVER_BOCA', 'DRIVER_DIENTES_TOP')
		cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 


		lista_01 = ['DRIVER_HOMBRO_IZQ_FK','GRP_DRIVER_PINKY_IZQ_1','DRIVER_DIENTES_BOTTOM','DRIVER_LENGUA','GRP_DRIVER_CABEZA','DRIVER_CLAVICULA_IZQ','DRIVER_MANO_IZQ','DRIVER_CODO_IZQ',
		'DRIVER_COLUMNA_TOP','DRIVER_COLUMNA_MIDDLE','DRIVER_COLUMNA_BOTTOM','DRIVER_CINTURA','DRIVER_RODILLA_IZQ','DRIVER_PIE_IZQ','DRIVER_ROOT','MOVE_ALL','IK_BRAZO_IZQ','IK_TALON_IZQ_RP',
		'ROOT','GRP_DRIVER_CUELLO']
		lista_02 = ['DRIVER_CLAVICULA_IZQ','DRIVER_PINKY_SEC_IZQ','DRIVER_BOCA','DRIVER_BOCA','DRIVER_CUELLO','DRIVER_COLUMNA_TOP','MOVE_ALL','MOVE_ALL','DRIVER_COLUMNA_MIDDLE',
		'DRIVER_COLUMNA_BOTTOM','DRIVER_ROOT','DRIVER_ROOT','MOVE_ALL','MOVE_ALL','MOVE_ALL','MASTER','MOVE_ALL','MOVE_ALL','MOVE_ALL','DRIVER_COLUMNA_TOP']
		self.multi(conexion = 'p', lst_01 = lista_01, lst_02 =lista_02)

		lista_01 = ['DRIVER_CINTURA','DRIVER_COLUMNA_BOTTOM','DRIVER_COLUMNA_MIDDLE','DRIVER_COLUMNA_TOP','DRIVER_CABEZA','DRIVER_BOCA','DRIVER_PINKY_SEC_IZQ','DRIVER_CLAVICULA_IZQ','DRIVER_CUELLO']
		lista_02 = ['CINTURA','COLUMNA_BAJA','COLUMNA_MEDIA','COLUMNA_ALTA','CABEZA','MANDIBULA_INUTIL','PINKY_SEC_IZQ','CLAVICULA_IZQ','CUELLO']
		self.multi(conexion = 'or', lst_01 = lista_01, lst_02 =lista_02)

		self.multi(conexion = 'pac', lst_01=['DRIVER_LENGUA','DRIVER_ROOT','DRIVER_DIENTES_TOP','DRIVER_DIENTES_BOTTOM'],lst_02=['LENGUA_2','ROOT','DIENTES_ARRIBA','DIENTES_BAJA'])
		self.multi(conexion = 'aim', lst_01 = ['DRIVER_OJO_IZQ'], lst_02 =['OJO_IZQ'])
		self.multi(conexion = 'poc', lst_01 = ['DRIVER_MANO_IZQ'], lst_02 =['IK_BRAZO_IZQ'])


		#BLOQUEAR Y OCULTAR ATRIBUTOS(COMIENZA)
		lst_drivers_block_ts = ['DRIVER_TOE_IZQ','DRIVER_BALL_IZQ','DRIVER_HEEL_IZQ','DRIVER_MANO_IZQ_FK','DRIVER_CODO_IZQ_FK','DRIVER_HOMBRO_IZQ_FK','DRIVER_CINTURA','DRIVER_COLUMNA_BOTTOM'
		,'DRIVER_COLUMNA_MIDDLE','DRIVER_COLUMNA_TOP','DRIVER_BOCA','DRIVER_CABEZA','DRIVER_CUELLO']
		self.atributos(bloquear = 'ts', lst_drivers_block = lst_drivers_block_ts)

		lst_drivers_block_s = ['DRIVER_LENGUA','DRIVER_DIENTES_TOP','DRIVER_DIENTES_BOTTOM','DRIVER_MANO_IZQ','DRIVER_ROOT','DRIVER_PIE_IZQ','MOVE_ALL',
		'DRIVER_CLAVICULA_IZQ']
		self.atributos(bloquear = 's', lst_drivers_block = lst_drivers_block_s)

		lst_drivers_block_rs = ['DRIVER_CODO_IZQ','DRIVER_RODILLA_IZQ','DRIVER_TOE_FINGERS_IZQ','DRIVER_OJO_IZQ']
		self.atributos(bloquear = 'rs', lst_drivers_block = lst_drivers_block_rs)

		lst_drivers_block_v = ['MASTER','DRIVER_THUMB_IZQ_1','DRIVER_THUMB_IZQ_2','DRIVER_THUMB_IZQ_3','DRIVER_INDEX_IZQ_1','DRIVER_INDEX_IZQ_2','DRIVER_INDEX_IZQ_3','DRIVER_MIDDLE_IZQ_1',
		'DRIVER_MIDDLE_IZQ_2','DRIVER_MIDDLE_IZQ_3','DRIVER_CANCEL_IZQ_1','DRIVER_CANCEL_IZQ_2','DRIVER_CANCEL_IZQ_3','DRIVER_PINKY_IZQ_1','DRIVER_PINKY_IZQ_2','DRIVER_PINKY_IZQ_3']
		self.atributos(bloquear = 'v', lst_drivers_block = lst_drivers_block_v)

		# Bloquear X y Z de la rotacion en el FK codo
		self.atributos(bloquear = 'r', lst_drivers_block = ['DRIVER_CODO_IZQ_FK','DRIVER_CODO_IZQ_FK'], eje_attr=['x', 'z'])
		self.atributos(bloquear = 'tsr', lst_drivers_block = ['OJO_IZQ_REFERENCIA'])

		#CAMBIA COLORES OVERRIDES 
		lista_01 = ['DRIVER_THUMB_IZQ_1','DRIVER_INDEX_IZQ_1','DRIVER_MIDDLE_IZQ_1','DRIVER_CANCEL_IZQ_1','DRIVER_PINKY_SEC_IZQ','DRIVER_MANO_IZQ','DRIVER_CODO_IZQ',
		'DRIVER_CLAVICULA_IZQ','DRIVER_PIE_IZQ','DRIVER_RODILLA_IZQ','DRIVER_OJO_IZQ', 'DRIVER_HOMBRO_IZQ_FK','OJO_IZQ_REFERENCIA']
		self.multi(conexion = 'set', lst_01 = lista_01, offset=6, ampliar_lst=0)

		lista_01 = ['DRIVER_THUMB_DER_1','DRIVER_INDEX_DER_1','DRIVER_MIDDLE_DER_1','DRIVER_CANCEL_DER_1','DRIVER_PINKY_SEC_DER','DRIVER_MANO_DER','DRIVER_CODO_DER',
		'DRIVER_CLAVICULA_DER','DRIVER_PIE_DER','DRIVER_RODILLA_DER','DRIVER_OJO_DER', 'DRIVER_HOMBRO_DER_FK','OJO_DER_REFERENCIA']
		self.multi(conexion = 'set', lst_01 = lista_01, offset=13, ampliar_lst=0)

		lista_01 = ['DRIVER_BOCA','DRIVER_DIENTES_TOP','MOVE_ALL','DRIVER_CINTURA','DRIVER_COLUMNA_BOTTOM','DRIVER_SOMBRERO','DRIVER_LENTES']
		self.multi(conexion = 'set', lst_01 = lista_01, offset=18, ampliar_lst=0)

		lista_01 = ['MASTER','DRIVER_ROOT','DRIVER_COLUMNA_TOP']
		self.multi(conexion = 'set', lst_01 = lista_01, offset=17, ampliar_lst=0)

		self.multi(conexion = 'set', lst_01 = ['ROOT'], offset=1, ampliar_lst=0)


		#Cambia todos los orient y parent Constrains a shortest
		for cons in cmds.ls(et='orientConstraint'):
		   cmds.setAttr(cons + '.interpType', 2)

		for cons in cmds.ls(et='parentConstraint'):
		   cmds.setAttr(cons + '.interpType', 2)
		

		#Crea los grupos
		cmds.group('CRV_REFR_RODILLA_IZQ', 'CLR_RODILLA_IZQ_1', 'CLR_RODILLA_IZQ_2', 'crv_refr_brazo_IZQ', 'CLR_CODO_IZQ_1', 'CLR_CODO_IZQ_2', 'CRV_REFR_RODILLA_DER',
			'CLR_RODILLA_DER_1', 'CLR_RODILLA_DER_2', 'crv_refr_brazo_DER', 'CLR_CODO_DER_1','CLR_CODO_DER_2', n='GRP_CURVS_REFERENCIA')
		
		cmds.group('DEFORM_CURV_PARPADO_DER','DEFORM_CURV_OREJA_DER','DEFORM_CURV_DER','DEFORM_CURV_BOCA_INF','DEFORM_CURV_BOCA_SUP','DEFORM_CURV_NARIZ', n='GRP_CURVS_CARA')
		
		cmds.group( 'GRP_CURVS_REFERENCIA','GRP_CURVS_CARA','MASTER', n='GRP_RIGG' )

		#CREAR LAYER Y OCULTAR BASURA(COMIENZA)
		cmds.select( d=True )
		cmds.createDisplayLayer( noRecurse=True, name='no_tocar' )
		cmds.editDisplayLayerMembers( 'no_tocar', 'IK_BRAZO_IZQ', 'IK_BRAZO_DER', 'IK_TALON_IZQ_RP', 'IK_TALON_DER_RP','IK_DEDOS_PIE_IZQ_SC', 'IK_DEDOS_PIE_DER_SC', 
			'IK_PUNTA_PIE_IZQ_INUTIL_SC', 'IK_PUNTA_PIE_DER_INUTIL_SC', 'CLR_CODO_IZQ_1', 'CLR_CODO_IZQ_2','CLR_CODO_DER_1', 'CLR_CODO_DER_2', 'REV_IZQ_1', 'REV_DER_1', 
			'CLR_RODILLA_IZQ_1', 'CLR_RODILLA_DER_1', 'CLR_RODILLA_IZQ_2', 'CLR_RODILLA_DER_2')





		lado = 'IZQ'
		var_lado = 0

		while var_lado < 2:

			if var_lado == 1:
				lado = 'DER'

			#CREACION DE LOCATORS (COMIENZA)
			cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 0)

			cmds.spaceLocator(n='LOC_HOMBRO_%s_FK' %lado)
			cmds.spaceLocator(n='LOC_CODO_%s_FK' %lado)
			cmds.spaceLocator(n='LOC_MANO_%s_FK' %lado)

			cmds.parentConstraint('DRIVER_HOMBRO_%s_FK' %lado, 'LOC_HOMBRO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_HOMBRO_%s' %lado)
			cmds.parentConstraint('DRIVER_CODO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s' %lado)
			cmds.parentConstraint('DRIVER_MANO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

			cmds.delete('LOCATOR_CONSTRAIN_HOMBRO_%s' %lado, 'LOCATOR_CONSTRAIN_CODO_%s' %lado, 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

			cmds.select('LOC_HOMBRO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado)
			cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

			cmds.parent( 'LOC_MANO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado)
			cmds.parent( 'LOC_CODO_%s_FK' %lado, 'LOC_HOMBRO_%s_FK' %lado)

			cmds.parentConstraint('HOMBRO_%s_IK' %lado, 'LOC_HOMBRO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_HOMBRO_%s_ROTATE' %lado, mo =1)
			cmds.parentConstraint('CODO_%s_IK' %lado, 'LOC_CODO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_CODO_%s_ROTATE' %lado, mo =1)
			cmds.parentConstraint('MANO_%s_IK' %lado, 'LOC_MANO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_MANO_%s_ROTATE' %lado, mo =1)



			cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 1)

			cmds.spaceLocator(n='LOC_CODO_%s_IK' %lado)
			cmds.spaceLocator(n='LOC_MANO_%s_IK' %lado)

			cmds.parentConstraint('DRIVER_CODO_%s' %lado, 'LOC_CODO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s' %lado)
			cmds.parentConstraint('DRIVER_MANO_%s' %lado, 'LOC_MANO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

			cmds.delete('LOCATOR_CONSTRAIN_CODO_%s' %lado, 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

			cmds.select('LOC_CODO_%s_IK' %lado, 'LOC_MANO_%s_IK' %lado)
			cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

			cmds.pointConstraint('CODO_%s_FK' %lado, 'LOC_CODO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s_ROTATE_IK' %lado)
			cmds.parentConstraint('MANO_%s_FK' %lado, 'LOC_MANO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s_ROTATE_IK' %lado, mo =1)

			cmds.editDisplayLayerMembers( 'no_tocar', 'LOC_HOMBRO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado, 'LOC_CODO_%s_IK' %lado, 'LOC_MANO_%s_IK' %lado)
			#CREACION DE LOCATORS (TERMINA)



			#CORRECION SWITCH RODILLA (COMIENZA)
			cmds.group('DRIVER_RODILLA_%s' %lado, n='GRP_DRIVER_RODILLA_%s' %lado)
			cmds.group('GRP_DRIVER_RODILLA_%s' %lado, n='GRP_PRC_DRIVER_RODILLA_%s' %lado)


			cmds.parentConstraint( 'DRIVER_PIE_%s' %lado, 'GRP_DRIVER_RODILLA_%s' %lado, mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_RODILLA_%s' %lado)
			cmds.parentConstraint( 'DRIVER_ROOT', 'GRP_PRC_DRIVER_RODILLA_%s' %lado, mo=1, name = 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s' %lado)


			cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
			cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 0)

			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))

			cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 1 )
			cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 1)

			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))

			cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 2 )
			cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
			cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 1)

			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))
			cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado))

			cmds.setAttr( 'DRIVER_RODILLA_%s.SWITCH_RODILLA_%s' %(lado, lado), 0 )
			#CORRECION SWITCH RODILLA (TERMINA)

			var_lado = var_lado+1

			pass
		cmds.group('LOC_HOMBRO_IZQ_FK','LOC_CODO_IZQ_IK','LOC_MANO_IZQ_IK','LOC_HOMBRO_DER_FK','LOC_CODO_DER_IK','LOC_MANO_DER_IK', n='LOCATORS_MATCH')
		cmds.parent('LOCATORS_MATCH', 'GRP_RIGG')


		#SWITCH OJOS,CABEZA, CUELLO, LENTES Y SOMBRERO (COMIENZA)
		lista_01 = ['DRIVER_CUELLO','DRIVER_COLUMNA_TOP']
		lista_02 = ['GRP_DRIVER_CABEZA','GRP_DRIVER_CUELLO']
		lista_03 = ['PARENT_CONSTRAIN_CABEZA_TRANSLATE','PARENT_CONSTRAIN_CUELLO_TRANSLATE']
		self.multi(conexion = 'pac', lst_01 = lista_01, lst_02 =lista_02, lst_03 = lista_03, sinr =["x","z","y"])

		lista_01 = ['DRIVER_CUELLO','MOVE_ALL','DRIVER_COLUMNA_TOP','MOVE_ALL']
		lista_02 = ['GRP_DRIVER_CABEZA','GRP_DRIVER_CABEZA','GRP_DRIVER_CUELLO','GRP_DRIVER_CUELLO']
		lista_03 = ['PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE']
		self.multi(conexion = 'pac', lst_01 = lista_01, lst_02 =lista_02, lst_03 = lista_03, sint =["x","z","y"])

		self.multi(conexion = 'pac', lst_01 =['CABEZA_INUTIL','MOVE_ALL'], lst_02 =['GRP_DRIVER_OJOS','GRP_DRIVER_OJOS'], lst_03 =['PARENT_CONSTRAIN_OJOS','PARENT_CONSTRAIN_OJOS'])
		
		lista_01 = ['CABEZA_INUTIL','CABEZA_INUTIL','MOVE_ALL','MOVE_ALL']
		lista_02 = ['GRP_DRIVER_LENTES','GRP_DRIVER_SOMBRERO','GRP_DRIVER_LENTES','GRP_DRIVER_SOMBRERO']
		lista_03 = ['PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_SOMBRERO','PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_SOMBRERO']
		self.multi(conexion='pac',lst_01=lista_01,lst_02=lista_02,lst_03=lista_03)

		lista_01 = ['PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_OJOS','PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_SOMBRERO']
		self.multi(conexion = 'set', lst_01 = lista_01, lst_02 =['DRIVER_CUELLOW0','DRIVER_COLUMNA_TOPW0','CABEZA_INUTILW0','CABEZA_INUTILW0','CABEZA_INUTILW0'], attr=0)
		self.multi(conexion = 'set', lst_01 = lista_01, lst_02 =['MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1'], attr=1)


		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_OJOS','PARENT_CONSTRAIN_OJOS'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_OJOS')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CABEZA_ROTATE'], lst_02 =['DRIVER_CUELLOW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE'], lst_02 =['DRIVER_COLUMNA_TOPW0','MOVE_ALLW1'], solver='DRIVER_CUELLO.SWITCH_CUELLO_FOLLOW')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_LENTES'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_LENTES')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_SOMBRERO','PARENT_CONSTRAIN_SOMBRERO'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_SOMBRERO')


		lista_01 = ['DRIVER_CABEZA','DRIVER_CUELLO','DRIVER_CABEZA','DRIVER_CABEZA','DRIVER_CABEZA','PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_OJOS',
		'PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_SOMBRERO']
		lista_02 = ['SWITCH_CABEZA_FOLLOW','SWITCH_CUELLO_FOLLOW','SWITCH_OJOS','SWITCH_LENTES','SWITCH_SOMBRERO','DRIVER_CUELLOW0','DRIVER_COLUMNA_TOPW0','CABEZA_INUTILW0','CABEZA_INUTILW0',
		'CABEZA_INUTILW0']
		self.multi(conexion = 'set', lst_01 = lista_01, lst_02 =lista_02, attr=1)

		lista_01 = ['PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_OJOS','PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_SOMBRERO']
		lista_02 = ['MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1','MOVE_ALLW1']
		self.multi(conexion='set',lst_01=lista_01,lst_02=lista_02,attr=0)


		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_OJOS','PARENT_CONSTRAIN_OJOS'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_OJOS')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_CABEZA_ROTATE','PARENT_CONSTRAIN_CABEZA_ROTATE'], lst_02 =['DRIVER_CUELLOW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_CUELLO_ROTATE','PARENT_CONSTRAIN_CUELLO_ROTATE'], lst_02 =['DRIVER_COLUMNA_TOPW0','MOVE_ALLW1'], solver='DRIVER_CUELLO.SWITCH_CUELLO_FOLLOW')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_LENTES','PARENT_CONSTRAIN_LENTES'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_LENTES')
		self.multi(conexion = 'sdk', lst_01 = ['PARENT_CONSTRAIN_SOMBRERO','PARENT_CONSTRAIN_SOMBRERO'], lst_02 =['CABEZA_INUTILW0','MOVE_ALLW1'], solver='DRIVER_CABEZA.SWITCH_SOMBRERO')


		lista_01 = ['DRIVER_CABEZA','DRIVER_CABEZA','DRIVER_CUELLO','DRIVER_CABEZA','DRIVER_CABEZA']
		lista_02 = ['SWITCH_OJOS','SWITCH_CABEZA_FOLLOW','SWITCH_CUELLO_FOLLOW','SWITCH_LENTES','SWITCH_SOMBRERO']
		self.multi(conexion = 'set', lst_01 =lista_01, lst_02 =lista_02, attr=0)
		#SWITCH OJOS,CABEZA, CUELLO, LENTES Y SOMBRERO (TERMINA)

		#Agrega el switch del hombro
		self.spaceSwitchClavicle('DRIVER_HOMBRO_IZQ_FK', 'IZQ')
		self.spaceSwitchClavicle('DRIVER_HOMBRO_DER_FK', 'DER')

		#Desbloquea los wires
		elements = cmds.listRelatives('GRP_CURVS_CARA', children=True)
		for curv in xrange(0, len(elements)):
			cmds.setAttr(elements[curv]+ '.template', 0)


		#Si el personaje es femenino
		if self.sex.isChecked():
			pass

		else:
			cmds.group( 'DRIVER_BUSTO_IZQ', 'DRIVER_BUSTO_DER' , n='GRP_TEMP' )
			cmds.pointConstraint( 'GRP_TEMP', 'DRIVER_BUSTO', n='CONST_TEMP')
			cmds.delete('CONST_TEMP')
			cmds.ungroup( 'GRP_TEMP' )

			self.multi(conexion = 'p', lst_01=['DRIVER_BUSTO','DRIVER_BUSTO_IZQ'], lst_02=['DRIVER_COLUMNA_TOP','DRIVER_BUSTO'])

			cmds.select('DRIVER_BUSTO')
			cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1)

			self.multi(conexion = 'pac', lst_01=['DRIVER_BUSTO_IZQ'], lst_02=['BUSTO_IZQ'])

			self.multi(conexion = 'cat', lst_01=['DRIVER_BUSTO_IZQ.scale'], lst_02=['BUSTO_IZQ.scale'])

			self.multi(conexion = 'set', lst_01 = ['DRIVER_BUSTO_IZQ'], offset=6, ampliar_lst=0)
			self.multi(conexion = 'set', lst_01 = ['DRIVER_BUSTO_DER'], offset=13, ampliar_lst=0)




	def freeze(self, obj):
		cmds.select(obj)
		cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1)

	''' Si conexion es 'p' se crea un parent si es,  'or' = se crea un orientConstraint si es, 'pac' = parentConstraint si es, 'aim' = aimConstraint si es, 'poc' = pointConstraint y si es 
	'ik' = ikHandle, como dato se puede mandar con solver 'SC' o 'RP' y los constrains con maintain offset si no pones offset es igual a con maintain si quieres desactivarlo manda 0
	* La conexion 'set' = crear setAttr tienes que mandar el valor a cambiar con attr =
	* Adicional puede generar conexion de atributos si ocupamos 'cat' = connectAttr, 'pcv' = poleVectorConstraint
	* Mostrar te imprime las listas que se estan uniendo y offset te ofrece cambiar el maintain offset de los constrains, '0' = sin maintain y '1' o nada es igual a con maintain'''
	def multi (self, conexion, lst_01, lst_02=None, mostrar=None, offset =None, lst_03 = None ,solver = None, attr=None, ampliar_lst=None, sinr=None, sint=None):
		myoffset = 1
		if offset != None:
			myoffset = offset
		if sinr == None:
			sinr = 'none'
		if sint == None:
			sint = 'none'

		l2_aux = None
		l3_aux = None
		l1_aux = deepcopy(lst_01)
		if lst_02 != None:
			l2_aux = deepcopy(lst_02)
		if lst_03 != None:
			l3_aux = deepcopy(lst_03)


		if ampliar_lst == None:
			for element in xrange(0, len(l1_aux)):
				if l1_aux[element].find('IZQ') != -1:
					l1_aux.append(l1_aux[element].replace('IZQ', 'DER'))
					if l2_aux!=None:
						if  l2_aux[element].find('IZQ') != -1:
							l2_aux.append(l2_aux[element].replace('IZQ', 'DER'))
							if l3_aux!=None:
								if  l3_aux[element].find('IZQ') != -1:
									l3_aux.append(l3_aux[element].replace('IZQ', 'DER'))
								else:
									l3_aux.append(l3_aux[element])
						else :
							l2_aux.append(l2_aux[element])
							if l3_aux!=None:
								if l3_aux[element].find('IZQ') != -1:
									l3_aux.append(l3_aux[element].replace('IZQ', 'DER'))
								else:
									l3_aux.append(l3_aux[element])
				elif l2_aux!=None:
					if l2_aux[element].find('IZQ') != -1:
						l1_aux.append(l1_aux[element])
						l2_aux.append(l2_aux[element].replace('IZQ', 'DER'))
						if l3_aux!=None:
							if l3_aux[element].find('IZQ') != -1:
								l3_aux.append(l3_aux[element].replace('IZQ', 'DER'))
							else:
								l3_aux.append(l3_aux[element])
				elif l3_aux!=None:
					if l3_aux[element].find('IZQ') != -1:
						l1_aux.append(l1_aux[element])
						l2_aux.append(l2_aux[element])
						l3_aux.append(l3_aux[element].replace('IZQ', 'DER'))

			
		if mostrar ==1:
			for imprimir in xrange(0, len(l1_aux)):
				if l3_aux == None:
					if l2_aux == None:
						print l1_aux[imprimir] + ' '+ conexion 
					else:
						print l1_aux[imprimir] + ' '+ conexion + ' ' + l2_aux[imprimir]
				else:
					print l1_aux[imprimir] + ' '+ conexion + ' ' + l2_aux[imprimir] + ' ' + l3_aux[imprimir]


		for conect in xrange(0, len(l1_aux)):

			if conexion == 'p':
				cmds.parent( l1_aux[conect], l2_aux[conect])

			elif conexion == 'or':
				cmds.orientConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset)

			elif conexion == 'pac':
				if l3_aux == None:
					cmds.parentConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset, sr=sinr, st=sint)
				else:
					cmds.parentConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset, sr=sinr, st=sint, n= l3_aux[conect])

			elif conexion == 'aim':
				cmds.aimConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset)

			elif conexion == 'poc':
				if l3_aux == None:
					cmds.pointConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset )
				else:
					cmds.pointConstraint( l1_aux[conect], l2_aux[conect], mo=myoffset, n=l3_aux[conect] )

			elif conexion == 'cat':
				cmds.connectAttr(l1_aux[conect], l2_aux[conect])

			elif conexion == 'pvc':
				cmds.poleVectorConstraint( l1_aux[conect], l2_aux[conect], w =  1)

			elif conexion == 'ik':
				cmds.ikHandle( sj=l1_aux[conect], ee=l2_aux[conect], sol = 'ik'+solver+'solver', name = 'IK_'+l2_aux[conect]+'_'+solver )

			elif conexion == 'set':
				
				if offset !=None:
					cmds.setAttr( l1_aux[conect]+'.overrideEnabled', 1 )
					cmds.setAttr( l1_aux[conect]+'.overrideColor', myoffset )
				else:
					cmds.setAttr( l1_aux[conect]+'.'+l2_aux[conect], attr )

			elif conexion == 'sdk':
				lado =''
				if l1_aux[conect].find('IZQ') != -1 or l2_aux[conect].find('IZQ') != -1:
					lado = 'IZQ'
					cmds.setDrivenKeyframe( l1_aux[conect]+'.'+l2_aux[conect], cd=solver + lado)
				elif l1_aux[conect].find('DER') != -1 or l2_aux[conect].find('DER') != -1:
					lado = 'DER'
					cmds.setDrivenKeyframe( l1_aux[conect]+'.'+l2_aux[conect], cd=solver + lado)
				else:
					cmds.setDrivenKeyframe( l1_aux[conect]+'.'+l2_aux[conect], cd=solver)

	#Si tu valor es 's' = bloquear escala, si es 'ts' = bloquea translacion y escala, si es 'rs' = bloquea rotacion y escala, si es 'v' = solo visibilidad, todos bloquean visibilidad
	def atributos(self, bloquear, lst_drivers_block, eje_attr=None):
		eje = ['x','y','z']

		if eje_attr != None:
			eje = deepcopy(eje_attr)

		for repetir in xrange(0, len(lst_drivers_block)):

			cmds.setAttr(lst_drivers_block[repetir] + '.v', channelBox = 0, keyable=0, l=1)
			if lst_drivers_block[repetir].find('IZQ') != -1:
				cmds.setAttr(lst_drivers_block[repetir].replace('IZQ', 'DER') + '.v', channelBox = 0, keyable=0, l=1)
	
			if bloquear != 'v' :
				for block in xrange(0, len(bloquear)):
					for blocksec in xrange(0, len(eje)):
						cmds.setAttr(lst_drivers_block[repetir] + '.' + bloquear[block] + eje[blocksec], channelBox = 0, keyable=0, l=1)
						
						if lst_drivers_block[repetir].find('IZQ') != -1:
							cmds.setAttr(lst_drivers_block[repetir].replace('IZQ', 'DER') + '.' + bloquear[block] + eje[blocksec], channelBox = 0, keyable=0, l=1)



	def spaceSwitchClavicle(self, clav_ctrl, side):
		AXIS = ['X','Y','Z']
		
		clavicleLoc = cmds.spaceLocator(n = 'clavicleLoc_' + side)[0]
		clavicleLoc = cmds.parent(clavicleLoc, 'HOMBRO_' + side)[0]
		grp_ClavicleCtrl = cmds.group(clav_ctrl, n= 'GRP_CTRL_CLAV_' + side)

		for ax in range(0, len(AXIS)):
			cmds.setAttr(clavicleLoc + '.translate' + AXIS[ax], 0)

		clavicleLoc = cmds.parent(clavicleLoc, 'CLAVICULA_' + side)[0]
		posLoc = cmds.xform(clavicleLoc, q=True, ws=True, t=True)
		
		for ax in range(0, len(AXIS)):
			cmds.setAttr(grp_ClavicleCtrl + '.rotatePivot' + AXIS[ax], posLoc[ax])
			cmds.setAttr(grp_ClavicleCtrl + '.scalePivot' + AXIS[ax], posLoc[ax])


		cmds.parent(grp_ClavicleCtrl, 'DRIVER_COLUMNA_TOP')
		orientCons = cmds.parentConstraint('MASTER', clavicleLoc, grp_ClavicleCtrl, st =('x', 'y', 'z'), mo=True)[0]
		cmds.parentConstraint(clavicleLoc, grp_ClavicleCtrl, sr =('x', 'y', 'z'), mo=True)

		cmds.addAttr(clav_ctrl, longName='SWT_CLAVICULA', defaultValue=0, minValue=0, maxValue=1, at='double')
		cmds.setAttr(clav_ctrl + '.SWT_CLAVICULA', e=True, keyable=True)

		cmds.setDrivenKeyframe(orientCons + '.MASTERW0', cd= clav_ctrl + '.SWT_CLAVICULA', dv=0, v=1)
		cmds.setDrivenKeyframe(orientCons + '.MASTERW0', cd= clav_ctrl + '.SWT_CLAVICULA', dv=1, v=0)
		cmds.setDrivenKeyframe(orientCons + '.' + clavicleLoc +'W1', cd= clav_ctrl + '.SWT_CLAVICULA', dv=0, v=0)
		cmds.setDrivenKeyframe(orientCons + '.' + clavicleLoc +'W1', cd= clav_ctrl + '.SWT_CLAVICULA', dv=1, v=1)
		cmds.editDisplayLayerMembers( 'no_tocar', 'clavicleLoc_' +side)