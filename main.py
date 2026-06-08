from task import Task
from timeslot import TimeSlot
from scheduler import schedule_tasks
from constraints import no_overlap, fits_duration, no_study_at_night
from google_calendar import get_calendar_service, create_event

calendar_service = get_calendar_service()

schedule = {}
#example tasks
tasks = [
    Task("Study SQL", 2, "high", "Study"),
    Task("Go to the gym", 1, "low", "Exercise"),
    Task("Read a book", 1, "medium", "Leisure")
]

#Example slots
slots = [
    TimeSlot(18,20),
    TimeSlot(20,21), 
    TimeSlot(21,22)
]

priority_order = {
    "high": 3,
    "medium": 2,
    "low": 1
}

tasks.sort(
    key=lambda task: 
    priority_order[task.priority],
    reverse=True
)

#Scheduling tasks
scheduled_tasks = schedule_tasks(
    tasks,
    slots
)

DATE = "2026-06-08"
for task in scheduled_tasks:
    print(task.name)
    if task.assigned_slot:
        start = (
            f"{DATE}T{task.assigned_slot.start:02d}:00:00"
        )
        end = (
            f"{DATE}T{task.assigned_slot.end:02d}:00:00"
        )
        print(start, end)
        create_event(
            calendar_service,
            task.name,
            start,
            end
        )