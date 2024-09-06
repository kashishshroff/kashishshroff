
def is_key_exist(key,mydict):
    if key in mydict.keys():
        return True
    else:
        return False
    

def valkey(key):        
    if not str(key).isnumeric():
        return "Key should be numeric !"
    
    elif key not in range(1,61):
        return "Key should be in range of 1 to 60 !"

    else:
        return True
           
def valname(name):
    if not name.isalpha():
        return "Name should be only Alphabets"
    else:
        return True

def valmark(mark):
    if not str(mark).isnumeric():
        return "Marks should be numeric"
    
    elif mark not in range(1,101):
        return "Marks should be in range of 1-100"

    else:
        return True
    
    
def insert(key,mydict):
    
    innerdict = {}
    print("Enter Student Information:")

        name = input("Name:")
        if valname(name) == True:
            innerdict["name"] = name.title()
            
            print("Marks:")
            p = input("Physics:")
            c = input("Chemistry:")
            m = input("Maths:")

            if valmark(p) and valmark(c) and valmark(m) == True:                
                innerdict["P"] = float(p)
                innerdict["C"] = float(c)
                innerdict["M"] = float(m)
            
                mydict[key] = innerdict
            else:

                if type(valmark(p)) != bool:
                    print("Physics: " +  valmark(p))
                if type(valmark(c)) != bool:
                    print("Chemistry: " + valmark(c))
                if type(valmark(m)) != bool:
                    print("Maths: " + valmark(m))
                                           
                    print("INCORRECT TRY AGAIN ! ")
                    
                    
        else:
                print(valname(name))
                print("INCORRECT TRY AGAIN ! ")
                          





    
def create(mydict):

    
    print("CREATE")
    key = int(input("Enter Rollno: "))
    
    if valkey(key) == True:
        if is_key_exist(key,mydict) == False:
        insert(key,mydict)
        
        else:
            print(valkey(key))
            print("INCORRECT TRY AGAIN ! ")      
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")
        

            

def remove(mydict):
    print("REMOVE")
    key = input("Enter Key : ")
    
    if is_key_exist(key) == True:
        print("Deleted item : ")
        print(mydict.pop(key,"INVALID KEY"))
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")

    

def update(mydict):
    print("UPDATE")
    key = input("Enter Key : ")
    
    if valkey(key) == True:
        if is_key_exist(key,mydict) == True:
            insert(key,mydict)
        
        else:
            print("Roll no doesnt exist")
            print("INCORRECT TRY AGAIN ! ")      
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")
        
        

def display(mydict):
    print("DISPLAY")
    key = input("Enter Key : ")
    
    if valkey(key) == True:
        if is_key_exist(key,mydict) == True:
            print(mydict[key])
        
        else:
            print("Roll no doesnt exist")
            print("INCORRECT TRY AGAIN ! ")      
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")
        
    
    


def crud():

    mydict = {}
    choice = 1
    
    while True:
        choice = int(input(" 1. CREATE \n 2. REMOVE \n 3. UPDATE \n 4. DISPLAY \n 5. EXIT \n "))
        
        if choice == 1:
            create(mydict)
            
        elif choice == 2:
            remove(mydict)
            
        elif choice == 3:
            update(mydict)            
            
        elif choice == 4:
            display(mydict)
            
        else:
            break
    
crud()
