try:
    N = int(input())
    a = [int(input()) for _ in range(N)]
    first = a.index(0)
    last = N - 1 - a[::-1].index(0)
    total = 0
    if last - first > 1:
        total = sum(a[first + 1:last])
    print(total)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")