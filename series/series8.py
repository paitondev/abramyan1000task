try:
    N = int(input())
    K = 0
    for _ in range(N):
        x = int(input())
        if x % 2 == 0:
            print(x)
            K += 1
    print(K)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")