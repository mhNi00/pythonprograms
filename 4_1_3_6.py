def czy_przestepny(rok):
    if (rok%4==0 and rok%100!=0) or rok%400==0:
        return True
    else:
        return False

dane_testowe = [2012, 1996, 2000, 1900]
wyniki_testow = [True, True, True, False]
for i in range(len(dane_testowe)):
	r = dane_testowe[i]
	print(r,"->",end="")
	wynik = czy_przestepny(r)
	if wynik == wyniki_testow[i]:
		print("OK")
	else:
		print("Nie powiodło się")
