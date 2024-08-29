import random
from words import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()

def display_hangman(tries):
    stages = [  """
        -------------
        |           |
        |          /O\\
        |          \\|/
        |           |
        |          / \\
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O\\
        |          \\|/
        |           |
        |          / \\
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |          \\|/
        |           |
        |          / \\
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |          \\|/
        |           |
        |          / 
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |          \\|/
        |           |
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |          \\|
        |           |
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |           |
        |           |
        |
        |
    -
    """,
    """
        -------------
        |           |
        |           O
        |
        |
        |
        |
    -
    """,
    """
        -------------
        |           
        |
        |
        |
        |
        |
    -
    """
    ]

    return stages[tries]

def play(word):
    word_guess = "_ " * len(word)
    answer = False
    letters_guessed = []
    words_guessed = []
    tries = 8
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(word_guess)
    print("\n")
    
    while not answer and tries > 0:
        userans = input("Please guess a letter or a word: ").upper()

        if len(userans) == 1 and userans.isalpha():
            if userans in letters_guessed:
                print("Already guessed", userans, "please try another letter")
            elif userans not in word:
                print(userans, "is not in the word")
                tries -= 1
                letters_guessed.append(userans)
            else:
                print("Yay!", userans, "is in the word. Good job!")
                letters_guessed.append(userans)
                word_as_list = list(word_guess)
                indices = [i for i, letter in enumerate(word) if letter == userans]
                for index in indices:
                    word_as_list[index * 2] = userans
                word_guess = "".join(word_as_list)
                if "_" not in word_guess:
                    answer = True
        elif len(userans) == len(word) and userans.isalpha():
            if userans in words_guessed:
                print("Already guessed", userans, "please try another word")
            elif userans != word:
                print(userans, "is not the word")
                tries -= 1
                words_guessed.append(userans)
            else:
                answer = True
                word_guess = word

        else:
            print("Invalid guess")
        
        print(display_hangman(tries))
        print(word_guess)
        print("\n")

    if answer:
        print("Good job! You guessed the word!!")
    else:
        print("Sorry, you did not win :( The word was:", word, "Better luck next time!")

def main():
    word = get_word()
    play(word)
    while input("Play again? Y or N: ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
