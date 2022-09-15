# Clases y sus metodos
class Biblioteca:
    """Clase Biblioteca
    """

    def __init__(self, sector):
        """Constructor Biblioteca
        Args:
            sector (String): Sector o Rubro del libro
        """
        self.sector = sector


class Libro(Biblioteca):
    """Clase Libro
        Hereda de Biblioteca
    Args:
        Biblioteca (Biblioteca): Clase padre de Libro
    """

    def __init__(self, sector, isbn, nombre, autor, editorial, num_ejemplares, num_prestados):
        """Constructor de libro

        Args:
            sector (String): sector o rubro del libro heredado de biblioteca
            isbn (String): numero de serie del libro
            nombre (String): nombre del libro
            autor (String): nombre del autor
            editorial (String): nombre de la editorial
            num_ejemplares (Integer): numero de libros que hay
            num_prestados (Integer): numero de libros prestados
        """
        super().__init__(sector)
        self.isbn = isbn
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.num_ejemplares = num_ejemplares
        self.num_prestados = num_prestados

    def prestamo_libro(lista_libros):
        if len(lista_libros) == 0:
            print('\nNo hay libros cargados\n---')
        else:    
            libro_abuscar = input('Ingrese el libro que quiere retirar: ')
            for libroP in lista_libros:
                if (libroP.nombre == libro_abuscar):
                    if (libroP.num_ejemplares > 0):
                            libroP.num_ejemplares = libroP.num_ejemplares - 1
                            libroP.num_prestados += 1
                            
                            print('\nLibro prestado')
                    else:
                            print('\nNo hay Ejemplares')    
                else:
                    print('\nNo hay libros para prestar')

    def devolucion_libro(lista_libros):
        if len(lista_libros) == 0:
            print('\nNo hay libros cargados\n---')
        else:
            libro_abuscar = input('Ingrese el libro que quiere devolver: ')
            for libroD in lista_libros:
                if (libroD.nombre == libro_abuscar):
                    libroD.num_ejemplares = libroD.num_ejemplares + 1
                    libroD.num_prestados -= 1
                    print('\nLibro devuelto')
                else:
                    print('\nEse libro no esta')



# Metodos y Variables Globales
lista_libros = []


def crear_varios_libro(cant, lista_libros):

    for i in range(0, cant):
        print('\nSe le solicitaran datos del libro num ', (i+1))
        libro_Aux = Libro(sector=input('\nIngrese nombre del area pertenece libro (Ejem: Economia, Novela, Ficcion): '),
                          isbn=input('Ingrese el ISBN del libro: '),
                          nombre=input('Ingrese nombre del libro: '),
                          autor=input('Ingrese el nombre del autor: '),
            editorial=input('Ingrese el nombre de la editorial: '),
            num_ejemplares=int(input('Ingrese cantidad ejemplares: ')),
            num_prestados=0
        )
        lista_libros.append(libro_Aux)


def mostrar_libros(lista_libros):
    k = 0
    while k < len(lista_libros):
        print(f'Libro {k+1}, Sector: {lista_libros[k].sector}, ISBN: {lista_libros[k].isbn}, Nombre: {lista_libros[k].nombre}, Autor: {lista_libros[k].autor}, Editorial: {lista_libros[k].editorial}, Ejemplares: {lista_libros[k].num_ejemplares}, Prestados: {lista_libros[k].num_prestados}')
        k += 1
    if len(lista_libros) == 0:
        print('\nNo hay libros cargados\n-----')


def borrar_libro(lista_libros):
    auxB = False
    while auxB == False:
        nombre_borrar = input('\nIngrese Nombre del Libro a Borrar: ')
        for libro in lista_libros:
            if (libro.nombre == nombre_borrar):
                lista_libros.remove(libro)
                auxB = True
                print('\nLibro eliminado')
                break

        if auxB == False:
            respuesta = input(
                '\n\nEl libro ingresado No se encuentra\n\nDesea buscar denuevo, S (Si)/N (No): ').upper()
            if respuesta == 'N':
                auxB = True


def administrador_acciones():
    print('\n--- Bienvenido al sistema Carga de libros ---\n')
    while True:
        print('\n1 - Agregar Libros\n2 - Mostrar Libros\n3 - Borrar Libros\n4 - Salir')
        opcion_Adm = int(input('\nIngrese la opcion deseada: '))
        if opcion_Adm == 1:
                cantidad_libros_ingresar = int(
                    input('\nIngrese cantidad libros a ingresar: '))
                crear_varios_libro(cantidad_libros_ingresar, lista_libros)
        elif opcion_Adm == 2:
                print('---- Listado de Libros ----')
                mostrar_libros(lista_libros)
        elif opcion_Adm == 3:
                borrar_libro(lista_libros)
        elif opcion_Adm == 4:
                break
        else:
                print('\nLa opcion de Administrador ingresada NO corresponde\n')

def usuario_acciones():
    print('\n--- Bienvenido al sistema Usuarios Bibioteca ---\n')
    while True:
        print('\n1 - Mostrar Libros\n2 - Pedir Libro\n3 - Devolver Libro\n4 - Salir')
        opcion_usu = int(input('\nIngrese la opcion deseada: '))
        if opcion_usu == 1:
            print('---- Listado de Libros a Pedir ----')
            mostrar_libros(lista_libros)
        elif opcion_usu == 2:
            Libro.prestamo_libro(lista_libros)
        elif opcion_usu == 3:
            Libro.devolucion_libro(lista_libros)
        elif opcion_usu == 4:
            break
        else:
            print('\nLa opcion de Administrador ingresada NO corresponde\n')



# Codigo del Programa
while True:
    print('\n--- Bienvenido a la Biblioteca ---\n1 - Usuario\n2 - Administrador\n3 - Salir')
    opcion = int(input('\nIngrese la opcion deseada: '))
    if opcion == 1:
        usuario_acciones()
    elif opcion == 2:
        administrador_acciones()
    elif opcion == 3:
        break
    else:
        print('\nLa opcion ingresada de la Biblioteca NO corresponde\n')

print('Gracias por su visita - Fin a Salido del Sistema')
