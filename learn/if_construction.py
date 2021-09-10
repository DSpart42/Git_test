
number = 23
guess = int(input("Введите целое число: "))

if guess == number :
    print('Молодец, ты отгодал число')
elif guess < number :
    print("Число чуть больше")
else :
    print("Число чуть меньше")

print("Попробуй в другой раз")