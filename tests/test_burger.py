import pytest
import pytest_cov
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    @pytest.mark.parametrize('expected_result', ['Флюоресцентная булка R2-D3', 'Краторная булка №200i'])
    def test_set_buns(self, expected_result):
        mock_bun = Mock()
        mock_bun.bun = expected_result
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun



