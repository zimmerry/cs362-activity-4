def get_string():
    string = input("Enter a string: ")
    return string

def is_palindrome(string):
    return string == string[::-1]

def main():
    string = get_string()
    if is_palindrome(string):
        print(string, "is a palindrome.")
    else:
        print(string, "is not a palindrome.")

if __name__ == '__main__':
    main()