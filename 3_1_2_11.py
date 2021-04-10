slowo_bez_samoglosek = ""

# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika.
slowo_uzytkownika = input("Wprowadz slowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

# Uzupełnij pętlę for poniżej.
for litera in slowo_uzytkownika:
    if litera=="A" or litera=="E" or litera=="I" or litera=="O" or litera=="U":
        continue
    else:
        slowo_bez_samoglosek += litera

print(slowo_bez_samoglosek)
