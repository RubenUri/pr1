#| /usr/bin/env python
#-*- coding: utf-8 -*-
edad=raw_input('Introduce tu edad:')

if edad<18:
  print 'Eres menor de edad'
elif edad>=18 and edad<31:
  print 'Eres joven'
elif edad>30 and edad<46:
  print 'Eres maduro'
else: 
  print 'Eres un viejuno'

  
  

