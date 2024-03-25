#     Project Requirements

#     User Interface (UI):

#         Create a command-line interface (CLI) for the To-Do List Application.

#         Display a welcoming message and a menu with the following options:

#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit

#     To-Do List Features:
#         Implement the following features for the To-Do List:
#             Adding a task with a title (by default “Incomplete”).
#             Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
#             Marking a task as complete.
#             Deleting a task.
#             Quitting the application.

#     User Interaction:
#         Allow users to interact with the application by selecting menu options using input().
#         Implement input validation to handle unexpected user input gracefully.

#     Error Handling:
#         Implement error handling using try, except, else, and finally blocks to handle potential issues.

#     Code Organization:
#         Organize your code into functions to promote modularity and readability.
#         Use meaningful function names with appropriate comments and docstrings for clarity.

#     Testing and Debugging:
#         Thoroughly test your application to identify and fix any bugs.
#         Consider edge cases, such as empty task lists or incorrect user input.

#     Documentation:
#         Include a README file that explains how to run the application and provides a brief overview of its features.

#     Optional Features (Bonus):
#         If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

#     GitHub Repository:
#         Create a GitHub repository for your project.
#         Commit your code to the repository regularly.
#         Include a link to your GitHub repository in your project documentation.

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
