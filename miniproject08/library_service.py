from datetime import datetime, timedelta


class LibraryManager:

    def __init__(self):
        self.items = {}
        self.members = {}
        self.loans = {}

    def register_item(self,item):
        if item.item_id in self.items:
            print("Item is already exist!")
        else:
            self.items[item.item_id] = item
            print("Item registration successfully!")

    def register_member(self,member):
        if member.member_id in self.members:
            print("Member is already existed!")
        else:
            self.members[member.member_id] = member
            print("Member registration successsfuly!")


    def borrow_item(self,member_id,item_id):
        if member_id not in self.members:
            print("Member not found!")
            return
        
        if item_id not in self.items:
            print("Item not found!")
            return

        member = self.members[member_id]
        item = self.items[item_id]

        if not item.available:
            print("Item is already borrowed!")
            return

        if item.loan_period_days == 0:
            print("This item cannot be borrowed!")
            return

        if not member.can_borrow():
            print("Borrowing limit reached!")
            return

        issue_date = datetime.today().date()
        due_date = issue_date + timedelta(days=item.loan_period_days())

        item.mark_borrowed()
        member.add_loan(item_id)

        self.loans[item_id] = {
            "member_id":member_id,
            "issue_date":str(issue_date),
            "due_date":str(due_date)
        }

        print("Item borrowed successfully..")
        print("Due date:",due_date)

        if hasattr(member,"send_notice"):
            member.send_notice(f"You borrowed {item.title}. Due date: {due_date}")


    def return_item(self,item_id):
        if item_id not in self.loans:
            print("No active loan found!")
            return
        loan = self.loans[item_id]
        member = self.members[loan["member_id"]]
        item = self.items[item_id]

        due_date = datetime.strptime(loan["due_date"],"%Y-%m-%d").date()
        today = datetime.today().date()

        overdue_days = max(0,(today-due_date).days)

        fine = self.calculate_fine(overdue_days)

        item.mark_returned()
        member.remove_loan(item_id)
        del self.loans[item_id]

        print("item returned successfully!")
        print("Overdue days:",overdue_days)
        print("Fine:",fine)

    def calculate_fine(self,overdue_days):
        fine_per_day = 5
        return fine_per_day * overdue_days

    def show_all_items(self):
        for item in self.items.values():
            print(item.item_id, item.title, item.available)


    def show_available_items(self):
        for item in self.items.values():
            if item.available:
                print(item.item_id, item.title)

    def show_active_loans(self):
        for item_id, loan in self.loans.items():
            print("Item:", item_id,end=" ")
            print("Member:", loan["member_id"],end=" ")
            print("Due Date:", loan["due_date"])


    def show_overdue_loans(self):
        today = datetime.today().date()
        for item_id, loan in self.loans.items():
            due_date = datetime.strptime(loan["due_date"], "%Y-%m-%d").date()
            if today > due_date:
                print("Item:", item_id,end=" ")
                print("Member:", loan["member_id"],end=" ")
                print("Overdue Days:", (today - due_date).days)


    def show_members(self):
        for member in self.members.values():
            print(member.member_id,member.name,"Borrowed:", len(member.active_loan))
