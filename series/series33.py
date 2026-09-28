try:
    K = int(input())
    N = int(input())
    for _ in range(K):
        pos = 0
        for i in range(1, N + 1):
            if int(input()) == 2:
                pos = i
        print(pos)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")