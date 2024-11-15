class SelectionSort:
    def sort(self, elementos):
        quantidade_trocas = 0
        quantidade_comparacoes = 0
        n = len(elementos)

        for i in range(n):
            # Encontre o índice do menor elemento no restante da lista
            indice_minimo = i
            for j in range(i + 1, n):
                quantidade_comparacoes += 1
                if elementos[j] < elementos[indice_minimo]:
                    indice_minimo = j

            # Troca o elemento atual com o menor encontrado
            if indice_minimo != i:
                elementos[i], elementos[indice_minimo] = elementos[indice_minimo], elementos[i]
                quantidade_trocas += 1

        return elementos, quantidade_trocas, quantidade_comparacoes