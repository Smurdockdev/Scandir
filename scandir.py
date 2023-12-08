import os

path = input('Enter the path: ')

def convMB(value):
    mb = 1024**2
    return round(value/mb, 2)

def getDirSize(path):
    pathtotal = 0
    for (root,dirs,files) in os.walk(path):
        print('Root Dir Path: ', root)
        total = 0
        for item in files:
            filePath = os.path.join(root, item)
            total += os.path.getsize(filePath)
        print('Subdirs: ', len(dirs),' Files: ', len(files),' Size: ', total)
        pathtotal += total
        print('-' * 40)
    return convMB(pathtotal)


print(getDirSize(path), 'MB')

