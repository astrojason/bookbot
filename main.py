def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_obj = {}
    for char in text:
        char = char.lower()
        if char in 'abcdefghijklmnopqrstuvwxyz':
            char_obj[char] = char_obj.get(char, 0) + 1
    return char_obj


with open('./books/frankenstein.txt') as f:
    file_contents = f.read()

print('---Begin report  of books/frankenstein.txt---')
print(f'{count_words(file_contents)} found in the document')
print('')
chars = count_chars(file_contents)
for char, count in chars.items():
    print(f"The '{char}'' was found {count} times")
print('---End report---')
