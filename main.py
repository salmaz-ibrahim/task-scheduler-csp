from task import Task
from timeslot import TimeSlot
from scheduler import schedule_tasks
from constraints import no_overlap, fits_duration, prioritize, no_study_at_night

schedule = {}

used_slots = set()

#example tasks
tasks = [
    Task("Study SQL", 2, "high","Study"),
    Task("Go to the gym", 1, "low","Exercise"),
    Task("Read a book", 3, "medium","Leisure")
]

#Example slots
slots = [
    TimeSlot(18,20),
    TimeSlot(20,21), 
    TimeSlot(21,22)
]

#Prioritize tasks by priority
tasks.sort(
    key=lambda t:
    t.priority == "high",
    reverse=True
)

#Schedule tasks
schedule = schedule_tasks(
    tasks,
    slots)

for task, slot in schedule.items():
    print(f"{task}: {slot}")

priority_order = {
    "high": 3,
    "medium": 2,
    "low": 1
}

tasks.sort(
    key=lambda task: priority_order[task.priority],
    reverse=True
)
