# --------------------------
# Notes:
# This code demonstrates the use of `try-except` blocks to handle multiple types of runtime errors.
# It handles:
# - ValueError when invalid input is given
# - ZeroDivisionError when dividing by zero
# - Any other unexpected errors using a general Exception handler
# --------------------------
while True:
    # explain the try and except , chatgot will do it !
    try :
        a= int(input("enter number 1: ")) # now it expects to always input integer , but what if we enter a string ?? will through error right ... what can we do for this
        b= int(input("enter number 2: "))
        # Attempt division and print the result
        print (f'The divis {a/b}')
    except ValueError:
        print(f" please  dont  perform bad typecast")

    except ZeroDivisionError:
        print(f" hey dont divide by 0 ")

    except Exception as e:
        print(f"Unknown error occured : " , e)

        


