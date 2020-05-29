import random


class Tabuleiro:
    tabuleiro = []
    meta = [[1, 2, 3], [8, '.', 4], [7, 6, 5]]
    distancia = 0
    pai = None
    heuristica = 1

    def __init__(self, pai=None, dificuldade=0, heuristica=1):
        self.pai = pai
        self.heuristica = heuristica
        if pai:
            self.tabuleiro = pai.tabuleiro[:]
        elif dificuldade != 0:
			self.aleatorizar(dificuldade)
        if heuristica == 1:
            print('tentou1')
            self.Distancia_Manhattan()
        else:
            print('tentou2')
            self.Fora_Lugar()
        print('chega de aleatorizar')

    def aleatorizar(self, dificuldade):
        print('aleatorizando')
        z = -1
        self.tabuleiro = self.meta
        i = 0
        round = 100
        if dificuldade == 1:
			i = 20
        elif dificuldade == 2:
        	i = 50
        elif dificuldade == 3:
        	i = 100
        while i > 0 and self.tabuleiro == self.meta and round > 0:
            round -= 1
            i -= 1
            a = random.randint(1, 4)
            i, j = self.findDot()
            if abs(z-a) == 1 or z == a:
            	i += 1
            elif a == 1 and self.findDot()[0] != 2:
            	print('direita')
                self.direita(i, j)
                z = a
            elif a == 2 and self.findDot()[0] != 0:
            	print('esquerda')
                self.esquerda(i, j)
                z = a
            elif a == 3 and self.findDot()[1] != 0:
            	print('cima')
                self.cima(i, j)
                z = a
            elif a == 4 and self.findDot()[1] != 2:
            	print('baixo')
                self.baixo(i, j)
                z = a


    def movimentos(self):
        print('vendo movimentos')
        i, j = self.findDot()
        a = []
        if i == 2:
            if j == 2:
                a.append(self.cima)
                a.append(self.esquerda)
            elif j == 0:
                a.append(self.cima)
                a.append(self.direita)
            else:
                a.append(self.cima)
                a.append(self.direita)
                a.append(self.esquerda)
        elif i == 0:
            if j == 2:
                a.append(self.baixo)
                a.append(self.esquerda)
            elif j == 0:
                a.append(self.baixo)
                a.append(self.direita)
            else:
                a.append(self.baixo)
                a.append(self.direita)
                a.append(self.esquerda)
        else:
            if j == 2:
                a.append(self.baixo)
                a.append(self.esquerda)
                a.append(self.cima)
            elif j == 0:
                a.append(self.baixo)
                a.append(self.direita)
                a.append(self.direita)
            else:
                a.append(self.baixo)
                a.append(self.direita)
                a.append(self.esquerda)
                a.append(self.cima)
        return a

    def direita(self, i, j):
        print('ponto para direita')
        if not j == 2:
            novo = Tabuleiro(pai=self, heuristica=self.heuristica)
            aux = novo.tabuleiro[i][j+1]
            novo.tabuleiro[i][j+1] = novo.tabuleiro[i][j]
            novo.tabuleiro[i][j] = aux
            return novo

    def esquerda(self, i, j):
        print('ponto para esquerda')
        if not j == 0:
            novo = Tabuleiro(pai=self, heuristica=self.heuristica)
            aux = self.tabuleiro[i][j-1]
            self.tabuleiro[i][j-1] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux
            return novo

    def cima(self, i, j):
        print('subiu ponto')
        if not i == 0:
            novo = Tabuleiro(pai=self, heuristica=self.heuristica)
            aux = self.tabuleiro[i-1][j]
            self.tabuleiro[i-1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux
            return novo

    def baixo(self, i, j):
        print('baixou ponto')
        if not i == 2:
            novo = Tabuleiro(pai=self, heuristica=self.heuristica)
            aux = self.tabuleiro[i+1][j]
            self.tabuleiro[i+1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux
            return novo

    def findDot(self):
        print("find DOT")
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '.':
                    return [i, j]

    def Distancia_Manhattan(self):
        print("vendo distancia")
        for i in range(3):
            for j in range(3):
                if self.starter[i][j] != self.tabuleiro[i][j]:
                    k = 0
                    l = 0
                    for k in range(3):
                        for l in range(3):
                            if self.tabuleiro[i][j] == self.starter[k][l]:
                                break
                    self.distancia += abs((i-k)) + abs((j-l))

    def Fora_Lugar(self):
        for i in range(3):
            for j in range(3):
                if(self.meta[i][j] != self.tabuleiro[i][j]):
                    self.distancia += 1

    def printar(self):
        for i in self.tabuleiro:
            print(i)
        print("")

    def final(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != self.meta[i][j]:
                    return False
        return True
