#---------------------------------------------------PORTAFOLIO 2-------------------------------------------------------

#EJERCICIO 1
"""
Nombre: invertirLista
Entradas: una lista, ya sea de números enteros, boolenos, flotantes o string.
Salida: la misma lista pero invertida
Restricciones: si la lista es vacía que devuelva 0, y que el parámetro de entrada sea una lista
"""


def invertirLista(lista):
     if(isinstance(lista, list)):
         if(lista == []):
             return 0
         else:
             return invertirLista_aux(lista, [], largoLista(lista)-1)
     else:
          return print("Error: debe ingresar como parámetro una lista")

        
def invertirLista_aux(lista, invertida, posicion):
     if(posicion == -1):
          return invertida
     else:
          invertida += [lista[posicion]]
          return invertirLista_aux(lista, invertida, posicion-1)
        

def largoLista(lista):
     if(isinstance(lista, list) and lista != []):
         if(lista == []):
             return 0
         else:
          return largoListaAux(lista, 0)
     else:
          return -1 #Error de entrada
        
def largoListaAux(lista, cont):
     if(lista == []):
          return cont
     else:
          return largoListaAux(lista[:-1], cont+1)



#======================================================================================================================#


#EJERCICIO 2


"""
Nombre: extremosLista
Entrada: una lista de números enteros
Salida: una lista que devuelva el número menor y el número mayor de la lista ingresada
Restricciones: si la lista está vacía que retorne "error" y se debe comprobar que el
parámetro de entrada sea una lista. Además si todos los números de la lista son iguales,
en la salida solo debe mostrarse un número en la lista.
"""


def extremosLista(lista):
    if(isinstance(lista,list)):
        if(listaEnteros(lista) and (lista != [])):
            return extremosLista_aux(lista,[])
        else:
            return print("Error, la lista no puede ser vacía y solo debe contener números enteros")
    

def extremosLista_aux(lista, resultado):
     menor = menorLista(lista)
     mayor = mayorLista(lista)
     if(lista == []):
          return resultado
     elif(menor == mayor):
          return(mayor)
     else:
          return(menor + mayor)
#-----------------------------------------------
def menorLista(lista):
    if lista == []:
        return "Error"
    else:
        return menorLista_aux(lista[1:],lista[0])

def menorLista_aux(lista,resultado):
    if lista == []:
        return [resultado]
    elif(lista[0] < resultado):
        return menorLista_aux(lista[1:],lista[0])
    else:
        return menorLista_aux(lista[1:],resultado) 
#------------------------------------------------
def mayorLista(lista):
    if lista == []:
        return "Error"
    else:
        return mayorLista_aux(lista[1:],lista[0])

def mayorLista_aux(lista,resultado):
    if(lista == []):
        return [resultado]
    elif lista[0] > resultado:
        return mayorLista_aux(lista[1:],lista[0])
    else:
         return mayorLista_aux(lista[1:],resultado) 
#-------------------------------------------------
def listaEnteros(lista):
    if(isinstance(lista,list) and (lista != [])):
        if(lista == []):
             return -1 #Error de entrada
        else:
            return listaEnteros_aux(lista, True)
    else:
        return -1 #Error de entrada

def listaEnteros_aux(lista, esEntera):
    if(lista == []):
        return esEntera
    else:
        if(isinstance(lista[0],int)):
            return listaEnteros_aux(lista[1:],True)
        else:
            return False

#=======================================================================================================================#

#EJERCICIO 3

"""
Nombre: eliminarDigito
Entradas: dos números enteros positivos, uno será el número y el otro el dígito que deseamos eliminar del número.
Salidas: El número, pero sin el dígito que eliminamos.
Restricciones: el número y el dígito deben ser enteros positivos y el número debe ser diferente de cero.
"""

def eliminarDigito(numero, digito):
     if(isinstance(numero,int) and isinstance(digito,int) and numero >= 0 and digito >= 0):
          if(numero != 0):
               numero=str(numero)
               digito=str(digito)
               return eliminarDigito_aux(numero,digito,"")
          else:
               return print("Error, el número no puede ser cero")
     else:
          return print("Error, ambos números ingresados deben ser enteros positivos")

def eliminarDigito_aux(numero, digito,nuevoNumero):
     if(numero == ""):
          return int(nuevoNumero)
     elif(numero[0] == digito):
        return eliminarDigito_aux(numero[1:], digito, nuevoNumero)
     else:
          return eliminarDigito_aux(numero[1:], digito, nuevoNumero + numero[0])
          
     
#=======================================================================================================================#

#EJERCICIO 4
             
    
"""
Nombre: nivelesLista
Entrada: una lista con sublistas
Salida: retorna la cantidad de lista existentes en una sublista
Restricciones: validar que el parámetro de entrada sea una lista
"""

def nivelesLista(lista):
    if(isinstance(lista,list)):
        return nivelesLista_aux(lista,[])
    else:
        return print("Error, debe ingresar como parámetro una lista")

def nivelesLista_aux(lista, resultado):
    if(lista == []):
        return resultado
    elif(isinstance(lista[0],list)):
       contador = cantidadListas(lista[0], 1)
       return nivelesLista_aux(lista[1:],resultado+[contador])
    else:
        return nivelesLista_aux(lista[1:],resultado+[0])

def cantidadListas(lista, contador):
    if(lista == []):
        return contador
    else:
        if(isinstance(lista[0],list)):
            return cantidadListas(lista[0], contador + 1)
        else:
            return cantidadListas(lista[0], contador)


#=======================================================================================================================#

#EJERCICIO 5


"""
Nombre: obtenerIndicesListaVectores
Entrada: Recibe como parámetro 3 vectores de tipo numérico enteros
Salida: Devolver los índices de una lista de vectores cuyo valor sean cero o un número negativo
Restricciones: se valida que los 3 vectores sean una lista y que sean enteros y del mismo tamaño.
"""
def obtenerIndicesListaVectores(v1, v2, v3):
    if(isinstance(v1,list) and isinstance(v2,list) and isinstance(v3,list)):
        if(tamañoVector(v1) == tamañoVector(v2) == tamañoVector(v3)):
            if(vectoresEnteros(v1) and vectoresEnteros(v2) and vectoresEnteros(v3)):
                v4=indinces(v1,0,[])
                v5=indinces(v2,0,[])
                v6=indinces(v3,0,[])
                v7=[v4]+[v5]+[v6]
                return v7
            else:
                return print("Los vectores deben ser de tipo enteros") 
        else:
            return print("Los vectores deben tener el mismo tamaño")
    else:
        return print("Los vectores deben ser de tipo listas")
            
           
def indinces(vector, contador, lista):
    if(vector == []):
        return lista
    elif(vector[0] <= 0):
        return indinces(vector[1:], contador + 1, lista + [contador])
    else:
        return indinces(vector[1:], contador + 1, lista)


def vectoresEnteros(vectores):
    if(isinstance(vectores,list) and (vectores!= [])):
        return vectoresEnteros_aux(vectores, True)
    else:
        return print("Error, debe ingresar una lista que no esté vacía")

def vectoresEnteros_aux(vectores, esEntero):
    if(vectores == []):
        return esEntero
    else:
        if(isinstance(vectores[0],int)):
            return vectoresEnteros_aux(vectores[1:],True)
        else:
            return False


def tamañoVector(vector):
    if (isinstance(vector,list)):
        if(vector == []):
            return 0
        else:
            return tamañoVector_aux(vector,0)
    else:
        return print("Error, debe ingresar como parámetro una lista")

def tamañoVector_aux(vector,contador):
    if (vector == []):
        return contador
    else:
        return tamañoVector_aux(vector[1:], contador+1)
