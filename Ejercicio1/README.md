1) Haz una clase llamada Persona que siga las siguientes condiciones:

    Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el mÃ¡s adecuado, tambiÃ©n su tipo. Si quieres aÃ±adir algÃºn atributo puedes hacerlo.
    Por defecto, todos los atributos menos el DNI serÃ¡n valores por defecto segÃºn su tipo (0 nÃºmeros, cadena vacÃ­a para String, etc.). Sexo sera mujer por defecto.
    Se implantaran varios constructores:
        Un constructor con todos los atributos como parÃ¡metro.
    Los mÃ©todos que se implementaran son:
        calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2  en m)), devuelve un -1 si esta por debajo de su peso ideal, un 0 si esta en su peso ideal y un 1 si tiene sobrepeso . TambiÃ©n devuelve el IMC.
        esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
        introducirSexo(char sexo):  introducido el sexo. Si no es correcto, sera M. No sera visible al exterior.
        toString(): devuelve toda la informaciÃ³n del objeto.
        generaDNI(): genera un numero aleatorio de 8 cifras, genera a partir de este su nÃºmero su letra correspondiente. Este mÃ©todo sera invocado cuando se construya el objeto. 
        MÃ©todos set de cada parÃ¡metro, excepto de DNI. 

Ahora, crea una clase ejecutable que haga lo siguiente:

    Pide por teclado el nombre, la edad, sexo, peso y altura.
    Crea 3 objetos de la clase anterior, el primer objeto obtendrÃ¡ las anteriores variables pedidas por teclado, el segundo objeto obtendrÃ¡ todos los anteriores menos el peso y la altura y el Ãºltimo por defecto, para este Ãºltimo utiliza los mÃ©todos set para darle a los atributos un valor.
    Para cada objeto, deberÃ¡ comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
    Indicar para cada objeto si es mayor de edad.
    Por Ãºltimo, mostrar la informaciÃ³n de cada objeto.
