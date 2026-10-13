try:
    number = int(input("Enter a age: "))
    print("The age entered is", number)
    if number%2==0:
        print("Age is even")
    elif number%2==1:
        print("Age is odd")
except ValueError as ex:
    print("Exception:", ex)