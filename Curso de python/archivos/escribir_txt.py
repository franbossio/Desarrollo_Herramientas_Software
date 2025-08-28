with open('archivos\\texto.txt','w',encoding='UTF-8') as archivo: #con a podes agregar y no sobreescribir
    #escrive el archivo pero borra todo y escribe lo nuevo
    #archivo.write('jjaajjaj, te la recontra cambie')
    
    #escribe lineas, pero no sobreescriber
    archivo.writelines(['hola como estas?','\nhoal'])