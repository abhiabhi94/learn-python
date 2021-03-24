import os


cwd = os.chdir('/home/curious/Desktop/temp/module/junk')


def create(prefix='file', extension='txt'):
    for num in range(1, 1001):
        filename = f'{prefix}_{num}.{extension}'
        with open(filename, 'x'):
            pass


def rename():
    filenames = os.listdir(cwd)
    # 01_file.txt
    for filename in filenames:
        name, extension = filename.split('.')
        name, num = name.split('_')

        num = num.zfill(2)
        os.rename(filename, f'{num}_{name}.{extension}')



def delete():
    filenames = os.listdir(cwd)
    for filename in filenames:
        os.remove(filename)
