import numpy as xy
x = xy.random.randint(0, 20, 15)
print("Array")
print(x)
print("Frequently repeted value is:")
print(xy.bincount(x).argmax())