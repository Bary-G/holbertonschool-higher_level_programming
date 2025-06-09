#!/usr/bin/python3
import csv
import json
"""
Module:
A file that runs Python functions.
"""


def convert_csv_to_json(filename):
    """
    Convert CSV data to JSON format.
    """

    try:
        with open(filename, mode='r', encoding='UTF8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        json_filename = filename.replace('.csv', '.json')
        with open(json_filename, mode='w', encoding='UTF8') as json_file:
            json.dump(data, json_file)
        return 0
    except FileNotFoundError:
        return 2
    except Exception as e:
        return 1
