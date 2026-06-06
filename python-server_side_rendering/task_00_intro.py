#!/usr/bin/python3
"""
Module to generate personalized invitation files from a template.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a template and a list
    of attendee dictionaries.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print(f"Error: Template must be a string. Got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Placeholders to look for
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        for ph in placeholders:
            # Get value, default to "N/A" if missing or None
            value = attendee.get(ph)
            if value is None:
                value = "N/A"
            
            # Replace placeholder in the template
            processed_template = processed_template.replace(f"{{{ph}}}", str(value))

        # 4. Generate Output Files
        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

# Example usage (as per instructions):
if __name__ == "__main__":
    # Ensure template.txt exists or define template_content directly
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
