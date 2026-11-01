from models import (
    Book, Magazine, ReferenceBook,
    StudentMember, ResearchStudent,
    FacultyMember, NotificationMember
)

from library_service import LibraryManager
from storage import save_data, load_data


library = LibraryManager()

load_data(library)

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Register Book")
    print("2. Register Magazine")
    print("3. Register Reference Book")
    print("4. Register Student")
    print("5. Register Research Student")
    print("6. Register Faculty")
    print("7. Borrow Item")
    print("8. Return Item")
    print("9. Show All Items")
    print("10. Show Available Items")
    print("11. Show Active Loans")
    print("12. Show Overdue Loans")
    print("13. Show Members")
    print("14. Save Data")
    print("15. Exit")
    print("16. Register Notified Member")

    choice = input("Enter your choice: ")
    if choice == "1":
        item_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        library.register_item(Book(item_id, title))

    elif choice == "2":
        item_id = input("Enter Magazine ID: ")
        title = input("Enter Magazine Title: ")
        library.register_item(Magazine(item_id, title))

    elif choice == "3":
        item_id = input("Enter Reference Book ID: ")
        title = input("Enter Reference Book Title: ")
        library.register_item(ReferenceBook(item_id, title))

    elif choice == "4":
        member_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        library.register_member(StudentMember(member_id, name))

    elif choice == "5":
        member_id = input("Enter Research Student ID: ")
        name = input("Enter Research Student Name: ")
        library.register_member(ResearchStudent(member_id, name))

    elif choice == "6":
        member_id = input("Enter Faculty ID: ")
        name = input("Enter Faculty Name: ")
        library.register_member(FacultyMember(member_id, name))

    elif choice == "7":
        member_id = input("Enter Member ID: ")
        item_id = input("Enter Item ID: ")
        library.borrow_item(member_id, item_id)

    elif choice == "8":
        item_id = input("Enter Item ID: ")
        library.return_item(item_id)

    elif choice == "9":
        library.show_all_items()

    elif choice == "10":
        library.show_available_items()

    elif choice == "11":
        library.show_active_loans()

    elif choice == "12":
        library.show_overdue_loans()

    elif choice == "13":
        library.show_members()

    elif choice == "14":
        save_data(library)

    elif choice == "15":
        save_data(library)
        print("Exiting Library Management System!")
        break

    elif choice == "16":
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        limit = int(input("Enter borrowing limit: "))
        library.register_member(
            NotificationMember(member_id, name, limit)
        )

    else:
            print("Invalid choice! Try again.")