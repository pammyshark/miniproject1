def validation():
    while True:
        add_priority = input("Write something: ")
        try:
            int_add_priority = int(add_priority)
            print("You entered a great priority, congrats!")
            return int_add_priority
        except ValueError:
            print("This is not a number, please try other one")

validation ()