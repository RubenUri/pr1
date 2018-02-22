import os

def crea_dir(directorio):
	if os.access(directorio,0):
		return 1
	else:
		os.mkdir(directorio)
		return 0


def lista_fic(directorio):
	if not os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	lista=os.listdit(directorio)
	for fichero in lista:
		f1=directorio+'/'+fichero
		if os.path.isfile(f1):
			print fichero+ '--->'+str(os.path.getsize(f1))
