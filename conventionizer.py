import os

# print(os.getcwd())

for root, dirs, files in os.walk('test_env'):

    print('Root path : ', root)
    print('Directories : ', dirs)
    print('Files : ', files)

    for d in dirs:
        if d[:].isupper():
            d_source = os.path.join(root, d)
            d_lower = os.path.join(root, d[:].lower())
            os.rename(d_source, d_lower)
            print('Set folder to lowercase: {0} > {1}'.format(d_source, d_lower))

    for f in files:
        if f[:].isupper():
            f_source = os.path.join(root, f)
            f_lower = os.path.join(root, f[:].lower())
            os.rename(f_source, f_lower)
            print('Set file to lowercase: {0} > {1}'.format(f_source, f_lower))
