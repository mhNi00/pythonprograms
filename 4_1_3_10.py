def l100kmtompg(litry):
    mpg=(100*3.785411784/1.609344)/litry
    return mpg

def mpgtol100km(mile):
    l100km=(100*3.785411784/1.609344)/mile
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
