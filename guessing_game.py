import random

class GuessingGame():
    def __init__(self,answer,user_guess = None):
        self.answer = answer
        self.user_guess = user_guess
    
    def guess(self,user_guess):
        self.user_guess = user_guess
        if user_guess == None:
            return None
        if int(user_guess) > self.answer:
            return "High"
        if int(user_guess) < self.answer:
            return "Low"
        if int(user_guess) == self.answer:
            return "Correct"

    
    def solved(self):
        if self.guess(self.user_guess) == "Correct":
            return True
        return False

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")

#print(game.solved())
#print(game.guess(5))
#print(game.guess(20))
#print(game.solved())
#print(game.guess(10))
#print(game.solved())
