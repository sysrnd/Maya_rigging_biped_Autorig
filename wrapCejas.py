import maya.cmds as cmds

AXIS = ['X','Y','Z']
ATTR = ['.translate', '.rotate', '.scale']

def rename():
	wrapped = False

	for geo in cmds.ls(et='mesh'):
		if geo.find('CEJAS') != -1:
			if geo.find('_MD') != -1:
				if wrapped == False:
					print geo
					geoParent = cmds.listRelatives(geo, p=True)[0]
					geoParent = cmds.rename(geoParent, 'CEJAS_MD')
					wrap(geoParent)

					wrapped = True
					cmds.select(cl=True)

def wrap(geo):
	
	md_CejasWrap = cmds.duplicate(geo, rr=True, n='CEJAS_WRAP_BS')[0]

	bs_rootPos = cmds.xform('ROOT_BS', q=True, ws=True, t=True)

	for ax in range(0, len(AXIS)):
		cmds.setAttr(md_CejasWrap + '.translate' + AXIS[ax], l=False)
		cmds.setAttr(md_CejasWrap + '.translate' + AXIS[ax], bs_rootPos[ax])

	cmds.select(cl=True)
	cmds.select(md_CejasWrap, 'ROOT_BS')
	cmds.CreateWrap()
	cmds.select(cl=True)

	for grp in cmds.ls(et='transform'):
		if grp.find('GRP') != -1 and grp.find('BLEND') != -1:
			cmds.parent(md_CejasWrap, grp)


def block():

	for geo in cmds.ls(et='nurbsCurve'):
		if geo.find('DEFORM_CURV') != -1:
			geoParent = cmds.listRelatives(geo, p=True)[0]

			for attrib in ATTR:
				for ax in AXIS:
					try:
						cmds.setAttr(geoParent  + attrib + ax, l=True, k=False, cb=False)
					except:
						pass


