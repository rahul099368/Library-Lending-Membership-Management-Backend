from abc import ABC, abstractmethod

class LibraryItems(ABC):


    def __init__(self,item_id,title):
        self.item_id=item_id
        self.title=title
        self.available = True

    @abstractmethod
    def loan_period_days(self):
        pass

    def available(self):
        return self.available

    def mark_borrowed(self):
        self.available = False

    def mark_returned(self):
        self.available = True

    


class Book(LibraryItems):
    def __init__(self,item_id,title):
        super().__init__(item_id,title)
    def loan_period_days(self):
        return 14

class Magazine(LibraryItems):
    def __init__(self,item_id,title):
        super().__init__(item_id,title)
    def loan_period_days(self):
        return 7
    
class ReferenceBook(LibraryItems):
    def __init__(self,item_id,title):
        super().__init__(item_id,title)
    def loan_period_days(self):
        return 0



class Member:
    library_name = "My Library"
    max_active_loans_default = 3

    def __init__(self,member_id,name,borrowing_limit):
        self.member_id = member_id
        self.name = name
        self.borrowing_limit = borrowing_limit
        self.active_loan = []

    @property
    def acive_loan(self):
        return self.active_load.copy()
    
    def can_borrow(self):
        return len(self.active_loan) < self.borrowing_limit

    @classmethod
    def set_default_limit(cls,limit):
        cls.max_active_loans_default = limit


    def add_loan(self,item_id):
        self.active_loan.append(item_id)

    def remove_loan(self,item_id):
        if item_id in self.active_loan:
            self.active_loan.remove(item_id)
    


class StudentMember(Member):
    def __init__(self,member_id,name):
        super().__init__(member_id,name,2)

class ResearchStudent(StudentMember):
    def __inti__(self,member_id,name):
        super().__inti__(member_id,name)
        self.borrowing_limit = 4

class FacultyMember(Member):
    def __init__(self,member_id,name):
        super().__init__(member_id,name,5)


class NotificationMixin:
    def send_notice(self,message):
        print(self,message)

class NotificationMember(Member,NotificationMixin):
    def __inti__(self,member_id,name,borrowing_limit):
        super().__init__(member_id,name,borrowing_limit)

