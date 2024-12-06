"""
File: count_words.py
--------------------
This program is supposed to count each word in a text file.

But it does something else. 
 - What does it do?
 - Can you fix it?
"""

import sys

FILENAME = "tinytext.txt"
# FILENAME = "smalltext.txt" # Uncomment to use this file
# FILENAME = "gettysburg.txt" # Uncomment to use this file

# What does this function do? Can you fix it?
def count_each_word(text):
    counts = {}

    for word in text:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    print("Results:")
    print(counts)


# =======
# You don't need to read/change anything below this
# =======


PUNCTUATION = '.!?,-:;'
def delete_punctuation(s):
    result = ''
    for char in s:
        # Check char is not a punctuation mark
        if char not in PUNCTUATION:
            result += char      # append non-punctuation characters

    return result


def main():
    with open(FILENAME, 'r') as file:   # Open file to read
        all_text = ""
        for line in file:
            line = line.strip().lower() # Lowercase, remove newline
            line = delete_punctuation(line)
            all_text += line + " "
        count_each_word(all_text)


# Python boilerplate.
if __name__ == '__main__':
    main()
