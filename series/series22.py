try:
    N = int(input())
    prev = float(input())
    result = 0
    for i in range(2, N + 1):
        x = float(input())
        if result == 0 and x >= prev:
            result = i
        prev = x
    print(result)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")