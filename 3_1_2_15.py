c0=int(input("Podaj liczbe nieujemna i niezerowa: "))
liczba_krokow=0
while c0<=0:
    c0=int(input("Wprowadz poprawna liczbe: "))
while c0!=1:
    if c0%2==0:
        c0=c0//2
    else:
        c0=3*c0+1
    liczba_krokow +=1
    print(c0)

print("Liczba krokow =",liczba_krokow)
