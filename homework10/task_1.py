# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# gen = generate_random_name()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
from random import randint


def generate_random_name():
    # от 97 до 122 латинские букви нижнего регистра

    alphabet = [chr(i) for i in range(97, 123)]

    while True:
        def length():
            length = randint(2, 15)
            return length

        def letter():
            let = random.choice(alphabet)
            return let

        w1 = ''.join([letter() for i in range(1, length())])
        w2 = ''.join([letter() for i in range(1, length())])
        yield f'{w1} {w2}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


