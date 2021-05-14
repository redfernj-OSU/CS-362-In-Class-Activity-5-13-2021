def check_palindrome(word):

    if (word == word[::-1]):
        return True
    else:
        return False

def main():
    print("Enter a word: ", end="")
    word = input()

    if (check_palindrome(word) == False):
        print(word, "is not a palindrome.")
    else:
        print(word, "is a palindrome.")


if __name__ == '__main__':
    main()
