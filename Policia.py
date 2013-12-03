import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

VELOCIDAD = 100

NORTE = 0
SUR = 2
ESTE = 1
OESTE = 3

class BasePersonajeRPG(Actor):
    def __init__(self, mapa, x=0, y=0, imagen="rpg/maton.png", velocidad=3):
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(imagen, 3, 4)

        self.mapa = mapa

        self.direccion = pilas.actores.personajes_rpg.SUR
        self.hacer(Esperando())
        self.velocidad = velocidad

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)
        self.definir_centro((17, 48))

    def actualizar(self):
        pass

class Esperando(Comportamiento):

    def iniciar(self, receptor):

        self.receptor = receptor
        if (self.receptor.direccion == pilas.actores.personajes_rpg.NORTE):
            self.receptor.definir_cuadro(1)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.ESTE):
            self.receptor.definir_cuadro(4)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.SUR):
            self.receptor.definir_cuadro(7)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.OESTE):
            self.receptor.definir_cuadro(10)

    #def actualizar(self):
        #if pilas.escena_actual().control.izquierda:
        #   self.receptor.hacer(Caminando())
        #elif pilas.escena_actual().control.derecha:
         #   self.receptor.hacer(Caminando())
        #elif pilas.escena_actual().control.arriba:
         #   self.receptor.hacer(Caminando())
        #elif pilas.escena_actual().control.abajo:
         #   self.receptor.hacer(Caminando())

class Caminando(Esperando):



    def __init__(self,direccion):
        self._repeticion_cuadro = 3

        self.cuadros = [[1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2],
                        [4,4,4,4,3,3,3,3,4,4,4,4,5,5,5,5],
                        [7,7,7,7,6,6,6,6,7,7,7,7,8,8,8,8],
                        [10,10,10,10,9,9,9,9,10,10,10,10,11,11,11,11]]

        self.paso = 0
        self.dx = 0
        self.dy = 0
        self.direccion=direccion

    def iniciar(self, receptor):
        self.receptor = receptor


    def actualizar(self):

        self.avanzar_animacion()

        if self.direccion=="izquierda":
            self.dx = self.receptor.velocidad * -1
            self.receptor.direccion = pilas.actores.personajes_rpg.OESTE
            
        if self.direccion=="derecha":
            self.dx = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.ESTE
        if self.direccion == "arriba":
            self.dy = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.NORTE
        if self.direccion == "abajo":
            self.dy = self.receptor.velocidad * -1
            self.receptor.direccion = pilas.actores.personajes_rpg.SUR
        

    def avanzar_animacion(self):

        self.paso += 1

        if self.paso >= len(self.cuadros[self.receptor.direccion]):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.receptor.direccion][self.paso])

class Policias(BasePersonajeRPG):


    def __init__(self, mapa, x=0, y=0):
        BasePersonajeRPG.__init__(self, mapa, x=x, y=y, imagen="rpg/maton.png", velocidad=2)
        initX = self.x
        direccion = "arriba"
        self.hacer(Caminando(direccion))

