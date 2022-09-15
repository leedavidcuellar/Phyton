# Clase
class Animal:

    def __init__(self,especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self, sonido):
        print(sonido)
        pass


class Perro(Animal):
    # Atributos de clase == global
    # especie = 'mamiferos'

    def __init__(self, nombre, raza, especie, edad): # Es el constructor
        # Atributos de intancia  == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie,edad)

    # Metodos
   

    def jugar (self, objeto):
        print('El perro esta jugando con ', objeto)   

    def saludar(self):
        print(f'{self.nombre} dio la pata')         

perro_1 = Perro('Rex','Collie')
print(f'Perro 1 ->{perro_1.nombre},{perro_1.raza},{perro_1.especie},{perro_1.edad}')
perro_1.ladrar()
perro_1.jugar('Pelota')
perro_1.saludar()        



#perosnajes, supor, jungla, top, ct y antiterrorista