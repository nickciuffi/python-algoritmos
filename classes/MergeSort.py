class MergeSort:
    def sort(self, elementos):
        # Define os contadores de trocas e comparações como atributos da classe
        self.quantidade_comparacoes = 0
        self.quantidade_trocas = 0
        return self._merge_sort(elementos), self.quantidade_trocas, self.quantidade_comparacoes

    def _merge_sort(self, elementos):
        if len(elementos) > 1:
            meio = len(elementos) // 2

            # Divisão em duas metades
            esquerda = elementos[:meio]
            direita = elementos[meio:]

            # Chamada recursiva nas duas metades
            self._merge_sort(esquerda)
            self._merge_sort(direita)

            # Merge das duas metades ordenadas
            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                self.quantidade_comparacoes += 1
                if esquerda[i] < direita[j]:
                    elementos[k] = esquerda[i]
                    i += 1
                else:
                    elementos[k] = direita[j]
                    j += 1
                k += 1
                self.quantidade_trocas += 1

            # Adiciona os elementos restantes da esquerda
            while i < len(esquerda):
                elementos[k] = esquerda[i]
                i += 1
                k += 1
                self.quantidade_trocas += 1

            # Adiciona os elementos restantes da direita
            while j < len(direita):
                elementos[k] = direita[j]
                j += 1
                k += 1
                self.quantidade_trocas += 1

        return elementos
