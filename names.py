# month = int(input("Enter number and it wil convert to month "))

# match month:
#     case 1:
#         print("its january ")
#     case 2:
#         print("its February ")
#     case 3:
#         print("its March ")
#     case 4:
#         print("its April ")
#     case 5:
#         print("its may")
#     case 6:
#         print("its July")
#     case 7:
#         print("its juny")
#     case 8:
#         print("its August")
#     case 9:
#         print("its September")
#     case 10:
#         print("its Oqtober")
#     case 11:
#         print("its November")
#     case 12:
#         print("its December")
#     case _:
#         print("its not a month")



                                                                             # With function

def main():
    month = int(input("Enter number and it will convert to month: "))
    print(month_converter(month))



def month_converter(num):
        match num:
            case 1:
                return("its january ")
            case 2:
                return("its February ")
            case 3:
                return("its March ")
            case 4:
                return("its April ")
            case 5:
                return("its may")
            case 6:
                return("its July")
            case 7:
                return("its juny")
            case 8:
                return("its August")
            case 9:
                return("its September")
            case 10:
                return("its Oqtober")
            case 11:
                return("its November")
            case 12:
                return("its December")
            case _:
                return("its not a month")
            
main()

