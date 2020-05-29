# -*- coding: utf-8 -*-
from tabuleiro import Tabuleiro as tab


class rodar:
	abertos = []
	fechados = []

	def starter(self, inicial):
		self.abertos.append(inicial)
		b = inicial
		while b.distancia > 0:
			print('{} caminhos por verificar'.format(len(self.abertos)))
			print('{} caminhos verificados até o momento'.format(len(self.fechados)))
			print('tamanho do vetor: '.format(len(self.abertos)))
			b = self.min()
			self.fechados.append(self.abertos.remove(b))
			novos = b.movimentos() if b.distancia > 0 else []
			novos = [x for x in novos if not x in self.abertos]
			self.abertos.append(novos)
		else:
			print('final alcançado')
			for i in self.abertos:
				if i.final():
					b = i
					break

			while(b != None):
				b.printar()
				print("{} caminhos foram verificados".format(len(self.fechados)))
				b = b.pai

	def min(self):
		x = self.abertos[0]
		for i in self.abertos:
			if i.distancia < x.distancia:
				x = i
		return x


a = tab(dificuldade=3, heuristica=2)
a.printar()
rodar().starter(a)
