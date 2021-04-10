moja_lista = [1,22,4,4,1,482,6,23,91,12,321,4214,1,32,45]
sum=0
lista_pomocnicza = []
for i in moja_lista:
    if i not in lista_pomocnicza:
        lista_pomocnicza.append(i)
    sum +=1
moja_lista=lista_pomocnicza[:]
print("Lista tylko z unikalnymi elementami:")
print(moja_lista)
