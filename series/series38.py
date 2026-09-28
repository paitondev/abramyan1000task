try:
    K = int(input())
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
        if increasing:
            print(1)
        elif decreasing:
            print(-1)
        else:
            print(0)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")