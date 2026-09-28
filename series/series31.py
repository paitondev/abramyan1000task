try:
    K = int(input())
    N = int(input())
    count = 0
    for _ in range(K):
        has2 = False
        for _ in range(N):
            if int(input()) == 2:
                has2 = True
        if has2:
            count += 1
    print(count)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")