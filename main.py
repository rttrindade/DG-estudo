import random

CordX = 0
CordY = 0
local = [CordX, CordY]

def OndeEstou(Cord, passos):
    print("Você esta em: "+ str(Cord[0])+ ", "+ str(Cord[1])+ "\nAinda resta: "+ str(passos)+ " passo(s)")

def validaEntrada(entrada):
    total = 5
    entrada = total - entrada
    if entrada == 4:
        return 1
    if entrada == 3:
        return 0
    if entrada == 2:
        return 3
    if entrada == 1:
        return 2

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
        global local
        if direc == '1' and self.caminhos[0]:
            local[1] += 1
            print("Você foi pro Norte")
            return 1
        elif direc == '2' and self.caminhos[1]:
            local[1] -= 1
            print("Você foi pro Sul")
            return 2
        elif direc == '3' and self.caminhos[2]:
            local[0] += 1
            print("Você foi pro Leste")
            return 3
        elif direc == '4' and self.caminhos[3]:
            local[0] -= 1
            print("Você foi pro Oeste")
            return 4
        else:
            print("Caminho bloqueado, deve haver outra saida.")
            return -1



class JOGADOR():
    def __init__(self):
        self.trajeto = []
        self.ultimoMov =1

    def setUltimoMov(self, movimento):
        self.ultimoMov = movimento

    def getUltimoMov(self):
        return self.ultimoMov

##############################################################################################################

jogador = JOGADOR()
passos = 5
while passos > 0:
    sala1 = SALA(local, Saidas(validaEntrada(jogador.getUltimoMov())))
    OndeEstou(local,passos)
    moveu = False
    while moveu != True:
        jogador.setUltimoMov(sala1.JogadorEscolhe(sala1.MostraOpc(sala1.caminhos)))
        if jogador.getUltimoMov() != -1:
            passos -= 1
            moveu = True


print("GAME OVER")

#print(sala1.MostraOpc(sala1.caminhos))