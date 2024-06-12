# To - Do List Application - 1
# 1. Add Task: Allows the user to add a new task to the list.
import pandas as pd
import validation


def task(df):
    # user inputs strings to the add_task
    add_task = input("Please add a task to the list: ")

    # add priority and validate
    add_priority = input("Please choose a priority (high, medium, low): ")
    add_priority = validation.validation_priority(add_priority)

    # receiving date and validating it
    add_date = input("Please add the deadline (YYYY-MM-DD): ")

    add_date = validation.validation_date(add_date)

    # after receiving all the info, in correct form, display it

    print(f"{add_task} with priority {add_priority} and deadline {add_date} has been added to your list")
    # storaging the add_task to the list called "task_list"

    # adding add_task to the general list task_list

    df_new = pd.DataFrame({"Task": [add_task], "Priority": [add_priority], "Deadline": [add_date]})

    df_new = pd.concat([df, df_new], ignore_index=True)

    return df_new
