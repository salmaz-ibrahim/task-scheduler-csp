import itertools

#define time domains
time_domains = ["Morning", "Afternoon", "Evening", "Night"]

def solve_schedule(input_string):
    #Define tasks by asking user input
    tasks = input_string.split(",")  # Split input by commas
    tasks = [task.strip() for task in tasks if task.strip() != ""]  # Remove any extra whitespace, and ignore empty tasks

    if not tasks: #In case of empty input, exit()
        return "❌ Please enter at least one valid task"

    #Handle duplicate tasks
    if len(set(tasks)) != len(tasks):
        return "⚠️ Duplicate tasks detected. Please ensure all tasks are unique."

    #Check if there are enough time slots for the tasks
    if len(tasks) > len(time_domains):
        return "❌ Not enough time slots for tasks"

    #Generate assignments
    all_assignments = itertools.product(time_domains, repeat=len(tasks))

    for assignment in all_assignments:
        #Rule, enforce 1 task per time slot
        if len(set(assignment)) == len(assignment):
            task_map = dict(zip(tasks, assignment))
            formatted = "\n".join([f"{task}: {slot}" for task, slot in task_map.items()])
            return f"✅ Valid Schedule:\n{formatted}"

    return "❌ No valid schedule found. Please adjust your tasks or time slots."