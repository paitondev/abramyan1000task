try:
    N = int(input())
    product = 1.0
    for _ in range(N):
        x = float(input())
        frac = x - int(x)
        print(frac)
        product *= frac
    print(product)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")