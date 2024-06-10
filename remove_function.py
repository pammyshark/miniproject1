# Remove a task from the to-do list.
a = ["a", "b", "c"]
def remove_tasks ():
    remove1 = input("Write a task you want to remove")
    print(remove1)
    a.remove(remove1)
    print(a)

remove_tasks()