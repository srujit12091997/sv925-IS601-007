#SV925
#Srujit varasala
# time  8:25 PM
# code: the code is a task management, where each function is responsible for a specific task-related add_task is resposnible for adding the task for name description and due uupdate_task is to update the task, view_task is for viewing the updated or the default task and lastly delete task is for deleting the taskwhich is incomplete
# this code works as we like to add the task with the things we would like to track about the tasks. we can add, update,delete and view the task status. On the each task provided the tracking system have a date and time noted each next to it
from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    current_datetime=datetime.now()
    task["lastActivity"] = current_datetime

    try:
        task["name"]=name # Srujit Varasala(SV925)
        task["description"]=description # For example addition function is to add the task to the list
        task["due"]=str_to_datetime(due) #visual format: mm/dd/yy hh:mm:ss
        tasks.append(task)
        print("New Task Added")
    except:
        print("Task not added.Please provide valid data for name,description,due date")
    save()

    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # make sure any checks/conditions clearly display an appropriate message of what failed

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index <0 or index >= len(tasks):
        print("Invalid index.Task not updated")
        return
    task=tasks[index]
    print(f"Updating task with given info '{task['name']}'")
    name = input(f"What's the name of this task? (Current: {task['name']}) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (Current: {task['description']}) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (Current: {task['due']}) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    save()
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:24 pm
    #code explination: this function is used to update the task if wants to replace the related task or the scenario of the task info.

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not updated.")
        return
    task = tasks[index]
    current_datetime = datetime.now()
    task["lastActivity"] = current_datetime

    if name:
        task["name"] = name
    if description:
        task["description"] = description
    if due:
        try:
            task["due"] = str_to_datetime(due)
        except ValueError:
            print("Failed to update due date. Please provide a valid due date format.")

    if task != tasks[index]:
        print("No changes found. Task not updated.")
        #print("Task updated successfully.")
    else:
        print("Task updated successfully.")
    save()
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:54 pm
    # solution: This helps to update the task to track the task delivered from the name of the task to date and time of the task
def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not marked as done.")
        return

    task = tasks[index]
    current_datetime = datetime.now()

    if not task["done"]:
        task["done"] = current_datetime
        print(f"Task '{task['name']}' marked as done.")
    else:
        print(f"Task '{task['name']}' is already marked as done.")
    save()
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:37 pm
    # solution:Completion of the task is briefly to summerize the solution which check for the task which is complety done
def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
    if index < 0 or index >= len(tasks):
        print("Invalid task index. No task to view.")
        return

    task = tasks[index]
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:37 pm
    # solution: This view statement will revert the task indexing with the following tasks with it!

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not deleted.")
        return

    deleted_task = tasks.pop(index)
    print(f"Task '{deleted_task['name']}' deleted successfully.")
    save()
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:37 pm
    # solution: This delete task is used for deleting the task which are in the indexes

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    incomplete_tasks = [task for task in tasks if not task["done"]] # <-- this is a placeholder to populate based on the above requirements
    if incomplete_tasks:
        print("Incomplete tasks:")
        list_tasks(incomplete_tasks)
    else:
        print("No incomplete tasks found.")
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:37 pm
    # solution: will give the task which are not done detalis with the task indexes

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    current_datetime = datetime.now() # <-- this is a placeholder to populate based on the above requirements
    overdue_tasks = [task for task in tasks if not task["done"] and task["due"] < current_datetime]
    if overdue_tasks:
        print("Overdue tasks:")
        list_tasks(overdue_tasks)
    else:
        print("No overdue tasks found.")
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 9:37 pm
    # solution: will give the task which are overdue detalis with the task indexes

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # <-- this is a placeholder to populate based on the above requirements
    # do your print logic here
    if index < 0 or index >= len(tasks):
        print("Invalid task index. Cannot calculate time remaining.")
        return

    task = tasks[index]
    current_datetime = datetime.now()

    if task["done"]:
        print(f"Task '{task['name']}' is already marked as done.")
    elif task["due"] < current_datetime:
        time_difference = current_datetime - task["due"]
        print(f"Task '{task['name']}' is {time_difference} overdue.")
    else:
        time_difference = task["due"] - current_datetime
        days, seconds = time_difference.days, time_difference.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Time remaining for task '{task['name']}': {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    #name and UCID : Srujit Varasala SV925
    #Time: 10/9/23 11:11 pm
    # this shows the remaining time for the tasks

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            description = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, description, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()