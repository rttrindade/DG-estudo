import random

CordX = 0
CordY = 0
local = [CordX, CordY]

def OndeEstou(Cord):
    print("Você esta em:", Cord[0], ",", Cord[1])

def Saidas(entrada=1):
    saidas = []
    while len(saidas) <= 3:
        saidas.append(not not (random.randint(0, 1)))
    saidas[entrada] = True
    return saidas


class SALA():
    def __init__(self, local, caminhos):
        self.cordenada = local
        self.caminhos = caminhos
     #   self.MostraOpc()
     #   self.JogadorEscolhe()

    def MostraOpc(self,saidas):
        texto = "Pra onde deseja ir?\n"
        if saidas[0]:
            texto += "1 - Norte\n"
        if saidas[1]:
            texto += "2 - Sul \n"
        if saidas[2]:
            texto += "3 - Leste \n"
        if saidas[3]:
            texto += "4 - Oeste \n"
        return texto

    def JogadorEscolhe(self,texto):
        direc = input(texto)
        if direc == '1':
            print("Você foi pro Norte")
        elif direc == '2':
            print("Você foi pro Sul")
        elif direc == '3':
            print("Você foi pro Leste")
        elif direc == '4':
            print("Você foi pro Oeste")




sala1 = SALA([0,0],Saidas())
print(sala1.caminhos)
sala1.JogadorEscolhe(sala1.MostraOpc(sala1.caminhos))
#print(sala1.MostraOpc(sala1.caminhos))