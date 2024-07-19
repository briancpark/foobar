def solution(l):
    # Your code here
    permutations = 0
    combinations = [[] for _ in range(len(l))]

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                combinations[i].append(j)

    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                permutations += len(combinations[j])

    return permutations
