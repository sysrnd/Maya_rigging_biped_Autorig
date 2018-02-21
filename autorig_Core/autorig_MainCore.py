import maya.cmds as cmds
import Utils.os_Find_Env.findEnv_app as findEnv

class autoRig_mainCore(object):

	def __init__(self):
		pass
	def importRig(self):
		'''
		namespace=':' to delete namespaces
		'''
		fileEnv = findEnv.findEnvVar_()
		cmds.file(fileEnv + '/Rigging/Maya_rigging_biped_Autorig/maya_files/RIGG_BASE.ma', type='mayaAscii', ignoreVersion=True, ra=True, mergeNamespacesOnClash=True, namespace= ':', pr=True, i=True)

