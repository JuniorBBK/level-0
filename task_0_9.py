def vowels_in_string(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u"]
    output = "Vowels: "

    for i in set(word):
        for j in vowels:
            if i == j:
                output += f'{i}, '

    print(output[:-2])
