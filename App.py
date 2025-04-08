import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file): 
        with open(data_file, 'r') as file:
            return json.load(file)
        return []
    
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the aothor of the book")
    year = input("Enter the year of he book:")
    genre = input("Enter the genre of the book")
    read = input("Enter the read of the book? (yes/no): ").lower() == "yes"

    new_book = {
        'title' : title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book {title} added succcessfully.')

def remove_book(library):
    title = input("Eneter the title book to remove from the library")
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f"book {title} removed successfully.")
    else:
        print(f"book {title} not foun in the library.")
    
def search_library(library):
    search_by = input("search by title or author").lower()
    search_term = input(f"Enter the {search_by}").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status ="Read" if book["read"] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"no books found matching '{search_term}' in the {search_by} field.") 

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book ['author']} - {book["year"]} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

def display_statistic(library):
    total_books = len(library)
    read_books = len(book for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0 

    print(f"Total books: {read_books}")
    print(f"Percentage read :{percentage_read}")

def main():
    library = load_library()
    while True:
        print("Manu")
        print("1. add a book")
        print("2. Remove a book") 
        print("3. Search the library")
        print("4. Display all book")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice =='2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistic(library)
        elif choice == '6':
            print("Goods Bye")
            break
        else :
            print("Invelid choice.Pelase tryagain.")

if  __name__ == '__main__':
    main()


            






 

