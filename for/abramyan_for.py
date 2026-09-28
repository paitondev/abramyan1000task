import math

# For1
k = int(input("K: "))
n = int(input("N: "))
for _ in range(n):
    print(k)


# For2
a = int(input("A: "))
b = int(input("B: "))
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print("N =", count)


# For3
a = int(input("A: "))
b = int(input("B: "))
count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print("N =", count)


# For4
price = float(input("Цена 1 кг: "))
for i in range(1, 11):
    print(i, price * i)


# For5
price = float(input("Цена 1 кг: "))
for i in range(1, 11):
    w = i / 10
    print(round(w, 1), round(price * w, 2))


# For6
price = float(input("Цена 1 кг: "))
for i in range(5):
    w = 1.2 + i * 0.2
    print(round(w, 1), round(price * w, 2))


# For7
a = int(input("A: "))
b = int(input("B: "))
s = 0
for i in range(a, b + 1):
    s += i
print(s)


# For8
a = int(input("A: "))
b = int(input("B: "))
p = 1
for i in range(a, b + 1):
    p *= i
print(p)


# For9
a = int(input("A: "))
b = int(input("B: "))
s = 0
for i in range(a, b + 1):
    s += i * i
print(s)


# For10
n = int(input("N: "))
s = 0.0
for i in range(1, n + 1):
    s += 1 / i
print(s)


# For11
n = int(input("N: "))
s = 0
for i in range(n, 2 * n + 1):
    s += i * i
print(s)


# For12
n = int(input("N: "))
p = 1.0
for i in range(1, n + 1):
    p *= 1 + i / 10
print(p)


# For13
n = int(input("N: "))
s = 0.0
sign = 1
for i in range(1, n + 1):
    s += sign * (1 + i / 10)
    sign = -sign
print(s)


# For14
n = int(input("N: "))
s = 0
for i in range(1, n + 1):
    s += 2 * i - 1
    print(s)


# For15
a = float(input("A: "))
n = int(input("N: "))
p = 1.0
for _ in range(n):
    p *= a
print(p)


# For16
a = float(input("A: "))
n = int(input("N: "))
p = 1.0
for _ in range(n):
    p *= a
    print(p)


# For17
a = float(input("A: "))
n = int(input("N: "))
s = 1.0
term = 1.0
for _ in range(n):
    term *= a
    s += term
print(s)


# For18
a = float(input("A: "))
n = int(input("N: "))
s = 1.0
term = 1.0
sign = -1
for _ in range(n):
    term *= a
    s += sign * term
    sign = -sign
print(s)


# For19
n = int(input("N: "))
f = 1.0
for i in range(1, n + 1):
    f *= i
print(f)


# For20
n = int(input("N: "))
s = 0.0
f = 1.0
for i in range(1, n + 1):
    f *= i
    s += f
print(s)


# For21
n = int(input("N: "))
s = 1.0
f = 1.0
for i in range(1, n + 1):
    f *= i
    s += 1 / f
print(s)


# For22
x = float(input("X: "))
n = int(input("N: "))
s = 1.0
f = 1.0
term = 1.0
for i in range(1, n + 1):
    f *= i
    term *= x
    s += term / f
print(s)


# For23
x = float(input("X: "))
n = int(input("N: "))
s = 0.0
sign = 1
for i in range(n + 1):
    k = 2 * i + 1
    s += sign * x ** k / math.factorial(k)
    sign = -sign
print(s)


# For24
x = float(input("X: "))
n = int(input("N: "))
s = 0.0
sign = 1
for i in range(n + 1):
    k = 2 * i
    s += sign * x ** k / math.factorial(k)
    sign = -sign
print(s)


# For25
x = float(input("X: "))
n = int(input("N: "))
s = 0.0
term = 1.0
sign = 1
for i in range(1, n + 1):
    term *= x
    s += sign * term / i
    sign = -sign
print(s)


# For26
x = float(input("X: "))
n = int(input("N: "))
s = 0.0
sign = 1
for i in range(n + 1):
    k = 2 * i + 1
    s += sign * x ** k / k
    sign = -sign
print(s)


# For27
x = float(input("X: "))
n = int(input("N: "))
s = x
num = 1.0
den = 1.0
for i in range(1, n + 1):
    num *= 2 * i - 1
    den *= 2 * i
    s += num * x ** (2 * i + 1) / (den * (2 * i + 1))
print(s)


# For28
x = float(input("X: "))
n = int(input("N: "))
s = 1.0
term = 1.0
for i in range(1, n + 1):
    if i == 1:
        term = x / 2
    else:
        term *= -(2 * i - 3) * x / (2 * i)
    s += term
print(s)


# For29
n = int(input("N: "))
a = float(input("A: "))
b = float(input("B: "))
h = (b - a) / n
print("H =", h)
for i in range(n + 1):
    print(a + i * h)


# For30
n = int(input("N: "))
a = float(input("A: "))
b = float(input("B: "))
h = (b - a) / n
print("H =", h)
for i in range(n + 1):
    x = a + i * h
    print(x, 1 - math.sin(x))


# For31
n = int(input("N: "))
a = 2.0
for _ in range(n):
    a = 2 + 1 / a
    print(a)


# For32
n = int(input("N: "))
a = 1.0
for k in range(1, n + 1):
    a = (a + 1) / k
    print(a)


# For33
n = int(input("N: "))
f1, f2 = 1, 1
for i in range(1, n + 1):
    if i <= 2:
        print(1)
    else:
        f1, f2 = f2, f1 + f2
        print(f2)


# For34
n = int(input("N: "))
a1, a2 = 1.0, 2.0
print(a1)
if n >= 2:
    print(a2)
for _ in range(3, n + 1):
    a1, a2 = a2, (a1 + 2 * a2) / 3
    print(a2)


# For35
n = int(input("N: "))
a1, a2, a3 = 1, 2, 3
print(a1, a2, a3)
for _ in range(4, n + 1):
    a1, a2, a3 = a2, a3, a3 + a2 - 2 * a1
    print(a3)


# For36
n = int(input("N: "))
k = int(input("K: "))
s = 0.0
for i in range(1, n + 1):
    s += i ** k
print(s)


# For37
n = int(input("N: "))
s = 0.0
for i in range(1, n + 1):
    s += i ** i
print(s)


# For38
n = int(input("N: "))
s = 0.0
for i in range(1, n + 1):
    s += i ** (n - i + 1)
print(s)


# For39
a = int(input("A: "))
b = int(input("B: "))
for i in range(a, b + 1):
    for _ in range(i - a + 1):
        print(i, end=" ")
    print()


# For40
a = int(input("A: "))
b = int(input("B: "))
for i in range(a, b + 1):
    for _ in range(i - a + 1):
        print(i, end=" ")
    print()