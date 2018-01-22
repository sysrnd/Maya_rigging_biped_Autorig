CTRL_DER = 'DRIVER_THUMB_DER_'
CTRL_IZQ = 'DRIVER_THUMB_IZQ_'
JNT_DER = 'THUMB_DER_'
JNT_IZQ = 'THUMB_IZQ_'
AXIS = ['X']

JNTHAND = 'MANO_DER'
for num in xrange(2, 4):
	num = str(num)
	inconmingCons = cmds.listConnections(CTRL_DER + num, scn=True, t='orientConstraint')[0]
	cmds.delete(inconmingCons)

for num in xrange(2, 4):
	num = str(num)
	cmds.parent('GRP_' + CTRL_DER + num, JNTHAND)

for num in xrange(2, 4):

	if num == 2:
		resta = 160
	else:
		resta = 90

	num = str(num)
	srcJnt = 'GRP_' + CTRL_IZQ + num
	destJnt = 'GRP_' + CTRL_DER + num
	attr = cmds.getAttr(srcJnt + '.rotateX')
	attr -= resta
	cmds.setAttr(destJnt + '.rotateX', attr)


for num in xrange(2, 4):
	num = str(num)
	CTRL = CTRL_DER + str(int(num) - 1)
	cmds.parent('GRP_' + CTRL_DER + num, CTRL)

for num in xrange(2, 4):
	num = str(num)
	cmds.orientConstraint(CTRL_DER + num, JNT_DER + num, mo=True)