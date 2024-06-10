# To - Do List Application - 1
# 1. Add Task: Allows the user to add a new task to the list.
import pandas
def task(add_task):
    # user inputs strings to the add_task
    add_task = input("Please add a task to the list: ")
    print(f"Awesome! you added {add_task} to your to-do list")
    # storaging the add_task to thee list called "task_list"
    task_list = []
    # adding a add_task to the general list task_list
    task_list.append(add_task)
    print(task_list)

task("")

