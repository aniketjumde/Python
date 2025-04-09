from importlib.metadata import pass_none

from myerrors.errors import InvalidRollNumberError, InvalidPercentageError, InvalidNameError


def get_rno():
    while True:
        try:
            rno = int(input("Enter the Roll Number : "))
            if rno < 1:
                raise InvalidRollNumberError("InvalidRollNumberError : Negative number not allowed")
        except InvalidRollNumberError as re:
            print(re)
        except ValueError as ve:
            print("Given input is not a Number :", ve)
        except:
            print("Unknown Error !!!")
        else:
            return rno


def get_name():
    while True:
        try:
            name = input("Enter the Name : ")
            if not name.isalpha() :
                raise InvalidNameError("InvalidNameError : Name should have Alphabets")
        except InvalidNameError as ne:
            print(ne)
        except :
            print("Unknown Error !!")
        else :
            return name

def get_per():
    while True:
        try:
            per = float(input("Enter the Percentage : "))
            if per < 0 or per > 100:
                raise InvalidPercentageError("InvalidPercentageError : Percentage Should be between 0 and 100 !!")
        except InvalidPercentageError as pe:
            print(pe)
        except ValueError as ve:
            print("Given input is not a Number :", ve)
        except:
            print("Unknown Error !!!")
        else:
            return per
