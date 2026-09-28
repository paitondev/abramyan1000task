try:
    K = int(input())
    N = int(input())
    for _ in range(K):
        s = 0
        has2 = False
        for _ in range(N):
            x = int(input())
            s += x
            if x == 2:
                has2 = True
        print(s if has2 else 0)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")