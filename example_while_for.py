saved_password = '123456'
typed_password = ''
reps = 0

while saved_password != typed_password:
    typed_password = input(f'Your password ({reps}x): ')
    
    reps += 1

print(f'The loop ended after {reps} reps, and your password is now correct.')

