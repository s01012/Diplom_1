import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name_bun, price', [['Флюоресцентная булка R2-D3', 1.0],
                                                 ['Краторная булка №200i', 0.99]])
    def test_get_exact_name(self, name_bun, price):
        bun = Bun(name_bun, price)
        assert bun.get_name() == name_bun

    @pytest.mark.parametrize('name_bun, price', [['Флюоресцентная булка R2-D3', 1.0],
                                                 ['Краторная булка №200i', 0.99]])
    def test_get_exact_price(self, name_bun, price):
        bun = Bun(name_bun, price)
        assert bun.get_price() == price