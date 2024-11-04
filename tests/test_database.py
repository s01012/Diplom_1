import pytest
from praktikum.database import Database
from praktikum.ingredient_types import *


class TestDatabase:

    def test_get_available_buns(self):
        database = Database()
        list_available_buns = database.available_buns()
        assert len(list_available_buns) == 3

    def test_get_available_ingredient(self):
        database = Database()
        list_available_ingredient = database.available_ingredients()
        assert len(list_available_ingredient) == 6

    def test_get_count_available_ingredient_type_sauce(self):
        database = Database()
        list_available_ingredient = database.available_ingredients()
        available_sauces = []
        for ingredient in list_available_ingredient:
            if ingredient.get_type() == INGREDIENT_TYPE_SAUCE:
                available_sauces.append(ingredient)
        assert len(available_sauces) == 3

    def test_get_count_available_ingredient_type_filling(self):
        database = Database()
        list_available_ingredient = database.available_ingredients()
        available_filling = []
        for ingredient in list_available_ingredient:
            if ingredient.get_type() == INGREDIENT_TYPE_FILLING:
                available_filling.append(ingredient)
        assert len(available_filling) == 3

    @pytest.mark.parametrize('name_ingredient,price', [['hot sauce', 100],
                                                       ['sour cream', 200],
                                                       ['chili sauce', 300],
                                                       ['cutlet', 100],
                                                       ['dinosaur', 200],
                                                       ['sausage', 300]])
    def test_get_price_available_ingredient(self, name_ingredient, price):
        database = Database()
        list_available_ingredient = database.available_ingredients()
        available_price = {}
        for ingredient in list_available_ingredient:
            available_price[ingredient.get_name()] = ingredient.get_price()
        assert available_price[name_ingredient] == price
