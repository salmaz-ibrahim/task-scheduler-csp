from google_calendar import (
    get_calendar_service,
    create_event
)

service = get_calendar_service()

create_event(

    service,

    "Task Planner Test",

    "2026-06-08T20:00:00",

    "2026-06-08T21:00:00"

)

print(
    "Calendar event created!"
)