# chapter1 - 03
import re
string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word_list = string.split(' ')
number_of_character = []

for e in word_list:
    number_of_character.append(len(e))
