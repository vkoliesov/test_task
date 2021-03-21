for number in range(11, 80):
    
    if number % 3 == 0 and number % 5 == 0:
        print('$$@@')
    
    elif number % 3 == 0:
        print('$$')
    
    elif number % 5 == 0:
        print('@@')

    else:
        print(f'Number is {number}')