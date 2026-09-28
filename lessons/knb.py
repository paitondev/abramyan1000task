import random

player_wins = 0
robot_wins = 0

while True:
    a = int(input("Введите число от 1 до 3. (1 - Камень, 2 - Ножницы, 3 - Бумага): "))
    b = random.randint(1, 3)
    print("Робот выдал:", b)
    
    if a == 1 and b == 2:
        print("Ваша победа.")
        player_wins += 1
    elif a == 1 and b == 3:
        print("Вы проиграли.")
        robot_wins += 1
    elif a == 2 and b == 1:
        print("Вы проиграли.")
        robot_wins += 1
    elif a == 2 and b == 3:
        print("Вы победили.")
        player_wins += 1
    elif a == 3 and b == 1:
        print("Вы победили.")
        player_wins += 1
    elif a == 3 and b == 2:
        print("Вы проиграли.") 
        robot_wins += 1
    elif a == b:
        print("Ничья.")

    print(f"Текущий счет - Игрок: {player_wins} | Робот: {robot_wins} \n")

    print("Сыграем еще раз? (+-)")
    answer = input()
    if answer != "+":
        print("До встречи.")
        print(f"Итоговый счет игры - Игрок: {player_wins} | Робот: {robot_wins}")
        break
