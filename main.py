import json
import os

datafile = 'library.txt'

def loadData():
    if os.path.exists(datafile):
        with open(datafile, 'r') as file:
            return json.load(file)
    return []

def saveData(library):
    with open(datafile, 'w') as file:
        json.dump(library, file, indent=4)

def addBook(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read_input = input('Have you read the book? (yes/no): ').strip().lower()
    read = True if read_input == 'yes' else False

    newBook = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(newBook)
    saveData(library)
    print(f'Book "{title}" added successfully!')

def removeBook(library):
    title = input('Enter the title of the book to remove: ').strip().lower()
    initial_length = len(library)
    updated_library = [book for book in library if book['title'].strip().lower() != title]

    if len(updated_library) < initial_length:
        saveData(updated_library)
        print(f'Book "{title}" successfully removed!')
    else:
        print(f'Book "{title}" not found in the library.')

    library.clear()
    library.extend(updated_library)

def searchBook(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    option = input("Enter your choice: ").strip()

    if option == '1':
        searchBy = 'title'
    elif option == '2':
        searchBy = 'author'
    else:
        print("Invalid option. Please choose 1 or 2.")
        return

    searchTerm = input(f'Enter the {searchBy}: ').strip().lower()
    results = [book for book in library if searchTerm in book[searchBy].strip().lower()]

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, start=1):
            status = 'Read' if book['read'] else 'Not Read'
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(f'No books found matching {searchBy}: "{searchTerm}".')

def displayAllBooks(library):
    if library:
        print("\nBooks in the Library:")
        for book in library:
            status = 'Read' if book['read'] else 'Not Read'
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print('No books in the library.')

def displayStatistics(library):
    totalBooks = len(library)
    totalRead = len([book for book in library if book['read']])
    percentageRead = (totalRead / totalBooks) * 100 if totalBooks > 0 else 0
    print(f'\nLibrary Statistics:')
    print(f'Total books: {totalBooks}')
    print(f'Books read: {totalRead}')
    print(f'Percentage read: {percentageRead:.2f}%')

def main():
    library = loadData()
    while True:
        print('\nWelcome to the Library Management System!')
        print('''
        1. Add a book
        2. Remove a book
        3. Search for a book
        4. Display all books
        5. Display statistics
        6. Exit
        ''')
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            addBook(library)
        elif choice == '2':
            removeBook(library)
        elif choice == '3':
            searchBook(library)
        elif choice == '4':
            displayAllBooks(library)
        elif choice == '5':
            displayStatistics(library)
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
