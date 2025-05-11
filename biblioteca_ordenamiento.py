#EJERCICIO 1

#Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente 
def ordenar_nombres_ascendente(uno:list, dos:list):
 '''
 La funcion  ordena de manera ascendente los nombres, mientras que repeta su respectiva edad
 ''' 
 
 for i in range (len(uno)-1):
    for j in range(i+1, len(uno)):
    
       if (uno[i] > uno[j]) :
            aux = uno[i]
            uno[i] = uno[j]   
            uno[j] = aux     

            edad_aux = dos[i]
            dos[i] = dos[j]
            dos[j] = edad_aux

def imprimir_nombres_edades(uno, dos):
 '''
 La funcion recorre la nueva lista y la muestra
 '''
 print("nombres ordenados de manera descendente: ")
 for i in range (len(uno)):
  print(uno[i], dos[i])    

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]  
ordenar_nombres_ascendente(Nombres, Edades)
imprimir_nombres_edades(Nombres, Edades)
 
#EJERCICIO 2
#Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente. 

def ordenar_nombres_puntos_ascendentes(nom:list, puntos:list):
    for i in range (len(nom)-1):
        for j in range (i+1, len(nom)):
            if (nom[i] > nom[j]) :
                aux = nom[i]
                nom[i] = nom[j] 
                nom[j] = aux 

                aux1 = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux1

            elif nom[j] == nom[i] :
                 if puntos[i] < puntos[j]: 
                   
                   aux2 = puntos[i]  
                   puntos[i] = puntos[j]
                   puntos[j] = aux2

                   aux3 = nom[i]
                   nom[i] = nom[j]
                   nom[j] = aux3

def imprimir_nombres_puntos(nom:list,puntos:list):
    for i in range(len(nom)):
       print((nom[i],puntos[i] ))  


nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Inglbra","Contabilidad","Artes","Algeistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza", "Matematica"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

ordenar_nombres_puntos_ascendentes(nombres, Puntos)
imprimir_nombres_puntos(nombres, Puntos)


#EJERCICIO 3
#Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera 
#ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente. 

def ordenar_apellidos_descendente(ape:list, nom:list, nota:list):
   for i in range(len(ape)-1):
      for j in range(i+1, len(ape)):

         if ape[i] > ape[j]:
            aux_ape = ape[i]
            ape[i] = ape[j]
            ape[j] = aux_ape

            aux_nom = nom[i]
            nom[i] = nom[j]
            nom[j] = aux_nom

            aux_nota = nota[i]
            nota[i] = nota[j]
            nota[j] = aux_nota
         elif ape[i] == ape[j]:
            if nom[i] > nom[j]:
             aux_nom = nom[i]
             nom[i] = nom[j]
             nom[j] = aux_nom

             aux_ape = ape[i]
             ape[i] = ape[j]
             ape[j] = aux_ape

             aux_nota = nota[i]
             nota[i] = nota[j]
             nota[j] = aux_nota
         elif nom[i] == nom[j]:
            if nota[i] < nota[j]:

               aux_nota = nota[i]
               nota[i] = nota[j]
               nota[j] = aux_nota

               aux_ape = ape[i]
               ape[i] = ape[j]
               aux_ape = ape[j] 

               aux_nom = nom[i]
               nom[i] = nom[j]
               aux_nom = nom[j]

def imprimir_nombre_apellido_nota(ape:list, nom:list, nota:list):
   for i in range(len(ape)):
      print(ape[i], nom[i], nota[i]) 

Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
ordenar_apellidos_descendente(Apellidos, Estudiantes, Nota)
imprimir_nombre_apellido_nota(Apellidos, Estudiantes, Nota)
            
#EJERCICIO 4
def listar_usuarios_mexico(pais, edad, postal, correo, name, mail, telefono, regiones):
    
    for i in range(len(pais)):
        if pais[i] == "Mexico":
            lista_mexico.append(pais[i])
            datos_mexico.append((edad[i], pais[i], postal[i], correo[i], name[i], mail[i], telefono[i], regiones[i]))
lista_mexico = []
datos_mexico = []

def acomodar_mexico_descendinte(mexico:list, datos:list):
   for i in range(len(mexico)-1):
      for j in range(i+1, len(mexico)):

         if mexico[i] > mexico[j]:
           auxiliar = mexico[i]
           mexico[i] = mexico[j]
           auxiliar = mexico[j]

           auxuliar1 = datos[i]
           datos[i] = datos[j]
           auxiliar1 = datos[j]

def imprimir_datos_mexico(lista:list):  
   print("datos usuario de mexico: ")
   for i in range(len(lista)):
      print(datos_mexico[i])        
     


def buscar_edad_joven(edad:list):
  menor = edad[0]
  for i in range(len(edad)):
     if edad[i] < menor:
        menor = edad[i] 
  return menor      

def guardar_datos_usuario_menor(edades: list, nombres:list, telefonos:list, mails:list, postalZip:list, address:list, region:list, country:list, joven:int):        
 for i in range(len(edades)):
   if edades[i] == joven:
     nombre_jovenes.append(nombres[i])
     menores.append((nombres[i], telefonos[i], mails[i], postalZip[i], address[i], region[i], country[i],edades[i]))


def comparar_nombres(nombre_jovenes:list, menores:list):
   for i in range (len(nombre_jovenes)-1):
      for j in range( i+1, len(nombre_jovenes)):
       if nombre_jovenes[i] > nombre_jovenes[j]:
         auxiliar = menores[i]
         menores[i] = menores[j]
         menores[j] = auxiliar



def mostrar_resulatdo(menores):
  for i in range (len(menores)):
   print(menores[i])                   

                     
nombre_jovenes = []
menores = []

def buscar_mexico_brasil_cp8000(country:list, postalZip:list, nombres:list, edades:list, address:list, telefonos:list, mails:list, region:list):
   for i in range(len(country)):
    if (country[i] == "Mexico" or country[i] == "Brasil") and postalZip[i] > 8000:
       datos_usuarios.append((nombres[i], address[i], edades[i], postalZip[i], country[i] , telefonos[i], mails[i], region[i]))
       nombre_usuario.append(nombres[i])
       edad_usuario.append(edades[i])
def ordenar_nombre_edad_descendente(datos, nombre, edad):
   for i in range(len(nombre)):
      for j in range(len(nombre)):
         if nombre[i] < nombre[j]:
            aux = datos[i]
            datos[i] = datos[j]
            datos[j] = aux
         elif nombre[i]  == nombre[j]:
            if edad[i] < edad[j]:
             aux = datos[i]
             datos[i] = datos[j]
             datos[j] = aux

def mostrar_usuarios(datos):
   for i in range(len(datos)):
      print(datos[i])
   


datos_usuarios = []
nombre_usuario = []
edad_usuario  = []


