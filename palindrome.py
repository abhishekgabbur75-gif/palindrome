def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    string = input("Enter a string (minimum 3 characters): ")

    if len(string.strip()) < 3:
        print("Error: Input must be at least 3 characters long.")
    else:
        if is_palindrome(string):
            print("Yes! It is a palindrome.")
        else:
            print("No! It is not a palindrome.")
