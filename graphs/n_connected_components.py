# find the number of islands - a group of connected ones forms an island

def dfs(arr, i, j, visited):
    n_rows, n_cols = arr.shape
    visited[i, j] = True
    for (x, y) in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if (0 <= x < n_rows) and (0 <= y < n_cols):
            if arr[x, y] == 1 and not visited[x, y]:
                dfs(arr, x, y, visited)


def count_connected_components(arr):
    n_rows, n_cols = arr.shape
    visited = np.zeros(arr.shape).astype(np.bool)
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if arr[i,j] == 0:
                continue
            else:
                if visited[i, j]:
                    continue
                else:
                    count = count + 1
                    dfs(arr, i, j, visited)
    return count


# sample input
import numpy as np
arr1 = np.array([
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1]
])

arr2 = np.array([
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 1],
[0, 1, 0, 0, 0],
[1, 0, 1, 0, 1]
])

print count_connected_components(arr1) # 5
print count_connected_components(arr2) # 2
