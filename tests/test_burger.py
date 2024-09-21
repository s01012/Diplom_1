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

    @pytest.mark.parametrize('expected_result', ['Мясо бессмертных моллюсков Protostomia',
                                                 'Говяжий метеорит (отбивная)',
                                                 'Биокотлета из марсианской Магнолии',
                                                 'Филе Люминесцентного тетраодонтимформа',
                                                 'Хрустящие минеральные кольца',
                                                 'Плоды Фалленианского дерева',
                                                 'Кристаллы марсианских альфа-сахаридов',
                                                 'Мини-салат Экзо-Плантаго',
                                                 'Сыр с астероидной плесенью'])
    def test_add_ingredient(self, expected_result):
        mock_ingredient = Mock()
        mock_ingredient.ingredient = expected_result
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        ingredient_values = []
        for ing in burger.ingredients:
            ingredient_values.append(ing.ingredient)
        assert expected_result in ingredient_values


