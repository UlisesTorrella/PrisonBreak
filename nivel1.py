#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from pilas.comportamientos import Avanzar
import Policia
from Policia import BasePersonajeRPG




class Lvl1 ():
	def __init__(self):
		mapa = pilas.actores.MapaTiled("Obstaculos.tmx")

		self.malo1 = Policia.Policias(mapa,658,-2272,"derecha")		
		self.malo2 = Policia.Policias(mapa,1258,-2147,"izquierda",rango=400,anchoVision=100,largoVision=300)
		self.malo3 = Policia.Policias(mapa,664,-1696,"derecha",rango=400,anchoVision=100,largoVision=300)
		self.malo4 = Policia.Policias(mapa,1085,-1638,"izquierda",rango=400,anchoVision=100,largoVision=300)
		self.malo5 = Policia.Policias(mapa,1600,-2300,"arriba",rango=600,anchoVision=300,largoVision=100)
		self.malo6 = Policia.Policias(mapa,1818,-2200,"derecha",rango=200,anchoVision=100,largoVision=100)
		self.malo7 = Policia.Policias(mapa,1930,-1278,"derecha",rango=70,anchoVision=100,largoVision=100)
		self.malo8 = Policia.Policias(mapa,1887,-1243,"derecha",rango=100,anchoVision=100,largoVision=100)

		self.protagonista=pilas.actores.Calvo(mapa,1)
		self.protagonista.aprender(pilas.habilidades.SiempreEnElCentro)
		self.protagonista.x = 1040
		self.protagonista.y = -2371

	def revision(self, protagonista, malo):
		if protagonista.x < malo.rectangulo.x+malo.largoVision/2 and protagonista.x > malo.rectangulo.x-malo.largoVision/2:
			if protagonista.y < malo.rectangulo.y + malo.anchoVision/2 and protagonista.y > malo.rectangulo.y - malo.anchoVision/2:
					self.detectado()


	def detectado(self):
		print "perdiste"

def iniciar():


	nivel=Lvl1()

	def colision_con_vision(self):
		print "hola amigo"
		nivel.revision(nivel.protagonista,nivel.malo1)
		nivel.revision(nivel.protagonista,nivel.malo2)
		nivel.revision(nivel.protagonista,nivel.malo3)
		nivel.revision(nivel.protagonista,nivel.malo4)
		nivel.revision(nivel.protagonista,nivel.malo5)
		nivel.revision(nivel.protagonista,nivel.malo6)
		nivel.revision(nivel.protagonista,nivel.malo7)
		nivel.revision(nivel.protagonista,nivel.malo8)

	pilas.eventos.actualizar.conectar(colision_con_vision)


