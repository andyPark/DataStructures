from heapq import heappush, heappop, heapify

def selection_sort(arr):
    for i in range(len(arr)):
        min_value = float('inf')
        min_i = len(arr)
        for j in range(i, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_i = j
        swap(arr, i, min_i)
    return arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def heap_sort(arr):
    h = []
    for v in arr:
        heappush(h, v)
    return [heappop(h) for i in range(len(h))]

# Helper Methods (not exported)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 
    return result

__all__ = ['merge_sort', 'selection_sort', 'heap_sort']