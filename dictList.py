dict1 = {"title":"Harry Potter and the Sorceror's Stone", "author":"J.K Rowling", "year":"1997"}
dict2 = {"title":"The Lord of the Rings: the Two Towers", "author":"J.R.R Tolkien", "year":"1954"}
dict3 = {"title": "The Great Gatsby", "author":"F. Scott Fitzgerald", "year":"1925"}
li = [dict1,dict2,dict3]

def findauth(title, li):
    for i in li:
        if i.title == title:
            print("Title and author found")
            print(i.author)
            author = i.author
            return author
    print("Title not found and author not found")

def addBook(addedbook, li):
    
    if addedbook.title != None:
        if addedbook.author != None:
            if addedbook.year != None:
                li.add(addedbook)
    

