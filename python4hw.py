import random

sentence = "Woah, did you just see that *noun run by!?"
sentence = sentence.split()
nouns = ["dog", "boy", "crocodile", "kangaroo", "spider"]

indexCount = 0
for word in sentence:
    if word == "*noun":
        wordChoice = random.choice(nouns)
        sentence[indexCount] = wordChoice
    indexCount += 1

sentence = " ".join(sentence)

print(sentence)
