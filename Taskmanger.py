#--- imports ---#
import os, sys

#--- variables ---#
task_list = []





def task_manager():
    try:
        os.system("cls")
        print("Heres a list of your current tasks:")
        print(task_list)
        print('========================================================')
        print('[1] Delete task(s)')
        print('[2] Add task(s)')
        print('[3] Exit program')
        match input("Choose: "):
            case '1':
                delete_task()
            case '2':
                add_task()
            case '3':
                os.system("cls")
                input("Program terminated")
                sys.exit()
            case _:
                input("Invalid choice, please try again.")
                task_manager()
    except:
        os.system("cls")
        first_task = input("You do not currently have any tasks added please enter your first task: ")
        task_list.append(first_task)

def delete_task():
    os.system("cls")
    for index, task in enumerate(task_list, start=1):
        print(f"[{index}] {task}\n")

    print("\nType 'r' to return to the task manager menu.")
    choice = input("Enter the number of the task you want to delete, or 'r' to return: ")

    if choice == 'r':
        task_manager()

    elif choice.isdigit():
        user_input = int(choice) - 1
        if 0 <= user_input < len(task_list):
            del task_list[user_input]
            print(f"Task successfully deleted.")

        else:
            print("Invalid task number.")

    else:
        print("Invalid input.")
        input()

    input("Press ENTER to continue.")
    task_manager() 


def add_task():
    os.system("cls")
    option = input("Press enter to ad a new task or type 'm' to return to task manger menu: ")
    if option == ('m'):
        task_manager()
    else:
        new_task = input("Enter a new task: ")
        task_list.append(new_task)

    
    task_manager()

    
task_manager()
