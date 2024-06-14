import sys
import random

thisComputerNumber = random.randint(1, 10)
# casting value from string to int

try:
    userNumber = int(input("Guess the number: "))
except Exception:
	print("Enter a valid number: ")
	sys.exit()
      
if (userNumber == thisComputerNumber):
	print("Congratulations 🚀🚀🚀🚀🚀🚀🚀!")
else:
	print("Try again 🔄!")






