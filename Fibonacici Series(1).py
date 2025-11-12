
def is_fibonacci_series(series):
    """Check if given list is a Fibonacci sequence"""
    for i in range(2, len(series)):
        if series[i] != series[i - 1] + series[i - 2]:
            return False
    return True


def analyze_fibonacci_complexity():
    print("------ Fibonacci Complexity Analyzer ------")

    # Step 1: Ask for number of terms
    n = int(input("Enter number of terms in Fibonacci series: "))

    # Step 2: Ask for Fibonacci numbers
    series_input = input(f"Enter {n} Fibonacci numbers separated by space: ")
    series = list(map(int, series_input.split()))

    # Step 3: Validate Fibonacci series
    if len(series) != n:
        print("⚠️ Error: You entered wrong number of terms.")
        return

    if not is_fibonacci_series(series):
        print("⚠️ Error: The entered numbers do not form a valid Fibonacci sequence.")
        return

    # Step 4: Ask user which method was used
    print("\nWhich method did you use to generate this series?")
    print("1️Recursive")
    print("2️Iterative")
    choice = int(input("Enter your choice (1 or 2): "))

    # Step 5: Display complexity based on user method
    print("\n Fibonacci Series Entered Successfully!")
    print("Series:", series)

    if choice == 1:
        print("\n Method: Recursive Fibonacci")
        print("Time Complexity: O(2^n)")
        print(" Space Complexity: O(n)")
    elif choice == 2:
        print("\n Method: Iterative Fibonacci")
        print(" Time Complexity: O(n)")
        print(" Space Complexity: O(1)")
    else:
        print("️ Invalid choice. Please enter 1 or 2.")

    print("\nProgram completed successfully ")


# Run the program
if __name__ == "__main__":
    analyze_fibonacci_complexity()



    #output

    ------ Fibonacci Complexity Analyzer ------
Enter number of terms in Fibonacci series: 3
Enter 3 Fibonacci numbers separated by space: 0 1 1

Which method did you use to generate this series?
1️⃣ Recursive
2️⃣ Iterative
Enter your choice (1 or 2): 1

 Fibonacci Series Entered Successfully!
Series: [0, 1, 1]

 Method: Recursive Fibonacci
Time Complexity: O(2^n)
 Space Complexity: O(n)

Program completed successfully 

    
