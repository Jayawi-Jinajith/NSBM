# Q6

word = str(input("Enter a word (A-Z, a-z): "))
word = word.lower()

vowels = {'a', 'e', 'i', 'o', 'u'} 
words = set()
i = 0

if (char in vowels for char in word):
    while i < len(word):
        words.add(word[i])
        i = i + 1
    # words = set(word)

    vowels_in_word = vowels & words
    # vowels_in_word = vowels.intersection(set(word))
    print(vowels_in_word)
else:
    print(word, "has no Vowels")

print()