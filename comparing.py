first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))



def largest_num(x,y,z):
    if x == z and y == z  and   x == y:
        print("Error thes numbers are same")
    elif x > z and x > y:
        print(f"the latgest number is {x}")
    elif y > x and y > z:
        print(f"the largest number is {y}")
    elif z > x and z > y:
        print(f"the largest number is {z}")
    else:
        print("Eroor")

    
largest_num(first_num,second_num,third_num)



