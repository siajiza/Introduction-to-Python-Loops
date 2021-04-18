# Introduction-to-Python-Loops
Python Loops:  introduction is going to be using a for-in loop


To Implement Python Loops for Lists, Tuples, and Dictionaries

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



# Loop Through the Characters of a Python String
          
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

 
# To Continue and Break in Python Loops with for

    usernames = [
      'jon',
      'tyrion',
      'theon',
      'cersei',
      'sansa',
    ]

# Using continue

    for username in usernames:
      if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
      else:
        print(f'{username} is allowed')


# Using break

    for username in usernames:
      if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
      print(username)

# other example with break

        def loop_and_break():
            vegetables = ["onion", "broccoli", "apple", "spinich"]

            for vegetable in vegetables:
                if vegetable == 'apple':
                    print(f'{vegetable} is not a vegetable')
                    break
                print(vegetables)

            return vegetables

        loop_and_break()

