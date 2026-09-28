try:
    K = int(input())
    for _ in range(K):
        a = []
        while True:
            x = int(input())
            if x == 0:
                break
            a.append(x)
        bad = 0
        for i in range(1, len(a) - 1):
            if not ((a[i] > a[i-1] and a[i] > a[i+1]) or
                    (a[i] < a[i-1] and a[i] < a[i+1])):
                bad = i + 1
                break
        if bad == 0:
            print(len(a))
        else:
            print(bad)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")