# Sort array containing 0,1,2s in linear time

def sort_arr(arr):
    n = len(arr)
    start = 0
    cur = 0
    end = n-1

    def swap(index1, index2):
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp

    while cur <= end:
        if arr[cur] == 0:
            swap(cur, start)
            start = start + 1
            cur = cur + 1
        elif arr[cur] == 1:
            cur = cur + 1
        else:
            swap(cur, end)
            end = end - 1
    return arr


# Sample
print sort_arr([2, 0, 1, 2, 2, 1, 1, 0, 1, 0, 0, 1, 1, 2, 2, 1, 2, 0, 2])
print sort_arr([1, 2, 0, 1, 2, 1, 0])
print sort_arr([0, 2, 1, 1, 0, 2])
