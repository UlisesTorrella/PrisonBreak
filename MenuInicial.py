#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from nivel1 import Nivel1
from Ayuda import EscenaAyuda

class EscenaDeMenu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        self.musica = pilas.sonidos.cargar("MusicaMenu.mp3")
        self.musica.reproducir()

        pilas.fondos.Fondo("FondoPB2.jpg")

        menu = [('Comenzar a jugar', self.comenzar),('Ayuda',self.ayuda),('Salir', self.salir)]

        self.menu = pilas.actores.Menu(menu,y =-100)
 
    def ayuda(self):
        self.musica.detener()
        pilas.cambiar_escena(EscenaAyuda())

    def comenzar(self):
        self.musica.detener()
        pilas.cambiar_escena(Nivel1())

    def salir(self):
        import sys
        sys.exit(0)

