#TODO
#parpados
import maya.cmds as cmds

class BSconnecter(object):
	def __init__(self):

		self.parentBS = 'DRIVER_CARA'
		self.rootBS = 'ROOT_BS'
		self.cejasWrap = 'CEJAS_WRAP_BS'
		self.wire = 'WIRE_BS'
		self.driverParpados = {'PARPADO_INFERIOR_IZQ': 'PARPADO_DOWN_CERRADO_IZQ_BS', 'PARPADO_INFERIOR_DER': 'PARPADO_DOWN_CERRADO_DER_BS', 'PARPADO_SUPERIOR_IZQ': 'PARPADO_UP_CERRADO_IZQ_BS', 'PARPADO_SUPERIOR_DER': 'PARPADO_UP_CERRADO_DER_BS'}
		self.bs = []
		self.forbiddenbs = ['ROOT_BS', 'CEJAS_WRAP_BS', 'CEJAS_WRAP_BSBase', 'ROOT_BSBase', 'ROOT_BSShape', 'CEJAS_WRAP_BSShape', 'CEJAS_WIRE_BS']
		self.attributes = {}
		self.lonelyBs = []

	def main(self):
		'''
		'''
		#initial bs and attributes query
		self.recAttrLookUp()
		self.getBS()
		self.matchBSToAttr()

		cabeza = self.findMDMesh('MD', 'CABEZA')
		cejas = self.findMDMesh('MD', 'CEJAS')

		rootBSNode = self.createBS(self.bs, self.rootBS, 'BLEND_ROOT')[0]
		gralBSNode = self.createBS(self.rootBS, cabeza, 'BLEND_GENERAL')[0]
		cejasBSNode = self.createBS(self.cejasWrap, cejas, 'BLEND_CEJAS')[0]
		
		cmds.setAttr(gralBSNode + '.' + self.rootBS, 1)
		cmds.setAttr(cejasBSNode + '.' + self.cejasWrap, 1)
		cmds.setAttr(rootBSNode + '.' + self.wire, 1)

		
		#bs to ctrls user-defined attrs
		for key, bs in self.attributes.iteritems():
			#appends leftover bs
			if bs == '':
				self.lonelyBs.append(key)
			else:
				self.directConn(key, rootBSNode + '.' + bs)
		
		for drv, bs in self.driverParpados.iteritems():
			if drv.find('SUPERIOR') != -1:
				attr = '.translateY'
				self.inverseConn(drv + attr, rootBSNode + '.' + bs)
			else:
				self.directConn(drv + attr, rootBSNode + '.' + bs)


	def recAttrLookUp(self):
		'''
		recursively looks up for attributes in DRIVER_CARA and children
		'''
		children = cmds.listRelatives(self.parentBS, ad=True)
		children.append(self.parentBS)

		for child in children:
			if child.find('Shape') == -1 and child.isupper() == True:
				attrs = cmds.listAttr(child, k=True, st='*BS*')
				if attrs != None:
					for attr in attrs:
						self.attributes[str(child + '.' + attr)] = ''

	def getBS(self):
		'''
		'''
		for mesh in cmds.ls(et='mesh'):
			meshParent = cmds.listRelatives(mesh, p=True)[0]
			if meshParent.find('BS') != -1 and meshParent not in self.forbiddenbs:
				self.bs.append(meshParent)

	def matchBSToAttr(self):
		'''
		matches bs to attributes
		'''
		for key, attr in self.attributes.iteritems():
			for bs in self.bs:

				skey = key.split('.')[-1][3:]
				sbs = bs[:-3]

				if skey.find(sbs) == 0:
					self.attributes[key] = bs

	def directConn(self, src, dest):
		cmds.connectAttr(src, dest, f=True)

	def inverseConn(self, src, dest):
		rev = cmds.shadingNode('multiplyDivide', au=True, n='_rev')
		cmds.setAttr(rev + '.input2X', -1)
		cmds.connectAttr(src, rev + '.input1X')
		cmds.connectAttr(rev + '.outputX', dest)

	def createBS(self, src, dest, name):
		cmds.select(cl=True)
		bsNode = cmds.blendShape(src, dest, n=name)
		return bsNode

	def findMDMesh(self, keyOne, keyTwo):
		foundMesh = ''

		for mesh in cmds.ls(et='mesh'):
			meshParent = cmds.listRelatives(mesh, p=True)[0]
			if mesh.find(keyOne) != -1 and mesh.find(keyTwo) != -1:
				foundMesh = meshParent

		return foundMesh




bs = BSconnecter()
bs.main()