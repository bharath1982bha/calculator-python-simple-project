import random

number=random.randint(1,50)
print('enter a number (1,50)')
for n in range(5):
    print(f'you left {5-n} chances')
    num=int(input('number: '))
    if num==number:
        print('you won!')
        print(number)
        break
    elif num<number:
        print("too low")
    else:
        print('too high')
else:
    print('you lost!')
    print('number was,',number)   
