class QuickSort:
    def sort(self, arr):
        return self.quick_sort(arr)

    def quick_sort(self, arr, contagem_comparacoes=0, contagem_trocas=0):
        if len(arr) <= 1:
            return arr, contagem_comparacoes, contagem_trocas
        else:
            pivot = arr[len(arr) // 2]
            left = []
            right = []
            middle = []

            for x in arr:
                contagem_comparacoes += 1
                if x < pivot:
                    left.append(x)
                    contagem_trocas += 1  # considerar como troca ao mover para uma nova lista
                elif x == pivot:
                    middle.append(x)
                else:
                    right.append(x)
                    contagem_trocas += 1  # mesma ideia para mover à lista da direita

            # Chamadas recursivas para as sublistas esquerda e direita
            sorted_left, comp_left, troca_left = self.quick_sort(left, contagem_comparacoes, contagem_trocas)
            sorted_right, comp_right, troca_right = self.quick_sort(right, contagem_comparacoes, contagem_trocas)

            # Soma os resultados das contagens de comparações e trocas
            total_comparacoes = comp_left + comp_right
            total_trocas = troca_left + troca_right

            return sorted_left + middle + sorted_right, total_comparacoes, total_trocas
