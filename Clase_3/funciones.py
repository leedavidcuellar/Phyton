# Nombre
# Argunmentos
# Codigo
# Retorno

def sumar(a,b):
    resultado = a + b

    return resultado

print(sumar(2,3))

# Funcion sin parametros
def resta():
    resultado = 2 - 3
    return resultado
print(resta())

# Funcion sin return
def resta_2():
    print(2-3)

resta_2()

# Funcion
def saludo(cantidad_saludos):
    """_summary_

    Args:
        cantidad_saludos (int): el numero de veces repetir pra guar nombres

    Returns:
        list: lista_nombre devuelve la lista nombres
    """
    lista_nombres =[]
    for i in range(cantidad_saludos):
        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)
        lista_nombres.append(nombre)  
    return lista_nombres

def orden(lista,sentido):
    """ Esta funcion ordena la lista nombres
    con sentido que es boleano
    """
    lista.sort(reverse=sentido)
    return lista


nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuiar: ')))
print(nombres) 

print(orden(nombres, False))



def prueba(a, b,c):
    
    print(a, b, c)

a = 420
b = 3
c = 5
prueba (b=b,c=c,a=a) # Asi subsano que corresponda a cada uno como lo declare


