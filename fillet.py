#!/usr/bin/env python
import hashlib
import StringIO
import os
from subprocess import *


def filetowallet(path, number):
	filin = open(path, 'r')
	filec = filin.read()
	filin.close()
	return hashlib.sha256(filec + number).digest().encode('hex')



from optparse import OptionParser

if __name__ == '__main__':

	parser = OptionParser(usage="%prog [options]", version="%prog 1.0")

	parser.add_option("--file", dest="file", 
		help="file")

	parser.add_option("--keynumber", dest="keynumber", 
		help="keynumber", default="1")

	parser.add_option("-p", "--pwpath", dest="pwpath", 
		help="pywallet.py directory")

	(options, args) = parser.parse_args()

	if options.file is None:
		print "You must provide a file"
		exit(0)

	if not os.path.isfile(options.file):
		print '%s doesn\'t exist'%(options.file)
		exit(0)

	seckey = filetowallet(options.file, options.keynumber)
	print options.file + ", key #" + options.keynumber + ": " + seckey

	if options.pwpath is not None:
		a=Popen(options.pwpath + "pywallet.py --info --importhex --importprivkey " + seckey, shell=True, bufsize=-1, stdout=PIPE).stdout
		print(a.read())
		a.close()





