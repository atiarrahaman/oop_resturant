class Restuarent:
    def __init__(self,name) -> None:
        self.name=name
        self.manager=[]
        self.chief=[]
        self.server=[]
        self.sale=0
        self.cash=0
        self.expens=0


    def add_empolee(self,empolee_type,empolee):
        if empolee_type == 'manager':
            self.manager.append(empolee)

        elif empolee_type == 'chief':
            self.chief.append(empolee)

        elif empolee_type == "server":
            self.server.append(empolee)
    
    def Show_empolee(self,empolee):
        if self.manager is not None:
            print(f'name:{empolee.name}')
    
    def Recive_payment(self,amount,customer,order):
        if amount >= order.bill:
            self.sale +=order.bill
            self.cash +=order.bill 
            customer.dua_amount=0
            print(self.sale)
            print(f'return mony {amount - order.bill}')


    def pay_expensive(self,amount,text):
        if self.cash > amount:
            self.cash -= amount
        

            