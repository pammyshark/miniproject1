import inquirer
import add_function
import validation
import remove_function
import display_tasks


def user_input(tdl):
    questions = [
        inquirer.List('choice',
                      message="To do list",
                      choices=['1. Add Task', '2. Remove Task', '3. View Tasks', '4. Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers["choice"] == "1. Add Task":
        tdl = add_function.task(tdl)
        user_input(tdl)
    if answers["choice"] == "2. Remove Task":
        tdl = remove_function.remove_tasks(tdl)
        user_input(tdl)
    if answers["choice"] == "3. View Tasks":
        display_tasks.print_TDL(tdl)
        user_input(tdl)
    if answers["choice"] == "4. Exit":
        exit()
