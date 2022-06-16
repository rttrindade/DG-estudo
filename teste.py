import random

def Saidas(entrada=1):
    saidas = []
    while len(saidas) <= 3:
        saidas.append(not not(random.randint(0,1)))
    saidas[entrada] = True
    print(saidas)
    return saidas

def MostraOpc(saidas):
    texto = "Pra onde deseja ir?\n"
    if saidas[0]:
        texto += "1 - Norte\n"
    if saidas[1]:
        texto += "2 - Sul \n"
    if saidas[2]:
        texto += "3 - Leste \n"
    if saidas[3]:
        texto += "4 - Oeste \n"
    print(texto)


MostraOpc(Saidas())