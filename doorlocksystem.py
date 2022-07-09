# Door lock system Challenge – Task One (Day 3)

from datetime import datetime

def doorlock():
    lock_password = 'qwerty'
    preceding = ''
    password = input("Please enter the doorlock password to proceed: ")
    if password == lock_password:
        print(">> Welcome to the doorlock system!!!")
        print("Please select one of the following: \n > Open \n > Close \n > Quit")                          
        while True:
            print("Enter a command to execute")
            option = input().lower()
            if option == 'open':
                if preceding == 'open':
                    print(">> The door is already open")
                    print(f">> Door last opened at: {time_opened}")
                else:
                    print(">> The door is now open")
                    time_opened = datetime.now()
                    preceding = option
            elif option == 'close':
                if preceding == 'close':
                    print(">> The door is already locked")
                    print(f">> Door last closed at: {time_closed}")
                else:
                    print(">> The door is now locked")
                    time_closed = datetime.now()
                    preceding = option
            elif option == 'quit':
                print(">> Thank you")
                break
            else:
                print(">> Invalid input")
    else:
        print("Sorry. The password is incorrect!.\n Please try again")
        doorlock()

doorlock()