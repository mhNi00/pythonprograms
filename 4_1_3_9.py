def czy_pierwsza(liczba):
    for i in range(2,liczba):
        if liczba%i==0:
            return False
    return True

for i in range(1, 100):
    if czy_pierwsza(i + 1):
        print(i + 1, end=" ")
print()
