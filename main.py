from menu import Burger,Pizza,Drinks,Menu
from user import User,Customer,Manager,Cheif,Server
from restuarent import Restuarent
from order import Order

class main():
    def __init__(self) -> None:
        # add item  burger
        menu=Menu()
        bur=Burger('beef burger',180,'beef')
        menu.Add_item(bur,'burger')
        bur2=Burger('chicke burger',180,'chicken')
        menu.Add_item(bur2,'burger')
        bur3=Burger('beef chese burger',220,'beef')
        menu.Add_item(bur3,'burger')


        # add item pizza

        piz=Pizza('piz',280,'small')
        menu.Add_item(piz,'pizza')
        piz2=Pizza('moj',1300,'big')
        menu.Add_item(piz2,'pizza')
        piz3=Pizza('koj',300,'small')
        menu.Add_item(piz3,'pizza')
        


        # Add item drinks

        dr=Drinks('pepsi',20,'cool')
        menu.Add_item(dr,'drinks')
        dr2=Drinks('cocacola',25,'cool')
        menu.Add_item(dr2,'drinks')
        dr3=Drinks('mojo',15,'cool')
        menu.Add_item(dr3,'drinks')

        #menu.Show_menu()



        # add empolle
        # create manager
        res=Restuarent('takeout')
        manager=Manager('sumon','dhanmondi',20000)
        res.add_empolee('manager',manager)

        # Create a chief 

        chief=Cheif('basar','dhanmondi',35000,'everthing')
        res.add_empolee('chief',chief)



        # create a server
        server=Server('noyon','dhanmondi',10000)
        res.add_empolee('server',server)

       # res.Show_empolee(server)
        

        # Add customer

        cus=Customer('atiar','nar',1000)
        order=Order(cus,[piz,bur])
        cus.Place_order(order)
        res.Recive_payment(50000,cus,order)
        
        



    






if __name__=='__main__':
    main()