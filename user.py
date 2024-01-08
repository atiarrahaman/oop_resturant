from abc import ABC ,abstractmethod


class User():
    def __init__(self,name,add) -> None:
        self.name=name
        self.add =add

class Customer(User):
    def __init__(self, name, add,wallet) -> None:
        self.wallet=wallet
        self.dua_amount=0
        self.__order=None
        super().__init__(name, add)

    @property
    def Order(self):
        return self.__order

    @Order.setter
    def Order(self,order):
        self.__order=order

    def Place_order(self,order):
        self.order=order
        print("order owner name",self.name)

    def pay_bill(self,amount):
        if self.wallet >= amount:
            self.wallet -= amount
            return self.wallet
        

    def pay_trips(self,amount):
        self.wallet -= amount
    

    def review(self):
        pass
        
        

class Empolee(User):
    def __init__(self, name, add,salary) -> None:
        super().__init__(name, add)
        self.salary=salary



class Manager(Empolee):
    def __init__(self, name, add, salary,) -> None:
        super().__init__(name, add, salary)


class Cheif(Empolee):
    def __init__(self, name, add, salary,cooking_item) -> None:
        super().__init__(name, add, salary)
        self.cooking_item=cooking_item


    def Cook_item(self):
        pass



class Server(Empolee):
    def __init__(self, name, add, salary) -> None:
        super().__init__(name, add, salary)


    def take_order(self,order):
        self.order=order

    def trsnfer_order(self):
        pass


    def Serve_order(self):
        pass