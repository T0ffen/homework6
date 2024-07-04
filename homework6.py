my_dicts = {'Viego': 1998, 'Hecarim': 1999, 'Varus': 2001}
print(my_dicts)
print(my_dicts['Viego'])
print(my_dicts.get('Vex', 1997))
my_dicts.update({'Kayn': 2000,
                 'Akali': 2000})
del my_dicts['Varus']
print(my_dicts.get('Varus', 2001))
print(my_dicts)

my_set = {2, 2, False, 2, 'rar',
          False, 2, 'rar'}
print(my_set)
my_set.add(9)
my_set.add('huh')
my_set.discard(False)
print(my_set)
