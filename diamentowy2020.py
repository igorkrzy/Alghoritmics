def openfile(path):
    with open(path) as file:
        lst = [[int(element) for element in line.split()] for line in file]
    return lst
#==============================================================================
def zad1(lst):
    liczby = lst[1]
    iloscel = lst[0][0]
    iloscoper = lst[0][1]
    for i in range(iloscoper):
        k = max(liczby)
        ind = liczby.index(k)
        w = k//2
        liczby[ind] = w
    print(sum(liczby))
#===============================================================================
def zad2(lst):
    liczby = lst[1]
    a = lst[0][1]
    count = 0
    for i in range(len(liczby)):
        zakres = [i for i in range(liczby[i]-a, liczby[i]+a+1)]
        for k in range(len(liczby)-1):
            if liczby[k+1] in zakres and liczby[k+1] != liczby[i]:
                count += 1 
                break
    print(count)
#================================================================================
def jednokwad(a):
    while a != 1 and a != 4:
        rozdziel = [int(element) for element in str(a)]
        p = 0
        for i in range(len(rozdziel)):
            p += (rozdziel[i]*rozdziel[i])
            a = p
    if a ==1:
        return True
    else:
        return False

def pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def zad3(L, U, K):
    zakres = [i for i in range(L,U+1)]
    count = 0
    for i in range(len(zakres)):
        if jednokwad(zakres[i]) == True and pierwsza(zakres[i]) == True and zakres[i] != 1:
            count +=1
            if count == K:
                print(zakres[i])
                break
    if count != K:
        print(-1)






#==============================================================================
if __name__ == "__main__":
    lst = openfile("minsum.txt")
    zad1(lst)
    lst2 = openfile("pary.txt")
    zad2(lst2)
    zad3(12,33,5)