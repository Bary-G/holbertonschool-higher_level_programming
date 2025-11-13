#!/usr/bin/env python3
"""
Module: generate personalized invitation files from a template.
"""
import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.
    
    Parameters:
    - template (str): The invitation template with placeholders.
    - attendees (list): A list of dictionaries, each containing attendee data.
    """
    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError("Expected a string for template and a list for attendees")
    if not template:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")
    
    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            raise ValueError(f"Attendee at index {index-1} is not a dictionary.")
        attendee = {k: ("N/A" if v is None else v) for k, v in attendee.items()}
        try:
            content = template.format(**attendee)
        except KeyError as e:
            raise KeyError(f"Missing key {e} in attendee data at index {index-1}")
        
        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
