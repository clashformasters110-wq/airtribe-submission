# main.py
from models import Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 42)
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling (item already borrowed)
print("--- 1. Borrowing & Already-Borrowed Check ---")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    print("Alice's current list:", alice.borrowed_titles())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each
print("\n--- 2. Borrow-Limit & Not-Borrowed Checks ---")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's max_items is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(dvd)  # should fail: Bob never borrowed the DVD
except ValueError as e:
    print("Could not return:", e)

# Valid return with late fee calculation
fee = alice.return_item(book, days_late=4)
print(f"Alice returned '{book.title}' (4 days late). Fee paid: Rs {fee}")

# 3. Polymorphism: one loop, no type checks
print("\n--- 3. Polymorphism (3 Days Late Fee) ---")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n--- 4. Shared Class Attribute ---")
print("Total items created:", Book.total_items)

# 5. Prove encapsulation (Step 6 checkpoint)
print("\n--- 5. Encapsulation Check ---")
try:
    print(book.__available)
except AttributeError as e:
    print("Direct access blocked with AttributeError:", e)
print("Proper access via book.is_available():", book.is_available())