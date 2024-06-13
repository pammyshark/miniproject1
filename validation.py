from datetime import datetime
import add_function


# for high, medium and low
def validation_priority(user_input):
    validation_text = {"high", "medium", "low"}
    if user_input in validation_text:
        return user_input
    else:
        new_input = input("Please insert it correctly: ")
        return validation_priority(new_input)


# This is to validate the date
def validation_date(user_input):
    try:
        valid_date = datetime.strptime(user_input, "%Y-%m-%d")
        return valid_date.strftime('%Y-%m-%d')
    except ValueError:
        new_input = input("Wrong date format, insert correct: ")
        return validation_date(new_input)

