
import random

class Persona:
    def __init__(self,nombre="", edad=0, sexo='M', peso=0, altura=0):
        self.nombre = nombre
        self.edad = int (edad)
        self.sexo =self.__introducirsexo(sexo)
        self.peso = peso
        self.altura  = altura
        self.dni = self.generaDNI()


    def calcularIMC(self):
        if (self.peso == 0): return -2, "No ha sido posible calcular el IMC"
        imc = (float(self.peso)/(float(self.altura)**2))
        if (imc<18.5):
            return -1, imc
        if (imc >= 18.5) and (imc <25):
            return 0, imc
        elif (imc > 25):
            return 1, imc

    def esMayorDeEdad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
    def __introducirsexo(self, sexo):
        if(sexo[0] == 'H') or (sexo[0] == 'h'):
            return 'H'
        else:
            return 'M'

    def toString(self):
        return "Nombre : " + self.nombre + ", Peso : " + str(self.peso) +", Sexo : " + self.sexo + ", Edad: " + str(self.edad) + ", Altura : " + str(self.altura) + "DNI : " + self.dni

    def generaDNI(self):
        dni = random.randint(00000000,99999999)
        letras = "TRWAGMYFPDXBNJZSQVHLCKEO"
        valor = int(dni / 23)
        valor *= 23
        valor = dni - valor;
        dnicompleto = str(dni) + letras[valor]
        return dnicompleto

    def setNombre(self,nombre):
        self.nombre = nombre
    def setAltura(self,altura):
        self.altura = altura
    def setPeso(self,peso):
        self.peso = peso
    def setEdad(self,edad):
        self.edad = edad
    def setSexo(self,sexo):
        self.sexo = sexo