#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
import Policia

pilas.iniciar()

mapa = pilas.actores.MapaTiled("Obstaculos.tmx")

malo = Policia.Policias(mapa,-250,-1260)




pitbull=pilas.actores.Calvo(mapa)
pitbull.aprender(pilas.habilidades.SiempreEnElCentro)
pitbull.x = 84
pitbull.y = -1340



pilas.ejecutar()