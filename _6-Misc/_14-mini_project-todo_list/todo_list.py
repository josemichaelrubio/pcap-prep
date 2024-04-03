# TODO:
#// main menu

# 2. Add Task
#  a. User enters task description and deadline
#  b. Program generates a unique id for the task
#  c. Store the task in a text file
#  d. After adding the task, the program goes back to the main menu
# 3. Complete task
#  a. Show the list of all existing tasks
#   i. If there are no tasks, show a message and go back to the main menu
#  b. User enters the id of the task to complete
#  c. Remove the task from the list of the text file
#  d. After completing the task, the program goes back to the main menu
# 4. Exit

import csv

class todo_list:
    def __init__(self):
        self.tasks = []
    
    def main_menu(self):

        try:
            stream = open('tasks.csv', 'a')
            print('\n')
            print(' == TODO LIST == ')
            print('1. Show Tasks')
            print('2. Add Task')
            print('3. Complete Task')
            print('4. Exit')
            print('\n')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.exit()
            else:
                print('Invalid choice. Please try again.')
                self.main_menu()
            
            stream.close()
        except Exception as e:
            print('An error occurred: ', e)
            print('Exiting the program...')
            exit()

    def show_tasks(self):
        print('1. == TASKS ==')
# 1. Show Tasks
#//  a. current to-do list with all the tasks loaded from a text file
        try:
            stream = open('tasks.csv', 'r')
            csv_reader = csv.reader(stream)
            next(csv_reader)
            if csv_reader == None:
                print('No tasks to show.')
            else:
                for row in stream:
                    print(row)
            stream.close()
        except Exception as e:
            print('An error occurred: ', e)
            print('Exiting the program...')
            exit()
        finally:
            self.main_menu()
# TODO   i. If there are no tasks, show a message and go back to the main menu
#//  b. each task shoud show: id, task description, deadline
#//  c. After showing the list, the program goes back to the main menu

    def add_task(self):
        print('inside add_task')

    def complete_task(self):
        print('inside complete_task')

    def exit(self):
        print('Goodbye!')
        exit()


def main():
    todo = todo_list()
    todo.main_menu()

main()