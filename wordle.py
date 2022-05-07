import pathlib

NUM_LETTERS = 5


def print_possibilities(guess, remaining_letters, words):
    if all(letter is not None for letter in guess):
        word = "".join(guess)
        if word in words:
            print(word)
        return

    for i in range(NUM_LETTERS):
        if guess[i] is None:
            for letter in remaining_letters:
                new_guess = guess[:i] + (letter,) + guess[i + 1 :]
                print_possibilities(new_guess, remaining_letters, words)
            return


def main():
    dict_path = pathlib.Path("/usr", "share", "dict", "words")
    words = [w.upper() for w in dict_path.read_text().split() if len(w) == NUM_LETTERS]
    guesses = [
        ("S", "I", "D", None, None),
        ("S", "I", None, "D", None),
        ("S", "I", None, None, "D"),
        (None, "I", "S", "D", None),
        (None, "I", "S", None, "D"),
        (None, "I", "D", "S", None),
        (None, "I", None, "S", "D"),
    ]
    remaining_letters = (
        "Q",
        "W",
        "R",
        "T",
        "Y",
        "I",
        "P",
        "S",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "Z",
        "X",
        "C",
        "V",
        "B",
        "M",
    )
    for g in guesses:
        print_possibilities(guess=g, remaining_letters=remaining_letters, words=words)


if __name__ == "__main__":
    main()
