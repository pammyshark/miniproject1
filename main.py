import inquirer
questions = [
  inquirer.List('choice',
                message="To do list",
                choices=['1. Add Task', '2. Remove Task', '3. View Tasks', '4. Exit'],
            ),
]
answers = inquirer.prompt(questions)
if answers["choice"] == "1. Add Task":
    print(1)
if answers["choice"] == "2. Remove Task":
    print(2)
if answers["choice"] == "3. View Tasks":
    print(3)
if answers["choice"] == "4. Exit":
    print(4)


