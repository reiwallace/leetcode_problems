def sort(arr):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(1, len(arr)):
            if ord(str(arr[i])) < ord(str(arr[i - 1])):
                current = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = current
                swaps += 1
        
    return arr