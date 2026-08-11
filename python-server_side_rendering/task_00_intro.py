def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid template type.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Invalid attendees type.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template

        name = attendee.get("name")
        event_title = attendee.get("event_title")
        event_date = attendee.get("event_date")
        event_location = attendee.get("event_location")

        output = output.replace("{name}", str(name) if name is not None else "N/A")
        output = output.replace("{event_title}", str(event_title) if event_title is not None else "N/A")
        output = output.replace("{event_date}", str(event_date) if event_date is not None else "N/A")
        output = output.replace("{event_location}", str(event_location) if event_location is not None else "N/A")

        with open(f"output_{index}.txt", "w") as file:
            file.write(output)
