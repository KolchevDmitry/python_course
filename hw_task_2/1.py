str_1 = 'Python asdqwe go asdqw sdf php C'

list_1 = str_1.split()

print(list(filter(lambda x: x != 'Python' and x != 'go' and x != 'php' and x != 'C', list_1)))
