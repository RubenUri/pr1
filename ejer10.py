#| /usr/bin/env python
#-*- coding: utf-8 -*-
#Pedir el nombre y ponerlo en mayúsculas

import sys
if len (sys.argv) !=2:
	print "falta algún argumento"
	exit()
print sys.argv[0]
print sys.argv[1]
print "Tu nombre en mayusculas es:" + sys.argv[1].upper()
	
  
  

