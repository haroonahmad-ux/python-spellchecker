name = {
    "taariq": "tariq",
    "heroon": "haroon",
    "kemran": "kamran",
    "shep": "shop",
    "omar": "umar",
    "mofassar": "mufassar",
    "chadger": "charger",
    "mabile": "mobile",
    "dasplay": "display"
}

home = [
    "tariq", "haroon", "kamran", "shop", "umar",
    "mufassar", "charger", "mobile", "display"
]


def word_checker(user):
    return user in home


def suggestions_checker(user):
    if user in name:
        return name[user]
    else:
        return False


def spell_checker():
    correct_count = 0
    wrong_count = 0
    user = ""

    while user != "exit":
        user = input("Enter your message: ").lower().strip()

        if user == "exit":
            break

        sentence = user.split()

        for word in sentence:
            if word_checker(word):
                correct_count += 1
                print("Correct word:", correct_count)
                print(f"Word: {word}")
                print("Correct word")

            else:
                wrong_count += 1
                print("Wrong word:", wrong_count)

                output = suggestions_checker(word)

                if output:
                    print(f"Word: {word}")
                    print(f"Suggested word: {output}")

                else:
                    print(f"Word: {word}")
                    print("Suggestions not available")


spell_checker()
