try:
    N = int(input())
    total = 0
    for _ in range(N):
        x = float(input())
        int_part = float(int(x))
        print(int_part)
        total += int_part
    print(total)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")