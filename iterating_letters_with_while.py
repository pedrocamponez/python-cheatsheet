sentence = 'This is a test sentence'

i = 0
letter_x_times = 0
most_recurrent_letter = ''

while i < len(sentence):
    current_letter = sentence[i]

    if current_letter == ' ':
        i += 1
        continue

    most_current_letter = sentence.count(current_letter)

    if letter_x_times < most_current_letter:
        letter_x_times = most_current_letter
        most_recurrent_letter = current_letter

    i += 1

print(
    'The letter that appeared most times was '
    f'"{most_recurrent_letter}", appearing '
    f'{letter_x_times}x'
)