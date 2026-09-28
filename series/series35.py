try:
    K = int(input())
    total = 0
    for _ in range(K):
        count = 0
        while True:
            x = int(input())
            if x == 0:
                break
            count += 1
        print(count)
        total += count
    print(total)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")