
#| /usr/bin/env python
#-*- coding: utf-8 -*-

import sys

def saludar(saludo):
	print saludo

def iniciales1(nombre,ape1,*apellidos):
	iniciales=nombre+[0]+'.'+ape1[0]
	for ape in apellidos:
		iniciales=iniciales+'.'+ape[0]
	return iniciales.upper()	

