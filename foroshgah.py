from foroshgah_db_fun import main, tables, items
from password import generate_password

creat = tables.create_tables()
def manager():
    while True :
        work  = int(input("""what are you here for ?
1.add item
2.delet item
3.edit item
4.cheak taskbar
5.exit 
    """))
        if work == 1 :
            name = input("enter the name of the item : ")
            price = input("enter the price of the item : ")
            description = input("write a description for the item : ")
            topic = input("chose a topic : ")
            new_item = items.add_item(name , price , description , topic)
            print("item added successfully")
        elif work == 2 :
            name = input("enter the name : ")
            id = input("enter the id : ")
            delete = items.delete_item(id , name)
            if delete == True:
                print("item deleted successfully")
            else:
                print("try again")
        elif work == 3 :
            topics = ["name" , "price" , "description" , "topic"]
            id = input("enter the id : ")
            topic = input("what are you going to change (name / price / description / topic ) : ")
            while topic in topics :
                new_data = input("enter the new data : ")
                update = items.update(id , topic, new_data)
                if update == True:
                    print("data updated")
                    break
                else:
                    print("not ok ")
        elif work == 4 :
            pass
        elif work == 5 :
            break



def customer():
    while True:
        kar = int(input("""what are you here for ?
    1.see items
    2.sabad khrid
    3.history 
    4.exit
    """))
        if kar == 1 :
            cheak_topic = int(input("""chose a topic : 
1.cloth
2.technology
3.food
4.show me all of theme . 
"""))
            if cheak_topic == 1 :
                list = items.filter("cloth")
                for i in list :
                    print(i)
            elif cheak_topic == 2 : 
                list = items.filter("technology")
                for i in list :
                    print(i)
            elif cheak_topic == 3 :
                list = items.filter("food")
                for i in list :
                    print(i)
            elif cheak_topic == 4 :
                list = items.show_all_items()
                for i in list :
                    print(i)
            
        elif kar == 2 :
            pass
        elif kar == 3 :
            pass
        elif kar == 4 :
            break
def ghabl_vorod():
    while True: 
        darkhast = int(input("""1.singup
2.login
3.exit
"""))
        if darkhast == 1 :
            name = input("enter your name : ")
            last_name = input("enter your last_name : ")
            username = input("choose a username for your self : ")
            while True :
                try:
                    phone_number = int(input("enter the phone number : "))
                    break
                except:
                    print("mojadad talash konid")
            pass_sug = int(input("""do you want us to suggest you a password or you are going to make it yourself ?  
1.us
2.myself
"""))
            if pass_sug == 1 :
                password = generate_password(8)
            elif pass_sug == 2 :
                password = input("enter your pass : ") 
            new_customer = main.add_customer(name, last_name, str(phone_number), username, password)
            print(new_customer)
            print("     \\\welcome///    ")
            customer()
        
        if darkhast == 2 :
            try:
                man_cust = int(input("""you are a manager or a customer ?
1.manager
2.customer
"""))
            except:
                print("enter number")
            if man_cust == 1 :
                x = 1
                while x < 4:
                    username = input("enter your username: ")
                    password = input("enter your password: ")
                    if main.check_manager(username, password):
                        print("manager exists.")
                        manager()
                        break 
                    else:
                        print("Invalid username or password.")
                        x = x + 1
                        if x == 4:
                            print("Too many failed attempts. Please try again later.")

            if man_cust == 2 :
                x = 1
                while x < 4:
                    username = input("enter your username: ")
                    password = input("enter your password: ")
                    if main.check_customer(username, password):
                        print("User exists.")
                        customer()
                        break 
                    else:
                        print("Invalid username or password.")
                        x = x + 1
                        if x == 4:
                            print("Too many failed attempts. Please try again later.")
        if darkhast == 3 :
            break
        
ghabl_vorod()