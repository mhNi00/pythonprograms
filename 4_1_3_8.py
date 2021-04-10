def czy_przestepny(rok):
    if (rok%4==0 and rok%100!=0) or rok%400==0:
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    miesiace=[31,28,31,30,31,30,31,31,30,31,30,31]
    if czy_przestepny(rok):
        if miesiac==2:
            return 29
        else:
            return miesiace[miesiac-1]
    else:
        return miesiace[miesiac-1]

def dzien_w_roku(rok, miesiac, dzien):
    suma=0
    for i in range(miesiac):
        suma+=dni_w_miesiacu(rok,i)
    return suma-(dni_w_miesiacu(rok,miesiac)-dzien)
        
        

print(dzien_w_roku(1999, 1, 25))
