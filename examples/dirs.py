import os

print(__file__)

here_relative = os.path.relpath(__file__)
here_real = os.path.realpath(__file__)

parent_dir = os.path.dirname(here_real)

text_file_loc = os.path.join(parent_dir, 'text.txt')

all_files = os.listdir(os.getcwd())
