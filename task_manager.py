#=====importing libraries===========
from datetime import date

#====Function definition 
def date_conversion(user_date):
    #This takes a string and converts it into a date object
    due_date_split = user_date.split('-')
    due_day = int(due_date_split[2])
    due_month = int(due_date_split[1])
    due_year = int(due_date_split[0])
    converted_date = date(due_year, due_month, due_day)
    return converted_date

def reg_user():
    if username != "admin":
        print()
        print("You must be an admin to register new users")
        print()
    else:
        #Reopens the users file for writing to the end of the file
        users = open('user.txt', 'a+')
        #Gets the new username
        new_user = input("Please input the new username: ")
        while True:
            #Checks whether the username is already contained within the user database as a username. 
            if (new_user in entries) and (entries.index(new_user) % 2 == 0):
                new_user = input("That username is already in use. Please select a different username: ")
                continue
            else:
                break
        while True:
            #Gets the user's password. If the two entered passwords do not match, the loop repeats again.
            new_pass = input("Please choose your password: ")
            confirm_pass = input("Please confirm your password: ")
            if new_pass != confirm_pass:
                print("Error: Passwords do not match")
                continue

            #If the passwords do match, the data is written to the .txt file and the user is returned to the menu.
            else:
                users.write('\n' + new_user + ', ' + new_pass)
                print(f"Thank you. A new user with the username '{new_user}' has been created.\n")
                #Closes the users file to ensure the new data is written
                users.close()
                break

def add_task():
    #Opens the task file in append mode
    tasks = open('tasks.txt', 'a+')

    responsible = input("Enter the person responsible for the new task: ")
    while True:
        #Checks whether the person being assigned the task is a user that currently exists. 
        if (responsible not in entries) or (entries.index(responsible) % 2 != 0):
            responsible = input("That person is not yet registered. Please assign the task to a registered user: ")
            continue
        else:
            break

    #Gets task info from the user
    task_title = input("Enter the title of the new task: ")
    task_description = input("Enter a description of the task: ")
    #This block onverts the user's input into a date object to allow comparison for checking whether as task is overdue
    #The input is split into a list and each list item is passed into the datetime.date operation.
    due_date_input = input("Enter the due date of the task in the format YYYY-MM-DD: ")
    due_date = date_conversion(due_date_input)
    created_date = date.today()
    complete = "No"
        
    #Adds the task to the file on a new line
    tasks.write(f"{responsible}, {task_title}, {task_description}, {created_date}, {due_date}, {complete}\n")
    #Closes the file so the task is saved
    tasks.close()
    print("Thank you, your task has been added\n")
    
def view_all():
#Opens the tasks document in read only mode
    tasks = open('tasks.txt', 'r')
    for line in tasks:
        #Removes spaces to clean up readability
        line.replace(', ', ',')

        #Splits each line into a list and defines variables for each item based on index position
        task_data = line.split(',')
        responsible = task_data[0]
        task_title = task_data[1]
        task_description = task_data[2]
        created_date = task_data[3]
        due_date = task_data[4]
        #removes the new line character from the end of the completed line
        complete = task_data[5].replace('\n', '')

        #prints all of the variables with tab characters for optimal spacing
        print(f'''
Task:\t\t  {task_title}
Assigned to:\t   {responsible}
Date assigned:\t  {created_date}
Due date:\t  {due_date}
Task completed:\t  {complete}
Task description: {task_description}''')
    tasks.close()
    print()

def view_mine():
    def complete_task():
        #Accesses the list of tasks, and replaces the 'No' with 'Yes' to show the task has been completed. The newline character at the end ensures that other instances of 'No' will not be replaced
        contents = open('tasks.txt', 'r+')
        text_content = contents.read()
        text_content = text_content.replace(index_dict[user_selection], (index_dict[user_selection].replace(", No\n", ', Yes\n')))
        contents.close()
        re_write = open('tasks.txt', 'w')
        re_write.write(text_content)
        re_write.close()
        print("Task successfully marked as complete!")
        

    def edit_task():
        while True:
            #This prevents completed tasks from being edited. 
            if ' Yes' in task_dict[user_selection]:
                print("You can't make changes to a completed task. Please select another option")
                print()
                break
                        
            else:
                edit_mode = input("Type 'u' to edit the assigned user for the task, or 'd' to edit the due date: ").lower()
                if edit_mode == 'u':
                    new_assigned = input('Who should this task be assigned to? ')
                    while True:
                        #Checks whether the person being assigned the task is a user that currently exists. 
                        if (new_assigned not in entries) or (entries.index(new_assigned) % 2 != 0):
                            new_assigned = input("That person is not yet registered. Please assign the task to a registered user: ")
                            continue
                        else:
                            break

                    #Username is stored when the user logs in, so this can easily be replaced with the new user.     
                    contents = open('tasks.txt', 'r+')
                    text_content = contents.read()
                    text_content = text_content.replace(index_dict[user_selection],(index_dict[user_selection].replace(username,new_assigned)))
                    contents.close()
                    re_write = open('tasks.txt', 'w')
                    re_write.write(text_content)
                    re_write.close()
                    print("Task successfully reassigned")
                    break

                if edit_mode == 'd':
                    #The selected task is split into a list. As all tasks are in the same format, the due date will always be in the second-last index.
                    task_list = index_dict[user_selection].split(', ')
                    new_date_input = input("What is the new due date for this task? (DD/MM/YYYY) ")
                    new_date_split = new_date_input.split('/')
                    new_due_day = int(new_date_split[0])
                    new_due_month = int(new_date_split[1])
                    new_due_year = int(new_date_split[2])
                    new_due_date = date(new_due_year, new_due_month, new_due_day)
                    #The due date is replaced with the new date, and the list is re-joined into a string. 
                    task_list[-2] = new_due_date
                    new_task = ', '.join(task_list)
                    contents = open('tasks.txt', 'r+')
                    text_content = contents.read()
                    text_content = text_content.replace(index_dict[user_selection], new_task)
                    contents.close()
                    re_write.write(text_content)
                    re_write.close()
                    print("Due date successfully changed")
                    break

    tasks = open('tasks.txt', 'r+')
    
    #Sets the outstanding tasks count to 0
    tasks_outstanding = 0
    task_number = 0
    #Establishes empty dictionaries for retrieving specific tasks later
    task_dict = {}
    index_dict = {}
    for line in tasks:
        #Removes spaces to clean up readability
        line.replace(', ', ',')

        #Splits each line into a list and defines variables for each item based on index position
        task_data = line.split(',')
        responsible = task_data[0]
        task_title = task_data[1]
        task_description = task_data[2]
        created_date = task_data[3]
        due_date = task_data[4]
        #removes the new line character from the end of the completed line
        complete = task_data[5].replace('\n', '')

        #Checks if the logged in user is responsible and only prints their tasks.
        if responsible == username:
            tasks_outstanding += 1
            task_number += 1
        #prints all of the variables with tab characters for optimal spacing
            task_display = (f'''
Task number:\t  {task_number}
Task:\t         {task_title}
Assigned to:\t  {responsible}
Date assigned:\t {created_date}
Due date:\t {due_date}
Task completed:\t {complete}
Task description:{task_description}''')

            #Adds the user's tasks to a dictionary, with the assigned number as the key for each item
            #Index_dict stores the data in the same format as tasks.txt to allow replacement. 
            #task_dict stores the data in the user friendly display format. 
            #task_number iterates each time the loop runs, to ensure that the numbering is consistent for only this user's tasks.
            index_dict[task_number] = line
            task_dict[task_number] = task_display
            
    #Shows that a user has no tasks assigned to them if they don't    
    if tasks_outstanding == 0:
        print()
        print("You have no tasks currently outstanding")
        print()

    #Asks the user for the task number they want to access.    
    else:
        while True:
            print('Your outstanding tasks:')
            print('\t'+task_display)
            print()
            user_selection = int(input("Please select a task number, or enter -1 to return to the main menu: "))
            if user_selection == -1:
                print()
                break

            elif user_selection not in task_dict.keys():
                user_selection = int(input("Task number not found. Please select a valid task number: "))
                pass

            #Gets the user input and calls one of the edit functions above, or goes back to the menu.
            else:
                print(task_dict[user_selection])
                print()
                user_action = str(input("What would you like to do with this task?\nEnter 'c' to mark the task as complete or 'e' to edit, or -1 to select another task: ").lower())
                
                if user_action == '-1':
                    pass

                if user_action == 'c':
                    while True:
                    #This prevents completed tasks from being edited. 
                        if ' Yes' in task_dict[user_selection]:
                            print("This task has already been marked as complete. Please select another option.")
                            print()
                            break
                        
                        else:
                            complete_task()
                            break
                    
                if user_action == 'e':
                    edit_task()
                    pass

    tasks.close()

def generate_reports():
    #Generates the task overview document
    #The tasks file is opened and the contents stored. The number of lines is counted to give the total number of tasks.
    tasks = open('tasks.txt', 'r')
    tasks_contents = tasks.readlines()
    total_tasks = len(tasks_contents) 
    
    completed_tasks = 0
    overdue_tasks = 0

    for line in tasks_contents:
        #Each task is split into a list
        contents_list = line.split(', ')
        #Ths checks whether the complete status is yes or no
        if 'Yes' in contents_list[-1]:
            completed_tasks += 1
        #This compares the due date to the current date, and if the task is not complete then the task is flagged as overdue    
        if (date_conversion(contents_list[-2]) < date.today()) and 'No' in contents_list[-1]:
            overdue_tasks += 1

    #The number of outstanding tasks and percentages are calculated
    outstanding_tasks = total_tasks - completed_tasks
    incomplete_pct = round(((outstanding_tasks/total_tasks) * 100), 2)
    overdue_pct = round(((overdue_tasks/total_tasks) * 100), 2)

    #Writes the task data to the .txt file
    task_overview = open('task_overview.txt', 'w+')
    task_overview.write(f'''Task Statistics:

Total tracked tasks:    {total_tasks}
Tasks completed:        {completed_tasks}
Uncompleted tasks:      {outstanding_tasks} ({incomplete_pct}%)
Overdue tasks:          {overdue_tasks} ({overdue_pct}%)   
    ''')   
    task_overview.close()
        
    #Gererates the user overview document
    users = open('user.txt', 'r')
    user_data = users.readlines()
    total_users = len(user_data)

    #A dictionary is established for each user, to track their total, complete and overdue tasks, with the initial value set to 0
    user_dict_total = {}
    user_dict_complete = {}
    user_dict_overdue = {}
    for each_user in user_data:
        each_user = each_user.split(', ')
        user_dict_total[(each_user[0])] = 0
        user_dict_complete[(each_user[0])] = 0
        user_dict_overdue[(each_user[0])] = 0
    
    tasks = open('tasks.txt', 'r')
    task_data = tasks.readlines()
    #This runs through each username, and each task, and compares the assigned user. 
    #If the user and assigned data match, the relevant logic is applied to add to the complete and overdue count as necessary.
    for key in user_dict_total:
        for task in task_data:
            task = task.split(', ')
            if key == task[0]:
                user_dict_total[key] += 1
                if 'Yes' in task[-1]:
                    user_dict_complete[key] += 1
                if (date_conversion(task[-2]) < date.today()) and 'No' in task[-1]:
                    user_dict_overdue[key] += 1

    #The relevant data is written to the user_overview document.
    user_overview = open('user_overview.txt', 'w+')
    user_overview.write(f'''User Statistics:
    
Registered users:       {total_users}
Total tracked tasks:    {total_tasks}
    ''')
    for user in user_data:
        user = user.split(', ')
        user_name = user[0]
        #This avoids a division by 0 error if a user has no tasks.
        if user_dict_total[user_name] == 0:
            user_overview.write(f'''
User:               {user_name}
Tasks assigned:     0
            ''')
        else:
            user_overview.write(f'''
User:               {user_name}
Tasks assigned:     {user_dict_total[user_name]}
Completed tasks:    {user_dict_complete[user_name]} ({round((user_dict_complete[user_name]/user_dict_total[user_name])*100, 2)}%)
Uncompleted tasks:  {user_dict_total[user_name]-user_dict_total[user_name]} ({100.00 - round((user_dict_complete[user_name]/user_dict_total[user_name])*100, 2)}%)
Overdue tasks:      {user_dict_overdue[user_name]} ({round((user_dict_overdue[user_name]/user_dict_total[user_name])*100, 2)}%)
        ''')

    user_overview.close()
    print("Reports successfully generated. Please see output files for results.")
    print()

def display_stats():
    #The reports are generated if they do not exist, and the data is printed to the console.
    generate_reports()
    users = open('user_overview.txt', 'r')
    tasks = open('task_overview.txt', 'r')
    print(tasks.read())
    print(users.read())


#====Login Section====

#Imports and reads the file with user data
users = open('user.txt', 'r+')
open_file = users.read()
#Removes the commas and spaces and sets up a list with all usernames and passwords as individual items
no_spaces = open_file.replace(' ','')
data = no_spaces.replace('\n', ',')
entries = data.split(',')
#Sets the login check to False as default.
login = False

#Gets a username from the user. 
username = input("Enter your username: ")
while True:
    #Returns an error message if the username does not appear in the .txt file.
    #Also requires the username to be at an even index within the list, as otherwise passwords would count as valid usernames for the purpose of this check
    if (username not in entries) or (entries.index(username) % 2 != 0):
        username = input("Plese enter a valid username: ")
        continue

    else:
        #Checks to make sure the password is correct and belongs to that user.
        password = input("Enter your password:")
        for i in range(0, len(entries)):
            if ((i % 2 != 1) and (entries[i] == username)) and (entries[i + 1] == password):
                print("Login successful \n")
                login = True
                break 

            else:
                login = False
                #Loops back to the beginning if the password does not match the username.

    if login == False:
        username = input("Incorrect password. Please enter your username and try again")
        continue

    else:
        users.close()
        break
                
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Register a new user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit\n
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Register a new user
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit\n
: ''').lower()

#Section to register new users

    if menu == 'r':
        reg_user()
        continue      

#Section to add new tasks

    elif menu == 'a':
        add_task()
        continue
        

#Section to view all tasks

    elif menu == 'va':
        view_all()
        continue

#Section to view tasks for logged in user only

    elif menu == 'vm':
        view_mine()
        continue

#Selection for admin to generate reports

    elif menu == 'gr':
        generate_reports()
        continue

#Section for admin to view task statistics 
   
    elif menu == 'ds':
        display_stats()

        continue
       
#Exit section and error message
  
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again")