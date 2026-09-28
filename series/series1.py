try:
    total = 0
    for _ in range(10):
        total += float(input())
    print(total)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")