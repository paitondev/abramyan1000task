try:
    N = int(input())
    found = False
    for _ in range(N):
        if int(input()) > 0:
            found = True
    print("TRUE" if found else "FALSE")
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")