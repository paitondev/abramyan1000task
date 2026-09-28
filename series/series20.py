try:
    N = int(input())
    prev = int(input())
    K = 0
    for _ in range(N - 1):
        x = int(input())
        if prev < x:
            print(prev)
            K += 1
        prev = x
    print(K)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")