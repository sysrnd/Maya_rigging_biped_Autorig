import maya.cmds as cmds
AXIS = ['X','Y','Z']

def spaceSwitchClavicle(clav_ctrl, side):
	'''
	grp_ClavicleCtrl = cmds.listRelatives(Clav_jnt, parent=True)
	grp_ClavicleCtrl = cmds.listRelatives(grp_ClavicleCtrl, s=True)
	'''

	
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
	


