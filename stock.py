stock=input("What is your current stock: ")
if int(stock) < 100: 
    print ("Stock under the limit, we send the new stock order")
    print ("Please send email to stock@me.com")
    restock_1=input("How much you restock?: ")
    restock_=int(stock)+int(restock_1)
    stock=restock_
    print(f"The stock now its {stock}")

else:
    print("Your stock is fine")


#Same excerise but with a while
print("WHILE VERSION=======")
stockwhile=input("What is your current stock: ")
while int(stockwhile) < 100: 
    print ("Stock under the limit, we send the new stock order")
    print ("Please send email to stock@me.com")
    restock=input("How much you restock?: ")
    stockwhile=int(stockwhile)+int(restock)
    print(f"The stock now its {stockwhile}")
else:
    print("Your stock is fine")
