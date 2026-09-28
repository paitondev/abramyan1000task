try:
    N = int(input())
    total = 0
    for _ in range(N):
        x = float(input())
        r = int(x + 0.5) if x >= 0 else int(x - 0.5)
        print(r)
        total += r
    print(total)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")