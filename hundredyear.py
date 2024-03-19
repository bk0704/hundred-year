name = input("First things first, may I ask for your name: ")
print("Hello " + name + ", welcome to this program were I will tell you in which year you will turn 100 as well as your birthyear")
age = int(input("How old are you: "))
birthyear = int(2024-age)
hundredyear = int(birthyear + 100)
correctornah = input("You were born in " + str(birthyear) + ", is that correct?(enter yes/y or no/n) ")
birthandhunny = str("You were born in " + str(birthyear) + " and you will turn 100 in " + str(hundredyear))
if correctornah == "yes" or correctornah == "y":
    print(birthandhunny)
elif correctornah == "no" or correctornah == "n":
    birthyear = int(birthyear - 1)
    print(birthandhunny)
else:
    print("that is an invalid option, please restart the program and try again")