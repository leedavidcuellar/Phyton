# Str
a = "Esto es un cadena"
b = 'Esto es otra cadena'
print(a, type(a))
print(a, type(b))

c = str(120.56)
print(c,type(c))

print(len(a))
print(a[0:4])
print(a[-1])

# Metodos de String
print(a.lower()) 
print(a.upper())
print(a.split())
print(a.len(a.split()))

# List es conjunto o array que permite almacenar lo que sea
lista_1 = ['hola',4,2.5,True,[1,2,3,4],('a','b')]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_uno = lista_1[4]
print(var_uno)
print(type(var_uno))

# Una tupla no se puede cambiar es como una lista, cambio la lista si puedeo mutar 
# Metodos de List

lista_1.append('lista')
print(lista_1)

print(lista_1.index(('a','b')))
lista_1.insert(1,5)
print(lista_1)

# Diccionario son como los json, es estructura de datos, que permite manejar con clave y valor, la clave es str : y valor
usuario = {
    'nombre': 'Octavio',
    'apellido': 'Gomez',
    'edad': 38,
    'hobbies': ['Futbol','Musica'],
    'mascotas': False
}

print(usuario)
print(usuario['edad'])
print(len(usuario))

# Metodo de diccionario
print(usuario.get('Puesto','No encontrado'))
keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))

print(usuario.values())



