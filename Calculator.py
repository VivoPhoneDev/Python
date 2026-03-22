a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Выберите действие\n1 Сложение\n2 Вычитание\n3 Деление\n4 Умножение\nПоле ввода: "))
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3: 
    if b == 0:
        print("Ты чо на 0 незя делить")
    else:
        print(a/b)
else:
    print(a*b)
