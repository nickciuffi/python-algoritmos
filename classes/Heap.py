class Heap:
  def sort(self, arr):
    n = len(arr)
    metrics = {'comparacoes': 0, 'trocas': 0}

    for i in range(n // 2 - 1, -1, -1):
        self.heapify(arr, n, i, metrics)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        metrics['trocas'] += 1
        self.heapify(arr, i, 0, metrics)

    return arr, metrics['trocas'], metrics['comparacoes']
  
  def heapify(self, arr, n, i, metrics):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n:
        metrics['comparacoes'] += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        metrics['comparacoes'] += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        metrics['trocas'] += 1
        self.heapify(arr, n, largest, metrics)