# bubble_sort_for_book_titles.py
# This script asks the user for book titles, sorts them alphabetically, and prints the sorted list.

def bubble_sort(arr): 
    """Sort a list of strings alphabetically using bubble sort."""
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def main():
    """Get book titles from the user, sort them, and show the sorted list."""
    books = [] 
    n = int(input("How many books do you want to enter? ")) 
    for _ in range(n): 
        book = input("Enter a book title: ")
        books.append(book) 

    bubble_sort(books)
    print("Sorted Book Titles:", books)

if __name__ == "__main__":
    main()
