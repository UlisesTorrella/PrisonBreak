#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from MenuInicial import EscenaDeMenu
from nivel1 import Nivel1



class EscenaAtrapado(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):

        self.musica = pilas.sonidos.cargar("MusicaPerdiste.mp4")
        self.musica.reproducir()

        pilas.fondos.Fondo("ImagenAtrapado.jpg")

        opciones = [('Intentar de Nuevo', self.volver),('Volver al Menu', self.menu)]

        self.menu = pilas.actores.Menu(opciones)


    def volver(self):
        self.musica.detener()

        pilas.cambiar_escena(Nivel1())

    def menu(self):
        self.musica.detener()

        pilas.cambiar_escena(EscenaDeMenu())



