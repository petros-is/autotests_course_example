# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты


import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_zero_division():
    #Тестируем деление на 0
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)



@pytest.mark.smoke
def test_all_division():
    # Тестируем корректное деление
    assert all_division(10, 2) == 5

@pytest.mark.acceptance
def test_str():
    # str
    with pytest.raises(TypeError):
        all_division('az', 'az' )

@pytest.mark.smoke
def test_divide_negative():
    # negative
    assert all_division(10, -2) == -5

@pytest.mark.acceptance
def test_divide_float():
    # float
    assert all_division(10, 2.5) == 4.0

