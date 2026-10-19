# МНОЖЕСТВА

# 1
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
numbers_set = set(numbers)
print("Множество:", numbers_set)
print("Количество элементов:", len(numbers_set))

# 2
s = {10, 20, 30}
s.add(40)
s.remove(10)
print("Результат:", s)

# 3
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Объединение:", a | b)

# 4
print("Пересечение:", a & b)

# 5
print("Только в первом:", a - b)
print("Только во втором:", b - a)

# 6
print("Ровно в одном:", a ^ b)

# 7
x = 3
print(f"{x} в множестве:", x in a)

# 8
small = {1, 2}
big = {1, 2, 3, 4}
print("Первое — подмножество второго:", small <= big)

# 9
text = "hello world"
chars = set(text)
print("Символы:", chars)
print("Количество:", len(chars))

# 10
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 5]
common = sorted(set(list1) & set(list2))
print("Общие без повторов:", common)


# КОРТЕЖИ

#1
t = (10, 20, 30, 40, 50)
print("Первый:", t[0])
print("Последний:", t[-1])
print("Средний:", t[len(t) // 2])

# 2
t8 = (1, 2, 3, 4, 5, 6, 7, 8)
print("Первые два:", t8[:2])
print("Последние два:", t8[-2:])
print("Обратный порядок:", t8[::-1])

# 3
nums = (5, 2, 9, 1, 7)
print("Длина:", len(nums))
print("Сумма:", sum(nums))
print("Минимум:", min(nums))
print("Максимум:", max(nums))

# 4
t4 = (1, 2, 3, 2, 4, 2, 5)
x = 2
print(f"{x} в кортеже:", x in t4)
print("Количество вхождений:", t4.count(x))
print("Индекс первого вхождения:", t4.index(x))

# 5
t_a = (1, 2, 3)
t_b = (4, 5, 6)
print("Объединённый кортеж:", t_a + t_b)

# 6
single = (42,)
print("Тип:", type(single))
print("Значение:", single)

# 7
person = ("Иван", 25, "Москва")
name, age, city = person
print("Имя:", name)
print("Возраст:", age)
print("Город:", city)

# 8
v1, v2 = 10, 20
v1, v2 = v2, v1
print("v1 =", v1, ", v2 =", v2)

# 9
t9 = (1, 2, 3, 4)
t9_new = (t9[0], 99) + t9[2:]
print("Новый кортеж:", t9_new)

# 10
t10 = (5, 3, 5, 1, 3, 2, 9, 1)
t10_unique_sorted = tuple(sorted(set(t10)))
print("Без повторов, по возрастанию:", t10_unique_sorted)