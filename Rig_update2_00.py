import maya.cmds as cmds
AXIS = ['X', 'Y', 'Z']
class updateRig(object):
	def __init__(self):
		self.wiresList = ['LABIO_SUPERIOR_ESQ_DER', 'LABIO_INFERIOR_ESQ_DER', 'LABIO_SUPERIOR_DER', 'LABIO_INFERIOR_DER']
		self.clavicleList = ['DRIVER_CLAVICULA_DER']
		self.fingers = ['DRIVER_MIDDLE', 'DRIVER_CANCEL', 'DRIVER_INDEX', 'DRIVER_PINKY', 'DRIVER_THUMB']
		self.keywords = ['CABEZA', 'OJO', 'ESCLERA', 'CEJAS', 'DIENTES', 'LENGUA', 'ENCIA', 'CABELLO']
		self.latNames = {'squash': [True, 'Y'], 'stretch': [False, 'Y'], 'left': [False, 'X'], 'right': [True, 'X']}
	def mainWires(self, ctrls):
		for ctrl in ctrls:
			handle = self.getConn(ctrl, 'transform')
			self.replaceConn(handle, ctrl)
			grp = self.group(ctrl)
			self.setGroup(grp, 0)
	def mainClavicle(self, ctrls):
		for ctrl in ctrls:
			cons = self.getConn(ctrl, 'orientConstraint')
			jnt = self.getConn(cons, 'joint')
			cmds.delete(cons)
			grp = self.group(ctrl)
			self.setGroup(grp, 1)
			self.orientCons(ctrl, jnt)
	def mainFingers(self, ctrls):

		sides = ['_DER_', '_IZQ_']
		for ctrl in ctrls:
			for side in sides:
				for num in xrange(1, 4): #controls from finger_1 to finger_3


					ctrlDriver = ctrl + side + str(num)
					cons = self.getConn(ctrlDriver, 'orientConstraint')
					jnt = self.getConn(cons, 'joint')
					self.pointCons(ctrlDriver, jnt)
					for ax in AXIS:
						cmds.connectAttr(ctrlDriver + '.scale' + ax , jnt + '.scale' + ax, f=True)
						cmds.setAttr(ctrlDriver + '.translate' + ax, l=False, k=True)
						cmds.setAttr(ctrlDriver + '.scale' + ax, l=False, k=True)
	def mainHeadSquetch(self):
		latticesToGroup = []
		geo = self.getGeo(self.keywords)
		squetchCtrl = self.importCtrl()

		for lat in self.latNames:
			lattices = self.lattice(geo, lat)
			self.setupLat(lattices[0], lat, squetchCtrl)
			latticesToGroup.append(lattices[1])
			latticesToGroup.append(lattices[2])

		self.latsToHierarchy(latticesToGroup, 'DRIVER_CABEZA', squetchCtrl)
	def group(self, ctrl):
		grp = cmds.group(ctrl, n=ctrl.lower() + '_grp')
		return grp
	def setGroup(self, grp, option=10):
		cmds.xform(grp, cp=True)
		for x in range(0, 2):
			if 0 == option:
				cmds.setAttr(grp + '.rotateY', 180)
			elif 1 == option:
				cmds.setAttr(grp + '.rotateX', -10)
				cmds.setAttr(grp + '.rotateY', -180)
				cmds.setAttr(grp + '.rotateZ', 30)
	def deleteCons(self, cons):

		cmds.delete(cons)
	def orientCons(self, ctrl, jnt):

		cmds.orientConstraint(ctrl, jnt, mo=True)
	def scaleCons(self, ctrl, jnt):

		cmds.scaleConstraint(ctrl, jnt, mo=True)
	def pointCons(self, ctrl, jnt):

		cmds.pointConstraint(ctrl, jnt, mo=True)
	def getConn(self, ctrl, typeCons):
		cmds.select(ctrl)
		handle = cmds.listConnections(ctrl, type=typeCons)[0]
		return handle
	def replaceConn(self, handle, ctrl):

		mul = cmds.shadingNode('multiplyDivide', asUtility=True, n=handle + '_inv')
		cmds.connectAttr(mul + '.output', handle + '.translate', f=True)
		cmds.connectAttr(ctrl + '.translate', mul + '.input1', f=True)

		cmds.setAttr(mul +'.input2X', -1)
		cmds.setAttr(mul +'.input2Y', 1)
		cmds.setAttr(mul +'.input2Z', -1)
	def getPos(self, obj):
		axis = ['X', 'Y', 'Z']
		loc = cmds.spaceLocator()
		loc = cmds.parent(loc, obj)[0]

		for ax in axis:
			cmds.setAttr(loc + '.translate' + ax, 0)
			cmds.setAttr(loc + '.rotate' + ax, 0)

		pos = cmds.xform(loc, q=True, ws=True, t=True)
		cmds.delete(loc)
		return pos
	def getGeo(self, keywords):
		geo = []
		for x in cmds.ls(et='mesh', l=True):
		    if x.find('WRAP') == -1:
		        if x.find('MD') != -1:
		        	if x.find('WIRE') == -1:
			            for key in keywords:
			                if x.find(key) != -1:
			                    xParent = cmds.listRelatives(x, parent=True, f=True)[0]
			                    geo.append(xParent)
		return geo
	def lattice(self, geo, name):
		cmds.select(geo)
		print geo
		latticesNode = cmds.lattice(n = name + '_lat', objectCentered=True, dv=(3, 3, 3))
		cmds.select(cl=True)
		return latticesNode
	def setupLat(self, lattice, name, ctrl):

		clampNode = cmds.shadingNode('clamp', asUtility=True, n=name + '_clamp')
		cmds.setAttr(clampNode + '.maxR', 1)
		cmds.connectAttr(clampNode + '.outputR', lattice + '.envelope', f=True)
		if self.latNames[name][0]:
			invNode = cmds.shadingNode('multiplyDivide', asUtility=True, n=name + '_inv')
			cmds.setAttr(invNode + '.input2X', -1)
			cmds.connectAttr(invNode + '.outputX', clampNode + '.inputR', f=True)
			cmds.connectAttr(ctrl + '.translate' + self.latNames[name][1], invNode + '.input1X', f=True)
		else:
			cmds.connectAttr(ctrl + '.translate' + self.latNames[name][1], clampNode + '.inputR', f=True)
	def importCtrl(self):
		ctrl = cmds.file("Z:/RnD/Pipeline/Maya/Scripts/Rigging/MKF_Autorig/Autorig_v06_01122017/base_FaceCtrls.ma", i=True, rnn=True)
		print '####'
		print ctrl
		return ctrl[3]
	def latsToHierarchy(self, lats, headCtrl, squetchCtrl):
		squetchCtrlGrp = cmds.listRelatives(squetchCtrl, p=True)[0]
		cmds.group(lats)
		cmds.parent(lats, headCtrl)
		cmds.parent(squetchCtrlGrp, headCtrl)

uRig = updateRig()
uRig.mainWires(uRig.wiresList)
#uRig.mainClavicle(uRig.clavicleList)
uRig.mainFingers(uRig.fingers)
uRig.mainHeadSquetch()