# 5. Does a word have duplicate words

word = "hello"


def word_have_duplicate(word):
    seen = {}
    for letter in word:
        if letter in seen:
            return True
        else:
            seen[letter] = True
    return False


result2 = word_have_duplicate(word)
print(result2)
