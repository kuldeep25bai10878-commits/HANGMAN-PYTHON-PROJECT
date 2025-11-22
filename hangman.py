import random

# hangman_words.py

# A diverse list of words for Hangman
word_list = [
    "python", "variable", "function", "loop", "integer",
    "string", "boolean", "dictionary", "tuple", "list",
    "computer", "keyboard", "monitor", "internet", "network",
    "programming", "developer", "algorithm", "compile", "debug",
    "science", "planet", "galaxy", "ocean", "mountain",
    "forest", "desert", "island", "river", "valley",
    "school", "teacher", "student", "library", "university",
    "music", "guitar", "piano", "violin", "drums",
    "happy", "sad", "angry", "excited", "bored",
    "apple", "banana", "orange", "grape", "mango"
]
C = [word.upper() for word in word_list]
word=random.choice(C)
total_chances=8

guessed_word="-"*len(word)

while total_chances !=0:
  letter = input("Guess a letter: ").upper()

  if letter in word:
      for i in range(len(word)):
            if word[i]==letter:
                guessed_word=guessed_word[:i]+letter+guessed_word[i+1:]
                print(guessed_word)
      
      if guessed_word==word:
          print("Congratulations you won!!!!") 
          break   

          
  else:
      total_chances-=1
      print("Incorrect guess")
      print(f"You have {total_chances} chances left")
else:  
  print("Game Over")
  print("you LosE")   
  print("all the chances are exhausted")
  print("the correct word",word
      )