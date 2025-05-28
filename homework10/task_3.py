# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните


import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result', [pytest.param((10, 0), pytest.raises(ZeroDivisionError), marks=pytest.mark.smoke),
                                          pytest.param((10, 2), 5, marks=pytest.mark.skip),
                                          pytest.param((1, 1), 1),
                                          pytest.param((10, -2), -5),
                                          pytest.param((10, 2.5), 4.0)])
def test_giga(args, result):
    if 0 in args:
        with result:
            assert all_division(*args)
    else:
        assert all_division(*args) == result

