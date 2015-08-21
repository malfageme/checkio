def golf(n):
    while n:
        n+=1
        if all([n%x for x in range(2,n)])and str(n)==str(n)[::-1]:
            return n
