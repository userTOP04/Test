age = int(input("Сколько тебе лет? "))
if age % 10 == 0:
    print(age, "лет!")
elif age % 10 > 4 and age > 10 and age < 15:
    print(age, "лет!")
elif age % 10 == 1:
    print(age, "год!")
elif age % 10 > 1 and age % 10 < 5:
    print(age, "год!")

