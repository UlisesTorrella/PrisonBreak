#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from MenuInicial import EscenaDeMenu
from nivel1 import Nivel1



class EscenaGanaste(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo("ImagenGanaste.png")
        self.musica = pilas.sonidos.cargar("MusicaGanaste.mp4")
        self.musica.reproducir()

        opciones = [('Jugar de Nuevo', self.volver),('Volver al Menu', self.menu)]

        self.menu = pilas.actores.Menu(opciones,x=-100,y=-100)


    def volver(self):
        self.musica.detener()
        pilas.cambiar_escena(Nivel1())

    def menu(self):
        self.musica.detener()
        pilas.cambiar_escena(EscenaDeMenu())
