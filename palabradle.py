import csv
from operator import truediv
import random
import math

palabras = []
frecuencias = []

with open('listaDePalabras.csv', mode = 'r', encoding = 'utf-8') as archivo:

    csvReader = csv.reader(archivo)

    for linea in csvReader:
        palabras.append(linea[0])
        frecuencias.append(linea[1])

dificultad = int(input("¡Bienvenidos a PALABRADLE! Escoga un dificultad para empezar: 1 (más facil), 2, 3 (más difícil) \n"))
palabraSeleccionada = palabras[math.floor(random.random() * len(palabras)/(4-dificultad))]

jugarMas = True
while jugarMas:
    terminado = False
    numSuposiciones = 0
    while terminado == False:
        suposicion = input("Adivine una palabra de cinco letras:\n").lower()
        frecuenciasEnPalabra = {}

        if len(suposicion) != 5:
            print("Este no tiene cinco letras! Intente de nuevo.\n")
            continue

        else:
            salida = ""
            for i in range(len(suposicion)):
                frecuenciasEnPalabra.update({suposicion[i] : palabraSeleccionada.count(suposicion[i])})
            
            for i in range(len(suposicion)):
                if suposicion[i] == palabraSeleccionada[i]:
                    frecuenciasEnPalabra.update({suposicion[i] : frecuenciasEnPalabra.get(suposicion[i]) - 1})
                    salida += "✓"
                elif suposicion[i] in palabraSeleccionada:
                    frecuenciasEnPalabra.update({suposicion[i] : frecuenciasEnPalabra.get(suposicion[i]) - 1})
                    if frecuenciasEnPalabra.get(suposicion[i]) >= 0:
                        salida += "o"
                    else: 
                        salida += "x"
                else:
                    salida += "x"
        numSuposiciones += 1

        if salida == "✓✓✓✓✓":
            print("Felicidades! Toma " + str(numSuposiciones) + " suposiciónes.")
            terminado = True
        elif numSuposiciones >= 6:
            print("Usted ha agotado sus suposiciones. La palabra es: " + palabraSeleccionada)
            terminado = True
        
        print(salida)
    jugarMas = True if input("Jugar más? (Y/N) \n") == "Y" else False
    
    
