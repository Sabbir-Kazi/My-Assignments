for x in range(0, 101):
    if x%3==0:
        print('Fizz')

    elif x%5==0:
        print('Buzz')

    elif x%3==0 and x%5==0:
        print('FizzBuzz')
    else:
        print(x)