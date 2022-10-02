def main():
    # Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print ("hello")

    # What about as a while loop?
    loops = 2
    while (loops < 3):
        print ("hello")

    # The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 0
    while (count < 3):
        print("While loop iteration", count)
        count = count + 2

    # Same deal here!
    for x in range(3):
        print("For loop iteration:", x)

    # Uh oh I messed up and made an infinite loop... so silly of me!
    endless = 7
    while (endless < 5):
        print("I'm stuck in this loop!!!!")

    # print out your last name one letter at a time
    name = ["f", "a", "i", "x"]
    for x in name:
        print(x)

        # aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once... starts with a b... br....
        found == False
        while found == False:
            break
            print("i only printed once")

        # can you fill this out so that it prints found when it hits the letter r?
        for val in "Marist":
            if val == "r":
                print("found")

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out the value of each index :)
        print(numbers)


        lower_limit = int(input("20"))
        upper_limit = int(input("501"))

    for i in range (lower_limit,upper_limit+1):
         if(i%2 == 0):
            print(i)

main()
