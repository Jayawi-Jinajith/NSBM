# Q6 2nd answer -

word = str(input("Enter a word (A-Z, a-z): "))
word = word.lower()
n = len(word)
vowels = "aeiou"
i = 0
j = 0

while i < n:
    while j < 5:
        if word[i] == vowels[j]:
            print(vowels[j], " ", end=" ")
        j = j + 1
    i = i + 1
