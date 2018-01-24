nums = [1,2,3,4,5,6,7,8,9,10]
print "\n ***** List nums *****"
print nums
print " ***** ***** *****\n"

# List Comprehensions
print "\n **********=============**********"
print " *      LIST COMPREHENSIONS      *"
print " **********=============**********\n"

# If I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print "\n If I want 'n' for each 'n' in nums"
print my_list
print " ***** ***** *****\n"
print " COMPREHENSION - If I want 'n' for each 'n' in nums"
print [n for n in nums]
print " ***** ***** *****\n"

# If I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print "\n If I want 'n*n' for each 'n' in nums"
print my_list
print " ***** ***** *****\n"
print " COMPREHENSION - If I want 'n*n' for each 'n' in nums"
print [n*n for n in nums]
print " ***** ***** *****\n"
# Using a map & lambda  -- lambda is an anonymous function
my_list = map(lambda n: n*n, nums)
print " Using a map & lambda"
print my_list
print " ***** ***** *****\n"

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print "\n I want 'n' for each 'n' in nums if 'n' is even"
print my_list
print " ***** ***** *****\n"
print " COMPREHENSION - I want 'n' for each 'n' in nums if 'n' is even"
print [ n for n in nums if n % 2 == 0]
print " ***** ***** *****\n"
# Using a filter & lambda  -- lambda is an anonymous function
my_list = filter(lambda n: n % 2 == 0, nums)
print " Using a filter & lambda"
print my_list
print " ***** ***** *****\n"

# I want a (letter, number) pair for each letter in 'abcd' and each numbser '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print "\n I want a (letter, number) pair for each letter in 'abcd' and each numbser '0123'"
print my_list
print " ***** ***** *****\n"
print " COMPREHENSION - I want a (letter, number) pair for each letter in 'abcd' and each numbser '0123'"
print [(letter, num) for letter in 'abcd' for num in range(4)]   # outer loop followed by inner loop
print " ***** ***** *****\n"

# Dictionary Comprehensions
print "\n **********=============**********"
print " *   DICTIONARY COMPREHENSIONS   *"
print " **********=============**********\n"

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print " Using zip to print tuples of (names, heros) pairs"
print zip(names, heros)

# I want a dictionary like dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print "\n I want a dictionary like dict{'name': 'hero'} for each name, hero in zip(names, heros)'"
print my_dict
print " ***** ***** *****\n"
print " COMPREHENSION - I want a dictionary like dict{'name': 'hero'} for each name, hero in zip(names, heros)'"
print {name: hero for name, hero in zip(names, heros)}
print " Adding a restriction - name is not equal to Peter"
print {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print " ***** ***** *****\n"

# Dictionary Comprehensions
print "\n **********==============**********"
print " *       SET COMPREHENSIONS       *"
print " **********==============**********\n"
print " Set is like a list but has only unique values\n"

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
print " The data set that we will use is the following list:"
print nums
print " ***** ***** *****\n"

# Turn the list into a set -- ie unique values
my_set = set()
for num in nums:
    my_set.add(num)
print " Turn the list into a set -- ie unique values"
print my_set
print " ***** ***** *****\n"
print " COMPREHENSION - Turn the list into a set -- ie unique values"
print {n for n in nums}
print " ***** ***** *****\n"