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
            d = [False, False, False, False]
            x = min(self.abertos)
            a = self.abertos.remove(x)
            for i in self.abertos:
                if i.tabuleiro == a.direita.tabuleiro:
                    d[0] = True
                if i.tabuleiro == a.esquerda.tabuleiro:
                    d[1] = True
                if i.tabuleiro == a.cima.tabuleiro:
                    d[2] = True
                if i.tabuleiro == a.baixo.tabuleiro:
                    d[3] = True

            if a.direita() != None and d[0]:
                self.abertos.append(a.direita)
            if a.esquerda() != None  and d[1]:
                self.abertos.append(a.esquerda)
            if a.cima() != None and d[2]:
                self.abertos.append(a.cima)
            if a.baixo() != None and d[3]:
                self.abertos.append(a.baixo())
            b = self.contem()
        else:
            print('final alcançado')
            while(a != None):
                a.printar()
                a = a.pai


a = tab(dificuldade= 2)

rodar().starter(a)