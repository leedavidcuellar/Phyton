# Bucle de repeticion hay 2 en python

# For
'''for i in 'Python':
    print(i)

lista = [True, False, 1, 2, 3, 4, 'Hola']

for i in lista:
    print(i)

lista1 = []

for i in range(0,3): # Range no toma el ultimo valor si agrego un tercer parametro indico salto que quiero
    dato_ingreso = input('Ingrese un numero: ')
    
    if dato_ingreso.isnumeric():
        lista1.append(int(dato_ingreso))
    else:
        print('No es un numero')
        break

print(lista1) # Lo imprime como vector

# While
x = 10
while x > 0 :
    print(x)
    x -= 1
    '''



while True :
    print('\n1 - Deposito\n2 - Extranccion\n3 - Transferencia\n4 - Salir')    
    opcion = int(input('\nIngrese la opcion deseada: '))

    if opcion == 1:
        x = int(input('\nIngrese monto a Depositar: '))

    elif opcion == 2:
        x = int(input('\nIngrese monto a Extraer: '))  

    elif opcion == 3:
        x = int(input('\nIngrese monto a Transferir: ')) 
    elif opcion == 4:
        break       
    else:
        print('\nLa opcion ingresada no corresponde\n')


print('\nSalio del sistema')        



