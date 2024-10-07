import math 
import random

def geraVetorFaturamento():
    vetorFaturamento = []

    for _ in range(365):
        vetorFaturamento.append(random.randint(0,6))

    return vetorFaturamento

def calculaMediaAnual(vetorFaturamentoDiario:list[float]) -> float:
    soma = 0
    diasUteis = 0

    for faturamento in vetorFaturamentoDiario:
        if(faturamento == 0):
            continue

        soma += faturamento
        diasUteis += 1

    return soma / diasUteis

def calculaValoresFaturamento(vetorFaturamentoDiario:list[float]):
    menorValor = math.inf
    maiorValor = 0
    mediaAnual = calculaMediaAnual(vetorFaturamentoDiario)
    numeroSuperiorMedia = 0

    for faturamento in vetorFaturamentoDiario:
        if(faturamento < menorValor and faturamento != 0):
            menorValor = faturamento
        
        if(faturamento > maiorValor):
            maiorValor = faturamento

        if(faturamento > mediaAnual):
            numeroSuperiorMedia += 1

    return menorValor, maiorValor, numeroSuperiorMedia


vetorFaturamento = geraVetorFaturamento()
print(calculaValoresFaturamento(vetorFaturamento))
