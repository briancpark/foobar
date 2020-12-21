def solution(l):
    # Your code here
    if (sum(l) // 3) * 3 != sum(l):
        l.sort(reverse=True)
        
        string = ""
        for el in l:
            string += str(el)
            
        return int(string)
    else:
        return 0