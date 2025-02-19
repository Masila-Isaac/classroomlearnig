def sum_of_integers():
    numbers = input("Enter a list of integers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    total_sum = sum(numbers)
    print(f"The sum of the integers is: {total_sum}\n")

def favorite_books():
    favorite_books = ("Book One", "Book Two", "Book Three", "Book Four", "Book Five")
    print("Your favorite books are:")
    for book in favorite_books:
        print(book)
    print()

def person_info():
    person = {}
    person['name'] = input("What is your name? ")
    person['age'] = input("What is your age? ")
    person['favorite_color'] = input("What is your favorite color? ")
    print("\nPerson's Information:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
    print()

def intersection_of_sets():
    set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))
    set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))
    common_elements = set1.intersection(set2)
    print(f"The common elements are: {common_elements}\n")

def odd_length_words():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    odd_words = [word for word in words if len(word) % 2 != 0]
    print(f"Words with an odd number of characters: {odd_words}\n")

def main():
    while True:
        print("Choose an option:")
        print("1. Sum of integers in a list")
        print("2. Display favorite books")
        print("3. Store and display person information")
        print("4. Find intersection of two sets")
        print("5. List words with an odd number of characters")
        print("6. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            sum_of_integers()
        elif choice == '2':
            favorite_books()
        elif choice == '3':
            person_info()
        elif choice == '4':
            intersection_of_sets()
        elif choice == '5':
            odd_length_words()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()