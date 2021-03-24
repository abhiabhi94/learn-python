with open('meme.jpg', 'rb') as original_file:
    with open('meme_copy.jpg', 'wb') as copy_file:
        for line in original_file:
            copy_file.write(line)
