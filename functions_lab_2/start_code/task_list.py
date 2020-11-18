tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]




def uncompleted_compiler(task_list):
    uncompleted = []
    for task in task_list:
        if task['completed'] == False:
                uncompleted.append(task)
    print(uncompleted)
        

print('')

def completed_compiler(task_list):
    completed = []
    for task in task_list:
        if task['completed'] == True:
                completed.append(task)
    print(completed)

def description_compiler(task_list):
    description = []
    for task in task_list:
        description.append(task['description'])
    print(description)


def giventime(task_list, time):
    list_time = []
    for task in task_list:
        if task['time_taken'] >= time:
            list_time.append(task)
    print(list_time)

def task_description(task_list, description):
    for task in task_list:
        if task['description'] == description:
            print(task)


def task_completer(task_list, description):
    for task in task_list:
        if task['description'] == description:
            task['completed'] = True

def task_adder(task_list, task):
    task_list.append(task)

