def first_vowel_finder(string):
    vowels = "aeiouAEIOU"

    for char in string:
        if char in vowels:
            return char

    return "No vowels found"


print(first_vowel_finder("Mng"))
