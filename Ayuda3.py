#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pilas



class EscenaAyuda3(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        self.texto1 = pilas.actores.Texto("Abajo a tu derecha tienes tu Sigilo",y = 200)
        self.texto2 = pilas.actores.Texto("Si un guardia te ve reportara actividad sospechosa,",y = 150)
        self.texto4 = pilas.actores.Texto("Y los otros guardias estaran mas atentos",y = -130)

        color = pilas.colores.gris
        self.texto1.definir_color(color);
        self.texto2.definir_color(color);
        self.texto4.definir_color(color);        
 

        self.musica = pilas.sonidos.cargar("MusicaMenu.ogg")
        self.musica.reproducir(repetir=True)
        pilas.fondos.Fondo("FondoPB2.jpg")
        mapaImagen = "ayudaSigilo.png"

        menu = pilas.actores.Menu([('Volver al menu principal',self.volver)],y=-200)

        mapa = pilas.actores.Actor(mapaImagen)

    def volver(self):
        from MenuInicial import EscenaDeMenu
        self.musica.detener()
        pilas.cambiar_escena(EscenaDeMenu())
