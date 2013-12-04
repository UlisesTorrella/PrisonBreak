import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento
from pilas.comportamientos import Avanzar

VELOCIDAD = 100

NORTE = 0
SUR = 2
ESTE = 1
OESTE = 3
#soy un comentario

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


class Caminando(Esperando):



    def __init__(self,sentido,BasePersonajeRPG):
        self._repeticion_cuadro = 3

        self.cuadros = [[1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2],
                        [4,4,4,4,3,3,3,3,4,4,4,4,5,5,5,5],
                        [7,7,7,7,6,6,6,6,7,7,7,7,8,8,8,8],
                        [10,10,10,10,9,9,9,9,10,10,10,10,11,11,11,11]]

        self.paso = 0
        self.dx = 0
        self.dy = 0
        self.sentido=sentido
        self.personaje=BasePersonajeRPG

    def iniciar(self, receptor):
        self.receptor = receptor


    def actualizar(self):

        self.avanzar_animacion()

        if self.sentido=="izquierda":
            self.dx = self.receptor.velocidad * -1
            self.receptor.direccion = pilas.actores.personajes_rpg.OESTE
            self.personaje.x-=1
        if self.sentido=="derecha":
            self.dx = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.ESTE
            self.personaje.x+=1
        if self.sentido == "arriba":
            self.dy = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.NORTE
            self.personaje.y+=1
        if self.sentido == "abajo":
            self.dy = self.receptor.velocidad * -1
            self.personaje.y-=1
            self.receptor.direccion = pilas.actores.personajes_rpg.SUR

    def avanzar_animacion(self):

        self.paso += 1
        if self.paso >= len(self.cuadros[self.receptor.direccion]):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.receptor.direccion][self.paso])


class Policias(BasePersonajeRPG):


    def __init__(self, mapa, x=0, y=0,direccion="arriba",rango=500,anchoVision=100,largoVision=100):
        BasePersonajeRPG.__init__(self, mapa, x=x, y=y, imagen="rpg/maton.png", velocidad=2)
        
        self.sentido=direccion
        self.initX=self.x
        self.initY=self.y
        self.rango=rango
        self.hacer(Caminando(self.sentido,self))
        

        #inicio y fin del recorrido
        self.destinoX=0
        self.destinoY=0
        self.puntodecontrolX=0
        self.puntodecontrolY=0
        

        #Area de vision
        self.largoVision=largoVision
        self.anchoVision=anchoVision
        self.visionX=self.x
        self.visionY=self.y
        self.rectangulo = pilas.fisica.Rectangulo(self.visionX,self.visionY,largoVision,anchoVision,dinamica=False)
        

        if direccion=="izquierda":
            self.destinoX=self.initX-self.rango
            self.puntodecontrolX=self.initX+1

        elif direccion=="derecha":
            self.destinoX=self.initX+self.rango
            self.puntodecontrolX=self.initX-1

        elif direccion=="arriba":
            self.destinoY=self.initY+self.rango
            self.puntodecontrolY=self.initY-1

        elif direccion=="abajo":
            self.destinoY=self.initY-self.rango
            self.puntodecontrolY=self.initY+1


    def actualizar_vision(self):

        if self.sentido=="izquierda":
            self.rectangulo.x = self.x - self.largoVision/2
        elif self.sentido=="derecha":
            self.rectangulo.x = self.x + self.largoVision/2
        elif self.sentido=="arriba":
            self.rectangulo.y = self.y + self.anchoVision/2
        elif self.sentido=="abajo":
            self.rectangulo.y = self.y - self.anchoVision/2


    def cambiar_direccion(self):
        if self.sentido=="izquierda":
            self.sentido="derecha"
            #self.mirar_derecha()
        elif self.sentido=="derecha":
            self.sentido="izquierda"
        elif self.sentido=="arriba":
            self.sentido="abajo"
        elif self.sentido=="abajo":
            self.sentido="arriba"
        


    def actualizar(self):
        if self.x==self.destinoX:
            self.cambiar_direccion()
            self.hacer(Caminando(self.sentido,self))
        elif self.x==self.puntodecontrolX:
            self.cambiar_direccion()
            self.hacer(Caminando(self.sentido,self))

        if self.y==self.destinoY:
            self.cambiar_direccion()
            self.hacer(Caminando(self.sentido,self))
        elif self.y==self.puntodecontrolY:
            self.cambiar_direccion()
            self.hacer(Caminando(self.sentido,self))

        self.actualizar_vision()
