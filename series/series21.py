try:
    N = int(input())
    prev = float(input())
    ok = True
    for _ in range(N - 1):
        x = float(input())
        if x <= prev:
            ok = False
        prev = x
    print("TRUE" if ok else "FALSE")
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")