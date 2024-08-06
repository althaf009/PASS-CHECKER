import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess strength
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        return "Password is very strong.", ""
    elif score == 4:
        return "Password is strong.", "Consider adding more special characters or making the password longer for added security."
    elif score == 3:
        return "Password is medium.", "Add more variety: include uppercase letters, numbers, and special characters to strengthen it."
    elif score == 2:
        return "Password is weak.", "Your password should be at least 8 characters long and include uppercase letters, numbers, and special characters."
    else:
        return "Password is very weak.", "Use a mix of uppercase letters, lowercase letters, numbers, and special characters, and ensure the password is at least 8 characters long."

def main():
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)
    print(strength)
    if feedback:
        print("Suggestion:", feedback)

if __name__ == "__main__":
    main()
