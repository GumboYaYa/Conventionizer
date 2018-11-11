import os

print(os.getcwd())

for root, dirs, files in os.walk('./'):
    print('Root path : ', root)
    print('Directories : ', dirs)
    print('Files : ', files)
