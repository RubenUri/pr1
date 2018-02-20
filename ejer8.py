#| /usr/bin/env python
#-*- coding: utf-8 -*-
#Visualizar todos los shell scripts de un directorio

import os

directorio=raw_input('Introduce el directorio donde quieres buscar:')


if not os.access(directorio,0):
	print "El directorio no existe"
	exit()

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero[-3:]=='.sh':
		print fichero
  
  

