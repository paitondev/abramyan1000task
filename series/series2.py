try:
    product = 1
    for _ in range(10):
        product *= float(input())
    print(product)
except ValueError:
    print("Ошибка: введено не число")
except Exception as e:
    print(f"Ошибка: {e}")