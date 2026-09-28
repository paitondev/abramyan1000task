try:
    B = float(input())
    N = int(input())
    inserted = False
    for _ in range(N):
        x = float(input())
        if not inserted and B < x:
            print(B)
            inserted = True
        print(x)
    if not inserted:
        print(B)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")