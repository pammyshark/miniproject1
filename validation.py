from datetime import datetime
import add_function


# for high, medium and low
def validation_priority(user_input):
    validation_text = {"high", "medium", "low"}
    if user_input in validation_text:
        return user_input
    else:
        new_input = input("Please insert it correctly: ")
        validation_priority(new_input)


# This is to validate the date
def validation_date(user_input):
    try:
        if user_input == datetime.strptime(user_input, "%Y-%m-%d").strftime('%Y-%m-%d'):
            return user_input
    except ValueError:
        validation_date(input("Wrong date format, insert correct: "))

