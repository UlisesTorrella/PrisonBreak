#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from pilas.comportamientos import Avanzar
import Policia

pilas.iniciar()

mapa = pilas.actores.MapaTiled("Obstaculos.tmx")

malo = Policia.Policias(mapa,-250,-1260)
malo2 = Policia.Policias(mapa, -223, -1260,"derecha",500)
#malo2.hacer(Avanzar(20,2))



pitbull=pilas.actores.Calvo(mapa)
pitbull.aprender(pilas.habilidades.SiempreEnElCentro)
pitbull.x = 84
pitbull.y = -1340



pilas.ejecutar()