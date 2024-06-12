from datetime import datetime
import add_function


#for high, medium and low
def validation_priority(user_input):
    validation_text = {"high", "medium", "low"}
    if user_input in validation_text:
        print("You entered a great priority, congrats!")
        return user_input
    else:
        new_input = input("Please insert it correctly: ")
        validation_priority(new_input)


#This is to validate the date
def validation_date(user_input):
    print(user_input, "flag 1")
    try:
        if user_input == datetime.strptime(user_input, "%Y-%m-%d").strftime('%Y-%m-%d'):
            print(user_input, "flag 2")
            return user_input
    except ValueError:
        print("got here!")
        validation_date(input("Wrong date format, insert correct: "))
    # date_add_date = datetime.date.fromisoformat(user_input)
    # print(date_add_date)
    # if user_input in date_add_date:
    #     print("The date is set.")
    #     return user_input
    # else:
    #     new_input = input("Incorrect date format, please try again.")
    #     validation_date(new_input)

    #while True was here
    # add_date = input("Please add the deadline (YYYY-MM-DD): ")
    # try:
    #     date_add_date = datetime.date.fromisoformat(user_input)
    #     return user_input
    # except ValueError:
    #     print("Incorrect date format, please try again.")
    #     validation_date(user_input)
