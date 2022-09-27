# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

Player_0 = "Ruud Gullit" #Naam van de speler die de eerste goal gemaakt heeft
Player_1 = "Marco van Basten" #Naam van de speler die de tweede goal gemaakt heeft

goal_0 = 32 #tijd van eerste goal in minuten
goal_1 = 54 #tijd van tweede goal in minuten

scorers = Player_0 + " " + str(goal_0)+ ", " + Player_1 + " " + str(goal_1)
report = f'{Player_0} scored in the {goal_0}nd minute \n{Player_1} scored in the {goal_1}th minute'
print(report)

#part2
player = "Ronald Koeman"
x = player.find(" ") #zoekt naar spatie in de naam
first_name = player[:x]
last_name = player[x+1:]
last_name_len = len(last_name)
first_name_len = len(first_name)
name_short = first_name[0] + ". " + last_name

#Herhaling van de voornaam van player met toevoeging van een ! 
#Het aantal herhalingen is het aantal letters van de voornaam
chant = (first_name + str("! ")) * (first_name_len-1) + first_name + str("!") 

# Check if last character is a space
if chant[-1] != ' ': 
  good_chant = True
print(good_chant)
