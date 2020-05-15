# Health Management System created by Shourya
# 3 clients - Harry, Rohan and Shourya
print("Welcome to the HMS created by Shourya")

def getdate():
    import datetime
    return datetime.datetime.now()
d = str(getdate())

def retrieve():
    name= str(input("Enter name of client\n"))
    print("Name of the client = "+name)
    var= str(input("Do you want to retrieve data for diet or exercise\n"))
    
    if (name=="Harry" and var=="diet"):
        with open("Harryd.txt") as hd:
            print(hd.read())
    elif (name=="Harry" and var=="exercise"):
        with open("Harryd.txt") as hd:
            print(hd.read())

    elif (name=="Rohan" and var=="diet"):
        with open("Rohand.txt") as rd:
            print(rd.read())
    elif (name=="Rohan" and var=="exercise"):
        with open("Rohane.txt") as re:
            print(re.read())
            
    elif (name=="Shourya" and var=="diet"):
        with open("Shouryad.txt") as sd:
            print(sd.read())
    elif (name=="Shourya" and var=="exercise"):
        with open("Shouryae.txt") as se:
            print(se.read())

def getname():
    name= str(input("Enter name of client\n"))
    print("Name of the client = "+name)
    fl= str(input("Do you want to input data for diet or exercise\n"))
    
    if (name == "Harry" and fl == "diet"):
        with open("Harryd.txt", "a+") as hd:
            fd = input("Enter name of food:\n")
            hd.write("Food eaten at "+d+"\n"+fd+"\n")
        
    elif (name == "Harry" and fl == "exercise"):
        with open("Harrye.txt", "a+") as he:
            ex = input("Enter name of exercise:\n")
            he.write("Exercise done at "+d+"\n"+ex+"\n")

    elif (name == "Rohan" and fl == "diet"):
        with open("Rohand.txt", "a+") as rd:
            fd = input("Enter name of food:\n")
            rd.write("Food eaten at "+d+"\n"+fd+"\n")
        
    elif (name == "Rohan" and fl == "exercise"):
        with open("Rohane.txt", "a+") as re:
            ex = input("Enter name of exercise:\n")
            re.write("Exercise done at "+d+"\n"+ex+"\n")

    elif (name == "Shourya" and fl == "diet"):
        with open("Shouryad.txt", "a+") as sd:
            fd = input("Enter name of food:\n")
            sd.write("Food eaten at "+d+"\n"+fd+"\n")
        
    elif (name == "Shourya" and fl == "exercise"):
        with open("Shouryae.txt", "a+") as se:
            ex = input("Enter name of exercise:\n")
            se.write("Exercise done at "+d+"\n"+ex+"\n")

    else:
        print("Invalid input")




value = str(input("Do you want to 'enter' values or 'retrieve' values\n"))
if(value=="enter"):
    getname()
elif(value=="retrieve"):
    retrieve()
