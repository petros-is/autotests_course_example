import datetime


import pytest
import time

@pytest.fixture(scope='class')
def startnend():

    start_time = time.time()
    print(f'начало:{datetime.datetime.fromtimestamp(start_time)}')
    yield
    end_time = time.time()
    print(f'конец: {datetime.datetime.fromtimestamp(end_time)}')


@pytest.fixture()
def end_minus_start():
    start_time = time.time()
    yield
    end_time = time.time()
    ems = end_time - start_time
    print(f'время выполнения :{ems}')


# WITH STAR

@pytest.fixture(scope="function")
def get_test_id(request):
    id_value = request.node.get_closest_marker("id_check")
    print(f"Тест имеет ID: {id_value.args}")


