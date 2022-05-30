def common_letters(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    output = "Common letters: "

    for i in set(word1):
        for j in set(word2):
            if i == j:
                output += f'{i}, '

    return output[:-2]
