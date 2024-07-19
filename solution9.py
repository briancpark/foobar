# Bit manipulation is much like John Conway's game of life


def solution(g):
    x = len(g[0])
    y = len(g)

    c = [[False for _ in range(x - 1)] for _ in range(y - 1)]

    for i in range(y - 1):
        for j in range(x - 1):
            if (
                g[i][j] is True
                and g[i][j + 1] is False
                and g[i + 1][j] is False
                and g[i + 1][j + 1] is False
            ):
                c[i][j] = True
            if (
                g[i][j] is False
                and g[i][j + 1] is False
                and g[i + 1][j] is False
                and g[i + 1][j + 1] is False
            ):
                c[i][j] = True
            if (
                g[i][j] is False
                and g[i][j + 1] is False
                and g[i + 1][j] is True
                and g[i + 1][j + 1] is False
            ):
                c[i][j] = True
            if (
                g[i][j] is False
                and g[i][j + 1] is False
                and g[i + 1][j] is False
                and g[i + 1][j + 1] is True
            ):
                c[i][j] = True

    counter = 0

    for i in c:
        for j in i:
            if j:
                counter += 1

    print(counter)
    return counter


# solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
# 11567

solution([[True, False, True], [False, True, False], [True, False, True]])
# 4


# solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
# 254
