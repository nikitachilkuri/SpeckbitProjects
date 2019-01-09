""" A class used to represent a Product

   ...
    Attributes
    ----------
    prodid : int
        a variable to store and increment the product id each time a product is being created
    price : int
        a variable to store and display the price of the product
    quantity : int
        a variable to store and display the quantity of the product
    name : str
        a variable to store and display the name of the product

    Methods
    -------
    __init__(self,name,price,quantity)
        constructor that initializes the attribute values 
    """
class Product:
    #statid=0
    prodid=0
    #totval=0
    price=0
    quantity=0
    
    """
        Parameters
        ----------
        price : int
        a variable to store and display the price of the product
        quantity : int
        a variable to store and display the quantity of the product
        name : str
        a variable to store and display the name of the product

        """

    def __init__(self,name,price,quantity):
        #statid+=1
        self.name=name
        self.price=price
        self.quantity=quantity
        Product.prodid+=1
    
""" A class to keep track of various products and sum up the inventory value

   ...
    Attributes
    ----------
    prodlist : list()
        a list to store all the objects created
    ch : int
        a variable to accept choice from user
    prodid : int
        a variable to store and increment the product id each time a product is being created
    price : int
        a variable to store and display the price of the product
    quantity : int
        a variable to store and display the quantity of the product
    name : str
        a variable to store and display the name of the product
    """

class Inventory(Product):
    prodlist=[]
    print("1.New Product \n 2.Display Product details \n 3.Inventory Value \n 4.exit \n")
    while(True):
        print("enter your choice");
        ch=int(input())
        if ch==1:
            name=input("enter name of the product")
            price=int(input("enter price"))
            quantity=int(input("enter the quantity"))
            prodlist.append(Product(name,price,quantity))
        elif ch==2:
            for x in prodlist:
                print("name=",x.name,"price=",x.price,"quantity=",x.quantity)
        elif ch==3:
            val=0
            for i in prodlist:
                val+=i.price*i.quantity
            print("Total value of inventory=",val)
            print("number of products=",Product.prodid)
        elif ch==4:
            exit()
        else:
            print("wrong input")