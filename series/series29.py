try:
    K = int(input())
    N = int(input())
    total = 0
    for _ in range(K):
        for _ in range(N):
            total += int(input())
    print(total)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")