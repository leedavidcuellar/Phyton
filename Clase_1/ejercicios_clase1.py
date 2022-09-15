
# 1 Idear la manera de realizar la siguiente salida (a, b y c son variables).:
print("a\tb\tc\n2.4\t-3.21\t47.8")

# 2 Mostrar por pantalla alguna imagen o dibujo.

""" 3 Escriba un programa que lea 1 palabra (ingresadas por el usuario), 
 calcule la longitud de cada una de ellas y las despliegue junto con su longitud 
 indicada con asteriscos. Ejemplo: Árbol ***** Celular ******* Uno ***"""

print("Tiene que ingresar tres palabras: ")
palabra1 = input("Ingrese palabra 1: ")
palabra2 = input("Ingrese palabra 2: ")
palabra3 = input("Ingrese palabra 3: ")

print(palabra1,'\t', (len(palabra1)*'*'))
print(palabra2,'', (len(palabra2)*'*'))
print(palabra3,'\t', (len(palabra3)*'*'))

# 4. Crear un diccionario del ejercicio anterior.
diccionario = {
   'Palabra 1': palabra1,
   'Palabra 2': palabra2,
   'Palabra 3': palabra3
}
print(diccionario)
print(diccionario.keys())
print(diccionario.items())
print(diccionario.values())
print(diccionario.get('uno','no esta'))


print('''
   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWNX0OkkxxxxxxkkO0XNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWXkoc::;;;;;;;;;;;:cokKWWWWWWWWWWWWWW
WWWWWWWWWWWWWXo;ck0Oo;;;;;;;;;;;;;;l0WWWWWWWWWWWWW
WWWWWWWWWWWWWKl;l0XKo;;;;;;;;;;;;;;;xNWWWWWWWWWWWW
WWWWWWWWWWWWWKl;;:c:;;;;;;;;;;;;;;;;xNWWWWWWWWWWWW
WWWWWWWWWWWNWXOxkkxxkxkkoc:;;;;;;;;;xNWWWWWWWWWWWW
WWWWNKkdooooooooooooooooc:;;;;;;;;;;xNX00KKKXNWWWW
WWWXkc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;xXKO000O0KNWWW
WWNx:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kX0O0OO000KNWW
WWOc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oKX0OOO00000KNW
WNx;;;;;;;;;;;;;;;;:::::::::::::cokXX00OO00O00OKNW
WNd;;;;;;;;;;:lxkOOO0000000000000KXK0O00000O00O0NW
WNx;;;;;;;;;:xXXKK00000000000000000OO000000OO0O0NW
WWOc;;;;;;;;oXX0000000OO000000000000OOO000OOOO0KWW
WWNx:;;;;;;;xXK000000O00000000000000OOOO0OOO00KNWW
WWWXx:;;;;;:kNKO000000000000000OO000OOOOO00O0KNWWW
WWWWN0xollclONKO0000000000KKKKKKKKKKKKKKKKKXNWWWWW
WWWWWWWNNNNNWNKO000000O00KXXXXXXXXXXNWWWWWWWWWWWWW
WWWWWWWWWWWWWNKO00000OOOOOO0000000O0XWWWWWWWWWWWWW
WWWWWWWWWWWWWNKOOO00000OOOO000XNNX00XWWWWWWWWWWWWW
WWWWWWWWWWWWWWX0OO00000000OO00XNNK00XWWWWWWWWWWWWW
WWWWWWWWWWWWWWWNKK00000OOOOOOO000KKNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWNNXXXXXKXXXXXNNWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
   '''
)