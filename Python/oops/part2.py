'''
1. Class Atributes 
2. instance Attributes
3. Static Attributes'''

# class DataBaseConnection:
#     # class attribute
#     host='localhost'
#     port=5000

#    # instance/objects attributes
#     def __init__(self,u,p):
#         self.user=u
#         self.password=p

#     @classmethod
#     def change_port(cls):
#         cls.port= 100
#         return cls.port


# user1= DataBaseConnection("yamuna",12345)
# user1.port= 1000
# print(vars(user1))

# user2= DataBaseConnection("Kasi",567989)

# DataBaseConnection.change_port()
# print(user1.port,user2.port)


# Static Attributes--- we dont use class and objects -- independent of both 

# class DataBaseConnection:
#     # class attribute
#     host='localhost'
#     port=5000

#    # instance/objects attributes
#     def __init__(self,u,p):
#         self.user=u
#         self.password=p

#     @classmethod
#     def change_port(cls):
#         cls.port= 100
#         return cls.port
    
#     @staticmethod
#     def validate_password(password):
#         return len(str(password)) >=6

# user1= DataBaseConnection("yamuna",123456)
# print(vars(user1))


# print(user1.validate_password(user1.password))
# print(DataBaseConnection.validate_password(user1.password))


# staticmethod,classmethods -- call wrt classes not with object

'''Class Attributes and Methods**
*   Class attributes
*   These belong to the class itself (not individual objects).
*   Defined at the class level (outside of methods, same indent as def).
*   Shared by all instances.
*   If you change a class attribute, it affects everyone (unless overridden).'''








'''
You have a Product class with total_products as a class attribute. Explain how it would behave if you modify it via an instance vs the class.

How would you prevent users from purchasing more than available stock in a Product class?

In an e-commerce system, how would you implement a discount feature using class methods or static methods?

Explain a scenario where using a static method is more beneficial than an instance method in your Customer or Product class.

How would you implement an alternative constructor using @classmethod?

If multiple customers are purchasing products at the same time, how can class attributes like total_products or stock cause issues, and how would you handle it?
'''




'''Product class (attributes-- id,name,price,quantity,discount,tax,category)                , customer class (id,name,address,phonenumber,productname, quantity)'''
class Product:
    total_products= 0      # class atrributes
    producst_list=[]

    def __init__(self,id,name,price,qunatity,category,discount=0):
        self.product_id=id
        self.product_name= name
        self.__prodct_price= price
        self.__product_qunatity=qunatity    # private attributes 
        self.__product_discount=discount
        self.category= category
        Product.total_products+=1
        Product.producst_list.append(vars(self))

    def get_price(self):
        return self.__prodct_price
    
    def set_price(self):
        price = float(input("Enter the product price u want to change: "))
        self.__prodct_price=price

    # class also instance
    @staticmethod
    def validate_quantity(qty):
       return isinstance(qty,int) and qty > 0
    
    
    # instance method
    def purchase(self,quty):
        if Product.validate_quantity(quty):
            if quty <= self.__product_qunatity:
                self.__product_qunatity-=quty    # reduce the product count after purchased
                total_price= quty * self.__prodct_price
                print(f"{self.set_discount()} % is applied")


                total_price=  total_price- (self.apply_discount(self.category)*100)
                print(f"Product purchased sucessfully , total price is {total_price}")
            else:
                print(f"Only {self.__product_qunatity} {self.product_name} is available")
                return 0
        else:
            print("Invalid qunatity entered")
            return 0
        
    @staticmethod
    # create fun for discount based on the category, if electronics 2% -- final totalprice
    def apply_discount(category):
        if category == "electronics":
            discount_percentage=10
            return discount_percentage
        
    def set_discount(self):
           self.__product_discount= self.apply_discount(self.category)
           return self.__product_discount
           


p1= Product(1,"Headphone",1000,2,"electronics")
# print(vars(p1))
# Product.producst_list.append(vars(p1))

p2= Product(2,"smartphone",5000,5,2,"electronics")
# Product.producst_list.append(vars(p2))


print(Product.producst_list)
print(len(Product.producst_list))


p1.purchase(1)

# print(Product.total_products)
