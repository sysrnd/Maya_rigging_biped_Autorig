import maya.cmds as cmds

AXIS = ['X','Y','Z']

def rename():
	wrapped = False

	for geo in cmds.ls(et='mesh'):
		if geo.find('CEJAS') != -1:
			if geo.find('MD_') != -1:
				if wrapped == False:
					geoParent = cmds.listRelatives(geo, p=True)[0]
					geoParent = cmds.rename(geoParent, 'MD_CEJAS')
					wrap(geoParent)

					wrapped = True
					cmds.select(cl=True)

def wrap(geo):
	
	

	md_CejasWrap = cmds.duplicate(geo, rr=True, n='MD_CEJAS_WRAP')[0]

	bs_rootPos = cmds.xform('BS_ROOT', q=True, ws=True, t=True)

	for ax in range(0, len(AXIS)):
		cmds.setAttr(md_CejasWrap + '.translate' + AXIS[ax], bs_rootPos[ax])

	cmds.select(cl=True)
	cmds.select(md_CejasWrap, 'BS_ROOT')
	cmds.CreateWrap()
	cmds.select(cl=True)

rename()