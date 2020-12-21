def solution(n):
    # Your code here
    n = int(n)
    
    steps = 0
    
    while True:
        if n == 1:
            return steps
        if n % 2 == 0:
            n = n / 2
        elif n % 4 == 1 or n == 3:
            n = n - 1
        else:
            n = n + 1
        steps += 1
    
    #return solution_helper(n, steps)
    
# Recursive solution (not working because it's slower?)
def solution_helper(n, steps):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return solution_helper(n / 2, steps + 1)
    elif n % 4 == 1 or n == 3:
        return solution_helper(n - 1, steps + 1)
    else:
        return solution_helper(n + 1, steps + 1)