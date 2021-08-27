#Name: Sean (Seunguk) Kim


class Product:
    """
    Data type to represent a Product
      
    Instance attributes: name(str), productCode(str), type(str), typeCode(str), soldCount(int) stock(int), price(float), cost(float)
    Class attributes: totalNumPro(int)
    """
    totalNumPro = 0

    def __init__(self, name, productCode, type, typeCode, soldCount, stock, price, cost):
        # Check if two codes are valid
        # ProductCode must be five digit integer
        if len(productCode) != 5 or not productCode.isdigit():
            raise ValueError("Invalid product code")
        # TypeCode must be three digit alphabet
        if len(typeCode)!= 3 or not typeCode.isalpha():
            raise ValueError ("Invaild type code")
        
        self.name = name
        self.productCode = productCode
        self.type = type
        self.typeCode = typeCode
        self.soldCount = soldCount
        self.stock = stock
        self.price = price
        self.cost = cost

        # Update the total number of products
        Product.totalNumPro += 1

    def __str__(self):
        return self.name +"\t"+ self.typeCode +"-" + self.productCode + "\t" + self.price + "\t" + self.cost + "\t" + self.stock + "\t" + self.soldCount

    def addProduct(cls):
        name = input("Enter the name of product: ")
        typeCode = input("Enter the type code (three alphabet): ")
        productCode = input("Enter the product code (five digit number): ")
        


        return Product(name, )

    
