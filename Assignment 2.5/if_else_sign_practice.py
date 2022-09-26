def main():
    age = input("Enter your age: ")
    age = int(age)
    if age >= 25:
        print("You can buy alcohol, nicotine products, and rent a car")
    elif age >= 21 and age <25:
        print ("You can buy alcohol, nicotine products, but can't rent a car")
    elif age >= 18 and age <21:
        print ("you can only buy nicotine products in some states")
    elif age < 18:
        print ("you can only buy candy cigarettes and sody pops")

main()
