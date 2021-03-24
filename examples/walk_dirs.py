import os


current_working_directory = os.getcwd()


for dirpath, dirnames, filenames in os.walk(current_working_directory):
    print(
        f'inside the path: {dirpath}, the directories are:{dirnames}, '
        f'the files are: {filenames}'
    )
