#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from pilas.comportamientos import Avanzar
import Policia
from Policia import BasePersonajeRPG


class Nivel(pilas.escena.Base):
	
	def __init__(self):
		pilas.escena.Base.__init__(self)

	def cambiar_ropa(self,protagonista,ropa):
		self.visible=False
		self.protagonista.imagen = pilas.imagenes.cargar_grilla("rpg/maton.png", 3, 4)
		pilas.avisar("Ahora no puedes ser detectado")



	def detectado(self):
		import MenuAtrapado

		pilas.cambiar_escena(MenuAtrapado.EscenaAtrapado())

	def terminar(self,protagonista,salida):
		import sys
		sys.exit(0)
