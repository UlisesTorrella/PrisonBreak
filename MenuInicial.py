#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pilas
from pilas.comportamientos import Avanzar
import Policia
from Policia import BasePersonajeRPG
from nivel1 import Lvl1


pilas.iniciar()



nivel=Lvl1()

def detectado():
	print "perdiste"

def colision_con_vision(self):
	nivel.revision(nivel.protagonista,nivel.malo1)
	nivel.revision(nivel.protagonista,nivel.malo2)
	nivel.revision(nivel.protagonista,nivel.malo3)
	nivel.revision(nivel.protagonista,nivel.malo4)
	nivel.revision(nivel.protagonista,nivel.malo5)
	nivel.revision(nivel.protagonista,nivel.malo6)
	nivel.revision(nivel.protagonista,nivel.malo7)
	nivel.revision(nivel.protagonista,nivel.malo8)


pilas.eventos.actualizar.conectar(colision_con_vision)

pilas.ejecutar()