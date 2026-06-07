#Implementing CSP logic

#Only 1 taks at a time
def no_overlap(slot1,slot2):
    if (
        slot1.start < slot2.end
        and 
        slot2.start < slot1.end
    ):
        return False
    return True


#Task duration mush match free time on the calender
def fits_duration(task,slot):
    available_time = slot.end - slot.start
    return task.duration <= available_time


#No Studying at night
def no_study_at_night(task, slot):
    if task.category.lower() == "study" and slot.start >= 20:
        return False
    return True