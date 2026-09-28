try:
    K = int(input())
    N = int(input())
    for _ in range(K):
        s = 0
        for _ in range(N):
            s += int(input())
        print(s)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")