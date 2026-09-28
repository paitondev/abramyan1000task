try:
    K = int(input())
    count = 0
    while True:
        x = int(input())
        if x == 0:
            break
        if x < K:
            count += 1
    print(count)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")