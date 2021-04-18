# Introduction to Python Loops

# To Implement Python Loops for Lists, Tuples, and Dictionaries

# List and Tuples

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

# Dictionaries

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)



#Loop Through the Characters of a Python String
          
def loop_over_list():
    my_list = ['one', 'two', 'three', 'four', 'five']
    
    for num in my_list:
        print(num)
    
    return my_list

loop_over_list()   

# Looping Over Ranges in Python

def loop_over_range():
    
    for num in range(1, 11):
        print(num)
        
    return range

loop_over_range()
    
 



