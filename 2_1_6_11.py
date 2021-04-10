h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

h=(h+(d+m)//60)%24
m=(m+d)%60
print(h,m,sep=':')# wprowadź tutaj swój kod
