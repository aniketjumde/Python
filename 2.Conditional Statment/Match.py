#Accept number and Display it 1= 0ne
num=input("Enter the Number :")
match num:
    case '1' :
        print("One")
    case '2' :
        print("Two")
    case '3' :
        print("Three")
    case '4' :
        print("Four")
    case '5':
        print("Five")
    case '6':
        print("Six")
    case '7':
        print("Seven")
    case '8':
        print("Eight")
    case '9':
        print("Nine")
    case '0':
        print("Zero")
    case _:
        print("Invalid Option....!")