try:
    N = int(input())
    for i in range(1, N + 1):
        x = float(input())
        print(x ** i)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")