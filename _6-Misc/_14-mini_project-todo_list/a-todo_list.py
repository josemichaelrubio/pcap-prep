'''
MY VERSION OF THE TODO_LIST PROJECT
'''

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
                #self.show_tasks()
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

        try:
            stream = open('tasks.csv', 'r')
            csv_reader = csv.reader(stream)
            next(csv_reader, None)
            rows = list(csv_reader)
            print( len(rows) )
            if len(rows) == 0:
                print('No tasks to show.')
            else:
                for row in rows:
                    print(row)
            stream.close()
        except Exception as e:
            print('An error occurred: ', e)
            print('Exiting the program...')
            exit()
        finally:
            self.main_menu()

    def add_task(self):
        csv_file = 'tasks.csv'
        def get_last_id(filename):
            try:
                with open(filename, 'r', newline='') as csvfile:
                    rows = list(csv.reader(csvfile))
                    if not rows or int(rows[-1][0]) == 'id':
                        return 0
                    return int(rows[-1][0])
            except Exception as e:
                print(e)
                return 0
                
        def add_entry_with_unique_id(filename):
            last_id = get_last_id(filename)
            new_id = last_id + 1
            with open (filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                task = []
                description = input('Enter task description: ')
                deadline = input('Enter deadline: ')
                task.append(description)
                task.append(deadline)
                writer.writerow([new_id] + task)
        add_entry_with_unique_id(csv_file)
        self.main_menu()

    def complete_task(self):
        try:
            def delete_task(unique_id):
                with open ('tasks.csv', 'r', newline='') as csvfile:
                    records = list(csv.reader(csvfile))
                
                records = [record for record in records if record[0] !=str(unique_id)]

                with open ('tasks.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(records)
                
            input_id = int(input('Enter the id of the task you want to complete: '))
            delete_task(input_id)
            print('Task has been completed.')
            
        except Exception as e:
            print('An error occurred: ', e)
            print('Exiting the program...')
            exit()
        finally:
            self.main_menu()

    def exit(self):
        print('Goodbye!')
        exit()

def main():
    todo = todo_list()
    todo.main_menu()

main()