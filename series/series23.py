try:
    N = int(input())
    a = [float(input()) for _ in range(N)]
    result = 0
    for i in range(1, N - 1):
        if not ((a[i] > a[i-1] and a[i] > a[i+1]) or
                (a[i] < a[i-1] and a[i] < a[i+1])):
            result = i + 1
            break
    print(result)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")