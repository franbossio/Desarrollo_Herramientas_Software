def buscar_fecha(mayor_amp,menor_amp): #funcion para buscar la fecha especifica de medicion de una estacion
    lista=[] 
    lista2=[]
    lista3=[]
    with open('registro_temperatura365d_smn.txt') as arc:
        lineas = arc.readlines()[3:]
        for linea in lineas:
            lista.append(linea.strip()) #guardo el archivo en cada linea
       
        for listas in lista:
            if mayor_amp[0] in listas:
                lista2.append(listas)
            if menor_amp[0] in listas:
                lista3.append(listas)
        fecha,resto= lista2[mayor_amp[2]].split(maxsplit=1)
        fecha2,resto2= lista3[menor_amp[2]].split(maxsplit=1)
    
    return fecha,fecha2

datos = {}
with open('registro_temperatura365d_smn.txt') as archivo:
    lineas = archivo.readlines()[3:]
    for linea in lineas:
        partes = linea.strip().split(maxsplit=3)
        if len(partes)==4:
            fecha,temp1,temp2,nombre=partes
            if '.' in temp1 and '.' not in temp2: #[17082025, 3.6, ESCUELA, DE AVIACION MILITAR AERO ]
                nombre = temp2 + ' ' + nombre #escuela de aviacion miliatar aero
                tmax,tmin=None,float(temp1)
            elif '.' not in temp1 and '.' not in temp2:
                nombre = temp1 + temp2 + ' ' + nombre
                tmax,tmin = None, None
            else: 
                tmax,tmin = float(temp1),float(temp2)
        elif len(partes)==3: #[16082025,CHILECITO,AERO]
            fecha,temp_value,nombre=partes
            if '.' in temp_value:
                tmax, tmin= None,float(temp_value)
            elif '.' not in temp_value:
                nombre=temp_value + ' ' +nombre #chilecito aero
                tmax,tmin=None,None
        else:#len(partes)<=2 pero siempre es ==2 porque no puede ser ==1
            fecha,nombre=partes #[17082025,JACHAL]
            tmax,tmin=None,None
        if nombre not in datos:
            datos[nombre]={'tmax':[],'tmin':[]}
        datos[nombre]['tmax'].append(tmax)
        datos[nombre]['tmin'].append(tmin)
    for _ in range(9):  
        datos.popitem()

    
with open('reporte.txt','w',encoding='UTF-8') as reporte:
    reporte.write('\n------------TEMPERATURA MAXIMAS Y MINIMAS DE CADA ESTACION------------\n')
    for clave,valor in datos.items():
        try:
            temperatura_maxima=max(x for x in valor['tmax'] if x is not None)
        except ValueError:
            temperatura_maxima=' No hay registros'
        try:
            temperatura_minima=min(x for x in valor['tmin'] if x is not None)
        except ValueError:
            temperatura_maxima=' No hay registros'
        
        reporte.write(f'\n{clave}: TMAX:{temperatura_maxima}, TMIN:{temperatura_minima}')
        
    reporte.write('\n------------MAYOR Y MENOR AMPLITUD TERMICA EN UN DIA------------\n')
    
    mayor_amp = ("", -1, None)  # (est,amp,dia)
    menor_amp = ("", 9999, None)
    for dia in range(365):
        for clave,valor in datos.items():
            if dia >= len(valor["tmax"]) or dia >= len(valor["tmin"]):
                continue  # esta estación no tiene datos ese día
            tmax=valor['tmax'][dia]
            tmin=valor['tmin'][dia]
            if tmax is None or tmin is None:
                    continue
            amp=tmax-tmin
            if amp > mayor_amp[1]:
                mayor_amp = (clave, amp, dia)
            if amp < menor_amp[1]:
                menor_amp = (clave, amp, dia)
   
    fecha,fecha2=buscar_fecha(mayor_amp,menor_amp)
    reporte.write(f"Mayor amplitud: {mayor_amp[0]} con {mayor_amp[1]}°C el día {fecha[:2]}/{fecha[2:4]}/{fecha[4:]}\n")
    reporte.write(f"Menor amplitud: {menor_amp[0]} con {menor_amp[1]}°C el día {fecha2[:2]}/{fecha2[2:4]}/{fecha2[4:]}\n")
    
    reporte.write('\n------------DIFERENCIA MAXIMA Y MINIMA ENTRE ESTACCIONES EN UN MISMO DIA------------\n')
       
    max_dif = ("", "", None, -1, None, None)  # (est1, est2, dia, dif, tmax, tmin)
    min_dif = ("", "", None, 999, None, None)

    for dia in range(365):
        estaciones = list(datos.keys())
        for i in range(len(estaciones)):
            for j in range(len(estaciones)):
                if i == j:
                    continue  # no comparar la misma estación

                e1, e2 = estaciones[i], estaciones[j]

                if dia >= len(datos[e1]["tmax"]) or dia >= len(datos[e2]["tmin"]):
                    continue  # alguna estación no tiene datos ese día

                t1 = datos[e1]["tmax"][dia]
                t2 = datos[e2]["tmin"][dia]

                if t1 is None or t2 is None:
                    continue

                dif = abs(t1 - t2)
                if dif > max_dif[3]:
                    max_dif = (e1, e2, dia, dif, t1, t2)
                if dif < min_dif[3]:
                    min_dif = (e1, e2, dia, dif, t1, t2)
    fecha,fecha2=buscar_fecha(max_dif,min_dif)
 
    reporte.write(f"Máxima diferencia: {max_dif[0]} (Tmax={max_dif[4]}) vs {max_dif[1]} (Tmin={max_dif[5]}) "
                    f"= {max_dif[3]}°C el día {fecha[:2]}/{fecha[2:4]}/{fecha[4:]}\n")
    reporte.write(f"Mínima diferencia: {min_dif[0]} (Tmax={min_dif[4]}) vs {min_dif[1]} (Tmin={min_dif[5]}) "
                    f"= {min_dif[3]}°C el día {fecha2[:2]}/{fecha2[2:4]}/{fecha2[4:]}\n")
     
   
print('ARCHIVO REPORTE GENERADO CORRECTAMENTE')