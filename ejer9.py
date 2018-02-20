#| /usr/bin/env python
#-*- coding: utf-8 -*-
#Visualizar todos los ficheros que contengan una letra dada de un directorio

import os

directorio=raw_input('Introduce el directorio donde quieres buscar:')
letra=raw_input('Introduce la letra que quieres que tenga el nombre del fichero a mostrar:')


if not os.access(directorio,0):
	print "El directorio no existe"
	exit()

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero.count(letra)>0:
		print fichero
  
  

