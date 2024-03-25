menu = "Menu:\
        1. Add a task\
        2. View tasks\
        3. Mark a task as complete\
        4. Delete a task\
        5. Quit:"

tasks = {}

while(True):
    print(menu)
    try:
        inp = int(input())
        if inp == 1:
            task_to_add = input("Please enter a task name: ")
            tasks[task_to_add] = "Incomplete"
        elif inp == 2:
            for task in tasks:
                print(task, tasks[task])
        elif inp == 3:
            task_to_update = input("Please enter a task name to update: ")
            tasks[task_to_update] = "Complete"
        elif inp == 4:
            task_to_delete = input("Please enter a task name to delete: ")
            if task_to_delete in tasks:
                del tasks[task_to_delete]
            else:
                print("Please enter a task that exists within the current tasks!")
        elif inp == 5:
            break
    except ValueError:
        print("Please enter an acceptable int value 1 through 5 inclusive!")
    except OverflowError:
        print("Please enter an acceptable int value 1 through 5 inclusive!")
    except TypeError:
        print("Please enter an acceptable int value 1 through 5 inclusive!")
    finally:
        print("Thank you for using the To-Do list tool!")
