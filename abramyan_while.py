# While1
a = float(input("A: "))
b = float(input("B: "))

while a >= b:
    a -= b

print("Незанятая часть:", a)


# While2
a = float(input("A: "))
b = float(input("B: "))
count = 0

while a >= b:
    a -= b
    count += 1

print("Количество отрезков:", count)


# While3
n = int(input("N: "))
k = int(input("K: "))
quotient = 0

while n >= k:
    n -= k
    quotient += 1

print("Частное:", quotient)
print("Остаток:", n)


# While4
n = int(input("N: "))

while n > 1 and n % 3 == 0:
    n //= 3

print(n == 1)


# While5
n = int(input("N: "))
k = 0

while n > 1:
    n //= 2
    k += 1

print("K =", k)


# While6
n = int(input("N: "))
result = 1.0

while n > 0:
    result *= n
    n -= 2

print("Двойной факториал:", result)


# While7
n = int(input("N: "))
k = 1

while k * k <= n:
    k += 1

print("K =", k)


# While8
n = int(input("N: "))
k = 1

while (k + 1) * (k + 1) <= n:
    k += 1

print("K =", k)


# While9
n = int(input("N: "))
k = 1
power = 3

while power <= n:
    power *= 3
    k += 1

print("K =", k)


# While10
n = int(input("N: "))
k = 0
power = 1

while power * 3 < n:
    power *= 3
    k += 1

print("K =", k)


# While11
n = int(input("N: "))
k = 0
total = 0

while total < n:
    k += 1
    total += k

print("K =", k)
print("Сумма =", total)


# While12
n = int(input("N: "))
k = 0
total = 0

while total + (k + 1) <= n:
    k += 1
    total += k

print("K =", k)
print("Сумма =", total)


# While13
a = float(input("A: "))
k = 0
total = 0.0

while total <= a:
    k += 1
    total += 1.0 / k

print("K =", k)
print("Сумма =", total)


# While14
a = float(input("A: "))
k = 0
total = 0.0

while total + 1.0 / (k + 1) < a:
    k += 1
    total += 1.0 / k

print("K =", k)
print("Сумма =", total)


# While15
p = float(input("P: "))
money = 1000.0
months = 0

while money <= 1100:
    money += money * p / 100
    months += 1

print("Месяцев:", months)
print("Итог:", money)


# While16
p = float(input("P: "))
daily = 10.0
total = 10.0
days = 1

while total <= 200:
    daily += daily * p / 100
    total += daily
    days += 1

print("Дней:", days)
print("Пробег:", total)


# While17
n = int(input("N: "))

while n > 0:
    print(n % 10, end=" ")
    n //= 10
print()


# While18
n = int(input("N: "))
count = 0
digits_sum = 0

while n > 0:
    digits_sum += n % 10
    count += 1
    n //= 10

print("Количество цифр:", count)
print("Сумма цифр:", digits_sum)


# While19
n = int(input("N: "))
reversed_n = 0

while n > 0:
    reversed_n = reversed_n * 10 + n % 10
    n //= 10

print("Перевёрнутое число:", reversed_n)


# While20
n = int(input("N: "))
found = False

while n > 0:
    if n % 10 == 2:
        found = True
        break
    n //= 10

print(found)


# While21
n = int(input("N: "))
has_odd = False

while n > 0:
    if (n % 10) % 2 != 0:
        has_odd = True
        break
    n //= 10

print(has_odd)


# While22
n = int(input("N: "))
is_prime = True
d = 2

while d * d <= n:
    if n % d == 0:
        is_prime = False
        break
    d += 1

print(is_prime)


# While23
a = int(input("A: "))
b = int(input("B: "))

while b != 0:
    a, b = b, a % b

print("НОД =", a)


# While24
n = int(input("N: "))
f1, f2 = 1, 1
fib = 1

while fib < n:
    fib = f1 + f2
    f1 = f2
    f2 = fib

print(fib == n)


# While25
n = int(input("N: "))
f1, f2 = 1, 1
fib = 1

while fib <= n:
    fib = f1 + f2
    f1 = f2
    f2 = fib

print("Первое число Фибоначчи > N:", fib)


# While26
n = int(input("N: "))
f1, f2 = 1, 1

while f2 < n:
    f1, f2 = f2, f1 + f2

print("Предыдущее:", f1)
print("Следующее:", f1 + f2)


# While27
n = int(input("N: "))
f1, f2 = 1, 1
k = 2

while f2 < n:
    f1, f2 = f2, f1 + f2
    k += 1

print("K =", k)


# While28
eps = float(input("Epsilon: "))
prev = 2.0
curr = 2.0 + 1.0 / prev
k = 2

while abs(curr - prev) >= eps:
    prev = curr
    curr = 2.0 + 1.0 / prev
    k += 1

print("K =", k)
print("A(k-1) =", prev)
print("A(k) =", curr)


# While29
eps = float(input("Epsilon: "))
a1 = 1.0
a2 = 2.0
a3 = (a1 + 2 * a2) / 3.0
k = 3

while abs(a3 - a2) >= eps:
    a1 = a2
    a2 = a3
    a3 = (a1 + 2 * a2) / 3.0
    k += 1

print("K =", k)
print("A(k-1) =", a2)
print("A(k) =", a3)


# While30
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

cols = 0
rows = 0

side = a
while side >= c:
    side -= c
    cols += 1

side = b
while side >= c:
    side -= c
    rows += 1

total = 0
for _ in range(rows):
    total += cols

print("Количество квадратов:", total)