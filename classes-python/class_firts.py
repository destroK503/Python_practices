#object orienten Programming exercise number 1
contact = [2452, 123, 345]

## Create a class phone
class phone:
    def __init__(self, contact): #the init methon is the constructor 
        self.contact = contact
    
    #defining the methods
    def make_call(self, number): #make call to simulate calling
        if number == self.contact[1]:
            print("calling your fried")
            return True
        else:
            print(f"calling {number}")
            

    
    def take_photo(self, amount = None): #take photo to simulate taking photo
        if amount == None:
            print("taking photo")
        else:
            print(f"taking {amount} photos")


#this is an example of how use to classes

class Your_friend_phone:
    def __init__(self):
        pass
    
    def recieve_call(self,):
        print("recieving call from your friend")

cell = phone(contact)
friend = Your_friend_phone()

if cell.make_call(123):
    friend.recieve_call()
cell.take_photo(2)
cell.make_call(2452)

