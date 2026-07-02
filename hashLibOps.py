import hashlib

print(hashlib.algorithms_guaranteed)
h = hashlib.new("SHA256")
randomPassword = "SOMEPASSWORD12345678"
anotherPassword = "ABUNCHOFTHINGS"
h.update(randomPassword.encode())

hash = h.hexdigest()
print(hash)

ht = []

def insert(ht, password): #Inserts a hash into h
    h.update(password.encode())
    ht.append(h.hexdigest())      


def get(ht, h): #Only gets the current implemented hash in h
    for i in ht:
        if i == h:
            print(i)
            return i

insert(ht, randomPassword)
print(ht)
        
    