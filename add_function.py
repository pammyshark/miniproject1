# To - Do List Application - 1
# 1. Add Task: Allows the user to add a new task to the list.
import pandas as pd
import validation


def task(df):

    # user inputs strings to the add_task
    add_task = input("Please add a task to the list: ")
    add_priority = input("Please choose a priority (high, medium, low): ")
    add_priority = validation.validation_priority(add_priority)
    add_date = input("Please add the deadline (YYYY-MM-DD): ")
    add_date = validation.validation_date(add_date)
    print(f"Awesome! you added {add_task} with {add_priority} due {add_date} to your to-do list")
    # storaging the add_task to the list called "task_list"
    # adding a add_task to the general list task_list
    df_new = pd.DataFrame({"task": [add_task], "priority": [add_priority], "date": [add_date]})
    df_new = pd.concat([df, df_new])

    return df_new
