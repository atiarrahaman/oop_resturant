class Food():

    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price 


class Burger(Food):
    def __init__(self, name, price,types_of) -> None:
        super().__init__(name, price)
        self.types_of =types_of


class Pizza(Food):
    def __init__(self, name, price,size) -> None:
        super().__init__(name, price)
        self.size=size


class Drinks(Food):
    def __init__(self, name, price,types) -> None:
        super().__init__(name, price)
        self.tpyes=types


class Menu:
    def __init__(self,) -> None:
        self.burgers=[]
        self.pizzas=[]
        self.drinks=[]


    def Add_item(self,item,item_type):
        if item_type=='burger':
            self.burgers.append(item)

        elif item_type == 'pizza':
            self.pizzas.append(item)

        elif item_type == 'drinks':
            self.drinks.append(item)

    def Show_menu(self):
        for burger in self.burgers:
            print(f'{burger.name} , price:{burger.price}')


        for pizza in self.pizzas:
            print(f'{pizza.name} , price:{pizza.price}')


        for drink in self.drinks:
            print(f'{drink.name} , price:{drink.price}')
