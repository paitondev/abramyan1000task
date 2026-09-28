try:
    N = int(input())
    total = 0
    product = 1
    for _ in range(N):
        x = float(input())
        total += x
        product *= x
    print(total, product)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")