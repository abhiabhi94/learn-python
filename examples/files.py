with open('text.txt', 'r') as f:
    for num, line in enumerate(f):
        if line.find('text') > -1:
            print(f'The word text is present on the line {num + 1}')


# print(content)
