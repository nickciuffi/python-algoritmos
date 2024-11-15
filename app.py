import random
import time
from classes import Bubble, ImprovedBubble, Comb, Heap

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
  
def lerArquivo(nomeArquivo):
  numeros = []
  with open(nomeArquivo, "r") as arquivo:
    for linha in arquivo:
      numeros.append(int(linha.strip()))
  return numeros

#Aqui voce escolhe qual arquivo vai ser lido
nums = lerArquivo("numeros-melhor-10k.txt")
  
#aqui voce escolhe qual classe vai ser executada
rodaAlgoritmo(nums, Bubble())

