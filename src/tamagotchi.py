class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax
        self.idadeAtual = 0
        self.diamantes = 0

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energiaAtual > 0 and self.saciedadeAtual > 0 and self.limpezaAtual > 0:
            return True

        elif self.idadeAtual > self.idadeMax:
            self.idadeAtual = self.idadeMax
            return False

        else:
            if self.energiaAtual <= 0:
                self.energiaAtual = 0
                return False
            if self.saciedadeAtual <= 0:
                self.saciedadeAtual = 0
                return False
            if self.limpezaAtual <= 0:
                self.limpezaAtual = 0
                return False

    def brincar(self):
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeMax():
                self.idadeAtual += 1
                self.energiaAtual -= 2
                self.saciedadeAtual -= 1
                self.limpezaAtual -= 3
                self.diamantes += 1
                return True
            else:
                self.energiaAtual -= 2
                self.saciedadeAtual -= 1
                self.limpezaAtual -= 3
                self.diamantes += 1
                return True
        else:
            return False

    def comer(self):
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeMax():
                self.idadeAtual += 1
                self.energiaAtual -= 1
                self.saciedadeAtual += 4
                self.limpezaAtual -= 2
                self.diamantes += 0
                return True
            else:
                self.energiaAtual -= 1
                self.saciedadeAtual += 4
                self.limpezaAtual -= 2
                self.diamantes += 0
                return True
        else:
            return False


    def dormir(self):
        if self.getEstaVivo() == True and self.getEnergiaMax() - self.getEnergiaAtual() >= 5:
            if self.getIdadeAtual() + (self.energiaMax - self.energiaAtual) <= self.getIdadeMax():
                self.idadeAtual += (self.energiaMax - self.energiaAtual)
                self.energiaAtual = self.getEnergiaMax()
                self.saciedadeAtual -= 2
                return True

            else:
                self.energiaAtual = self.getEnergiaMax()
                self.saciedadeAtual -= 2
                return True
        else:
            return False

    def banhar(self):
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 2 <= self.getIdadeMax():
                self.idadeAtual += 2
                self.energiaAtual -= 3
                self.saciedadeAtual -= 1
                self.limpezaAtual = self.getLimpezaMax()
                self.diamantes += 0
                return True

            else:
                self.energiaAtual -= 3
                self.saciedadeAtual -= 1
                self.limpezaAtual = self.getLimpezaMax()
                self.diamantes += 0
                return True
        else:
            return False