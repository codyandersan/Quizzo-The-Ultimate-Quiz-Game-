#--- API:— https://opentdb.com/api.php---

import requests as r # To fetch API
from time import sleep 
from json import loads # Response>JSON
from base64 import b64decode as bytedecode # To Decode the response
from random import shuffle # Shuffle
from sys import exit

class Quiz:
 def __init__(self):
  self.score = 0
  self.categories = ["General Knowledge",
"Entertainment: Books",
"Entertainment: Film",
"Entertainment: Music",
"Entertainment: Musicals and Theatres",
"Entertainment: Television",
"Entertainment: Video Games",
"Entertainment: Board Games",
"Science and Nature",
"Science: Computers",
"Science: Mathematics",
"Mythology",
"Sports",
"Geography",
"History",
"Politics",
"Art",
"Celebrities",
"Animals",
"Vehicles",
"Entertainment: Comics",
"Science: Gadgets",
"Entertainment: Japanese Anime and Manga",
"Entertainment: Cartoon and Animations"
]

# Get Category
 def get_category(self):
  print("Choose any one Category:—\n")
  sleep(1)
  for i in self.categories:
   print(self.categories.index(i)+1  , end=">\t")
   print(i)
  sleep(0.5)
  try:
   choice = int(input("\n>>>>>\t"))
  except:
   exit("Invalid Choice!\nTry Again Later!")
  if choice not in range(1,25):
   exit("Invalid Choice!\nTry Again Later!")
  return choice+8

# Get Difficulty    
 def get_difficulty(self):
  try:
   ch = int(input("\nChoose the difficulty level:—\n1>\tEasy\n2>\tMedium\n3>\tHard\n>>>>>\t"))
   print("\n")
  except:
   exit("Invalid Choice!\nTry Again Later!")
   
  if ch not in (1,2,3):
   exit("Invalid Choice!\nTry again later...")
  else:
   if ch == 1:
    return "easy"
   elif ch == 2:
    return "medium"
   elif ch == 3:
    return "hard"

# Get Question        
 def get_question(self,category,difficulty):
  return_list = []
  x = loads(r.get(f"https://opentdb.com/api.php?amount=5&category={category}&difficulty={difficulty}&type=multiple&encode=base64").text)
 
  for result in x["results"]:
    ques = bytedecode(result["question"]).decode("utf-8")
    answer = bytedecode(result["correct_answer"]).decode("utf-8")
    options = [bytedecode(i).decode("utf-8") for i in result["incorrect_answers"]]
 
    options.append(answer)
    shuffle(options)
   
    return_list.append({"question":ques,
   "answer":answer,
   "options":options
   })
  return return_list

# Update the score
 def update_score(self):
  self.score += 1

# Check if user wants to play again    
 def wanna_continue(self):
  choice = input("\nWould you like to play another match? (y/n)\n>>>>>\t")
  if "y" in choice.lower():
   return True
  else:
   return False
   
# Main Function to play the quiz 
 def play(self): 
  category_id = self.get_category()
  difficulty = self.get_difficulty()
  
  print("Getting your question....\n")
  response = self.get_question(category_id,difficulty)
  
  for resp in response:
   question = resp["question"]
   answer = resp["answer"]
   options = resp["options"]
   
   print("Question:",question)
   sleep(2)
   print("Your Options are:—")
   for i in options:
    print(options.index(i)+1,">\t",i)
   sleep(1)
   
   try:
    ch = int(input("Your Answer:\t"))
   except:
    exit("Invalid Choice!\nTry Again Later!")
   if ch not in range(1,5):
    exit("Invalid Choice!\nTry Again Later!")
   
   if ch-1 == options.index(answer):
    print("\n\nCorrect Answer!\n\n")
    self.update_score()
   else:
    print("\n\nWrong Answer!\nThe Correct Answer is:   ",answer,"\n\n")
   sleep(1)
  print("Your Score is:\t",self.score,"out of 5!")
  self.score = 0
#---------End of Class--------------  

if __name__ == "__main__":      
 quiz = Quiz()
 quiz.play()
 while True:
  if quiz.wanna_continue():
   quiz.play()
  else:
   break
 exit("\nThanks for playing!\nHave a nice day!")
