import random

class Tabuleiro:
    tabuleiro = []
    starter = [[1,2,3],[8,'.',4],[7,6,5]]
    distancia = 0
    def __init__(self, pai = None, dificuldade = 0):
        if pai:
            self.tabuleiro = pai.tabuleiro[:]
        elif dificuldade != 0:
            self.tabuleiro = self.starter
            i = 0
            if dificuldade == 1:
                i = 20
            elif dificuldade == 2:
                i = 50
            elif dificuldade == 3:
                i = 100
            while i > 0:
                i-=1
                a = random.randint(0,3)
                if a == 0 and self.findDot()[0] != 2:
                    self.direita()
                elif a == 1 and self.findDot()[0] != 0:
                    self.esquerda()
                elif a == 2 and self.findDot()[1] != 0:
                    self.cima()
                elif a == 3 and self.findDot()[1] != 2:
                    self.baixo()
                else: 
                    i+=1
        self.Distancia()
    
    def __eq__(self, value):
        return self.distancia.__eq__(value.distancia)

    def direita(self):
        i, j = self.findDot()[0], self.findDot()[1]
        if not j == 2:
            novo = Tabuleiro(pai = self)
            aux = novo.tabuleiro[i][j+1]
            novo.tabuleiro[i][j+1] = novo.tabuleiro[i][j]
            novo.tabuleiro[i][j] = aux
            return novo
        else: 
            return None
        
    def esquerda(self):
        i, j = self.findDot()[0], self.findDot()[1]
        if not i == 0:
            novo = Tabuleiro(pai = self)
            aux = self.tabuleiro[i][j-1]
            self.tabuleiro[i][j-1] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux
            return novo
        else: 
            return None

    def cima(self):
        i, j = self.findDot()[0], self.findDot()[1]
        if i == 0:
            novo = Tabuleiro(pai = self)
            aux = self.tabuleiro[i-1][j]
            self.tabuleiro[i-1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux  
            return novo  
        else: 
            return None

    def baixo(self):
        i, j = self.findDot()[0], self.findDot()[1]
        if not i == 2:
            novo = Tabuleiro(pai = self)
            aux = self.tabuleiro[i+1][j]
            self.tabuleiro[i+1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = aux
            return novo
        else: 
            return None

    def findDot(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '.':
                    return [i,j]

    def Distancia(self):
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

    def printar(self):
        for i in self.tabuleiro:
            print(i)

    def sorter(self):
        return self.distancia