def number_of_vowels(text):
    counter = 0
    for i in text:
        match i:
            case 'a' | 'e' | 'i' | 'u' | 'o' | 'A' | 'E' | 'I' | 'U' | 'O':
                counter += 1
    return counter

print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)