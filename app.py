import random
import time
from classes import Bubble

def rodaAlgoritmo(nums, algo):
  

  inicio = time.time()

  elementos_ordenados, trocas, comparacoes = algo.sort(nums)

  fim = time.time()
  tempo_execucao = fim - inicio

  # Calcula o tempo em minutos e segundos
  tempo_minutos = tempo_execucao // 60
  tempo_segundos = tempo_execucao % 60

  print(f"Tempo de Execução: {tempo_execucao} segundos")
  print(f"Tempo de Execução: {int(tempo_minutos)} minutos e {tempo_segundos:.2f} segundos")
  print(f"Quantidade de Trocas: {trocas}")
  print(f"Quantidade de Comparações: {comparacoes}")
  #print("Primeiros elementos ordenados:", elementos_ordenados[:100])


with open("numeros-melhor-1k.txt", "r") as arquivo:
  numeros = [int(linha.strip()) for linha in arquivo]
  
rodaAlgoritmo(numeros, Bubble())
  
