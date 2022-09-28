#import random
a = ""
b = "собака"
print("Какое животное лучший друг человека")
while a != b:
    a = input("Введите ответ: ")
    if a == b:
        print("вы угадали")
    else:
        print("Ne pravil'no")

print("Game over")