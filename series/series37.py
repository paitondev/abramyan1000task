try:
    K = int(input())
    count = 0
    for _ in range(K):
        prev = int(input())
        increasing = True
        decreasing = True
        while True:
            x = int(input())
            if x == 0:
                break
            if x <= prev:
                increasing = False
            if x >= prev:
                decreasing = False
            prev = x
        if increasing or decreasing:
            count += 1
    print(count)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")