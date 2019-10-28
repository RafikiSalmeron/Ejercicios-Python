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
p3.setEdad(15)
p3.setAltura(1.8)
p3.setSexo('H')
p3.setPeso(85)

#PESO IDEAL
print("")
if(p.calcularIMC()[0] == -1): print("p esta delgado, su IMC es " + str(p.calcularIMC()[1]))
if(p.calcularIMC()[0] == 0): print("p esta en su peso ideal, su IMC es " + str(p.calcularIMC()[1]))
if(p.calcularIMC()[0] == 1): print("p esta en sobrepeso, su IMC es " + str(p.calcularIMC()[1]))

if(p2.calcularIMC()[0] == -1): print("p2 esta delgado, su IMC es " + str(p2.calcularIMC()[1]))
if(p2.calcularIMC()[0] == 0): print("p2 esta en su peso ideal, su IMC es " + str(p2.calcularIMC()[1]))
if(p2.calcularIMC()[0] == 1): print("p2 esta en sobrepeso, su IMC es " + str(p2.calcularIMC()[1]))

if(p3.calcularIMC()[0] == -1): print("p3 esta delgado, su IMC es " + str(p3.calcularIMC()[1]))
if(p3.calcularIMC()[0] == 0): print("p3 esta en su peso ideal, su IMC es " + str(p3.calcularIMC()[1]))
if(p3.calcularIMC()[0] == 1): print("p3 esta en sobrepeso, su IMC es " + str(p3.calcularIMC()[1]))


##EDAD
print("")
if(p.edad >= 18):
    print("p es mayor de edad.")
else:
    print("p es menor de edad.")

if(p2.edad >= 18):
    print("p2 es mayor de edad.")
else:
    print("p2 es menor de edad.")

if(p3.edad >= 18):
    print("p3 es mayor de edad.")
else:
    print("p3 es menor de edad.")


#Toda la Información
print(p.toString())
print(p2.toString())
print(p3.toString())
