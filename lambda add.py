def add(x):
    return lambda y:y+x
addn = add(25)
print(addn(10))