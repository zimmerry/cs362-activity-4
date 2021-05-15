def get_string():
    string = input("Enter a string: ")
    return string

def get_word_count(string):
    word_count = 0
    if len(string) == 0:
        return word_count
    elif string[0] != ' ':
        word_count += 1
    for i in range(1, len(string)):
        if string[i] == ' ' and string[i-1].isalpha():
            word_count += 1
    return word_count

def main():
    string = get_string()
    word_count = get_word_count(string)
    print(string, "has", word_count, "words.")

if __name__ == '__main__':
    main()