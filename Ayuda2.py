#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pilas



class EscenaAyuda2(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        self.texto1 = pilas.actores.Texto("Esta es la vision de un policia",y = 200)
        self.texto2 = pilas.actores.Texto("te veran si entras en su campo de vision",y = 150)
        self.texto3 = pilas.actores.Texto("Mapa:",x = -200,y = 50)
        self.texto4 = pilas.actores.Texto("intenta pasar por detras",y = -100)

        color = pilas.colores.gris
        self.texto1.definir_color(color);
        self.texto2.definir_color(color);
        self.texto3.definir_color(color);
        self.texto4.definir_color(color);        


        self.musica = pilas.sonidos.cargar("MusicaMenu.mp3")
        self.musica.reproducir()
        pilas.fondos.Fondo("FondoPB2.jpg")
        mapaImagen = "RangoVision.png"

        menu = pilas.actores.Menu([('Mas ayuda',self.masAyuda),('Volver',self.volver)],y=-150)

        mapa = pilas.actores.Actor(mapaImagen)

    def masAyuda(self):
        from Ayuda3 import EscenaAyuda3
        self.musica.detener()
        pilas.cambiar_escena(EscenaAyuda3())

    def volver(self):
        from MenuInicial import EscenaDeMenu
        self.musica.detener()
        pilas.cambiar_escena(EscenaDeMenu())
