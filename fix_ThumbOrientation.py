import maya.cmds as cmds

CTRL_DER = 'DRIVER_THUMB_DER_'
CTRL_IZQ = 'DRIVER_THUMB_IZQ_'
JNT_DER = 'THUMB_DER_'
JNT_IZQ = 'THUMB_IZQ_'
AXIS = ['X']

JNTHAND = 'MANO_DER'
	
def replaceNameHi(names):
	for name in names:
		if name.find('Shape') == -1:
			newName = name.split('|')[-1]
			newName = newName.replace('IZQ', 'DER')
			cmds.rename(name, newName)
			children = cmds.listRelatives(newName, c=True, f=True)
			if children != None:
				replaceNameHi(children)

def mainThumbs():
	#dealts in the dirtiest possible way the mirror of thumb controls
	cmds.delete(cmds.listRelatives(CTRL_DER + '2', parent=True)[0])
	parent = cmds.listRelatives(CTRL_IZQ + '2', p=True)[0]
	dup = cmds.duplicate(parent, n=CTRL_IZQ + 'GRP_2')
	dup = cmds.parent(dup[0], w=True)
	newGrp = cmds.group(dup[0], n='tempGrp')
	cmds.xform(newGrp, ws=True, piv=(0, 0, 0))
	cmds.setAttr(newGrp + '.scaleX', -1)
	ctrl_der_parented = cmds.parent(cmds.listRelatives(newGrp, c=True), CTRL_DER + '1')
	##

	replaceNameHi(cmds.listRelatives(CTRL_DER + '1', c=True, f=True))

	for num in xrange(2, 4):
		num = str(num)
		cmds.orientConstraint(CTRL_DER + num, JNT_DER + num, mo=True)

	cmds.delete('tempGrp')
