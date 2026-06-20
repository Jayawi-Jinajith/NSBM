# Q6 -

word = str(input("Enter a word (A-Z, a-z): "))
word = word.lower()
vowels = {"a", "e", "i", "o", "u"}
n = len(word)
i = 0
word_char = set()

while i < n:
    char = word[i]
    word_char.add(char)
    i = i + 1
vowel_word = vowels & word_char

if vowel_word == set():
    print("No vowels in the word, ", word)
else:
    print("Vowels found in word, ",word)
    print(vowel_word)
