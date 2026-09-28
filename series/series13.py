try:
    total = 0
    while True:
        x = int(input())
        if x == 0:
            break
        if x > 0 and x % 2 == 0:
            total += x
    print(total)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")