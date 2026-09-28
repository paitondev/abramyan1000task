try:
    N = int(input())
    a = [int(input()) for _ in range(N)]
    last_zero = -1
    prev_zero = -1
    for i in range(N - 1, -1, -1):
        if a[i] == 0:
            if last_zero == -1:
                last_zero = i
            else:
                prev_zero = i
                break
    total = 0
    if last_zero - prev_zero > 1:
        total = sum(a[prev_zero + 1:last_zero])
    print(total)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")