# Ejercicio 1, Realizar menu de un cajero automatico
from ast import match_case


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


# Ejercicio 2 
print('\nLe solicitaremos dos numeros enteros\npara obtener en ese rango numeros pares.\nSiendo el 1er numero menor que el 2do numero que ingrese')
primer_num = int(input('\nIngrese 1er numero: '))
segundo_num = int(input('Ingrese 2do numero: '))

lista_pares = []

for i in range(primer_num,segundo_num + 1):
    if i%2 == 0:
        lista_pares.append(i)
print('\n',' Los numeros pares encontrados en el rango ('f'{primer_num}'','f'{segundo_num}',')',lista_pares)  
