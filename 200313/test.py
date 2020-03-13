def compare_word(F_word, S_word):
    save_word = []
    if len(F_word) != len(S_word):
        return F_word, S_word
    elif len(F_word) == len(S_word):
        save_word = [F_word, S_word]
        save_word.sort()
        F_word = save_word[0]
        S_word = save_word[1]
        return F_word, S_word

print(compare_word("paple", "apple"))
print(compare_word("egg", "lemon"))