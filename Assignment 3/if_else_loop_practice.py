def main():

    numbers = [2, 17, 25, 29, 33, 39, 42, 49]

    for number in numbers:
        if number > 35:
            print("{} is greater than 35".format(number))
        elif number >= 20 and number <= 35:
            print("{} is between 20-35".format(number))
        elif number >= 5 and number <=20:
            print("{} is between 5 and 20".format(number))
        else:
            print("{} is less than 5".format(number))

main()
