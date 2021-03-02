"""
Madlibs.py
Prompts the user for works, then prints a story with those words.
"""

# The template for the story

STORY = "Esta manhã %s acordou sentindo %s. 'Vai ser um %s dia!' Lá fora, vários %ss estavam protestando para manter %s nas lojas. Eles começaram a %s ao ritmo de %s, o que tornava todos os %ss muito %s. Preocupado, %s enviou uma mensagem de texto para %s, que voou %s para %s e caiu %s em uma poça de %s congelada. %s acordou no ano %s, em um mundo onde %ss governava o mundo."

print("MadLibs is starting!")

name = raw_input('Enter a Name: ')

adjective1 = raw_input('Enter an adjective: ')
adjective2 = raw_input('Enter an adjective: ')
adjective3 = raw_input('Enter an adjective: ')

verb = raw_input('Enter a verb: ')

noun1 = raw_input('Enter a noun: ')
noun2 = raw_input('Enter a noun: ')

animal = raw_input('Enter an animal: ')
food = raw_input('Enter a food: ')
frut = raw_input('Enter a frut: ')
superhero = raw_input('Enter a superhero: ')
country = raw_input('Enter a country: ')
dessert = raw_input('Enter a dessert: ')
year = raw_input('Enter a year: ')

print STORY%(name, adjective1, adjective2, animal, food, verb, noun1, frut, adjective3, name, superhero, name, country, name, dessert, name, year, noun2)
