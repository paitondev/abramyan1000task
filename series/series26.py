try:
    K = int(input())
    N = int(input())
    for _ in range(N):
        x = float(input())
        print(x ** K)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")