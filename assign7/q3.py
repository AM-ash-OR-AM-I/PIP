# Write a function that takes a number as an input parameter and returns the correspond text in words, for example, on input 452, the function should return ‘Four Five Two’. Use a dictionary for mapping digits to their string representation.

# Code

def num_to_words(num):
    num_dict = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    num = str(num)
    num_words = ''
    for i in num:
        num_words += num_dict[int(i)] + ' '
    return num_words

