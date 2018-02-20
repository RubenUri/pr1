#| /usr/bin/env python
#-*- coding: utf-8 -*-
#Pedir el nombre y apellidos y visualizar iniciales

import sys
if len (sys.argv) !=4:
	print "Los argumentos son el nombre y apellidos"
	exit()
iniciales=  sys.argv[1][0]+'.' + sys.argv[2][0]+'.' + sys.argv[3][0]+'.'
print "Tus iniciales son:" +iniciales.upper()	
  
  

