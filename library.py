book=[("1","Of Mice and Men", "John Steinbeck",1998,"2","The Little Prince ","Antoine de Saint-Exupery","3","The Old Man and the Sea","Ernest","4","the grapes of wrath","John Steinbeck")]
while True:
    print("\n 1.search 2. display 3. count")
    choice = input("enter choice:")
    if choice=="1":
         a=(input("enter the id or title to search"))
         book.search(a)
         print("search found ")
