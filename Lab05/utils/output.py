import csv
import json
from typing import List, Dict


def save_as_csv(data: List[Dict], filename="output.csv"):
    """Save data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "rating"])
        writer.writeheader()
        writer.writerows(data)


def save_as_json(data: List[Dict], filename="output.json"):
    """Save data to a JSON file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)