list=["apple","orange","grapes"]
print(list)
print(list[0])
print(list[1:2])
list.append("mango")
print(list)
if "apple"in list:
    print ("apple is present")
else:
    print("not present")
list.remove("orange")
print(list)    
while True:
    print("\n 1.add 2. view 3. exit")
    choice = input("enter choice:")
    if choice=="1": 
        a=input("enter item:")   
        list.append(a)
        print("item added successfully")
    elif choice=="2":
        for i,it in enumerate(list,start=1):
             print(i,it)
    else:
        print("exit")    
        break 
    print(list)

list=[{"item":"apple","quantity":"1kg","price":200},
         {"item":"grapes","quantity":"1kg","price":200},
         {"item":"orange","quantity":"1kg","price":200}]  

while True:
    item=(input("enter the item"))
    quantity=(input("enter the quantity"))
    price=(input("enter the price"))
    list.append({"item":item,"quantity":quantity,"price":price},)
    print(f"added:{item} qty:{quantity} price:{price}")
    print(list)
# while True:
#     item=(input("enter the item"))
#     quantity=(input("enter the quantity"))
#     price=(input("enter the price"))
#     list.append({"item":item,"quantity":quantity,"price":price},)
#     print(f"added:{item} qty:{quantity} price:{price}")
#     print(list)


# for i in list:
#     print(i)   
