# MADLIBS GENERATOR

### DESCRIPTION

    The idea of this project is that we will have some type of story will have replaceable words like an adjective or a location or weather condition etc. We will then ask the user to give us all of the different words we will then inject them into the story and read the story back out to the user.

### Steps taken to develop the project

---

1. First step is to generate a story and open a file and put it as a text file. The words we want the user to be able to change starts and is enclosed in <>
2. Then the next step is to read the file document where the story is.
   ```py
   with open("story.txt", "r") as f:
       story = f.read()
   ```
3. Then step is to set some variables that will help with the code such as and empty list for words, start of the word to not select anything, what we want to target at the start and what we would love to target at the end.

   ```py
       words = set()
       start_of_word = -1

       target_start = "<"
       target_end = ">"
   ```

4. Next step is to use a for loop to get both the index and the character to help us identify the words we want to work on.

   ```py
       for i, char in enumerate(story):

   ```

5. inside the loop the next step is to identify where the target word is starting with < then set starting word as that position index.

   ```py
       if char == target_start:
       start_of_word = i
   ```

6. Next step after this is to know the target word ending is > then select that wword and slice through it and then appends in words.

   ```py
       if char == target_end and start_of_word != -1:
           word = story[start_of_word: i + 1]
           words.add(word)
           start_of_word = -1
   ```

7. Next step is to generate a value for each of those words by first creating a dictionary.

   ```py
       answers = {}
   ```

8. The next step is to loop to assign each word in words into the dictionary.
   ```py
       for word in words:
           answer = input("Enter a word for" + word + ": ")
           answers[word] = answer
   ```
9. The final step is to replace those words in the dictionary into the story.
   ```py
       for word in words:
           story = story.replace(word, answers[word])
   ```

## OUTCOME EXECUTION

![alt text](<project image 1.png>)
