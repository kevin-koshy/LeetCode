def partition(arr, l, h):
    def swap(a, b):
        return b, a

    pivot = arr[l]
    i, j = l, h

    while i < j:
        while True:
            i += 1
            if arr[i] <= pivot:
                break

    while True:
        j -= 1
        if arr[j] > pivot:
            break

    if i < j:
        swap(arr[i], arr[j])

    swap(arr[l], arr[j])
    return j

def quick_sort(arr,l,h):
    if l < h:
        j = partition(arr, l, h)
        quick_sort(arr, l, j)
        quick_sort(arr, j+1, h)

arr1 = [1,3,7,123,23,4,0]
arr1.append(999999999)
quick_sort(arr1, arr1[0],arr1[-1])