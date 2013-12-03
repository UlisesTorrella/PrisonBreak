#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from pilas.comportamientos import Avanzar
import Policia
from Policia import BasePersonajeRPG
from nivel import Nivel

class Nivel1(Nivel):
	
	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):



		mapa = pilas.actores.MapaTiled("Obstaculos.tmx")

		self.malo1 = Policia.Policias(mapa,658,-2272,"derecha",rango=500,anchoVision=100,largoVision=300)		
		self.malo2 = Policia.Policias(mapa,1258,-2147,"izquierda",rango=400,anchoVision=100,largoVision=300)
		self.malo3 = Policia.Policias(mapa,664,-1696,"derecha",rango=400,anchoVision=100,largoVision=300)
		self.malo4 = Policia.Policias(mapa,1085,-1638,"izquierda",rango=400,anchoVision=100,largoVision=300)
		self.malo5 = Policia.Policias(mapa,1620,-2300,"arriba",rango=600,anchoVision=300,largoVision=100)
		self.malo6 = Policia.Policias(mapa,1818,-2200,"derecha",rango=200,anchoVision=100,largoVision=100)
		self.malo7 = Policia.Policias(mapa,1930,-1278,"derecha",rango=100,anchoVision=100,largoVision=100)
		self.malo8 = Policia.Policias(mapa,1887,-1243,"derecha",rango=140,anchoVision=100,largoVision=100)
		self.malo9 = Policia.Policias(mapa,1750,-810,"abajo",rango=400,anchoVision=200,largoVision=150)
		self.malo10 = Policia.Policias(mapa,1480,-810,"abajo",rango=400,anchoVision=200,largoVision=150)
		self.malo11 = Policia.Policias(mapa,1140,-1080,"derecha",rango=300,anchoVision=100,largoVision=300)
		self.malo12 = Policia.Policias(mapa,1310,-810,"abajo",rango=200,anchoVision=200,largoVision=150)
		self.malo13 = Policia.Policias(mapa,630,-810,"abajo",rango=400,anchoVision=300,largoVision=150)
		self.malo14 = Policia.Policias(mapa,710,-1300,"arriba",rango=400,anchoVision=300,largoVision=150)


		self.protagonista=pilas.actores.Calvo(mapa,1)
		self.protagonista.aprender(pilas.habilidades.SiempreEnElCentro)
		self.protagonista.x = 1040
		self.protagonista.y = -2371


		puerta = "puerta.jpg"
		self.salida=pilas.actores.Actor(puerta)
		self.salida.x=673
		self.salida.y=-777


		imagen = "ropa.png"
		self.ropa=pilas.actores.Actor(imagen,x=927,y=-810)

		self.puntodecontrol = False
		self.visible=True


		pilas.escena_actual().colisiones.agregar(self.protagonista, self.ropa, self.cambiar_ropa)
		pilas.escena_actual().colisiones.agregar(self.protagonista, self.salida, self.ganar)
		pilas.eventos.actualizar.conectar(self.colision_con_vision)

		self.musica = pilas.sonidos.cargar("MusicaJuego.mp3")
		self.musica.reproducir()

	def ganar(self,protagonista,salida):

		from MenuGanaste import EscenaGanaste
		self.musica.detener()

		pilas.cambiar_escena(EscenaGanaste())


	def revision(self, protagonista, malo):
		if self.visible==True:
			if protagonista.x < malo.rectangulo.x+malo.largoVision/2 and protagonista.x > malo.rectangulo.x-malo.largoVision/2:
				if protagonista.y < malo.rectangulo.y + malo.anchoVision/2 and protagonista.y > malo.rectangulo.y - malo.anchoVision/2:
						self.musica.detener()
						self.detectado()

			if self.puntodecontrol == False:
				if protagonista.x > 1650:
					if protagonista.y < -2270:
						pilas.avisar("Busca un uniforme de policia para salir sin ser detectado")
						self.puntodecontrol = True


	def colision_con_vision(self,actor):
		self.revision(self.protagonista,self.malo1)
		self.revision(self.protagonista,self.malo2)
		self.revision(self.protagonista,self.malo3)
		self.revision(self.protagonista,self.malo4)
		self.revision(self.protagonista,self.malo5)
		self.revision(self.protagonista,self.malo6)
		self.revision(self.protagonista,self.malo7)
		self.revision(self.protagonista,self.malo8)
		self.revision(self.protagonista,self.malo9)
		self.revision(self.protagonista,self.malo10)
		self.revision(self.protagonista,self.malo11)
		self.revision(self.protagonista,self.malo12)
		self.revision(self.protagonista,self.malo13)
		self.revision(self.protagonista,self.malo14)
