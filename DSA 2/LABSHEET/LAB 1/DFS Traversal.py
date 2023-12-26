n = 0
not_visited = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
visited = []
fin = []
matrix = [
    # a b  c  d  e  f  g
    [n, 1, 0, 1, 1, 0, 0],
    [1, n, 1, 0, 1, 1, 0],
    [0, 1, n, 0, 1, 1, 1],
    [1, 0, 0, n, 1, 0, 0],
    [1, 1, 1, 1, n, 1, 0],
    [0, 0, 1, 0, 1, n, 1],
    [0, 0, 1, 0, 0, 1, n]
]
index = [0]

while index:
    current_node = index.pop()
    if not_visited[current_node] not in visited:
        visited.append(not_visited[current_node])       
        fin.append(not_visited[current_node])
        for i in range(len(matrix[current_node])):
            if matrix[current_node][i] and not_visited[i] not in visited:
                index.append(i)

print(fin)