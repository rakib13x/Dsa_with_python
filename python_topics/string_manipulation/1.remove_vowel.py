# 1.Remove vowel from the string
def remove_vowel(string):
    result = ""

    vowels = "aeiouAEIOU"

    for char in string:
        if char not in vowels:
            result += char

    return result


print(remove_vowel("hello"))

# 2. Take a string and return it backwards using a for loop.


def string_reverser(string):
    reverse_string = ""

    for char in string:
        reverse_string = char + reverse_string
    return reverse_string


print(string_reverser("hello"))


# 3. Vowel_replacer:
def vowel_replacer(string):
    vowels = "aeiouAEIOU"
    new_str = string  # start with the original
    for char in string:
        for v in vowels:
            if char == v:
                new_str = new_str.replace(char, "*")  # replace from new_str, not string
    return new_str


print(vowel_replacer("hello"))

# 4. count total_vowel from a word


def count_vowel(string):
    count_vowel = {}
    vowels = "aeiouAEIOU"

    for char in string:
        if char in vowels:
            if char in count_vowel:
                count_vowel[char] += 1
            else:
                count_vowel[char] = 1
    return sum(count_vowel.values())


print(count_vowel("Helloo"))


# 5.capitalize all the vowels
def vowel_replacer(string):
    vowels = "aeiouAEIOU"
    new_str = string  # start with the original
    for char in string:
        for v in vowels:
            if char == v:
                new_str = new_str.replace(
                    char, char.capitalize()
                )  # replace from new_str, not string
    return new_str


print(vowel_replacer("hello"))

# 6. First vowel finder


def first_vowel_finder(string):
    vowels = "aeiouAEIOU"

    for char in string:
        if char in vowels:
            return char

    return "No vowels found"


print(first_vowel_finder("Mango"))
