class ImprovedBubble:
  def sort(self, elementos):
    n = len(elementos)
    trocas = 0  # Contador de trocas
    comparacoes = 0  # Contador de comparações

    for i in range(n):
        troca = False
        for j in range(n - 1 - i):
            comparacoes += 1  # Incrementa o número de comparações
            if elementos[j] > elementos[j + 1]:
                elementos[j], elementos[j + 1] = elementos[j + 1], elementos[j]
                trocas += 1  # Incrementa o número de trocas
                troca = True
        if not troca:
            break

    return elementos, trocas, comparacoes