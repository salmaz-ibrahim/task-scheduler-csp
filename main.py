from ai_helper import create_schedule_with_ollama
from google_calendar import create_event_from_body, get_calendar_service
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def read_planning_request():
    print("Describe your day, tasks, priorities, and any time preferences.")
    print("Press Enter on an empty line when you are done.\n")

    lines = []

    while True:
        line = input("> ")

        if not line.strip():
            break

        lines.append(line)

    return "\n".join(lines).strip()


def print_schedule(events):
    print("\nGenerated calendar events:\n")

    if not events:
        print("No events were created.")

    for event in events:
        print(
            f"{event['start']['dateTime']} - "
            f"{event['end']['dateTime']} | "
            f"{event['summary']}"
        )


def build_calendar_events(events):

    timezone = ZoneInfo("Africa/Cairo")
    today = datetime.now(timezone).date()

    calendar_events = []

    for event in events:

        start_dt = datetime(
            today.year,
            today.month,
            today.day,
            event["start"],
            0,
            tzinfo=timezone
        )

        end_dt = datetime(
            today.year,
            today.month,
            today.day,
            event["end"],
            0,
            tzinfo=timezone
        )

        calendar_events.append({
            "summary": event["summary"],
            "start": {
                "dateTime": start_dt.isoformat(),
                "timeZone": "Africa/Cairo"
            },
            "end": {
                "dateTime": end_dt.isoformat(),
                "timeZone": "Africa/Cairo"
            }
        })

    return calendar_events

def add_events_to_calendar(events):

    if not events:
        return

    calendar_service = get_calendar_service()

    for event in events:
        create_event_from_body(
            calendar_service,
            event
        )
        
def schedule_tasks(tasks):

    current_hour = 9
    events = []
    priority_order = {
    "high": 0,
    "medium": 1,
    "low": 2}

    tasks = sorted(
        tasks,
        key=lambda task: priority_order[task["priority"]]
    )

    for task in tasks:

        start = current_hour
        end = start + task["duration_hours"]

        events.append({
            "summary": task["name"],
            "start": start,
            "end": end
        })

        current_hour = end
    return events

def main():
    user_input = read_planning_request()

    if not user_input:
        print("No planning request entered.")
        return

    try:
        task_payload = create_schedule_with_ollama(user_input)

    except Exception as error:
        print(
            f"Birdy failed: "
            f"{type(error).__name__}: {error}"
        )
        return

    events = schedule_tasks(
        task_payload["tasks"]
    )
    calendar_events = build_calendar_events(events)
    print("\nGenerated Calendar Events:\n")

    for event in calendar_events:
        print(
            f"{event['start']['dateTime']} | "
            f"{event['summary']}"
        )
    add_events_to_calendar(calendar_events)

if __name__ == "__main__":
    main()