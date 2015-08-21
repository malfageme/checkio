def golf2(n):
    return [i for i in range(n+1,9999) if  str(i)==str(i)[::-1]and all([i%x for x in range(2,i)])][0]
