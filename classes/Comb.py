class Comb:
  def sort(self, arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False
    trocas = 0
    comparacoes = 0

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(arr) - gap):
            comparacoes += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                trocas += 1
                sorted = False

    return arr, trocas, comparacoes