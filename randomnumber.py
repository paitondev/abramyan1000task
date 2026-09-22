import random

tries = 0
print("Угадай число от 1 до 100.")
a = random.randint(1, 100)

while True:
    b = int(input())
    if a > b:
        print("Загаданное число больше.")
        tries += 1
    elif a < b:
        print("Загаданное число меньше.")
        tries += 1
    elif a == b:
        tries += 1
        print("Вы угадали. Число было: ", a)
        print("Ваше число попыток: ", tries)
        
        c = input("Продолжим? (+/-) ")
        if c == "+":
            print("Угадай число от 1 до 100.")
            a = random.randint(1, 100)
            tries = 0
        else:
            print("До скорого!")
            break
