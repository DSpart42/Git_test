
from random import randrange

number = randrange(31)
running= True

print("Отгадай число от 1 до 30")
print("Удачи!")

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