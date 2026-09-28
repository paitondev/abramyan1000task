try:
    K = int(input())
    count = 0
    for _ in range(K):
        prev = int(input())
        increasing = True
        while True:
            x = int(input())
            if x == 0:
                break
            if x <= prev:
                increasing = False
            prev = x
        if increasing:
            count += 1
    print(count)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")