import json
import csv
import xml.etree.ElementTree as ET

def read_json(file_path):
    """Read JSON file and return data"""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    """Write data to a JSON file"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_csv(file_path):
    """Read CSV file and return a list of dictionaries"""
    with open(file_path, newline='') as file:
        return list(csv.DictReader(file))

def write_csv(file_path, data):
    """Write list of dictionaries to a CSV file"""
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_xml(file_path):
    """Read XML file and return root"""
    tree = ET.parse(file_path)
    return tree.getroot()
