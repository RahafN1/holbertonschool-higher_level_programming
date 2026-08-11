def generate_invitations(template, attendees):
    for attendee in attendees:
        output = template
        output = output.replace("{name}", attendee["name"])
        output = output.replace("{event_title}", attendee["event_title"])
        output = output.replace("{event_date}", attendee["event_date"] if attendee["event_date"] is not None else "N/A")
        output = output.replace("{event_location}", attendee["event_location"] if attendee["event_location"] is not None else "N/A")

        print(output)