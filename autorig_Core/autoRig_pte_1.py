import maya.cmds as cmds

class autoRig_01():

    def __init__(self, sexo, lst_drivers, lst_grupos_dedos):

        #Define variable si es hombre o mujer
        self.sex = sexo

        #Listado de huesos originales comienza
        self.lst_huesos_original=['R_ROOT','R_COLUMNA_BAJA',"R_COLUMNA_MEDIA","R_COLUMNA_ALTA","R_CUELLO","R_CABEZA","R_CABEZA_INUTIL","R_DIENTES_ARRIBA",
            "R_LENGUA_1","R_LENGUA_2","R_LENGUA_3_INUTIL","R_MANDIBULA_INUTIL","R_BOCA","R_DIENTES_BAJA","R_CLAVICULA_IZQ","R_HOMBRO_IZQ","R_CODO_IZQ","R_CODO_SEC_IZQ",
            "R_MANO_IZQ","R_MIDDLE_IZQ_1","R_MIDDLE_IZQ_2","R_MIDDLE_IZQ_3","R_MIDDLE_IZQ_4_INUTIL","R_PINKY_SEC_IZQ","R_PINKY_IZQ_1","R_PINKY_IZQ_2","R_PINKY_IZQ_3",
            "R_PINKY_IZQ_4_INUTIL","R_CANCEL_IZQ_1","R_CANCEL_IZQ_2","R_CANCEL_IZQ_3","R_CANCEL_IZQ_4_INUTIL","R_INDEX_IZQ_1","R_INDEX_IZQ_2","R_INDEX_IZQ_3","R_INDEX_IZQ_4_INUTIL",
            "R_THUMB_IZQ_1","R_THUMB_IZQ_2","R_THUMB_IZQ_3","R_THUMB_IZQ_4_INUTIL","R_CINTURA","R_PIERNA_IZQ","R_RODILLA_IZQ","R_TALON_IZQ","R_DEDOS_PIE_IZQ","R_PUNTA_PIE_IZQ_INUTIL",
            "R_REV_IZQ_1","R_REV_IZQ_2","R_REV_IZQ_3","R_REV_IZQ_4","R_OJO_IZQ","R_BUSTO_IZQ"]
        
        #Listado de drivers
        self.lst_drivers = lst_drivers

        #Lista de huesos ik y fk
        self.list_huesos_extendida=["HOMBRO_IZQ_IK","CODO_IZQ_IK","CODO_SEC_IZQ_IK","MANO_IZQ_IK","HOMBRO_IZQ_FK","CODO_IZQ_FK","CODO_SEC_IZQ_FK","MANO_IZQ_FK","CLAVICULA_DER","HOMBRO_DER",
        "CODO_DER","CODO_SEC_DER","MANO_DER","MIDDLE_DER_1","MIDDLE_DER_2","MIDDLE_DER_3","MIDDLE_DER_4_INUTIL","PINKY_SEC_DER","PINKY_DER_1","PINKY_DER_2","PINKY_DER_3","PINKY_DER_4_INUTIL"
        ,"CANCEL_DER_1","CANCEL_DER_2","CANCEL_DER_3","CANCEL_DER_4_INUTIL","INDEX_DER_1","INDEX_DER_2","INDEX_DER_3","INDEX_DER_4_INUTIL","THUMB_DER_1","THUMB_DER_2","THUMB_DER_3",
        "THUMB_DER_4_INUTIL","PIERNA_DER","RODILLA_DER","TALON_DER","DEDOS_PIE_DER","PUNTA_PIE_DER_INUTIL","REV_DER_1","REV_DER_2","REV_DER_3","REV_DER_4","OJO_DER","BUSTO_DER",
        "HOMBRO_DER_IK","CODO_DER_IK","CODO_SEC_DER_IK","MANO_DER_IK","HOMBRO_DER_FK","CODO_DER_FK","CODO_SEC_DER_FK","MANO_DER_FK"]

        #Lista de grupos dedos
        self.lst_grupos_dedos = lst_grupos_dedos

        
    def principal(self):
        #Crea y enlaza los huesos con los locators comienza

        listaloc = []
        for loc in xrange(1, len(self.lst_huesos_original)+1):
            loctemp = cmds.spaceLocator(n= 'LOC_' + str(loc))
            cmds.pointConstraint(self.lst_huesos_original[loc-1],loctemp)
            listaloc.append(loctemp)
            #print self.lst_huesos_original[loc-1]+" "+str(loctemp)


        #CREAR JOINTS(COMIENZA)  minimo y maximo= Dan Rango de ciclo, union cambia hacia donde se conecta un joint y hacia donde se reorienta, jointOrient crear un primer joint sin orientacion
        #jointStart cambia el ciclo de incio del orientado
        cmds.select( d=True )

        self.cadenaJoints(minimo = 2, maximo = 7, jointOrient = 1) #Construye columna 7 joints, el primer joint no se reoerienta ni se une a uno previo
        self.cadenaJoints(minimo = 8, maximo = 8, union = 7) # Contruye dientes arriba 1 joint
        self.cadenaJoints(minimo = 9, maximo = 11, union = 7) # Construye Lengua 3 joints
        self.cadenaJoints(minimo = 12, maximo = 14, union =7) # Construye boca 3 joints
        self.cadenaJoints(minimo = 15, maximo = 23, union =4) # Constryue el brazo 9 joints
        self.cadenaJoints(minimo = 24, maximo = 28, union =19) # Construye pinky 5 joints
        self.cadenaJoints(minimo = 29, maximo = 32, union =19) # Construye cancel 4 joints
        self.cadenaJoints(minimo = 33, maximo = 36, union =19) # Cosntruye index 4 joints
        self.cadenaJoints(minimo = 37, maximo = 40, union =19) # Construye Thums 4 joints
        self.cadenaJoints(minimo = 42, maximo = 46, jointOrient = 41, union = 1) # Construye pierna 6 joints, el primer joint no se reorienta pero si se une al joint 1

        cmds.select( d=True ) # limpia la selecion

        self.cadenaJoints(minimo = 47, maximo = 50) # Construye revers 4 joints
        self.cadenaJoints(union = 7, jointOrient= 51) # Crear ojo 1 joint, no se reorienta
        self.cadenaJoints(jointOrient=52, union = 4)# Construye el busto 1 joint
        self.cadenaJoints(minimo = 16, maximo = 20, jointStart=53, union = 15) # Construye brazo ik 5 joints, el primer joint se orienta pero las siguientes orientaciones se forzan acomenzar en el joint 52
        self.cadenaJoints(minimo = 16, maximo = 20, jointStart=58, union = 15) # Construye brazo fk 5 joints, el primer joint se orienta pero las siguientes orientaciones se forzan acomenzar en el joint 57


        #Construye los huesos sin mirror directo de cambiar el valor de X (locator) a * -1
        self.cadenaJoints(minimo = 15, maximo = 23, union =4, JointMirror = 1, jointStart=63) # Constryue el brazo 9 joints
        self.cadenaJoints(minimo = 24, maximo = 28, union =67, JointMirror = 1, jointStart=72) # Construye pinky 5 joints
        self.cadenaJoints(minimo = 29, maximo = 32, union =67, JointMirror = 1, jointStart=77) # Construye cancel 4 joints
        self.cadenaJoints(minimo = 33, maximo = 36, union =67, JointMirror = 1, jointStart=81) # Cosntruye index 4 joints
        self.cadenaJoints(minimo = 37, maximo = 40, union =67, JointMirror = 1, jointStart=85) # Construye Thums 4 joints
        self.cadenaJoints(minimo = 42, maximo = 46, union = 41, JointMirror = 1, jointStart=89) # Construye pierna 6 joints, el primer joint no se reorienta pero si se une al joint 1

        cmds.select( d=True ) # limpia la selecion

        self.cadenaJoints(minimo = 47, maximo = 50, JointMirror = 1, jointStart=93) # Construye revers 4 joints
        self.cadenaJoints(union = 7, jointOrient= 51, JointMirror = 1, jointStart=98) # Crear ojo 1 joint, no se reorienta
        self.cadenaJoints(jointOrient=52, union = 4, JointMirror = 1, jointStart=99)# Construye el busto 1 joint
        self.cadenaJoints(minimo = 16, maximo = 20, jointStart=100, union = 63, JointMirror = 1) # Construye brazo ik 5 joints, el primer joint se orienta pero las siguientes orientaciones se forzan acomenzar en el joint 52
        self.cadenaJoints(minimo = 16, maximo = 20, jointStart=105, union = 63, JointMirror = 1) # Construye brazo fk 5 joints, el primer joint se orienta pero las siguientes orientaciones se forzan acomenzar en el joint 57
        

        cmds.delete('joint57', 'joint62','joint104','joint109') # Preguntar como almacenar esto en la variable de abajo
        huesos_borrados = 4 # recordar hardcore

        #CREAR JOINTS(TERMINA)


        #BORRAR LOCATORS(COMIENZA)

        type = cmds.ls(type= "locator")

        cmds.select(type)

        cmds.pickWalk( direction='up' )

        cmds.delete()


        #RENOMBRA HUESOS(COMIENZA)

        list_huesos=[]
        for names in xrange(0, len(self.lst_huesos_original)):
            list_huesos.append(self.lst_huesos_original[names][2:]) #quita RG_ de la lista
        
        list_huesos.extend(self.list_huesos_extendida)


        count_list = 0
        for rename in xrange(1, len(list_huesos)+1 + huesos_borrados): 
            if cmds.objExists('joint'+ str(rename)):
                cmds.rename('joint'+ str(rename), list_huesos[count_list]) #renombra los joints
                #print 'joint'+str(rename)+ '  '+ list_huesos[count_list]
                count_list = count_list+1



        #ELIMINA HUESOS REFERENCIA (COMIENZA)

        cmds.delete( 'R_ROOT', 'R_REV_IZQ_1' )


        #ACOMODAR DRIVER(COMIENZA)

        lst_huesos_acomodo = ['CINTURA','ROOT','COLUMNA_BAJA','COLUMNA_MEDIA','COLUMNA_ALTA','CABEZA','CLAVICULA_IZQ','CLAVICULA_DER','MANO_IZQ','MANO_DER','DIENTES_ARRIBA',
        'DIENTES_BAJA','MANDIBULA_INUTIL','LENGUA_2','CODO_IZQ','CODO_DER','RODILLA_DER','RODILLA_IZQ','TALON_DER','TALON_IZQ','PINKY_SEC_IZQ','PINKY_SEC_DER','OJO_IZQ','OJO_DER',
        'REV_IZQ_1','DEDOS_PIE_IZQ','PUNTA_PIE_IZQ_INUTIL','PUNTA_PIE_IZQ_INUTIL','REV_DER_1','DEDOS_PIE_DER','PUNTA_PIE_DER_INUTIL','PUNTA_PIE_DER_INUTIL','HOMBRO_IZQ_FK','CODO_IZQ_FK','MANO_IZQ_FK',
        'HOMBRO_DER_FK','CODO_DER_FK','MANO_DER_FK', 'CUELLO','CABEZA_INUTIL','CABEZA_INUTIL','BUSTO_IZQ','BUSTO_DER']

        for acomodo in xrange(0, len(self.lst_drivers)):
            #print lst_huesos_acomodo[acomodo]+" "+self.lst_drivers[acomodo]
            cmds.pointConstraint(lst_huesos_acomodo[acomodo] , self.lst_drivers[acomodo])


        lst_huesos_dedos = ['THUMB_IZQ_1','THUMB_IZQ_2','THUMB_IZQ_3','INDEX_IZQ_1','INDEX_IZQ_2','INDEX_IZQ_3','MIDDLE_IZQ_1','MIDDLE_IZQ_2','MIDDLE_IZQ_3',
        'CANCEL_IZQ_1','CANCEL_IZQ_2','CANCEL_IZQ_3','PINKY_IZQ_1','PINKY_IZQ_2','PINKY_IZQ_3']

        
        for acomodo in xrange(0, len(self.lst_grupos_dedos)):
            #print lst_huesos_dedos[acomodo]+" "+self.lst_grupos_dedos[acomodo]
            
            cmds.parentConstraint(lst_huesos_dedos[acomodo] , self.lst_grupos_dedos[acomodo])
            cmds.parentConstraint(lst_huesos_dedos[acomodo].replace('IZQ' , 'DER') , self.lst_grupos_dedos[acomodo].replace('IZQ' , 'DER'))


        type = cmds.ls(type= "pointConstraint")
        cmds.delete(type)

        type = cmds.ls(type= "parentConstraint")
        cmds.delete(type)


            
        #Prende todas las curvas de la escena
        for curva in cmds.ls(et='nurbsCurve'):
            curvaParent = cmds.listRelatives(curva, p=True)[0]
            
            try:
                cmds.setAttr(curvaParent + '.visibility', 1)
            
            except Exception as e:
                pass

        #Si el personaje es femenino
        if self.sex.isChecked():
            cmds.delete('DRIVER_BUSTO_IZQ','DRIVER_BUSTO_DER','DRIVER_BUSTO','BUSTO_IZQ','BUSTO_DER')
            self.lst_huesos_original.remove('R_BUSTO_IZQ')
            list_huesos.remove('BUSTO_IZQ')
            self.lst_drivers.remove('DRIVER_BUSTO_IZQ')
            self.lst_drivers.remove('DRIVER_BUSTO_DER')



    def crearJoint(self,loc, mirror=None):
        if mirror == None:
            PX = cmds.getAttr(loc+'.tx')
        else:
            PX = cmds.getAttr(loc+'.tx')
            PX = PX * -1
        
        PY = cmds.getAttr(loc+'.ty')
        PZ = cmds.getAttr(loc+'.tz')
        cmds.joint( p=(PX, PY, PZ) )
        #print "Cree un joint"

    def mirrorJoints(self,joint):

        for ciclo_mirror in joint:
            cmds.select( ciclo_mirror, visible=True )
            cmds.mirrorJoint(mirrorYZ=True,mirrorBehavior=True,searchReplace=('IZQ', 'DER') )

    def cadenaJoints(self, minimo= None, maximo= None, jointStart= None, jointOrient = None, union = None, JointMirror=None):

        if union != None:
            cmds.select('joint' + str(union))

        if jointOrient != None:
                self.crearJoint(loc="LOC_"+ str(jointOrient), mirror=JointMirror)
        
        if minimo != None and maximo != None: 

            for crear in xrange(minimo, maximo+1): 
                if union != None and jointOrient == None :
                    self.crearJoint(loc = ("LOC_" + str(crear)), mirror=JointMirror)
                    crear_mod = union
                    cmds.joint( 'joint'+ str(crear_mod) , e=True, zso=True, oj='xyz', sao = 'yup')
                    union = None

                else:
                    if jointStart == None:
                        self.crearJoint(loc = ("LOC_" + str(crear)), mirror=JointMirror)
                        crear_mod = crear-1
                        cmds.joint( 'joint'+ str(crear_mod) , e=True, zso=True, oj='xyz', sao = 'yup')

                    else:
                        self.crearJoint(loc = ("LOC_" + str(crear)), mirror=JointMirror)
                        crear_mod = jointStart
                        cmds.joint( 'joint'+ str(crear_mod) , e=True, zso=True, oj='xyz', sao = 'yup')
                        jointStart = jointStart +1