#!/usr/bin/python3
import xml.etree.ElementTree as ET
"""
Module:
A file that runs Python functions.
"""


def serialize_to_xml(dictionary, filename):
    """
    Serialize data into XML.
    """
    root = ET.Element("root")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
