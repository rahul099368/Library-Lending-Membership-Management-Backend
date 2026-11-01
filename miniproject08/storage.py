import json
import os

def save_data(manager):

    data = {
        "items": [],
        "members": [],
        "loans": manager.loans
    }

    for item in manager.items.values():
        data['items'].append({
            "type":type(item).__name__,
            "item_id": item.item_id,
            "title": item.title,
            "available": item.available
        })

    for member in manager.members.values():
        data['members'].append({
            "type":type(member).__name__,
            "member_id":member.member_id,
            "name":member.name,
            "borrowing_limit":member.borrowing_limit
        })

    with open("data.json","w") as file:
        json.dump(data,file,indent=4)

    print("Data saved successfully!")

from models import (
    Book,Magazine,ReferenceBook,
    StudentMember,ResearchStudent,
    FacultyMember,NotificationMember
)

def load_data(manager):

    if not os.path.exists("data.json"):
        print("No saved data found!")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Invalid or unreadable data file!")
        return

    item_classes = {
        "Book": Book,
        "Magazine": Magazine,
        "ReferenceBook": ReferenceBook
    }

    member_classes = {
        "StudentMember": StudentMember,
        "ResearchStudent": ResearchStudent,
        "FacultyMember": FacultyMember
    }

    for record in data.get("items", []):
        item_class = item_classes.get(record["type"])

        if item_class:
            item = item_class(record["item_id"], record["title"])

            if not record["available"]:
                item.mark_borrowed()

            manager.items[item.item_id] = item

    for record in data.get("members", []):
        member_type = record["type"]

        if member_type == "NotifiedMember":
            member = NotificationMember(
                record["member_id"],
                record["name"],
                record["borrowing_limit"]
            )
        else:
            member_class = member_classes.get(member_type)

            if not member_class:
                continue

            member = member_class(
                record["member_id"],
                record["name"]
            )

            member.borrowing_limit = record["borrowing_limit"]

        manager.members[member.member_id] = member

    manager.loans = data.get("loans", {})

    for item_id, loan in manager.loans.items():
        member = manager.members.get(loan["member_id"])

        if member:
            member.add_loan(item_id)

    print("Data loaded successfully!")