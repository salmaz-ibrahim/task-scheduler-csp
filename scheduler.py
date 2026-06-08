# scheduler.py

def schedule_tasks(
    tasks,
    slots
):
    for task, slot in zip(
        tasks,
        slots
    ):
        task.assigned_slot = slot
    return tasks