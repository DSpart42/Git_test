
while True:
    s = input("Введите что-нибудь: ")
    if s == "выход":
        print("Конец цикла")
        break
    if len(s) < 3:
        print("Слишком мало")
        continue
    print("Введенная строка достаточной длины")
    print("Длина строки", len(s))
