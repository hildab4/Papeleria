#Maria Fernanda Damian A01251918
#Sebastián Gálvez A01251884
#Alam López A01252135
#Hilda Beltrán A01251916
#Ena Azcona A01252031

#Definir una variable de string para ingresar los datos de la compra
texto = ''
#Definir variable para almacenar el precio total
suma = 0

#Función para obtener si es cliente o vendedor
def papeleria():
    persona  = str(input('Selecciona si es cliente C o vendedor V: '))
    print('\n' + '========================================='
          + '===========================================' + '\n')
    
    def cliente():
        #Abre el archivo con los datos del inventario para poder leerlos
        invent = open('invent.txt', 'r')
        matriz  = invent.readlines()
        invent.close()
        #Llama a las variables globales para poder almacenar información
        global texto
        global suma
        #Define los elementos del inventario
        lapizpluma = matriz[0].split(',')
        lapizpluma[5] = lapizpluma[5][0:len(lapizpluma[5])-1]
        pintura1 =  matriz[1].split(',')
        pintura1[5] = pintura1[5][0:len(pintura1[5])-1]
        pintura2 = matriz[2].split(',')
        pintura2[5] = pintura2[5][0:len(pintura2[5])-1]
        pincelsacapuntas =  matriz[3].split(',')
        pincelsacapuntas[5] = pincelsacapuntas[5]\
                              [0:len(pincelsacapuntas[5])-1]
        cuadernos = matriz[4].split(',')
        cuadernos[5] = cuadernos[5][0:len(cuadernos[5])-1]
        hojaspegamento =  matriz[5].split(',')
        hojaspegamento[5] = matriz[5][0:len(hojaspegamento[5])-1]
        
        #Muestra las opciones del menú
        print ('Si desea comprar lapiz marque L')
        print ('Si desea comprar plumas marque P')
        print ('Si desea comprar pinturas marque PI')
        print ('Si desea comprar pinceles marque PC')
        print ('Si desea comprar sacapuntas marque S')
        print ('Si desea comprar cuadernos marque C')
        print ('Si desea comprar hojas marque H')
        print ('Si desea comprar pegamento marque PEG' + '\n')
        
        #Guarda el producto que se quiere comprar
        art = str(input('Ingrese el producto que quiera comprar: '))
        print('\n' + '========================================='
          + '===========================================' + '\n')
        
        #Define a qué posición del inventario se resta la cantidad especificada
        #Añade el producto con la cantidad a la variable texto para después
        #añadirla al archivo de texto
        if art == 'L':
            tipo = str(input('Ingrese el tipo de lápiz a agregar: '
                             + '\n' + 'B para blando $5' + '\n' +
                             'M para medio $10' + '\n' + 'D para duro $15'
                             + '\n'))
            if tipo != 'B' and tipo != 'M' and tipo != 'D':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                
                if 'B' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[0]) > cantidad:
                            lapizpluma[0] = int(lapizpluma[0]) - cantidad
                            texto = texto + str(cantidad) + ' Lápiz blando'\
                                    + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'M' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[1]) > cantidad:
                            lapizpluma[1] = int(lapizpluma[1]) - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Lápiz medio' + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'D' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[2]) > cantidad:
                            lapizpluma[2] = int(lapizpluma[2]) - cantidad
                            texto = texto + str(cantidad) + ' Lápiz duro'\
                                    + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                
        elif art == 'P':
            tipo = str(input('Ingrese el color de pluma a agregar:'
                             + '\n' + 'N para negro $5' + '\n'
                             + 'A para azul $10' + '\n' + 'R para rojo $15'
                             + '\n'))
            if tipo != 'N' and tipo != 'A' and tipo != 'R':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'N' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[3]) > cantidad:
                            lapizpluma[3] = int(lapizpluma[3]) - cantidad
                            texto = texto + str(cantidad) + ' Pluma negra'\
                                    + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'A' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[4]) > cantidad:
                            lapizpluma[4] = int(lapizpluma[4]) - cantidad
                            texto = texto + str(cantidad) + ' Pluma azul'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'R' == tipo:
                    if cantidad > 0:
                        if int(lapizpluma[5]) > cantidad:
                            lapizpluma[5] = int(lapizpluma[5]) - cantidad
                            texto = texto + str(cantidad) + ' Pluma roja'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                
        
        elif art == 'PI':
            tipo = str(input('Ingrese el color de la pintura: '
                             + '\n' + 'A azul $5' + '\n' + 'AM amarilla $10'
                             '\n' + 'RO roja $15' + '\n' + 'RS rosa $5'
                             + '\n' + 'N naranja $10' + '\n' + 'V verde $15'
                             + '\n' + 'M morada $5' +  '\n' + 'C café $10'
                             + '\n' + 'B blanca $15' + '\n' + 'D dorada $5'
                             + '\n' + 'P plateada $10' + '\n'
                             'BR bronce $15' + '\n'))
            if (tipo != 'A' and tipo != 'AM' and tipo != 'RO' and
                tipo != 'RS' and tipo != 'N' and tipo != 'V' and
                tipo != 'M' and tipo != 'C' and tipo != 'B' and
                tipo != 'D' and tipo != 'P' and tipo != 'BR'):
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'A' == tipo:
                    if cantidad > 0:
                        if int(pintura1[0]) > cantidad:
                            pintura1[0] = int(pintura1[0]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura azul'\
                             + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'AM' == tipo:
                    if cantidad > 0:
                        if int(pintura1[1]) > cantidad:
                            pintura1[1] = int(pintura1[2]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura amarilla'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'RO' == tipo:
                    if cantidad > 0:
                        if int(pintura1[2]) > cantidad:
                            pintura1[2] = int(pintura1[3]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura roja'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'RS' == tipo:
                    if cantidad > 0:
                        if int(pintura1[3]) > cantidad:
                            pintura1[3] = int(pintura1[4]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura rosa'\
                             + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'N' == tipo:
                    if cantidad > 0:
                        if int(pintura1[4]) > cantidad:
                            pintura1[4] = int(pintura1[5]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura naranja'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'V' == tipo:
                    if cantidad > 0:
                        if int(pintura1[5]) > cantidad:
                            pintura1[5] = int(pintura1[2]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura verde'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'M' == tipo:
                    if cantidad > 0:
                        if int(pintura2[0]) > cantidad:
                            pintura2[0] = int(pintura2[0]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura morada'\
                             + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'C' == tipo:
                    if cantidad > 0:
                        if int(pintura2[1]) > cantidad:
                            pintura2[1] = int(pintura2[1]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura café'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'B' == tipo:
                    if cantidad > 0:
                        if int(pintura2[2]) > cantidad:
                            pintura2[2] = int(pintura2[2]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura blanca'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'D' == tipo:
                    if cantidad > 0:
                        if int(pintura2[3]) > cantidad:
                            pintura2[3] = int(pintura2[3]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura dorada'\
                             + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'P' == tipo:
                    if cantidad > 0:
                        if int(pintura2[4]) > cantidad:
                            pintura2[4] = int(pintura2[4]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura plateada'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'BR' == tipo:
                    if cantidad > 0:
                        if int(pintura2[5]) > cantidad:
                            pintura2[5] = int(pintura2[5]) - cantidad
                            texto = texto + str(cantidad) + ' Pintura bronce'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                
                
        elif art == 'PC':
            tipo = str(input('Ingrese el tamaño del pincel:' + '\n'
                             + 'C chico $5' + '\n' + 'M mediano $10' + '\n'
                             + 'G grande $15' + '\n'))
            if tipo != 'C' and tipo != 'M' and tipo != 'G':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'C' == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[0]) > cantidad:
                            pincelsacapuntas[0] = int(pincelsacapuntas[0])\
                                                  - cantidad
                            texto = texto + str(cantidad) + ' Pincel chico'\
                             + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'M'  == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[1]) > cantidad:
                            pincelsacapuntas[1] = int(pincelsacapuntas[1])\
                                                  - cantidad
                            texto = texto + str(cantidad) + ' Pincel mediano'\
                             + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'G' == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[2]) > cantidad:
                            pincelsacapuntas[2] = int(pincelsacapuntas[2])\
                                                  - cantidad
                            texto = texto + str(cantidad) + ' Pincel grande'\
                             + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                
                
        elif art == 'S':
            tipo = str(input('Ingrese el tamaño del sacapuntas:' + '\n' +
                             'C chico $5' + '\n' + 'M mediano $10' + '\n'
                             + 'G grande $15' + '\n'))
            if tipo != 'C' and tipo != 'M' and tipo != 'G':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'C' == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[3]) > cantidad:
                            pincelsacapuntas[3] = int(pincelsacapuntas[3])\
                                                  - cantidad
                            texto = texto + str(cantidad) +\
                             ' Sacapuntas chico' + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'M'  == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[4]) > cantidad:
                            pincelsacapuntas[4] = int(pincelsacapuntas[4])\
                                                  - cantidad
                            texto = texto + str(cantidad) +\
                             ' Sacapuntas mediano' + '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'G' == tipo:
                    if cantidad > 0:
                        if int(pincelsacapuntas[5]) > cantidad:
                            pincelsacapuntas[5] = int(pincelsacapuntas[5])\
                                                  - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Sacapuntas grande' + '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                
                
        elif art == 'C':
            tipo = str(input('Ingrese el tipo de cuaderno:' + '\n'
                             + 'C cuadriculado' + '\n' + 'L lineas' + '\n'))
            if tipo != 'C' and tipo != 'L':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                if 'C' == tipo:
                    tipo2 = str(input('Ingrese el tamaño:' + '\n'
                                      + 'C chico $5' + '\n' + 'M mediano $10'
                                      + '\n' + 'G grande $15' + '\n'))
                    if tipo2 != 'C' and tipo2 != 'M' and tipo2 != 'G':
                        print('\n' + '====================================='
                          + '==============================================='
                              + '\n')
                        print('Ingrese una opción valida')
                    else:
                        cantidad = int(input('Ingrese la cantidad a comprar '))
                    
                        if 'C' == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[0]) > cantidad:
                                    cuadernos[0] = int(cuadernos[0]) - cantidad
                                    texto = texto + str(cantidad) +\
                                            ' Cuaderno cuadro chico' + '\n'
                                    suma = suma + (5 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '=============================='
          + '======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
                        
                        elif 'M'  == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[1]) > cantidad:
                                    cuadernos[1] = int(cuadernos[1]) - cantidad
                                    texto = texto + str(cantidad) +\
                                            ' Cuaderno cuadro mediano' + '\n'
                                    suma = suma + (10 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '=============================='
          + '======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
                                
                        elif 'G' == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[2]) > cantidad:
                                    cuadernos[2] = int(cuadernos[2]) - cantidad
                                    texto = texto + str(cantidad) +\
                                            ' Cuaderno cuadro grande' + '\n'
                                    suma = suma + (15 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '=============================='
          + '======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
                    
                elif 'L' == tipo:
                    tipo2 = str(input('Ingrese el tamaño:' + '\n' + 
                                  'C chico $5' + '\n'
                            + 'M mediano $10' + '\n' + 'G grande $15' + '\n'))
                    if tipo != 'C' and tipo != 'M' and tipo != 'G':
                        print('\n' + '======================================'
                          + '=============================================='
                              + '\n')
                        print('Ingrese una opción valida')
                    else:
                        cantidad = int(input('Ingrese la cantidad a comprar '))
                
                        if 'C' == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[3]) > cantidad:
                                    cuadernos[3] = int(cuadernos[3]) - cantidad
                                    texto = texto + str(cantidad) +\
                                            ' Cuaderno línea chico' + '\n'
                                    suma = suma + (5 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '============================='
          + '=======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
                                
                        elif 'M'  == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[4]) > cantidad:
                                    cuadernos[4] = int(cuadernos[4]) - cantidad
                                    texto = texto + str(cantidad) + \
                                            ' Cuaderno línea mediano' + '\n'
                                    suma = suma + (10 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '=============================='
          + '======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
                                
                        elif 'G' == tipo2:
                            if cantidad > 0:
                                if int(cuadernos[5]) > cantidad:
                                    cuadernos[5] = int(cuadernos[5]) - cantidad
                                    texto = texto + str(cantidad) +\
                                            ' Cuaderno línea grande' + '\n'
                                    suma = suma + (15 * cantidad)
                                else:
                                    print('No disponible')
                                    art = ''
                            else:
                                print('\n' + '=============================='
          + '======================================================' + '\n')
                                print('Ingrese una cantidad mayor a 0')
                                art = ''
            
        elif art == 'H':
            tipo = str(input('Ingresa el tamaño del paquete de hojas:' + '\n'
                             + 'I individual $5' + '\n' + '100 $10' + '\n'
                             + '500 $15' + '\n' + '1000 $20' + '\n'))
            if (tipo != 'I' and tipo != '100' and tipo != '500'
                and tipo != '1000'):
                print('\n' + '========================================='
                  + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'I' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[0]) > cantidad:
                            hojaspegamento[0] = int(hojaspegamento[0])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Hoja individual' + '\n'
                            suma = suma + (5 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                                
                elif '100' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[1]) > cantidad:
                            hojaspegamento[1] = int(hojaspegamento[1])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Paquete 100 hojas' + \
                                    '\n'
                            suma = suma + (10 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '==============================='
          + '=====================================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif '500' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[2]) > cantidad:
                            hojaspegamento[2] = int(hojaspegamento[2])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Paquete 500 hojas' + \
                                    '\n'
                            suma = suma + (15 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '===================================='
          + '================================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif '1000' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[3]) > cantidad:
                            hojaspegamento[3] = int(hojaspegamento[3])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Paquete 1000 hojas' + '\n'
                            suma = suma + (20 * cantidad)
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '================================='
          + '===================================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
        elif art == 'PEG':
            tipo = str(input('Ingresa el tipo de pegamento:' + '\n'
                             + 'B barra $5' + '\n' + 'L liquido $10' + '\n'))
            if tipo != 'B' and tipo != 'L':
                print('\n' + '========================================='
                  + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if 'B' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[4]) > cantidad:
                            hojaspegamento[4] = int(hojaspegamento[4])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Pegamento en barra' + '\n'
                            suma += 5
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '====================================='
          + '===============================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                elif 'L' == tipo:
                    if cantidad > 0:
                        if int(hojaspegamento[5]) > cantidad:
                            hojaspegamento[5] = int(hojaspegamento[5])\
                                                - cantidad
                            texto = texto + str(cantidad) +\
                                    ' Pegamento líquido' + '\n'
                            suma += 10
                        else:
                            print('No disponible')
                            art = ''
                    else:
                        print('\n' + '==================================='
          + '=================================================' + '\n')
                        print('Ingrese una cantidad mayor a 0')
                        art = ''
                        
                else:
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                    print('Ingrese una opción valida')

        #Convierte las variables a string para poder escribirlas en el archivo
        lapizpluma[5] = str(lapizpluma[5]) + '\n'
        pintura1[5] = str(pintura1[5]) + '\n'
        pintura2[5] = str(pintura2[5]) + '\n'
        pincelsacapuntas[5] = str(pincelsacapuntas[5]) + '\n'
        cuadernos[5] = str(cuadernos[5]) + '\n'
        hojaspegamento[5] = str(hojaspegamento[5]) + '\n'
        #Añade los elementos a la lista
        matriz_final = []
        matriz_final.append(lapizpluma)
        matriz_final.append(pintura1)
        matriz_final.append(pintura2)
        matriz_final.append(pincelsacapuntas)
        matriz_final.append(cuadernos)
        matriz_final.append(hojaspegamento)
        #Abre el archivo y escribe los elementos
        pruebainvent = open('invent.txt', 'w')
        numero = ''
        for i in range(6):
            for j in range(6):
                if j <5:
                    numero = numero + str(matriz_final[i][j])+','
                else:
                    numero = numero + str(matriz_final[i][j])
        pruebainvent.write(str(numero))
        pruebainvent.close()
        print('\n' + '========================================='
          + '===========================================' + '\n')
        #Define si continuar con el programa
        continuar = str(input('Si desea agregar otro producto marque "SI"'
                              ', sino marque "NO" ' ))
        print('\n' + '========================================='
          + '===========================================' + '\n')
        if continuar == 'SI':
            cliente()
        else:
            #Pregunta el día de la semana para considerar las ventas de
            #cada día y por lo tanto, vendedor
            compra = open('Data.txt', 'r')
            x = compra.readlines()
            compra.close()
            
            if art != '':
                dia = str(input('¿Qué día de la semana nos visita?' + '\n' + 
                                '\n' + 'Lunes ' + 'Martes ' + 'Miércoles ' 
                                + 'Jueves ' + 'Viernes' + '\n' + '\n'))
                texto = texto + dia + '\n'
                print('\n' + '========================================='
          + '===========================================' + '\n')
                #Escribe la información en el archivo correspondiente
            recibos = open('Data.txt', 'w')
            recibos.write('Productos' + '\n')
            recibos.close()
            recibo = open('Data.txt', 'a')
            recibo.write(texto)
            recibo.close()
            reporte = open('Reporte.txt', 'a')
            reporte.write('\n' + '\n' + texto)
            reporte.close()
            texto = ''
            articulos = open('Data.txt', 'r')
            c = articulos.readlines()
            articulos.close()
                #Muestra el total de la compra
            for i in range(len(c)):
                    print(c[i])
            print('\n')
            print('El total es de ' + str(suma))
            print('\n' + '========================================='
              + '===========================================' + '\n')
            print('Gracias')
            return (matriz_final)
    
    
    def vendedor():
        #Lee el archivo con los datos del inventario
        invent = open('invent.txt', 'r')
        matriz  = invent.readlines()
        invent.close()
        #Define los elementos del inventario
        lapizpluma = matriz[0].split(',')
        lapizpluma[5] = lapizpluma[5][0:len(lapizpluma[5])-1]
        pintura1 =  matriz[1].split(',')
        pintura1[5] = pintura1[5][0:len(pintura1[5])-1]
        pintura2 = matriz[2].split(',')
        pintura2[5] = pintura2[5][0:len(pintura2[5])-1]
        pincelsacapuntas =  matriz[3].split(',')
        pincelsacapuntas[5] = pincelsacapuntas[5]\
                              [0:len(pincelsacapuntas[5])-1]
        cuadernos = matriz[4].split(',')
        cuadernos[5] = cuadernos[5][0:len(cuadernos[5])-1]
        hojaspegamento =  matriz[5].split(',')
        hojaspegamento[5] = matriz[5][0:len(hojaspegamento[5])-1]
        
        #Muestra las opciones del menú
        print ('Si desea agregar lapiz marque L')
        print ('Si desea agregar plumas marque P')
        print ('Si desea agregar pinturas marque PI')
        print ('Si desea agregar pinceles marque PC')
        print ('Si desea agregar sacapuntas marque S')
        print ('Si desea agregar cuadernos marque C')
        print ('Si desea agregar hojas marque H')
        print ('Si desea agregar pegamento marque PEG' + '\n')
        
        #Guarda el producto a agregar
        art = str(input('Ingrese el producto que quiera agregar: '))
        print('\n' + '========================================='
          + '===========================================' + '\n')
        
        #Dependiendo de la variable art añade la cantidad de producto al
        #inventario
        if art == 'L':
            tipo = str(input('Ingrese el tipo de lápiz a agregar: '
                             + '\n' + 'B para blando' + '\n' +
                             'M para medio' + '\n' + 'D para duro' + '\n'))
            if tipo != 'B' and tipo != 'M' and tipo != 'D':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                
                if cantidad > 0:
                    if 'B' == tipo:
                        lapizpluma[0] = int(lapizpluma[0]) + cantidad
                    elif 'M' == tipo:
                        lapizpluma[1] = int(lapizpluma[1]) + cantidad
                    elif 'D' == tipo:
                        lapizpluma[2] = int(lapizpluma[2]) + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                
        elif art == 'P':
            tipo = str(input('Ingrese el color de pluma a agregar: '
                             + '\n' + 'N para negro' + '\n' + 'A para azul'
                             + '\n' + 'R para rojo' + '\n'))
            if tipo != 'N' and tipo != 'A' and tipo != 'R':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                
                if cantidad > 0:
                    if 'N' == tipo:
                        lapizpluma[3] = int(lapizpluma[3]) + cantidad
                    elif 'A' == tipo:
                        lapizpluma[4] = int(lapizpluma[4]) + cantidad
                    elif 'R' == tipo:
                        lapizpluma[5] = int(lapizpluma[5]) + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                
        
        elif art == 'PI':
            tipo = str(input('Ingrese el color de la pintura: '
                             + '\n' + 'A azul' + '\n' + 'AM amarilla'
                             '\n' + 'RO roja' + '\n' + 'RS rosa' + '\n'
                             + 'N naranja' + '\n' + 'V verde' + '\n'
                             + 'M morada' +  '\n' + 'C café' + '\n' + 
                             'B blanca' + '\n' + 'D dorada' + '\n' + 
                             'P plateada' + '\n' + 'BR bronce' + '\n'))
            if (tipo != 'A' and tipo != 'AM' and tipo != 'RO' and
                tipo != 'RS' and tipo != 'N' and tipo != 'V' and
                tipo != 'M' and tipo != 'C' and tipo != 'B' and
                tipo != 'D' and tipo != 'P' and tipo != 'BR'):
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
            
                if cantidad > 0:
                    if 'A' == tipo:
                        pintura1[0] = int(pintura1[0]) + cantidad
                    elif 'AM' == tipo:
                        pintura1[1] = int(pintura1[2]) + cantidad
                    elif 'RO' == tipo:
                        pintura1[3] = int(pintura1[3]) + cantidad
                    elif 'RS' == tipo:
                        pintura1[4] = int(pintura1[4]) + cantidad
                    elif 'N' == tipo:
                        pintura1[5] = int(pintura1[5]) + cantidad
                    elif 'M' == tipo:
                        pintura2[0] = int(pintura2[0]) + cantidad
                    elif 'C' == tipo:
                        pintura2[1] = int(pintura2[1]) + cantidad
                    elif 'B' == tipo:
                        pintura2[2] = int(pintura2[2]) + cantidad
                    elif 'D' == tipo:
                        pintura2[3] = int(pintura2[3]) + cantidad
                    elif 'P' == tipo:
                        pintura2[4] = int(pintura2[4]) + cantidad
                    elif 'BR' == tipo:
                        pintura2[5] = int(pintura2[5]) + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                
                
        elif art == 'PC':
            tipo = str(input('Ingrese el tamaño:' + '\n' + 'C chico' + '\n'
                       + 'M mediano' + '\n' + 'G grande' + '\n'))
            if tipo != 'C' and tipo != 'M' and tipo != 'G':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                if cantidad > 0:
                    if 'C' == tipo:
                        pincelsacapuntas[0] = int(pincelsacapuntas[0])\
                                              + cantidad
                    elif 'M'  == tipo:
                        pincelsacapuntas[1] = int(pincelsacapuntas[1])\
                                              + cantidad
                    elif 'G' == tipo:
                        pincelsacapuntas[2] = int(pincelsacapuntas[2])\
                                              + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                
        elif art == 'S':
            tipo = str(input('Ingrese el tamaño:' + '\n' + 'C chico' + '\n'
                       + 'M mediano' + '\n' + 'G grande' + '\n'))
            if tipo != 'C' and tipo != 'M' and tipo != 'G':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                if cantidad > 0:
                    if 'C' == tipo:
                        pincelsacapuntas[3] = int(pincelsacapuntas[3])\
                                              + cantidad
                    elif 'M'  == tipo:
                        pincelsacapuntas[4] = int(pincelsacapuntas[4])\
                                              + cantidad
                    elif 'G' == tipo:
                        pincelsacapuntas[5] = int(pincelsacapuntas[5])\
                                              + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                
        elif art == 'C':
            tipo = str(input('Ingrese el tipo:' + '\n' + 'C cuadriculado'
                             + '\n' + 'L lineas' + '\n'))
            if tipo != 'C' and tipo != 'L':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                if 'C' == tipo:
                    tipo2 = str(input('Ingrese el tamaño:' + '\n' + 'C chico'
                                      +'\n' + 'M mediano' + '\n' + 'G grande'
                                      + '\n'))
                    if tipo2 != 'C' and tipo2 != 'M' and tipo2 != 'G':
                        print('\n' + '======================================'
                          + '=============================================='
                              + '\n')
                        print('Ingrese una opción valida')
                    else:
                        cantidad = int(input('Ingrese la cantidad a comprar '))
                        if cantidad > 0:
                            if 'C' == tipo2:
                                cuadernos[0] = int(cuadernos[0]) + cantidad
                            elif 'M'  == tipo2:
                                cuadernos[1] = int(cuadernos[1]) + cantidad
                            elif 'G' == tipo2:
                                cuadernos[2] = int(cuadernos[2]) + cantidad
                        else:
                            print('\n' + '================================='
          + '===================================================' + '\n')
                            print('Ingrese una cantidad mayor a 0')
                            
                elif 'L' == tipo:
                    tipo2 = str(input('Ingrese el tamaño:' + '\n' + 'C chico'
                                      + '\n' + 'M mediano' + '\n' + 'G grande'
                                      + '\n'))
                    if tipo2 != 'C' and tipo2 != 'M' and tipo2 != 'G':
                        print('\n' + '======================================'
                          + '=============================================='
                              + '\n')
                        print('Ingrese una opción valida')
                    else:
                        cantidad = int(input('Ingrese la cantidad a comprar '))
                        if cantidad > 0:
                            if 'C' == tipo2:
                                cuadernos[3] = int(cuadernos[3]) + cantidad
                            elif 'M'  == tipo2:
                                cuadernos[4] = int(cuadernos[4]) + cantidad
                            elif 'G' == tipo2:
                                cuadernos[5] = int(cuadernos[5]) + cantidad
                        else:
                            print('\n' + '==================================='
          + '=================================================' + '\n')
                            print('Ingrese una cantidad mayor a 0')
                            
        elif art == 'H':
            tipo = str(input('Ingresa el tamaño del paquete:' + '\n'
                             + 'I individual' + '\n' + '100' + '\n'
                             + '500' + '\n' + '1000' + '\n'))
            if (tipo != 'I' and tipo != '100' and tipo != '500'
                and tipo != '1000'):
                print('\n' + '========================================='
                  + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                if cantidad > 0:
                    if 'I' == tipo:
                        hojaspegamento[0] = int(hojaspegamento[0]) + cantidad
                    elif '100' == tipo:
                        hojaspegamento[1] = int(hojaspegamento[1]) + cantidad
                    elif '500' == tipo:
                        hojaspegamento[2] = int(hojaspegamento[2]) + cantidad
                    elif '1000' == tipo:
                        hojaspegamento[3] = int(hojaspegamento[3]) + cantidad
                else:
                    print('\n' + '========================================='
          + '===========================================' + '\n')
                    print('Ingrese una cantidad mayor a 0')
                    
        elif art == 'PEG':
            tipo = str(input('Ingresa el tipo:' + '\n' + 'B barra' + '\n'
                             + 'L liquido' + '\n'))
            if tipo != 'B' and tipo != 'L':
                print('\n' + '========================================='
                  + '===========================================' + '\n')
                print('Ingrese una opción valida')
            else:
                cantidad = int(input('Ingrese la cantidad a comprar '))
                if cantidad > 0:
                    if 'B' == tipo:
                        hojaspegamento[4] = int(hojaspegamento[4]) + cantidad
                    elif 'L' == tipo:
                        hojaspegamento[5] = int(hojaspegamento[5]) + cantidad
        
        #Convierte las variables a string para poder añadirlas al archivo de
        #texto
        lapizpluma[5] = str(lapizpluma[5]) + '\n'
        pintura1[5] = str(pintura1[5]) + '\n'
        pintura2[5] = str(pintura2[5]) + '\n'
        pincelsacapuntas[5] = str(pincelsacapuntas[5]) + '\n'
        cuadernos[5] = str(cuadernos[5]) + '\n'
        hojaspegamento[5] = str(hojaspegamento[5]) + '\n'
        #Se agregan a la lista para añadirlas al archivo de texto
        matriz_final = []
        matriz_final.append(lapizpluma)
        matriz_final.append(pintura1)
        matriz_final.append(pintura2)
        matriz_final.append(pincelsacapuntas)
        matriz_final.append(cuadernos)
        matriz_final.append(hojaspegamento)
        #Abre el archivo para poder escribir en el
        pruebainvent = open('invent.txt', 'w')
        numero = ''
        for i in range(6):
            for j in range(6):
                if j <5:
                    numero = numero + str(matriz_final[i][j])+','
                else:
                    numero = numero + str(matriz_final[i][j])
        pruebainvent.write(str(numero))
        pruebainvent.close()
        print('\n' + '========================================='
          + '===========================================' + '\n')
        #Define si continua el programa
        continuar = str(input('Si desea agregar otro producto marque "SI"'
                              + ', sino marque "NO" ' ))
        if continuar == 'SI':
            vendedor()
        else:
            print('\n' + '========================================='
          + '===========================================' + '\n')
            print('Gracias')
        #Retorna el valor de la matriz final
        return (matriz_final)
        
    #Si la persona es cliente, dar la bienvenida y llamar a la función cliente
    if persona == 'C':
        print('Bienvenido')
        print('\n' + '========================================='
          + '===========================================' + '\n')
        inventario_cliente = cliente()
        print('\n' + '========================================='
          + '===========================================' + '\n')
      
    #Si la persona es vendedor, pedir usuario y contraseña para ingresar
    #En caso de ser incorrectos desplegar mensaje de que algún dato es
    #incorrecto
    elif persona == 'V':
        usuario = str(input('Ingrese su usuario: '))
        contrasena = str(input('\n' + 'Ingrese su contraseña: '))
        print('\n' + '========================================='
          + '===========================================' + '\n')
        if usuario == 'abc123' and contrasena == '123abc':
            opcion = str(input('Seleccione agregar productos A o '
                               + 'ver órdenes V o consultar inventario C'
                               + ' o ver reporte R o eliminar reporte E: '))
            if opcion != 'A' and opcion != 'V' and opcion != 'C'\
               and opcion != 'R' and opcion != 'E':
                print('\n' + '========================================='
          + '===========================================' + '\n')
                print('Ingrese una opción valida')
                print('\n' + '========================================='
          + '===========================================' + '\n')
            else:
            #Llama a la función vendedor para agregar productos
                if opcion == 'A':
                    inventario_vendedor = vendedor()
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                
                #Despliega la última orden
                elif opcion == 'V':
                    ordenreciente = open('Data.txt', 'r')
                    x = ordenreciente.readlines()
                    ordenreciente.close()
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                    for i in range(len(x)):
                        print(x[i])
                elif opcion == 'C':
                    #Muestra el inventario
                    invent1 = open('invent.txt', 'r')
                    matriz  = invent1.readlines()
                    invent1.close()
                    
                    lapizpluma = matriz[0].split(',')
                    lapizpluma[5] = lapizpluma[5][0:len(lapizpluma[5])-1]
                    pintura1 =  matriz[1].split(',')
                    pintura1[5] = pintura1[5][0:len(pintura1[5])-1]
                    pintura2 = matriz[2].split(',')
                    pintura2[5] = pintura2[5][0:len(pintura2[5])-1]
                    pincelsacapuntas =  matriz[3].split(',')
                    pincelsacapuntas[5] = pincelsacapuntas[5]\
                                          [0:len(pincelsacapuntas[5])-1]
                    cuadernos = matriz[4].split(',')
                    cuadernos[5] = cuadernos[5][0:len(cuadernos[5])-1]
                    hojaspegamento =  matriz[5].split(',')
                    hojaspegamento[5] = matriz[5][0:len(hojaspegamento[5])-1]
                    
                    print('\n')
                    print('Lápiz blando ' + str(lapizpluma[0]))
                    print('Lápiz medio ' + str(lapizpluma[1]))
                    print('Lápiz duro ' + str(lapizpluma[2]))
                    print('Pluma negra ' + str(lapizpluma[3]))
                    print('Pluma azul ' + str(lapizpluma[4]))
                    print('Pluma roja ' + str(lapizpluma[5]))
                    print('Pintura azul ' + str(pintura1[0]))
                    print('Pintura amarilla ' + str(pintura1[1]))
                    print('Pintura roja ' + str(pintura1[2]))
                    print('Pintura rosa ' + str(pintura1[3]))
                    print('Pintura naranja ' + str(pintura1[4]))
                    print('Pintura verde ' + str(pintura1[5]))
                    print('Pintura morada ' + str(pintura2[0]))
                    print('Pintura café ' + str(pintura2[1]))
                    print('Pintura blanca ' + str(pintura2[2]))
                    print('Pintura dorada ' + str(pintura2[3]))
                    print('Pintura plateada ' + str(pintura2[4]))
                    print('Pintura bronce ' + str(pintura2[5]))
                    print('Pincel chico ' + str(pincelsacapuntas[0]))
                    print('Pincel mediano ' + str(pincelsacapuntas[1]))
                    print('Pincel grande ' + str(pincelsacapuntas[2]))
                    print('Sacapuntas chico ' + str(pincelsacapuntas[3]))
                    print('Sacapuntas mediano ' + str(pincelsacapuntas[4]))
                    print('Sacapuntas grande ' + str(pincelsacapuntas[5]))
                    print('Cuaderno cuadro chico ' + str(cuadernos[0]))
                    print('Cuaderno cuadro mediano ' + str(cuadernos[1]))
                    print('Cuaderno cuadro grande ' + str(cuadernos[2]))
                    print('Cuaderno línea chico ' + str(cuadernos[3]))
                    print('Cuaderno línea mediano ' + str(cuadernos[4]))
                    print('Cuaderno línea grande ' + str(cuadernos[5]))
                    print('Hoja individual ' + str(hojaspegamento[0]))
                    print('Paquete 100 hojas ' + str(hojaspegamento[1]))
                    print('Paquete 500 hojas ' + str(hojaspegamento[2]))
                    print('Paquete 1000 hojas ' + str(hojaspegamento[3]))
                    print('Pegamento en barra ' + str(hojaspegamento[4]))
                    print('Pegamento líquido ' + str(hojaspegamento[5]))
                    print('\n')
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                    
                elif opcion == 'R':
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                    reportef = open('Reporte.txt', 'r')
                    c = reportef.readlines()
                    reportef.close()
                    #Muestra el total de la compra
                    for i in range(len(c)):
                            print(c[i])
                    print('\n')
                    print('\n' + '========================================='
              + '===========================================' + '\n')
                
                elif opcion == 'E':
                    reporteb = open('Reporte.txt', 'w')
                    reporteb.write('')
                    reporteb.close()
                    print('\n' + '========================================='
              + '===========================================' + '\n')
        else:
            print('Usuario o contraseña incorrecta')
            print('\n' + '========================================='
          + '===========================================' + '\n')
    else:
        print('Ingrese una opción valida')
        print('\n' + '========================================='
          + '===========================================' + '\n')
#Llamar a la función 
while True:
    papeleria()
