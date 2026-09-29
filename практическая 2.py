print("1 арифметика")
print("2 Сравнение")
print("3 Логические операции")
print("4 Операции приналежности")
print("5 Операции тождественности")

choice = int(input("выберите раздел: "))
## Арифметика
if choice == 1:
    a = int(input("введите перове число: "))
    b = int(input("введите торое число: "))
    print("Возможные операторы: + - *  ** / // %")
    op = input("Введите оператор: ")

    if op == "+":
        print("Результат:", a+b)
    elif op == "-":
        print("Результат:", a-b)
    elif op == "*":
        print("Результат:", a*b)
    elif op == "**":
        print("Результат:", a**b)
    elif op == "/":
        if b != 0:
            print("Результат:", a/b)
        else:
            print("Нельзя делить на ноль")
    elif op == "//":
        if b != 0:
            print("Результат:", a//b)
        else:
            print("Нельзя делить на ноль")
    elif op == "%":
        if b != 0:
            print("Результат:", a%b)
        else:
            print("Нельзя делить на ноль")
    else:
        print("Неверный оператор")
## Сравнение
elif choice == 2:
    a = int(input("введите перове число: "))
    b = int(input("введите торое число: "))
    if a == b:
        print("Переменные равны")
    elif a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    if a != b:
        print("a != b")
## Логика
elif choice == 3:
    a = input("Введите первую переменную: ")
    b = input("Введите вторую переменную: ")
    if a == "True":
        a = True
    else:
        a = False
    if b == "True":
        b = True
    else:
        b = False
    print("a and b:", a and b)
    print("a or b:", a or b)
    print("not a:", not a, "not b:", not b)
## принадлежность
elif choice == 4:
    a = input("Введите перменную: ")
    Array = input("Введите список через пробел: ").split()
    print(Array)
    if a in Array:
        print("a in Array")
    else:
        print("a not in Array")
## тождественность
elif choice == 5:

    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a is b:
        print("a is b")
    else:
        print("a is not b")
else:
    print("Не существующий раздел")

    





