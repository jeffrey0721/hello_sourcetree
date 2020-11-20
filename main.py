import numpy as np

a = [1, 2, 3, 4,5, 6]
b = [7, 8, 9, 10, 11, 12]
a = np.array_split(a, 1)
b = np.array_split(b, 3)

print(a)
print(b)

* res = [x, y for x, y in zip(a, b)]