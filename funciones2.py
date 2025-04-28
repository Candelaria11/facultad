#EJERCICIO 1

def calular_area_triangulo(dato1,dato2)-> float:
    '''
    Funcion que reciba la base y altura de un triangulo,
    retorna el area del mismo
    '''
    area = base * altura
    return area


base = float(input("ingrese la base del rectangulo: "))  
altura = float(input("ingrese la altura del resctangulo: "))  
resultado = calular_area_triangulo(base, altura)
print("el area es de: " , resultado)

#EJERCICIO 2

def calcula_area_circulo(dato)-> float:
 '''
 La funcion recibe el radio de un circulo como parametro y devuelve el area del mismo
 '''
 pi = 3.14
 area = pi * dato **2
 print("el area del circulo el:" , area)
 return area




radio = float(input("ingrese el radio del circulo: "))
calcula_area_circulo(radio)


#EJERCICIO 3

def verificar_par_impar (num):
    '''
    La funcion verifica si un numero es par o impar
    imprime un mensaje indicando si es par o no 
    '''
    if num % 2 == 0:
        print("el numero es par")
    else:
        print("el numero no es par")    

verificar_par_impar(2)    


#EJERCICIO 4

def verificar_par_bool (num):
    '''
    La funcion recibe por parametro un numero, devuelva True si es par y devuelve False si no es par
    '''
    if num %2 == 0:
     return True
    else:
     return False
    
verificar_par_bool(9)    
if verificar_par_bool == True:
    print("es par")
else:
    print("es impar")    

#EJERCICIO 5

def hallar_maximo(uno:int,dos:int, tres:int) -> int:
    '''
    La funcion recibe 3 enteros
    los compara y determina cual es el mayor
    ''' 
    max = uno
    if dos > uno:
        max = dos
    elif tres > uno:
        max = tres    
    print("el numero mas grande ingresado fue", max) 
    return max   



numero1= int(input("ingrese el primer numero: "))
numero2= int(input("ingrese el segundo numero: "))    
numero3= int(input("ingrese el tercer numero: "))
hallar_maximo(numero1,numero2,numero3)

#EJERCICIO 6 

def calcular_portencia (uno,dos) -> int:
    '''
    La funcion recibe la base y el exponente como argumentos y devuelve como resultado la potencia
    '''
    multiplicacion = uno ** dos
    print("la potencia es:", multiplicacion)
    return multiplicacion



base = int(input("ingrese la base: "))
exponente = int(input("ingrese el exponente: "))
calcular_portencia(base,exponente)

#EJERCICI0 7

def retornar_primo(num)->bool:
    '''
    La funcion recibe un numero, retorna True si el numero es primo e imprime un mensaje aclarando,
    retorna False si no es primo e imprime un mensaje
    '''
    contador = 0
    for i in range (1,num + 1):
     if num % i == 0:
      contador += 1
    if contador > 2:
        print("no es primo")
        return True   
    else:
        print("es primo")
        return False
        
numero = int(input("ingrese un numero: "))
retornar_primo(numero )



#EJERCICIO 8 
def retornar_primo(num, inicio = 1)->int:
 '''
 La funcion retona la cantidad de numero encontrados entre la unidad
 y el numero ingresado
 '''
 contador2 = 0
 for i in range (inicio ,num + 1):
  contador = 0
  for j in range (inicio , num + 1):
     if i % j == 0:
      contador += 1
  if contador == 2:
     contador2 += 1

 return contador2
    
    

numero = int(input("ingrese un numero: "))
cantidad = retornar_primo(numero)
print(cantidad)


#EJERCICI0 9
def imprimir_tabla(num:int, uno=1, dos=10):
    '''
    La funcion imprime la tabla de multiplicar del numero recibido por parametro
    '''
    for i in range (uno, dos + 1):
        multiplicacion = num * i 
        print(multiplicacion)


numero = int(input("ingrese un numero: "))
imprimir_tabla(numero)

#EJERCICIO 1O

def pedir_retornar_num()->int:
    '''
    La funcion recibe y retorna un numero entero
    '''
    numero = (input("ingrese un numero: "))
    return numero

pedir_retornar_num()


#EJERCICIO 11
def pedir_float_retornar()-> float:
    '''
    La funcion recibe y retorna un numero float
    '''
    numero = float(input("ingrese un numero: "))
    return numero

pedir_float_retornar()


#EJERCICIO 12
def pedir_cadena_retornar()-> str:
    '''
    La funcion recibe y retorna un string
    '''
    cadena = str(input("ingrese una cadena: "))
    return cadena

pedir_cadena_retornar()

