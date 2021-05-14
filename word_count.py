def word_length(word):
    return len(word.split())

def main():
    print("Enter a word: ", end="")
    word = input()

    print("The word '", word,"' is", word_length(word) , "words long.")


if __name__ == '__main__':
    main()
