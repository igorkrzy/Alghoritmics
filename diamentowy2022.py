from itertools import permutations

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def ulamek_okresowy(L,M):
    result = []
    result.append(str(L // M) + '.')
    L %= M 
    reszty = {}
    while L != 0:
        if L in reszty:
            start =  reszty[L]
            result.insert(start, '(')
            result.append(')')
            return ''.join(result)
        reszty[L] = len(result)
        L *= 10
        result.append(str(L // M))
        L %= M
    return ''.join(result)
#===========================================================================================================================================

def silnia(a):
    x = 1
    for i in range(2,a+1):
        x *=i
    return x
def permutations_count(A, B):
    reszta = A-1
    dlug = reszta+B
    jed = [1] * reszta
    zer = [0] * B
    calosc = jed + zer
    print(calosc)
    kombinacje = set(permutations(calosc))
    wszystkie = []
    for i in kombinacje:
        binary_number = '1' +  ''.join(map(str, i))
        decimal_number = int(binary_number, 2)
        if czy_pierwsza(decimal_number) == False:          
            wszystkie.append((binary_number, decimal_number))
    print(len(wszystkie), wszystkie)

#============================================================================================================================================
def komnata(n, a):
    lst = a
    odwiedzone = set()
    b = c = 0
    odwiedzone.add((b,c))
    while b != n and c != n:
        if b < n-1 and lst[b+1][c] == '.'and (b+1,c) not in odwiedzone:
            b += 1
            print("D")
            odwiedzone.add((b,c))
        elif lst[b][c+1] != '.' and (b,c+1) not in odwiedzone:
            c += 1
            print("P")
            odwiedzone.add((b,c))
        if lst[b-1][c] == '.'and (b-1, c) not in odwiedzone:
            b -= 1
            print("G")
            odwiedzone.add((b,c))
        elif lst[b-1][c] != '.'and (b, c+1) not in odwiedzone:
            c += 1
            print("P")
            odwiedzone.add((b,c))
def komnaty(path):
    with open(path) as file:
        lst = [line.strip().split(' ') for line in file]
    return lst
#=============================================================================================================================================

def ciag():
    a = int(input("podaj długość ciagu: "))
    b = input("podaj liczniki i mianowniki tego ciagu: ")
    lst = b.split(" ")
    liczniki = []
    miano = []
    print(lst)
    for i in range(a*2):
        if int(lst[i])%2 != 0:
            liczniki.append(int(lst[i]))
        else:
            miano.append(int(lst[i]))
    roz = [(liczniki[i+1]/miano[i+1])/(liczniki[i]/miano[i]) for i in range(a-1)]
    count = 1
    najw = 0
    for i in range(len(roz)-1):
        print(roz[i],roz[i+1])
        if roz[i] == roz[i+1]:
            count += 1
        else:
            if count > najw:
                najw = count
            count = 1
    print(najw+1)
#=================================================================================================================================================
def sito(pocz,kon):
    n = kon +1
    lst = [True]*n
    lst[0] =lst[1] = False
    for i in range(2,int(kon**0.5)+1):
        if lst[i]:
            for j in range(i*i, kon+1, i):
                lst[j] = False
    pierwsze = [i for i in range(pocz,kon+1) if lst[i]]
    return pierwsze
    


if __name__ == "__main__":
    print(sito(0,500))