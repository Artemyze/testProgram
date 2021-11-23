def discrim(a, b, c):
    d = b ** 2 - 4 * a * c
    return d

a = int(input())
b = int(input())
c = int(input())
d = discrim(a, b, c)
if d>0:
    x1 = (- b - d**0.5)/2*a
    x2 = (- b - d**0.5)/2*a
    print(x1, x2)
elif d==0:
    x1 = x1 = -b/2*a
    print(x1)
else:
    print("Корней нет")


