from models.restaurant import Restaurant
from models.menu.dishes import Dish
from models.menu.drink import Drink
from fastapi import FastAPI, Query


app = FastAPI()

@app.get('/api/hello')
def hello():
    '''
    Wellcome endpoint, return if the application is successful
    '''
    return {'message': 'Hello, World!'}

@app.get('/api/restaurants/')
def get_restaurants(restaurant_name: str = Query(None)):
    '''
    Show a list of restaurant
    '''    
    if restaurant_name is None:
        return {'restaurants':Restaurant.restaurants}
    else:
        return {'restaurants': [restaurant for restaurant in Restaurant.restaurants if restaurant.name == restaurant_name]}

@app.get('/api/pop')
def pop_restaurant():
    main()


def main():
    restaurant = Restaurant("Gourmet", "Fast food")

    drink = Drink("Chocolate", 10,"drink made of cocoa","tall")
    dish = Dish("Chicken Wings", 15, "Chicken wings cooked in a special sauce")

    drink.discount()
    dish.discount()
    
    restaurant.add_in_menu(drink)
    restaurant.add_in_menu(dish)


    restaurant2 = Restaurant("Garden", "Fast food")

    drink2 = Drink("coffee", 5,"drink made of coffee","tall")
    dish2 = Dish("Chicken Wings", 5, "bufallo wings")

    drink2.discount()
    dish2.discount()
    
    restaurant2.add_in_menu(drink)
    restaurant2.add_in_menu(dish)

    print('-'*5 ,' SHOWING MENU ','-'*5)
    restaurant.show_menu


if __name__ == "__main__":
    main()