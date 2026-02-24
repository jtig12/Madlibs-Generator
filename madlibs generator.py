# read the file document
with open("story.txt", "r") as f:
    story = f.read()
# creating a word list for the selected
# note: we use set to get unique data in a list and to avoid repitition
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        # slice through the words
        word = story[start_of_word: i + 1]
        # we use add instead of append since we using set()s
        words.add(word)
        start_of_word = -1
# getting a value for each of those words
answers = {}

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])


print(story)
