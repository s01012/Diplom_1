import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    @pytest.mark.parametrize('type_ingredient,name_ingredient,price', [[INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90],
                                                          [INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерева', 874],
                                                 [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88],
                                                        [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000]])
    def test_get_exact_name(self, type_ingredient, name_ingredient, price):
        ingredient = Ingredient(type_ingredient, name_ingredient, price)
        assert ingredient.get_name() == name_ingredient

    @pytest.mark.parametrize('type_ingredient,name_ingredient,price', [[INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90],
                                                          [INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерева', 874],
                                                 [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88],
                                                        [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000]])
    def test_get_exact_price(self, type_ingredient, name_ingredient, price):
        ingredient = Ingredient(type_ingredient, name_ingredient, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('type_ingredient,name_ingredient,price', [[INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90],
                                                          [INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерева', 874],
                                                 [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88],
                                                        [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000]])
    def test_get_exact_type(self, type_ingredient, name_ingredient, price):
        ingredient = Ingredient(type_ingredient, name_ingredient, price)
        assert ingredient.get_type() == type_ingredient