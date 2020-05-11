# coding= UTF-8
from tabuleiro import Tabuleiro as tab
from operator import attrgetter

class rodar:
    abertos = []
    fechados = []
    def contem(self):
        for i in self.abertos:
            if i.tabuleiro == i.starter:
                return i
        return False

    def starter(self, inicial):
        self.abertos.append(inicial)
        b = self.contem()
        while b:
            x = min(self.abertos)
            a = self.abertos.remove(x)
            if a.direita() != None and a.direita not in self.abertos:
                self.abertos.append(a.direita)
            if a.esquerda() != None  and a.esquerda not in self.abertos:
                self.abertos.append(a.esquerda)
            if a.cima() != None and a.cima not in self.abertos:
                self.abertos.append(a.cima)
            if a.baixo() != None and a.baixo() not in self.abertos:
                self.abertos.append(a.baixo())
        else:
            print('final alcançado')
            while(a != None):
                a.printar()
                a = a.pai


a = tab(dificuldade= 2)

rodar().starter(a)