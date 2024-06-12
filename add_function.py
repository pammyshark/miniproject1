# To - Do List Application - 1
# 1. Add Task: Allows the user to add a new task to the list.
import pandas as pd


def task(tdl):

    # user inputs strings to the add_task
    add_task = input("Please add a task to the list: ")
    add_priority = input("Please choose a priority between 1-10: ")
    add_date = input("Please add the deadline (YYYY-MM-DD): ")
    print(f"Awesome! you added {add_task} with {add_priority} due {add_date} to your to-do list")
    # storaging the add_task to the list called "task_list"
    # adding a add_task to the general list task_list
    df = pd.DataFrame({"task": [add_task], "priority": [add_priority], "date": [add_date]})
    print(df)
    tdl.append(add_task)

    return df
