from random import randint, randrange


class Personaje:

    def __init__(self, historia, vida):
        """Constructor

        Args:
            historia (String): breve descripcion
            vida (int): cantidadvida
        """
        self.historia = historia
        self.vida = vida


class Terrorista(Personaje):
    def __init__(self, skin, armas, grupo, historia, vida): 
        self.skin = skin
        self.armas = armas
        self.grupo = grupo
        super().__init__(historia, vida) 

    def ataque_recibido(self, disparo):
        ataque = disparo * randint(1,4)
        self.vida = self.vida - ataque


class Antiterrorista(Personaje):
    def __init__(self, skin, armas, grupo, historia, vida):
        super().__init__(vida)   
        super().__init__(historia)  
        self.skin = skin
        self.armas = armas
        self.grupo = grupo


terrorista1 = Terrorista(skin='ropa',armas='ak47',grupo='SAS',vida=100,historia='Pertenece desde 1900')

print(terrorista1.armas)
terrorista1.ataque_recibido(1)
print(terrorista1.vida)