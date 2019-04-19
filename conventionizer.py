import os
import pyperclip


# print(os.getcwd())

#TODO Get the target path validation working
'''
basedir = ''
clipboard = pyperclip.paste()


def valid_path(path):
    if os.path.exists(path):
        global basedir
        basedir = path


if os.path.exists(clipboard):
    basedir = clipboard
else:
    print('Your clipboard is either empty or not a valid path.')
    while not os.path.exists(input()):
        print('Please enter a valid path:')
    basedir = input()

print('The following directory has been set as target directory:')
print(basedir)
'''

basedir = os.getcwd()
folders = []
files = []

for root, dirs, files in os.walk(basedir):
    d_index = 0
    for d in dirs:
        if d[0] == '.':
            del dirs[d_index]
        else:
            folders.append(d)
        d_index += 1

print('Folders:')
print(folders)

'''
for root, dirs, files in os.walk(basedir):

    #print('Root path : ', root)
    #print('Directories : ', dirs)
    #print('Files : ', files)

    # Set all folder and file names to lowercase.

    for d in dirs:
        # any returns True if upper case letter is on string
        if any(d.isupper() for d in d):
            d_source = os.path.join(root, d)
            d_lower = os.path.join(root, d[:].lower())
            os.rename(d_source, d_lower)
            print('Set folder to lowercase: {0} > {1}'.format(d_source, d_lower))

    for f in files:
        if any(f.isupper() for f in f):
            f_source = os.path.join(root, f)
            f_lower = os.path.join(root, f[:].lower())
            os.rename(f_source, f_lower)
            print('Set file to lowercase: {0} > {1}'.format(f_source, f_lower))


for entry in os.scandir(basedir):
    if entry.is_dir():
        folders.append(entry.path)
    if entry.is_file():
        files.append(entry.path)

print('Folders:')
print(folders)
'''

