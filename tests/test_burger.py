import pytest
import pytest_cov
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:

    @pytest.fixture(autouse=True)
    def burger_init(self):
        self.burger = Burger()

    @pytest.mark.parametrize('name_bun,price', [['Флюоресцентная булка R2-D3', 0.99],
                                                ['Краторная булка №200i', 1.0]])
    def test_set_buns(self, name_bun, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name_bun
        mock_bun.get_price.return_value = price
        self.burger.set_buns(mock_bun)
        assert self.burger.bun.get_name() == name_bun and self.burger.bun.get_price() == price

    @pytest.mark.parametrize('name_ingredient,price,type_ingredient', [
                                                 ['Мясо бессмертных моллюсков Protostomia', 0.99, INGREDIENT_TYPE_FILLING],
                                                 ['Говяжий метеорит (отбивная)', 0.98, INGREDIENT_TYPE_FILLING],
                                                 ['Соус сырный', 0.01, INGREDIENT_TYPE_SAUCE],
                                                 ['Филе Люминесцентного тетраодонтимформа', 1.01, INGREDIENT_TYPE_FILLING],
                                                 ['Хрустящие минеральные кольца', 2.00, INGREDIENT_TYPE_FILLING],
                                                 ['Соус томатный', 0.2, INGREDIENT_TYPE_SAUCE],
                                                 ['Кристаллы марсианских альфа-сахаридов', 3.00, INGREDIENT_TYPE_FILLING],
                                                 ['Мини-салат Экзо-Плантаго', 5.0, INGREDIENT_TYPE_FILLING],
                                                 ['Сыр с астероидной плесенью', 10.0, INGREDIENT_TYPE_FILLING]])
    def test_add_ingredient(self, name_ingredient, price, type_ingredient):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = name_ingredient
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = type_ingredient
        self.burger.add_ingredient(mock_ingredient)
        assert (self.burger.ingredients[0].get_name() == name_ingredient
                and self.burger.ingredients[0].get_price() == price
                and self.burger.ingredients[0].get_type() == type_ingredient)

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ['Кристаллы марсианских альфа-сахаридов']
        self.burger.add_ingredient(mock_ingredient)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 0
