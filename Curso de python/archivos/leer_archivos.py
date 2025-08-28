archivo = open('archivos\\texto.txt',encoding='UTF-8')
#leer archivos
#archivo_leer = archivo.read()
#leer linea por linea
#linea_1 = archivo.readlines()

#leer una sola linea
linea_1 = archivo.readline() #si ponemos un numero se lee la cantindad de caracteres que pusiste
print(linea_1)

archivo.close()