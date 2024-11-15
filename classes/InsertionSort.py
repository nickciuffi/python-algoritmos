class insertion_Sort:
    def sort(self, elementos):
        quantidade_trocas = 0
        quantidade_comparacoes = 0
        n = len(elementos)

        for i in range(1, n):
            chave = elementos[i]
            j = i - 1

            while j >= 0 and elementos[j] > chave:
                quantidade_comparacoes += 1  # Comparação dentro do loop while
                elementos[j + 1] = elementos[j]
                j -= 1
                quantidade_trocas += 1  # Cada deslocamento conta como uma troca

            elementos[j + 1] = chave  # Reposiciona a chave na posição correta

            if j >= 0:
                quantidade_comparacoes += 1  # Comparação fora do while

        return elementos, quantidade_trocas, quantidade_comparacoes