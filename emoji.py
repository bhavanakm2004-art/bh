emoji={"happy":"😁","sad":"😢","angry":"😡","crying":"😭"}
a=(input("enter your emotion"))
for word in emoji:
         if word in a:
            a=a.replace(word,emoji[word])
            print("emoji message:",a)
