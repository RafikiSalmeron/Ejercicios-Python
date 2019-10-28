from Persona import Persona

#CREACION DE OBJETOS
nombre = input("Introduce un nombre  ")
altura = input("Introduce la altura  ")
peso = input("Introduce el peso  ")
edad = input("Introduce la edad  ")
sexo = input("Introduce el sexo  ")
p = Persona(nombre,edad,sexo,peso,altura)
p2 = Persona(nombre,edad,sexo)
p3 = Persona()

p3.setNombre("Rafa")
p3.setEdad(18)
p3.setAltura(1.8)
p3.setSexo('H')
p3.setPeso(85)

#PESO IDEAL

if(p.calcularIMC()[0] == -1): print("p esta delgado, su IMC es " + str(p.calcularIMC()[1]))
if(p.calcularIMC()[0] == 0): print("p esta en su peso ideal, su IMC es " + str(p.calcularIMC()[1]))
if(p.calcularIMC()[0] == 1): print("p esta en sobrepeso, su IMC es " + str(p.calcularIMC()[1]))

if(p2.calcularIMC()[0] == -1): print("p esta delgado, su IMC es " + str(p2.calcularIMC()[1]))
if(p2.calcularIMC()[0] == 0): print("p esta en su peso ideal, su IMC es " + str(p2.calcularIMC()[1]))
if(p2.calcularIMC()[0] == 1): print("p esta en sobrepeso, su IMC es " + str(p2.calcularIMC()[1]))

if(p3.calcularIMC()[0] == -1): print("p esta delgado, su IMC es " + str(p3.calcularIMC()[1]))
if(p3.calcularIMC()[0] == 0): print("p esta en su peso ideal, su IMC es " + str(p3.calcularIMC()[1]))
if(p3.calcularIMC()[0] == 1): print("p esta en sobrepeso, su IMC es " + str(p3.calcularIMC()[1]))


