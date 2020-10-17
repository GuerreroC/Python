""" Python

    Python es usado para desarrollo web (Back-End), Machine learning, Big Data, Data Science, seguridad informatica y VideoJuegos.
    Paradigmas de programacion=[
        Programacion Estructurada,
        Programacion Orientado a Objetos,
        Programacion Funcional,
        Programacion Reactiva: Observar cambion en flujos de datos
    ]
    Imperativos: Es aquella que dice que se debe hacer explicando paso por paso
    Declarativos: Es aquella que le pides una funcion y el sistema lo hace 

    Para ejecutar un archivo python en cmd, se necesita citar la ubicacion del archivo usando "cd" + la direccion
    despues  ingresar "python" + nombreArchivo.py 
    """
#1---------------------------------Sintaxis Basica-------------------------------
"""
    Operadores de Comparacion
    ==, >, <, >=, <=,

    Operadores de Asignacion
    =, +=, -=, *=, /=, %=, **=, //=

    Operadores Especiales
    IS, IN, IS NOT, NOT IN

    Variables
    Las variables son determinadas por su contenido sin necesidad de declararlas como en otros lenguajes
    int, float, Boolean or string

    type() define el tipo de variable por su clase

    #print("Hola mundo"); print ("Adios") #Con ; se utiliza para separar los comandos.
        
    print("Escribe tu nombre:", end=" ")
    Nombre=input()
    Largo=len(Nombre)
    print(f"Tu nombre es: {Nombre}, y tiene {Largo} caracteres.")
    print("Tu nombre es: {}, y tiene {} caracteres.".format(Nombre, Largo))
    
    
    import sys
    print ('Escribe: python Intro.py "Hola, Mundo!" 5')
    comando = sys.argv
    #print(comando)
    if comando != ['Intro.py']:
        texto = sys.argv[1]
        repeticion= int(sys.argv[2])
        for i in range (repeticion):
            print (texto)
            
    a = None
    print(type(a))

    http://pyspanishdoc.sourceforge.net/
    """
#2--------------------------Listas, tuplas y Diccionarios------------------------
"""
    #LISTAS
    miLista=["hola", 24, 3.33, False]       #A diferencia del array aqui se pueden agregar cualqier constantes de cualquier valor #Se empieza a contar del 0  
    print (miLista[1])

    miLista.append("Carlos")        #Se agrega al ultimo de la lista
    print(miLista[:])

    miLista.insert(2,"CUU")         #Se agrega en el lugar que quieras
    print(miLista[:])

    miLista.extend(["extension", "de una lista"])       #se agrega una extension
    print(miLista[:])
    print(miLista.index("Carlos"))      #Pocision del elemento
    print("hola" in miLista)                #Saber si esta en la lista
    miLista.remove("de una lista")
    miLista.pop()
    print(miLista[:])

    #TUPLAS
    #Las tuplas no son modificables
    miTupla=("Carlos", 1, 5.5, True)            #la tupla lleva parentesis
    milista=list(miTupla)
    print(milista)
    milista=tuple(milista)
    print(miTupla)
    
    #CONJUNTOS
    #Son listas de elementos desordenados y no pueden haber dos elementos duplicados
    conjunto = set()
    Conjunto = {0,1,3,4,5}
    Conjunto.add(2)
    print (Conjunto)
    
    grupo = {'Carlos', 'Mariana', 'Pakish'}
    duda1 = 'Molcas' in grupo
    duda2 = 'Carlos' not in grupo
    print (duda1, duda2)
     
    lista = [1,2,3,3,2,1]
    print (lista)
    lista = set(lista)
    print (lista)

    #DICCIONARIO
    #Son conjuntos es un confunto de elementos con valores unicos y se basan del mappin
    #En otros lenguajes se conocen como arreglos asociativos
    midiccionario={"Dato1":"Info1","Dato2":"Info2", "Dato3":"Info3", "Dato4":"Info4"}
    print(midiccionario["Dato3"])
    print(midiccionario)            #Imprimir todo el diccionario
    midiccionario["Dato5"]="Info5"  #Añadir datos nuevos
    del midiccionario["Dato4"]      #Borra algun dato
    print(midiccionario)

    print("Escribe tu nombre:", end=" ")
    valor=input()
    print(f"Tu nombre tiene {len(valor)} caracteres")
    """
#3----------------------------Condicionales y Funciones--------------------------
"""
    #print ("Eres mayor") if int(input("Edad: ")) >=18 else print ("eres menor")

    print("Programa de evaluacion")
    print("ingrese la calificacion del alumno")
    nota_Alumno = input()

    def Evaluacion(Nota):           #El return de varios tipos te genera una tupla
        Valoracion ="Aprobado"
        if Nota<=5:
            Valoracion = "Reprobado"
        if Nota>10:
                Valoracion = "Valor incorrecto, ingreselo nuevamente"
        return Valoracion
            
    print(Evaluacion(int(nota_Alumno)))

    print("ingrese una palabra")
    dato = input()    
    print("su palabra tiene " + str(int(len(dato))) + " caracteres")
    
    #FUNCION RECURSIVA
    def factor(num):
        if num > 1:
            num = num * factor(num -1)
        return num
        
    print(factor(5))

    """
#4--------------------------------Bucle While & For------------------------------
"""
    for i in ["uno", "dos", "tres", "cuatro"]: 
        print(i, end = " ") #end hace que selecciones el metodo de separacion de los elemen
    print()

    for i in "num":
        print("hola")
        
    Palabra= [1,2,3]
    Dias= ["Lunes", "martes", "Miercoles", "Jueves", "Viernes"]
    for i in Dias:
        if i == "Lunes":
            print("Es hoy!")
        else:
            print(i)

    from time import sleep
    import sys

    for i in range(1,5):
        print(f"valor de la variable {i}") #la "f" significa format, concatena text con el valor de una variable
        sleep(1)
  
    """
#5-----------------------------------Generadores---------------------------------
"""
    def GeneraPares(limite):
        num = 1
        #miLista=[]
        
        while num<limite:
            #miLista.append(num*2)
            yield num*2
            num+=1
        #return miLista 
    #print(GeneraPares(11))
    devuelveP=GeneraPares(11)


    for i in devuelveP:
        print(i)
       

    def devuelve_ciudades(*ciudades):     # el * significa que recibira un numero inderterminado de elementos
            for elemento in ciudades:
                #for subElemento in elemento:
                    yield from elemento

    ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "CDMX", "Chihuahua")

    print(next(ciudades_devueltas))
    print(next(ciudades_devueltas))
    """
#6-----------------------------------Excepciones---------------------------------
"""
    La excepciones se usan cuando vas a personalizar una falla

    def suma (num1, num2):
            return num1 + num2
    def resta (num1, num2):
            return num1 - num2
    def multiplica(num1, num2):
            return num1 * num2
    def divide(num1, num2):
            while True:
                try:                                                         #try empleado para evitar que todo el codigo falle y salte este paso usando except
                    return num1 / num2
                    break
                except ZeroDivisionError:
                    print("no se puede dividir entre cero")
                    return Calcular() #"operacion invalida. intenta nuevamente"   
    def Calcular():
        while True:
            #op1 = (int(input("introduce el primer numero: ")))
            #op2 = (int(input("introduce el segundo numero: ")))
            while True:
                try:                                #try empleado para evitar que todo el codigo falle y salte este paso usando except
                    op1 = (int(input("introduce el primer numero: ")))
                    break
                except ValueError:
                    print("No escribiste un numero, intenta de nuevo.")
                    Calcular() 
            while True:
                try:                                                         
                    op2 = (int(input("introduce el segundo numero: ")))
                    break
                except ValueError:      #Se usa la funcion finally
                    print("No escribiste un numero, intenta de nuevo.")
                    Calcular() 
            
            operacion=input("introduce la operacion a realizar (suma, resta, multiplica o divide): ")

            if operacion == "suma":
                print(suma(op1, op2))

            elif operacion == "resta":
                print(resta(op1, op2))

            elif operacion == "multiplica":
                print(multiplica(op1, op2))

            elif operacion == "divide":
                resultado=divide(op1, op2)
                if resultado is not None:             #None es un objeto por el cual la comparativa es IS o IS NOT
                    print (resultado)
                    
            else:
                    print ("operacion invalida") 
            break    
    Calcular()

    #Segundo ejemplo
    import math

    def calculaRaiz(num1):
        if num1<0:
            raise ValueError("El numero no puede ser negativo")         #Excepcion para endicarte el tipo de falla y ponertela en el error
        else:
            return math.sqrt(num1)

    op1=(int(input("introduce un numero: ")))
    try: 
        print(calculaRaiz(op1))
    except ValueError as ErrorDeNumNegativo:                            #"as" puedes denominar tu __tipo de error
        print(ErrorDeNumNegativo)
    """
#7--------------------------------------POO--------------------------------------
"""
    CLASE: modelo donde se redactan las caracteristicas comunes de una grupo de objetos
    INSTANCIA, EJEMPLAR, OBJETO: Ejemplar permaneciente a una clase, tiene atributos y comportamientos o Metodos (Crear un objeto desde una clase)
    MODULARIZACION: separa programas en modulos o clases para facilitar su codigo.

    ABSTRACCION: Definicion de las caracteristicas especificas (metodos y atributos)que distinguen de los demas tipos de objetos.
    ENCAPSULACION: un clase no sabra del funcionamiento de otra.
    
    

    METODOS de ACCESO: conectar clases con otras, acceso a solo unas caracteristicas

    class Carro():
        __autonomia= 8          #Atributo encapsulado
        
        def __init__(self):                          #Constructor de Clase 
            #Propiedades de la clase or Attribute
            self.largoChasis = 400                 
            self.anchoChasis = 200
            self.tipo= "Sedan"                         #__ Encapsula una propiedad para que no lo cambie por fuera PERO debes encapsular el metodo
            self.enMarcha=False
            
        #Comportamientos de la clase
        def arrancar(self, arrancamos):             #SELF: objeto perteneciente a la clase
            self.enMarcha=arrancamos
            if (self.enMarcha==True):
                chequeo= self.chequeo_interno()
            if (self.enMarcha and chequeo):
                #loadingBar()                                             #linea 88 to 92
                print("Chequeo finalizado")
                print("El Carro esta en marcha")
            elif(self.enMarcha == True and chequeo == False):
                print("Comprobar Gasolina, Aceite y Puertas") 
            else:
                print("El Carro esta parado")
            
            self.enMarcha=True

        def estado(self):                 #Encapsula un metodo
            print(f"Propiedades de la clase: {self.largoChasis}, {self.anchoChasis}, {self.tipo} y autonomia de {self.__autonomia} km/l") 
            #la autonomia se ve a mostrar debido a que el metodo no esta encapsulado
                    
        def chequeo_interno(self):
            print("Realizando Chequeo interno antes de arrancar")
            self.gasolina="OK"
            self.aceite="OK"
            self.puertas= "CLOSE"
            
            if(self.gasolina== "OK" and self.aceite== "OK" and self.puertas== "CLOSE"):
                return True
              
            else:
                return False

    miCarro=Carro()                  #Instanciar una clase (crear un objeto)
    miCarro.arrancar(True)

    try:
        print(miCarro.__autonomia)
    except:
        print("La autonomia del carro no esta disponible debido al encapsulamiento.")

    miCarro.estado()
      
    #Segundo Objeto
    #miCarro2=Carro()
    #miCarro2.arrancar(True)
    
    #DESTRUCTOR
    def __del__(self):
        
    #Metodo STRING      #Esto aplica cuando: str(objeto)
    def __str__(self):
        return "En vez de que te aparezca la ubicacion del archivo en la memoria te aparece éste string :)"
        
    #Metodo LEN         #Esto aplica cuando: len(objeto)
    def __len__ (self):
        return 
            
    #EJEMPLO_2
    class carro:
        def __init__(self):
            self.__Arquitectura = "FNV2"
            self.modelo = 2020
        
        def __mostrarArquitectura(self):
            print(f"la aquitectura usada en el vehiculo es: {self.__Arquitectura}")
            
        def mostrarModelo(self):
            print (f"El modelo es: {self.modelo}")
            
    Leon = carro()
    Leon.mostrarModelo()
    try:
        Leon.__mostrarArquitectura()
        
    except:
        print("El metodo/atributo que buscas esta encapsulado")
        
    #ISINSTANCE
    class algo():
        pass
        def __str__(self):
            return "algo"
        
    objeto= algo()

    if isinstance(objeto, algo):
        print("El objeto si es de la clase seleccionada")

    """
#8----------------------------------POO HERENCIA---------------------------------
"""
    HERENCIA: una Clase hereda funcionalidades y atributos a subClases con nuevas modalidades. (SuperClase y subclase)
    
    class Vehicle():
        def __init__ (self, marca, modelo):
            self.marca=marca
            self.modelo=modelo
            self.enmarcha=False
            self.acelera=False
            self.frena=False
            
        def arrancar(self):
            self.enmarcha=True
            print ("Tu carro esta encendido")
        
        def acelerar(self):
            self.acelera=True
        
        def frenar(self):
            self.frena=False
            
        def estado(self):
            print ("marca: ", self.marca, "\nModelo: ", self.modelo)

    class Carro(Vehicle):     #Heredacion de clase, Se pueden agregar mas Superclases, Se le da prioridad al primer superclase que metas
        #pass           # No genera ninguna accion y pasa al sig linea
           
        def Motor(self,motor):
            self.motor=motor
                    
        def estado(self):
            print ("marca: ", self.marca, "\nModelo: ", self.modelo, "\nMotor: ", self.motor)
            
        def __str__(self):
            return "Este vehiculo es un Carro a gasolina"
     
    class Electrico(Vehicle):
        def Autonomia(self, autonomia):
            self.autonomia=autonomia
            print ("Tu vehiculo electrico tiene una autonomia de:",self.autonomia, "Km")
            
        def __str__(self):
            return "Este vehiculo es un vehiculo electrico"
            
    Input_Marca=input("Ingresa una Marca: ")
    Input_Modelo=input("Ingresa un Modelo: ")

    miCarro=Carro(Input_Marca, Input_Modelo)
    miCarro.Motor(float(input("Ingresa el tipo de motor: ")))
    miCarro.estado()
    miCarro.arrancar()
    miEV=Electrico("Ford", "Mustang E")
    miEV.Autonomia(int(input("Ingresa la autonomia de tu vehiculo en Km: ")))

    print(miCarro)
    print(miEV)
    
    #Ejemplo_2  HERENCIA_MULTIPLE
    class Persona():
        def __init__(self, nombre, edad, lugarResidencia):
            self.nombre=nombre
            self.edad=edad
            self.lugarResidencia= lugarResidencia
        def descripcion(self):
            print("Nombre: ", self.nombre, " Edad, ",self.edad, " Residencia: ", self.lugarResidencia)
            
    class Empleado(Persona):
        def __init__(self, salario, antiguedad):
            super().__init__("Antonio", 28, "CDMX")      #llama al metodo de la superclase Persona
            self.salario=salario
            self.antiguedad=antiguedad
        def descripcion(self):
            super().descripcion()
            print("El sueldo de",self.nombre, "es de :", self.salario)
                    
    class Minion():
        def Minion(self):
            print("Solo hago lo que me dice mi jefe")
            
    class Lider(Empleado,Minion):
        def Lider(self):
            print("Persona lider del equipo")

    Antonio=Empleado(22000, 2)
    Antonio.descripcion()
    print(isinstance(Antonio, Persona))

    Carlos=Lider(50000, 3)
    print(Carlos.edad)          #Super Herencia
    print(Carlos.salario)       #2da Herencia
    print(Carlos.Lider())       #3ra Herencia
    print(Carlos.Minion())      #4ta Herencia
    
    
    """
#9--------------------------------POO POLIMORFISMO-------------------------------
"""
    #POLIMORFISMO: Poder darle la misma Orden a diferentes objetos y que cada uno de ellos responda de la misma manera.
    
    Input=int(input("Selecciona un numero: "))
    class Coche():
        def desplazamiento(self):
            print("Me desplazo en cuatro ruedas")
            
    class Moto():
        def desplazamiento(self):
            print("Me desplazo en dos ruedas")

    class Camion():
        def desplazamiento(self):
            print("Me desplazo en seis ruedas")
            

    #Moto=Moto()
    #Moto.desplazamiento()
    #Carro=Coche()
    #Carro.desplazamiento()        
    #Trailer=Camion()
    #Trailer.desplazamiento()
         

    def desplazamientoVehiculo(vehiculo):
        vehiculo.desplazamiento()
    if Input==1:
        miVehiculo=Coche()
        desplazamientoVehiculo(miVehiculo) 

    if Input==2:
        miVehiculo=Moto()
        desplazamientoVehiculo(miVehiculo) 

    if Input==3:
        miVehiculo=Camion()
        desplazamientoVehiculo(miVehiculo)    
    """
#10------------------------------Metodos de cadenas------------------------------
"""
    #tambien llamado: Metodos de colecciones
    
    upper()             convierte en mayusculas todas las letrs del string
    lower()             convierte en minusculas todas las letras del string
    capitalize()        pone la primera letra en mayuscula  
    count()             contas cuantas veces aparece una letra o cadena en un string
    find()              representa la posicion de un caracter
    isdigit()           es valor num?
    isalnum()           es alphanumericos?    
    isalpha()           es solo letras (sin espacios)?
    split()             separa palabras con un espacio
    strip()             borra los espacion sobrantes al inicio y al final
    replace()           cambia una palabra o letra por otra
    rfind()             lo mismo que find() pero contando desde el ultimo caracter
    http://pyspanishdoc.sourceforge.net/lib/string-methods.html

    nombre=input("introduce tu nombre: ")

    #print(nombre.upper())
    print(nombre.lower())
    #print(nombre.isalnum())
    print(nombre.strip())
    """
#11-----------------------------------Modulos------------------------------------
"""
    #Opcion1
    import FuncionesMatematicas
    FuncionesMatematicas.suma(5,5)
    FuncionesMatematicas.multiplica(5,5)


    #Opcion2
    from FuncionesMatematicas import suma
    suma(10,15)


    #Opcion3
    from FuncionesMatematicas import *
    suma(5,5)
    resta(25,15)
    multiplica(5,2)
    """
#12-----------------------------------Paquetes-----------------------------------
"""
    #El archivo __init__.py hace que la carpeta funcione como paquete. No puede estan en la misma carpeta raiz.

    from Paquete1.FuncionesMatematicas import *
    suma(5,5)

    from Paquete1.Prints.Prints import Error
    Error()

    #IMPORTANTE: Distribucion de paquetes VIDEO 36
    """
#13-------------------------------Archivos Externos------------------------------
""" 
    #Conocidos tambien como FICHEROS
    Ver videos 37-40
    #https://docs.python.org/3/
    from io import open

    Datos=open("DatosPython.txt", "w", encoding="utf-8")
    Datos.write("Primer dato del archivo Intro \n")
    Datos.write("First test result is Fail \n")
    Datos.close()

    Read=open("DatosPython.txt", "r+")              #r+ es lectura y escritura
    #Read.seek(0)                 #Mover el cursor al caracter seleccionado
    Lectura=Read.read()

    End=len(Lectura)
    #Lista=Read.readlines()    #Convierte el texto del archivo en una lista
    #print(Lista[1])
    #Read.seek(End)
    Read.seek(32)
    Read.write("The result of second test is PASS\n")
    print(Lectura)
    Read.close()

    Leer=open("DatosPython.txt", "r") 
    print(Leer.read())
    Leer.close() 

    #Añadir=open("DatosPython.txt", "a")
    #Añadir.write("The result of second test was PASS")
    #Añadir.close()
    """
#14------------------------------Interfaces graficas-----------------------------
"""

    #Ver Archivo Primera_interface

   """
#15---------------------------------Funcion Lambda-------------------------------
"""
    Son funciones anonimas para hacer mas rapido un calculo sin tantas lineas de codigo, no aplica con condicionales y bucles
    #Opcion1
    def areaTriangulo(base, altura):
        return (base*altura)/2
        
    print(areaTriangulo(10,10))

    #Opcion Lambda
    areaTriangulo=lambda base,altura: (base*altura)/2; print(areaTriangulo(10,10))
    cubo=lambda numero:pow(numero, 3); print(cubo(2))
    """
#16---------------------------------Funcion Filter-------------------------------
"""
    Son funciones de orden superior usando un paradigma de programacion llamado programacion funcional 
    Verifica que los elementos de una secuencia cumplen una condicion, devolviendo un iterador con los elementos que cumplen con dicha condicion.
    Se usa para filtrar OBJETOS

    #Ejemplo con listas
    numeroPar=lambda numeroPar: numeroPar%2==0        
    numeros=[17,24,7,39,8,51,92]
    print(list(filter(numeroPar, numeros)))

    #Ejemplo con Objetos
    class Empleado():
        def __init__(self, nombre, cargo, salario):
            self.nombre=nombre
            self.cargo=cargo
            self.salario=salario
            
        def __str__(self):
            return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
            
    listaEmpleados=[
    Empleado("Carlos", "CEO", 85000),
    Empleado("Mariana", "CFO", 80000),
    Empleado("Seño", "HRM", 55000)
    ]

    listaDirectivos=filter(lambda empleado: empleado.salario>75000, listaEmpleados)

    for empleadoSalario in listaDirectivos:
        print(empleadoSalario)
    """
#17-----------------------------------Funcion Map--------------------------------
"""
    #Map aplica una funciona a cada elemento de una lista iterable.

    class Empleado():
        def __init__(self, nombre, cargo, salario):
            self.nombre=nombre
            self.cargo=cargo
            self.salario=salario
            
        def __str__(self):
            return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
            
    listaEmpleados=[
    Empleado("Carlos", "CEO", 120000),
    Empleado("Mariana", "CFO", 8000),
    Empleado("Seño", "HRM", 55000)
    ]

    def calculoComision(empleado):
        if (empleado.salario>=100000):
            empleado.salario=empleado.salario*1.03
            return empleado

    ComisionEmpleados=map(calculoComision, listaEmpleados)

    for empleado in ComisionEmpleados:
        print(empleado)
    """
#18-----------------------------Expresiones Anidadas-----------------------------
"""
    Expresiones anidadas
    1-Resolver lo que esta dentro de parentesis: (x+y)
    2-Expresiones aritmeticas: x*y+z
    3-Expresiones Relacionales: <=
    4-Espresiones logicas: and

    num1=10
    num2=5
    print(num1 * num2 - num2**2 == 20 and (num1 + num2) == 15) 
    #Primero: num1 * num2 - num2**2 == 20 and (15) == 15
    #Segundo: 25 == 20 and (15) == 15
    #Tercero: False and True
    #Cuarto: False
    """
#19-----------------------------Expresiones Regulares----------------------------
"""
    #Son secuencias de caracteres que forman un patron de busqueda

    #https://platzi.com/contributions/entendiendo-las-expresiones-regulares-con-python/

    import re  #regex

    cadena="Vamos a poner en practica las expresiones regulares"

    Found=re.search("practica", cadena)
    Start=Found.start()
    End=Found.end()-1
    print(f"La palabra fue encontrada en el string desde el caracter {Start} hasta el {End}")

    #re.findall
    Correos=["Carlos@gmail.com",
    "Carlos@ford.com",
    "Carlos@outlook.com",
    "Carlos@hotmail.com"
    ]

    for elemento in Correos:
        if re.findall('@ford.com', elemento):
            print(elemento)

    #Rango
    for i in Correos:
        if re.findall('[t-z]', i): 
            print(i)

    #Match, esta funcion busca al inicio de la busqueda
    Correo= "carlos@ford.com"
    if re.match("Carlos", Correo, re.IGNORECASE):
        print("Encontramos el correo del Carlos")
        
    Username= "7CR"
    if re.match("\d", Username):
        print("Tu nombre de usuario no puede empezar con un numero.")
        
    print('{:04d}'.format(10))      #En medio del : y del 4d va el caracter que desees
    print('{:04d}'.format(100))
    print('{:04d}'.format(1000))
    print('\n')
    print('{:7.3f}'.format(3.141592654))    #7 digitos incluyendo el . + .3 la cantidad de decimales
    print('{:7.3f}'.format(123.45))
    
    *args = lista
    **kwargs = Diccionarios
    
        
    """
#20----------------------------------Decoradores---------------------------------
"""
    #Funciones que añaden funcionalidades a otras funciones

    def Decorador(Parametro):
        def Interior(*args, **kwargs):    #*args admite n cantidad de parametros/argumentos
            #Acciones adicionales que se agregan
            print("Vamos a realizar un calculo: ")
            Parametro(*args, **kwargs)
            #Acciones adicionales que se agregan
            print("Hemos terminado el calculo")
        return Interior
    @Decorador
    def suma(num1,num2): #Con esto la funcion "Parametro" del decorador sera la funcion "suma"
        print(num1+num2)

    @Decorador
    def resta(num1,num2):
        print(num1-num2)

    @Decorador    
    def potencia(base, exponente):
        print(pow(base, exponente))
        
    suma(10,5)
    resta(15,5) 
    potencia(base=5, exponente=3)
    """
#21----------------------------------Documentacion-------------------------------
'''
    def Print():
        """Esta funcion imprime un Hola, Mundo!"""
        print("Hola, Mundo!")
        
    print(Print.__doc__) #Solo aplica para las triple comillas
    Print()
    #help(Print)

    #Testing
    def Suma(num1, num2):
        """ 
        Calcula la suma de dos numeros
        >>> Suma(10, 5)
        15
        """
        return num1+num2
        
    #Testing high level
    import math

    def raizCuadrada(ListaNumeros):
        """
        >>> lista=[]
        >>> for i in [4, 9, 16]:
        ...     lista.append(i)
        >>> raizCuadrada(lista)
        [2.0, 3.0, 5.0]
        """
        return [math.sqrt(n) for n in ListaNumeros]
    #print(raizCuadrada([9,16,25]))
            
    import doctest
    doctest.testmod()
    '''
#22-----------------------------------Ejecutables--------------------------------
"""
    1-From CMD seleccionar el path de la ubicacion del archivo de interfaz 
    2-Enviar el comando desde CMD: pyinstaller --windowed --onefile NombreArchivo.py
    3-Se generaran archivos y carpets 
    4-Abrir carpeta dist y todos los archivos deben de ir juntos.
    5-si le quieres colocar una imagen enviar adicionalmente: --icon=./Nombre.ico
    """
#23-----------------------------------Ejercicios---------------------------------
'''
    #print("Hola")

    #-Ordenar Elementos
    lista=[89,12,66,4,20,0,45,2,50]

    def bubble_sort(lista):
        for i in range(len(lista)-1):
            print(lista)
            for x in range (len(lista) - 1):
                if lista[x] > lista[x + 1]:
                    lista[x], lista[x+1] = lista[x + 1], lista[x]
                    
        return lista
    print(bubble_sort(lista))
    
    #-
    import re

    Variable = '0a2c53455256494345532f444154412f4543472f5350434d2f4343534d2f424c41434b4c4953545f555044415445220d5350434d56444d534f413432342a2c53455256494345532f444154412f4543472f5350434d2f4343534d2f424c41434b4c4953545f5550444154453a8f010a8c011a0d4d5535542d3134483132372d421a0d4d5535542d3134483132372d431a0d4d5535542d3134483132372d471a0d4d5535542d3134483132372d481a0d4d5535542d3134483132372d4c1a0d4d5535542d3134483132372d521a0d4d5535542d3134483132372d571a0f636f6d2e666f72642e6563672e474d1a10636f6d2e666f72642e6563672e52454d52036563675a03313330'
    #Variable = '333633'
    """
    Found=re.search("8f", Variable)
    Start=Found.start()
    End=Found.end()-1
    print(f"La palabra fue encontrada en el string desde el caracter {Start} hasta el {End}")
    """
    Variable1 = Variable[:216]
    #Variable2 = Variable[218:]
    #print(Variable)
    print(bytes.fromhex(Variable1).decode('ascii'))
    #print(Variable1)
    
    #-
    def sumatoria(numeros):
        acum = 0
        for n in numeros:
            #print("suma de {} + {}".format(acum, n))
            acum += n
            
        return acum
        
    print(sumatoria([1,2,3,4,5]))

    '''

#Reto
#Multiplicacion de numeros sin usar x o multiply
print(-25*13)
print(int(-25/(1/13)))





