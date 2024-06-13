# Remove a task from the to-do list.
import inquirer


def remove_tasks(tdl):
    task_list = tdl["Task"].tolist()
    questions = [
        inquirer.Checkbox('choice',
                          message="To do list",
                          choices=task_list,
                          ),
    ]
    answers = inquirer.prompt(questions)
    for i in answers["choice"]:
        tdl.drop(tdl[tdl["Task"] == i].index, inplace=True)
        print(f"{i} has been removed from the list.")

    return tdl
