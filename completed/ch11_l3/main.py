def count_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    mylist = []
    for letter in text:
        if letter in vowels:
            mylist.append(letter)

    myset = set(mylist)
    num_of_vowels = len(mylist)

    return num_of_vowels, myset