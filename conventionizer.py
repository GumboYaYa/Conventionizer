import os

# print(os.getcwd())

for root, dirs, files in os.walk('test_env'):
    print('Root path : ', root)
    print('Directories : ', dirs)
    print('Files : ', files)
    for d in dirs:
        if d[:].isupper():
            dlow = d[:].lower()
            os.rename(os.path.join(root, d), os.path.join(root, dlow))
            print('Set to lowercase: {0} > {1}'.format(os.path.join(root, d), os.path.join(root, dlow)))
