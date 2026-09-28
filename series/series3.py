try:
    total = 0
    for _ in range(10):
        total += float(input())
    print(total / 10)
except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
except Exception as e:
    print(f"Ошибка: {e}")