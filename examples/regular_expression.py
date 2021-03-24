import re


text = '''
this is a long string

a multi line string

46833

special characters that need to be escaped
. * ^ + ? | [ ] { }

'''
pattern = re.compile(r'\d{3}[\.-]\d{3}[\.-]\d{4}')

with open('data.txt') as f:
    for line in f:
        matches = pattern.finditer(line)
        for match in matches:
            print(match)
# sentence = 'this is a SENTENCE 23'
# sentence = 'aababcaabaaabc'
# pattern = re.compile(r'a?')

# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)
