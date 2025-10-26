print(
    False == False in [False],  # (False == False) and (False in [False])
    False is False is False,  # (False is False) and (False is False)
    True is False == False,  # (True is False) and (False == False)
    1 < 2 < 3,  # (1 < 2) and (2 < 3)
    sep='\n',
)
