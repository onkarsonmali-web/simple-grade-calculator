# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! Keep improving! 🙂"
    elif marks >= 60:
        return "D", "You passed! Work harder next time! 💪"
    else:
        return "F", "Don't give up! Try again! 🔁"


# Main program
def main():
    name = input("Enter student name: ")

    # Input validation using while loop
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("❌ Marks must be between 0 and 100. Try again.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    # Get grade
    grade, message = calculate_grade(marks)

    # Output result
    print("\n📊 RESULT FOR", name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run program
main()
