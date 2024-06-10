# Remove a task from the to-do list.

def remove_tasks(tdl):
    remove1 = input("Write a task you want to remove: ")
    print(remove1)
    tdl.remove(remove1)
    print(tdl)
    return tdl
