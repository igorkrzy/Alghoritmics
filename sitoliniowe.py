x = int(input())
liczby = [True] *(x+1)
p = 2
while p*p <= x:
    q = p
    while p*q <= x:
        a = p*q
        while a <= x:
            liczby[a] = False
            a *= p
        while 1:
            q += 1
            if liczby[q]:
                break
    while 1:
        p+=1
        if liczby[p]:
            break
print(" ".join(str(i) for i in range(2, x + 1) if liczby[i]))