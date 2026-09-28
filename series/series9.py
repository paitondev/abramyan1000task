try:
    N = int(input())
    K = 0
    for i in range(1, N + 1):
        x = int(input())
        if x % 2 != 0:
            print(i)
            K += 1
    print(K)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")