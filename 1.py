# Задача: определить, кто старше из Антона, Бориса и Виктора

print("Введите возраст трёх человек")
print("-" * 40)

anton = int(input("Возраст Антона: "))
boris = int(input("Возраст Бориса: "))
viktor = int(input("Возраст Виктора: "))

print("-" * 40)

# Находим максимальный возраст
max_age = max(anton, boris, viktor)

# Собираем, кто имеет этот максимальный возраст
oldest = []

if anton == max_age:
    oldest.append("Антон")
if boris == max_age:
    oldest.append("Борис")
if viktor == max_age:
    oldest.append("Виктор")

# Формируем красивый вывод
if len(oldest) == 1:
    print(f"Самый старший — {oldest[0]}")
elif len(oldest) == 2:
    print(f"{oldest[0]} и {oldest[1]} старше всех")
else:
    print("Антон, Борис и Виктор одного возраста")
