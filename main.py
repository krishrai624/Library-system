class Library:
    def __init__(self, list, name):
        self.book_list = list
        self.book_name = name
        self.lend = {}

    def show_books(self):
        print(f"The book listed on our library are {self.book_name}")
        for book in self.book_list:
            print(book)

    def lend_books(self, user, book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("The book list is updated.")
        else:
            print(f"The book is given to {self.lend[book]}")

    def add_books(self, book):
        self.book_list.append(book)
        print("Book has been added to book list.")

    def return_books(self, book):
        self.lend.pop(book)
        print("Book has been received in our library")

if __name__ == '__main__':

    list_of_books = Library(["Rise And Fall", "Atomic Habits", "Economics"], "Krish")
    print(f"Welcome to the {list_of_books.book_name} Library")

    while(True):
        print("Read the instructions given below and type the following keywords to have good respond on your output.")
        print("1. Display books.\n2. Lend a book.\n3. Add a book.\n4. Return a book.")

        user_input = input("Enter the numbers:")

        if user_input not in ["1", "2", "3", "4"]:
            print("Invalid number!!!")
            continue
        else:
            user_input = int(user_input)

        if user_input == 1:
            list_of_books.show_books()

        elif user_input == 2:
            user = input("Enter the name:")
            book = input("Enter the book name:")
            list_of_books.lend_books(user, book)

        elif user_input == 3:
            book = input("Enter the book name you want to add:")
            list_of_books.add_books(book)

        elif user_input == 4:
            book = input("Enter the book name you want to return:")
            list_of_books.return_books(book)

        else:
            print("Invalid number!!!")

        while(True):
            a = input("Enter c for continue and q for quit:")
            if a == "c":
                break
            elif a == "q":
                exit()
