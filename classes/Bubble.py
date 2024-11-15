class Bubble:
  def sort(self, elementos):
    
    n = len(elementos)
    quantidade_trocas = 0
    quantidade_comparacoes = 0


    # O loop externo percorre todos os elementos sem otimização
    for _ in range(n):
        troca = False  # Para verificar se houve trocas nesta passagem
        for i in range(n - 1):
            quantidade_comparacoes += 1
            if elementos[i] > elementos[i + 1]:
                # Removendo o print de troca para melhorar o desempenho
                elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i]
                troca = True
                quantidade_trocas += 1

    return elementos, quantidade_trocas, quantidade_comparacoes 