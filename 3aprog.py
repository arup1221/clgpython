Sentence = input("Enter a sentence")
wordList = Sentence.split(" ")
print("This sentence has: ", len(wordList), "words")
digcnt = upcnt = locnt = 0

for ch in Sentence:
    if '0' <= ch <= '9':
        digcnt += 1
    elif 'A' <= ch <= 'Z':
        upcnt += 1
    elif 'a' <= ch <= 'z':
        locnt += 1
print("This sentence has: ", digcnt, "digits", upcnt, "upper case letters", locnt, "lower case letters")