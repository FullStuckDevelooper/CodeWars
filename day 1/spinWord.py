def spin_word(sentence):
    x = sentence.split(' ')
    for i, word in enumerate(x):
        if len(word) >= 5:
            x[i] = word[::-1]
    return ' '.join(x)


print(spin_word('Ayam beranak banyak'))
