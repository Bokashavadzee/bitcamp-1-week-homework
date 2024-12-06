# 1 Username წმენდა
# შეამოწმეეთ თუ მომხმარებლის სახელის სიმბოლოების სიგრძე აღემატება 6-ს, მაშინ გამოიტანეთ რომ სახელი ვალიდურია, 
# თუ იგი შეიცავს სფეისებს ან 6 სიმბოლოზე მეტს, მაშინ გამოიტანეთ შეყობინება რომ ის არ არის ვალიდური 
# სანამ ამ ყველაფერს იზამთ მოშორეთ ზედმეტი სფეისები ინფუთს


# def main():
#     username = get_input()
#     validate = cleaned_user(username)
#     if validate:
#         print("this is valid")
#     else:
#         print('this is not valid ')


# def get_input():
#     name = input("Enter Name: ").strip()
#     return name


# def cleaned_user(username):
#     length =len(username)
#     if  length < 6 or " " in username :
#         return False
#     elif length >= 6: 
#         return True
    

# main()

# 2 შექმენით საპაროლე სისტემა

# უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს
# უნდა იყოს მინიმუმ 1 uppercase სიმბოლო
# უნდა იყოს მინიმუმ 1 lowercase სიმბოლო
# თუ პაროლი შეიცავს სიტყვა "password" ამოაგდოს ერორი 


# def main():
#     username  = input("Enter Your Username: ").strip()
#     password =  password_validator(input("Enter Your Password: "))

#     if password == True: 
#         print(f"Welcome {username} you`r loged in")
#     else:
#         print("oops somthings wrong ")



# def password_validator(password):
#     length = len(password)

#     if length >= 8:
#         if password != "password":
#             if password !=  password.lower():
#                 if password != password.upper():
#                      if not password.isalpha():
#                        return True
#     else:
#         return False

# main()


# match cases

# name = input("enter your name ")


# match name:
#     case "boka" | "lasha" | "giorgi" | "merabi" | "givi" | "maxo" :
#         print(name, "you are boy")
#     case "gvanca" | "mariam" | "nini" | "naniko" | "lile" | "eka" :
#         print(name, "you are girl")
#     case _:
#         print("who are you")




# 3



# def main():
#     greeting_input = greeting_regulator(input("Text here: "))
#     print(greeting_input)



# def greeting_regulator(greeting):
#       hello = greeting.startswith("hello") or greeting.startswith("Hello")
#     #   python = greeting.startswith("python") or greeting.startswith("Python")
#       end  = greeting.endswith("!")


#       if hello:
#         return "you are friendly!"
#       elif "python" or "Python" in greeting:
#         return "you are python enthusiast!" 
#       elif end:
#         return "you are excited!"
#       else:
#         return "you are mysterious!"
    

# main()