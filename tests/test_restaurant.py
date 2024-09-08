from models.menu.dishes import Dish
from models.menu.drink import Drink
import pytest
from pytest import mark

class TestClass:
    @mark.dishes
    def test_dish_should_not_be_null(self):
        dish = Dish('Dish name',10,'Description')
        assert dish._name is not None, "Name should not be null"

    @mark.dishes
    def test_dish_should_have_positive_price(self):
        dish = Dish('Dish Name',10,'Description')
        assert dish._price >= 0, "Price should be positive"


    @mark.drink
    def test_drink_should_not_be_null(self):
        drink = Drink('Drink name',10,None,10)
        assert drink._name is not None, "Name should not be null"
#
    @mark.drink
    def test_drink_should_have_positive_price(self):
        drink = Drink('Dish Name',10,None,10)
        assert drink._price >= 0, "Price should be positive"
#
    @mark.drink
    def test_drink_should_not_have_discount_greater_than_10_percent(self):
        discount = 10/100 #10%
        price = 10
        expected_price = price - (price * discount) #9
#
        drink = Drink("Drink name", price, "Description", "Tall")
        drink.discount()
        assert drink._price == expected_price, "Discount should not be greater than 10%"
#
    @mark.drink
    def test_drink_negative_value_should_return_exception(self):
        drink = Drink('Drink name',10,None,10)
        with pytest.raises(Exception):
            drink._price = -10
            result = drink.discount()
#
            assert result 
    