import os
print('Exist:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.F_OK))
print('Readable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.R_OK))
print('Writable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.W_OK))
print('Executable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.X_OK))
