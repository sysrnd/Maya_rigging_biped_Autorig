#TODO
#Reroute BSfile to mayaUtils
import maya.cmds as cmds

class BSconnecter(object):
	def __init__(self):

		BSfile = 'Z:/RnD/Pipeline/Maya/Scripts/Modeling/Maya_modeling_bsCreator/bsNames_Core/bs_list.mkf'
		self.parentBS = 'DRIVER_CARA'
		self.attributes = {}
		self.recAttrLookUp()
		self.bs = self.readLocalInfo(BSfile)
		self.matchBSToAttr()
		print self.attributes

	def main(self):
		pass

	def recAttrLookUp(self):
		
		children = cmds.listRelatives(self.parentBS, ad=True)
		children.append(self.parentBS)

		for child in children:
			if child.find('Shape') == -1 and child.isupper() == True:
				attrs = cmds.listAttr(child, k=True, st='*BS*')
				if attrs != None:
					for attr in attrs:
						self.attributes[str(attr)] = ''


	def matchBSToAttr(self):

		for key, attr in self.attributes.iteritems():
			for bs in self.bs:
				if key.find(bs) != -1:
					self.attributes[key] = bs
				

	def connectToRoot(self):
		pass

	def connectToDriver(self):
		pass

	def connectToVis(self):
		pass

	def readLocalInfo(self):
		'''
		'''
		localData = []

		for mesh in cmds.ls(et='mesh'):
			meshParent = cmds.listRelatives(mesh, p=True)[0]



bs = BSconnecter()
bs.main()