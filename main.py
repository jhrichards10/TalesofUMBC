# Welcome User to the game
print()
print("~ Tales of UMBC ~ ")
print("(A work of Fiction) ")
print()
print("You are knight in the year 650 CE, and you`re trying to become the most famous knight of the all.")
print()
print("You decide to go on an adventure at Castle UMBC to earn your glory!")
print()

# User picks a character to help
print("You are outside the castle grounds, and see three different people asking for help. You could talk to:")
print("  A. The local blacksmith, who needs a rare sword ")
print("  B. The town`s teacher, who has a question ")
print("  C. The king, who needs a brave warrior ")
myCharacter = input("Who will you talk to? Please select option A through C: ")
print()

# User picks character A
if(myCharacter == "A"):
  print("You meet with the town blacksmith, looking for a legendary sword.")
  print("They tell you that the legend is that the sword is frozen in ice waiting to found. ")
  print("You choose to search for it :")
  print("  A. In the desert ")
  print("  B. In the forest ")
  print("  C. In the Artic ")
  blackSmith = input("Please select A through C: ")
  if(blackSmith == "C"):
    print("After looking long and hard through the Artic, you`ve found it - the legendary sword of programming! ")
    print("The blacksmith is thrilled and rewards you with a suit of armor worthy of a hero!")
  else:
    print()
    print("You searched and searched for the rest of your life, but you never found it.")
    print("It might`ve been a good idea to heed the blacksmith`s advice and go to a cold place")

# User picks character B
if(myCharacter == "B"):
  print("You meet with the town teacher, who is asking you a question")
  print("'I haveto be honest with you,' they say. 'I am not really qualified to teach and am struggling with this question'")
  print("They gesture to a math equation that reads as follows:")
  print("y = 6 + 2 + 1")
  yAnswer = 6 + 2 + 1
  yAnswer = int(yAnswer)
  yAnswer = input("Please enter the solution to this problem: ")
  if(yAnswer == '9'):
    print("'That makes perfect sense!' the teacher cries, and they award you with an honorary  degree. ")
    print("You are forever known as one of the smartest in the land! ")
  else:
    print("'Oh NO!' the teacher exclaims, you have answered incorrectly and have failed the students.")

# User picks character C
if(myCharacter == "C"):
  print("You meet with the king of UMBC, looking for a brave warrior. ")
  print("'I need someone to conquer a nearby dragon to save the kingdom! There is no time, head east and be ready for battle!'")
  print("You head east and find the dragon. You ready yourself for battle. But in a twist, the dragon asks you to solve a riddle in exchange for your kingdom.")
  print("'What two numbers, when added together, equal ten?'")
  print()
  print("You ponder for a moment. There`s multiple answers to this question, aren`t there? ")
  print("After thinking for a moment, you answer with two numbers... ")
  firstNumber = input("Enter the first number: ")
  secondNumber = input("Enter the second number: ")
  firstNumber = int(firstNumber)
  secondNumber = int(secondNumber)
  onlyAnswer = firstNumber + secondNumber
  onlyAnswer = int(onlyAnswer)
  if(onlyAnswer == 10):
    print(f"'Ah yes, {firstNumber} and {secondNumber} add up to 10!' the dragon explained ")
    print("The dragon decides to leave your kingdom alone, and the King declares you are the greatest hero in all the land")
  else:
    print("'You have answered incorrectly' the dragon says excitedly. Your kingdom is now mine and you have failed all your fellow citizens.")

# Print the End
print()
print("~ The End ~ ")