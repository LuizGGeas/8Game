# -*- coding: utf-8 -*-
from tabuleiro import Tabuleiro as tab


class rodar:
	abertos = []
	fechados = []

	def contem(self):
		for i in self.abertos:
			if i.final():
				return i
		return False

	def starter(self, inicial):
		self.abertos.append(inicial)
		b = self.contem()
		while b == False:
			print('tamanho do vetor: '.format(len(self.abertos)))
			x = self.min()
			self.abertos.remove(x)
			novos = x.movimentos()
			novos = [x for x in novos if not self.alreadyIn(x)]
			self.abertos.append(novos)
			b = self.contem()
		else:
			print('final alcançado')
			b.printar()
			while(b.pai != None):
				b.printar()
				print(b.distancia)
				b = b.pai

	def alreadyIn(self, value):
		return value in self.abertos

	def min(self):
		x = self.abertos[0]
		for i in self.abertos:
			if i.distancia < x.distancia:
				x = i
		return x


a = tab(dificuldade=3, tipo=2)
a.printar()
rodar().starter(a)
