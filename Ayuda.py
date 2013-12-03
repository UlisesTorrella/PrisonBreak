#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas



class EscenaAyuda(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        self.texto1 = pilas.actores.Texto("Ayuda a Michael a escapar de Fox River",y = 200)
        self.texto2 = pilas.actores.Texto("Los guardias te veran si entras en su rango de vicion",y = 150)
        self.texto3 = pilas.actores.Texto("Mapa:",x = -200,y = 50)
        self.texto4 = pilas.actores.Texto("Si pasas por delante de un guardia te vera,",y = -120)
        self.texto5 = pilas.actores.Texto("intenta pasar por detras",y = -160)

        self.musica = pilas.sonidos.cargar("MusicaMenu.mp3")
        self.musica.reproducir()
        pilas.fondos.Fondo("FondoPB2.jpg")
        mapaImagen = "MiniMapa.png"

        menu = pilas.actores.Menu([('Volver',self.volver)],y=-220)

        mapa = pilas.actores.Actor(mapaImagen)

    def volver(self):
        from MenuInicial import EscenaDeMenu
        self.musica.detener()
        pilas.cambiar_escena(EscenaDeMenu())
