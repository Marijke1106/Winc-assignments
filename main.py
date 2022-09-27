# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from time import time


G = "Ruud Gullit"
B = "Marco van Basten"
goal_0 = 32 #tijd van eerste goal in minuten
goal_1 = 54 #tijd van tweede goal in minuten
scorers = (G + " " + (str(goal_0))+ ", " + B + " " + (str(goal_1)))
report = f'{G} scored in the {goal_0}nd minute''\n'f'{B} scored in the {goal_1}th minute'
print(report)

#part2
player = "Ronald Koeman"
x = player.find(" ") #zoekt naar spatie in de naam
first_name = (player[:x])
last_name = (player[x+1:])
last_name_len = len(last_name)
name_short = (first_name[0]) + ". " + last_name
chant = (first_name + str("! ")) *5 + (first_name + str("!"))

# Check if last character is a space
if chant[-1] != ' ': 
  good_chant = True
print(good_chant)
