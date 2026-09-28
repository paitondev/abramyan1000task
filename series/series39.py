try:
    K = int(input())
    count = 0
    for _ in range(K):
        a = []
        while True:
            x = int(input())
            if x == 0:
                break
            a.append(x)
        is_saw = True
        for i in range(1, len(a) - 1):
            if not ((a[i] > a[i-1] and a[i] > a[i+1]) or
                    (a[i] < a[i-1] and a[i] < a[i+1])):
                is_saw = False
                break
        if is_saw:
            count += 1
    print(count)
except ValueError:
    print("Ошибка: введено не целое число")
except Exception as e:
    print(f"Ошибка: {e}")