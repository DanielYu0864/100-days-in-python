# Write your code below this line 👇
def printTest():  
  a = 'Hello'
  b = 'world'
  print(f"{a} {b}!") #f-string
  print("Hello world!\"Hiiiiiiiiiiiiiiiiiiiii\"") #print double quotes in string
  print("Hello world!\nHello world!") # next line
  print('Hello ' + input('What\'s your name?')) #get input than print

printTest()

def bandGenerator():
  print('Welcome to the Band Name Generator.')
  city = input("What's name of the city you grew up in?")
  pet = input("What's your pet's name?")
  print(f"Your band name cound be {city} {pet}")

# bandGenerator()

def greeting():
  name = input('What\'s your name?')
  print('Hello {}!'.format(name))
  city = input('Where are you from?')
  print(f'Nice! I am from {city} too!')

# greeting()