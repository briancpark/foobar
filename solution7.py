# Problem is much harder and definitely a challenge.
# Here are some sources that I used to help me solve this:
# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
# https://cseweb.ucsd.edu/~dasgupta/book/index.html

#A maxflow min cut problem, using a modificaiton of ford fulkerson algorithm

def solution(entrances, exits, path):
    # Your code here
    max_val = sum(list(map(sum, path)))
    mat = []
    for i in range(len(path)):
        mat.append([])
        for j in range(len(path[i])):
            mat[i].append([0, path[i][j]])
        mat[i].append([0, 0])
        if i in exits:
            mat[i].append([0, max_val])
        else:
            mat[i].append([0, 0])
    mat.append([])
    mat.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            mat[-2].append([0, max_val])
        else:
            mat[-2].append([0, 0])
        mat[-1].append([0, 0])
    while bfs(mat, len(mat) - 2, len(mat) - 1):
        pass
    total = 0
    for i in range(len(mat)):
        total += mat[-2][i][0]
    return total


def bfs(matrix, start, end):
    visited = [-1 for i in range(len(matrix))]
    visited[start] = start
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[node][i][1] - matrix[node][i][0]) and visited[i] == -1:
                if i == end:
                    visited[end] = node
                    path = []
                    path.append(end)
                    temp = end

                    while temp != start:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()

                    total = float("inf")
                    curr = start
                    
                    for j in range(1, len(path) - 1):
                        entry = matrix[curr][path[j]]
                        total = min(total, abs(entry[1]) - entry[0])
                        curr = path[j]

                    curr = start
                    
                    for j in range(1, len(path) - 1):
                        entry = matrix[curr][path[j]]
                        if entry[1] < 0: 
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[j]][curr]
                        if entry[1] <= 0: 
                            entry[1] -= total
                        else:
                            entry[0] += total
                        curr = path[j]
                        
                    return True
                else:
                    visited[i] = node
                    queue.append(i)
    return False
