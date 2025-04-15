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
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read this book? (yes/no) ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" has been added successfully.')

def remove_book(library):
    title = input('Enter the title of the book to remove: ').lower()
    initial_length = len(library)
    
    library = [book for book in library if book['title'].lower() != title]
    
    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" has been removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

def search_library(library):
    search_by = input('Enter the search term (title, author, year, genre, read): ').lower()
    search_term = input(f'Enter the search {search_by}: ').lower()

    results = [book for book in library if search_term in str(book.get(search_by, '')).lower()]

    if results:
        for book in results:
            status = 'read' if book['read'] else 'unread'
            print(f"{book['title']} by {book['author']} published in {book['year']} in the {book['genre']} genre is {status}.")
    else:
        print('No books found.')

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage:.2f}%")

def main():
    library = load_library()
    while True:
        print('''
        1. Add a book
        2. Remove a book
        3. Search the library
        4. Display statistics
        5. Quit
        ''')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_statistics(library)
        elif choice == '5':
            save_library(library)
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()