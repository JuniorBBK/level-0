def common_letters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    output = "Common letters: "

    for i in set(str1):
        for j in set(str2):
            if i == j:
                output += f'{i}, '

    return output[:-2]

