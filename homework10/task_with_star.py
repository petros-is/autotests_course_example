# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest

@pytest.mark.usefixtures('get_test_id')
@pytest.mark.id_check(1, 2, 3)
def test():
    pass
