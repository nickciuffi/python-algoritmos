class Bubble:
    def sort(self, elementos):
        n = len(elementos)
        quantidade_trocas = 0
        quantidade_comparacoes = 0

        for j in range(n):  # Loop externo percorre todas as iterações
            for i in range(n - 1 - j):  # Reduz o número de comparações a cada iteração
                quantidade_comparacoes += 1
                if elementos[i] > elementos[i + 1]:
                    elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i]
                    quantidade_trocas += 1

        return elementos, quantidade_trocas, quantidade_comparacoes
