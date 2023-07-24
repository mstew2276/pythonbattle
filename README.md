# pythonbattle

To run: open vscode, click the top right play button on vscode to play the game in the terminal

Overview: Python Game is a project my classmates and I at Nucamp were told to create to show our understanding of variables and funcitons and how it can be used to create a simple turned based terminal game, I called mine battle of legends and added names and quotes from characters from animes 

What went well:
-The games character select functions very well in showing a minimal easy to choose select 
screen with a cool banner of the title which was generated with text to ascii generator

-The overall code is simple to understand and 103 lines long making it a perfect small showcase of my python knowledge

-The ability to be creative with the voicelines and characters is what makes this one of my more fun projects 

What issues I overcame:
-Ran into an issue in which I wanted to have the game prompt me to start again, added some code that would break out of the loop to reset the game but I have two for loop so it broke out of one but not the other and kept the characters the same health, to fix that issue I made it so that at the top of the for loop if one of the characters health was below zero it would break again to start at the very beginning of the game

-Ran into an issue in which I the damage was only a set amount and so the game would have the same outcome everytime, came up with a simple fix of importing random which allowed me to use random.randint to randomize the attack damage making it a little more up to chance of who will win

-Ran into an issue in which the game played through in a split second, realized there was no timing to the game to keep it from starting and finishing, to solve this I imported time and added time.sleep in the code so that there is enough time for the player to read the text and follow along with the code

What I learned:
-One thing I learned is that the capabilities of python can be used for so much more than just a backend language that works with data and sorting information but can be used to create fun games as well

What I want to improve:
-I want to add a lot more to the overall length of this so that it's not just a one and done thing but more of a full fledged story to the code

-This was part of the week 1 project for the python course, I would like to add more advanced conecepts that we learned later in the course such oop and data structures