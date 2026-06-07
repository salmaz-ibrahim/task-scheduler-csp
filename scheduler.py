# scheduler.py

def schedule_tasks(
    tasks,
    slots
):

    schedule = {}

    for task, slot in zip(
        tasks,
        slots
    ):

        schedule[task.name] = (
            slot.start,
            slot.end
        )

    return schedule