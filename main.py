#Application to find best combination of tasks within time limit
from scheduler import solve_schedule
#slots = get_time_slots_from_user()
#print("Suggested Time Slots:", slots)

def main():
    print("Welcome to the Task Scheduler!")
    user_input = input("Please enter your tasks for the day, separated by commas (e.g., Study, Gym, Cook): ")

    result = solve_schedule(user_input)
    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()