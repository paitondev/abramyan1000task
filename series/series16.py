try:
    K = int(input())
    index = 0
    result = 0
    while True:
        x = int(input())
        if x == 0:
            break
        index += 1
        if x > K:
            result = index
    print(result)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")