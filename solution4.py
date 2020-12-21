def solution(start, length):
    if length == 1:
        return start
    
    xor = xor_helper(start + 2 * (length - 1))
    
    if start > 1:
        xor = xor ^ xor_helper(start - 1)
    for i in range(length - 2):
        x = length - 2 - i
        y = start + length * (2 + i) - 1
        xor = xor ^ xor_helper(x + y) ^ xor_helper(y)
    return xor
    
def xor_helper(n):
    x = n % 4
    
    if x == 0:
        return n
    elif x == 1:
        return 1
    elif x == 2:
        return n + 1
    else:
        return 0
    