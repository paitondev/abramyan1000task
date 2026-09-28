try:
    N = int(input())
    prev = None
    for i in range(N):
        x = int(input())
        if i == 0 or x != prev:
            print(x)
        prev = x
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")