import datetime

#This is to validate priority but in a range of 1 to 10
def validation_priority():
    while True:
        add_priority = input("Please choose a priority between 1-10: ")
        try:
            int_add_priority = int(add_priority)
            if 1 <= int_add_priority <= 10:
                print("You entered a great priority, congrats!")
                return int_add_priority
            else:
                print("The number is not in the range 1 - 10. Please try again.")
        except ValueError:
            print("This is not a number, please try other one")

validation_priority()

#for high, medium and low
def validation_priority():
    validation_text = {"high", "medium", "low"}
    while True:
        add_priority2 = input("Please choose a priority between high, medium or low: ")
        if add_priority2 in validation_text:
            print("You entered a great priority, congrats!")
            return add_priority2
        else:
            print("The priority is not written as high, medium or low. Please try again.")
validation_priority()

#This is to validate the date
def validation_date():
    while True:
        add_date = input("Please add the deadline (YYYY-MM-DD): ")
        try:
            date_add_date = datetime.date.fromisoformat(add_date)
            return True
        except ValueError:
            print("Incorrect date format, please try again.")
validation_date()