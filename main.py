# -*- coding: utf-8 -*-
from tabuleiro import Tabuleiro as tab

a = tab(dificuldade=3, heuristica=2)
a.printar()

abertos = list()
fechados = list()

abertos.append(a)
b = a
while(b.getDistancia() > 0):
	print(type(abertos[0]))
	abertos.sort(key=lambda x : x.distancia)
	b = abertos[0]
	x = b.movimentos()
	x = [x for x in abertos if x not in abertos or x not in fechados] if abertos[0].getDistancia > 0 else []
	fechados.append(abertos.pop(0))
	abertos.append(x)
else:
	while b != None:
		b.printar()
		print(b.getDistancia())
		b = b.pai