
number = 23
running= True

while running:
    guess = int(input("Введите число: "))

    if guess == number:
        print("Ты отгодал число")
        running = False
    elif guess < number:
        print("Число чуть больше")
    else:
        print("Число чуть меньше")
else:
    print("Цикл закончен")

print("Завершение")