from sklearn import tree

import os

#Definimos la función estableciendo el nombre limpiarPantalla, no recibe parámetros
def limpiarPantalla(): 
	if os.name == "posix":
	   os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
	   os.system ("cls")

#Se crea la instancia del árbol de decisión.
clf = tree.DecisionTreeClassifier()

#[altura, peso, talla de zapato]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
#La salida donde se dice si es hombre o mujer
Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',
     'mujer', 'hombre', 'hombre']

#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)

#Se limpia la pantalla
limpiarPantalla()

#Se presenta el programa
print("******************************************************************************************************************************************")
print("* Programa que hace uso de IA para determinar el sexo de una persona según las características de Altura, Peso y Talla de calzado")
print("******************************************************************************************************************************************")

#Se captura la altura por consola
altura = int(input("Ingrese su Altura: "))

#Se captura el peso por consola
peso = int(input("Ingrese su Peso: "))

#Se captura la talla de calzado por consola
calzado = int(input("Ingrese su Talla de calzado: "))

#Se ingresan en el arreglo los datos capturados en el orden establecido (altura, peso y calzado)
datos = [altura,peso,calzado]

#Se envía el arreglo al objeto clf en su método predict donde se conmnutan los datos ingresados 
prediction = clf.predict([datos])

#Se muestra el resultado de la predicción de los datos ingresados
print('Según los datos ingresados el sexo es: ', prediction)

