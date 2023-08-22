# def kbc():
#     while(True):
#         print("A:Tiger  B:Lion \nC:Jaguar D:Cheetah")
#         n = (input("What is the national animal of India: "))
#         n = n.lower()
#         if (n == "a" or n == "tiger"):
#             print("7 crore")
#             break
#         else:
#             print("Yeh galat jawab hai")
#             continue
# kbc()


l=[["What is the national animal of India","Tiger","A:Tiger  B:Lion \n  C:Jaguar D:Cheetah"],["What is the national animal of India","Peacock","A:Tiger  B:Crocodile \n  C:Peacock  D:Magarmacchh"]]

def game():
    for i in l:
        print("Quesion\n ",i[0])
        print("OPtion\n ",i[2])
        user=input("Enter your anser: ")
        if user.lower()==i[1].lower():
            print("HAAAN Merii JAAAN!!!")
            print("------------------------------------\n")
        else:
            print("Nikal LAVDEEE")
            break
    
    
d=input("Do you want to play a KBC: ")
if d=="Yes" or d=="yes":
    game()
else:
    print("jaldi yaha niklo")
    