# This function is the entry point of our program
def main():
    # We get a positive integer value from the user
    number = get_number()
    # We then pass that value to another function called "meow"
    meow(number)


# This function asks the user to input a positive integer value and returns it
def get_number():
    # We use a while loop that keeps asking for input until a valid integer is entered
    while True:
        n = int(input("What is n? :"))
        # We check if the integer entered is greater than 0
        if n > 0:
            # If it is, we break out of the loop and return the value
            break
    return n


# This function prints the word "meow" "n" number of times
def meow(n):
    # We use a for loop to print "meow" "n" number of times
    for _ in range(n):
        print("meow")


# We call the "main" function to start the program
main()
