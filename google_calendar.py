import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/calendar.events"
]


def get_calendar_service():

    creds = None

    if os.path.exists("token.pkl"):

        with open(
            "token.pkl",
            "rb"
        ) as token:

            creds = pickle.load(token)

    if not creds:

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(
            port=0
        )

        with open(
            "token.pkl",
            "wb"
        ) as token:

            pickle.dump(
                creds,
                token
            )

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    return service


def create_event(
    service,
    title,
    start_time,
    end_time
):

    event = {

        "summary": title,

        "start": {
            "dateTime": start_time,
            "timeZone": "Africa/Cairo"
        },

        "end": {
            "dateTime": end_time,
            "timeZone": "Africa/Cairo"
        }

    }

    service.events().insert(
        calendarId="primary",
        body=event
    ).execute()