import datetime
def time():
    return datetime.datetime.now()
print()
print("HI, WELCOME TO THE HEALTH MANAGEMENT SYSTEM :)")
print()
name=''

def _name():

    global name
    name=input("Enter your name: ")
    print()
_name()
def main():
    global name 

    def should_we():
        print()
        again = input('Would you like to add something else(y/n): ')
        if again=='y':
            print()
            main()
        elif again=='n':
            print()
            print('Thanks for using our system :)')
            file.close()
            quit()
        else:
            print('INVALID INPUT :(')
            print()
            should_we()

    todo=input("Which log would you like to access[e(exercise)/f(food)]: ")
    print()
    if name=='harry' and todo=='f':
        file=open('harry_food.txt', 'a+')
        _added=input("What would you like to add: ")
        _time=str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what=='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    elif name=='harry' and todo=='e':
        file=open('harry_exercise.txt', 'a+')
        _added=input("What would you like to add: ")
        _time=str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what=='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    elif name=='rohan' and todo=='f':
        file=open('rohan_food.txt', 'a+')
        _added=input("What would you like to add: ")
        _time=str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what=='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    elif name=='rohan' and todo=='e':
        file=open('rohan_exercise.txt', 'a+')
        _added=input("What would you like to add: ")
        _time=str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what =='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    elif name ==' hammad' and todo == 'f':
        file = open('hammad_food.txt', 'a+')
        _added = input("What would you like to add: ")
        _time = str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what=='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    elif name=='hammad' and todo=='e':
        file=open('hammad_exercise.txt', 'a+')
        _added=input("What would you like to add: ")
        _time=str(time())
        file.write('[')
        file.write(_time)
        file.write(']')
        file.write(' - ')
        file.write(_added)
        file.write('\n')
        file.seek(0)
        print()
        print('Successfully added :)')
        print()
        def _choice():
            choice=input('Would you like to retrieve the data(y/n): ')
            print()
            if choice=='y':
                print('So, the data in your file is:')
                print()
                for i in file:
                    print(i)
                should_we()

            elif choice=='n':
                def _choice_2():
                    what=input('So, would you like to quit(y/n): ')
                    if what=='y':
                        quit()
                    elif what=='n':
                        should_we()
                    else:
                        print('INVALID INPUT :(')
                        _choice_2()
                _choice_2()
            else :
                print()
                print('INVALID INPUT:(')
                print()
                _choice()
        _choice()
    else:
        print('INVALID INPUT :(')
        print()
        _name()
        main()
main()
