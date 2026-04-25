
while True:
    n1=int(input('enter the first number:'))
    n2=int(input('enter the second number:'))
    operator=input('enter the operator(+,-,*,/):')
    if operator=='+':
        print(n1+n2)
        print('enter q to quit or to continue enter any key')
        quit=input()
        if quit=='q':
            break
        elif quit!='q':
            continue
    
    elif operator=='-':
        print(n1-n2)
        print('enter q to quit or to continue enter any key')
        quit=input()
        if quit=='q':
            break
        elif quit!='q':
            continue
    elif operator=='*':
        print(n1*n2)
        print('enter q to quit or to continue enter any key')
        quit=input()
        if quit=='q':
            break
        elif quit!='q':
            continue
    elif operator=='/':
        if n2!=0:
            print(n1/n2)
            print('enter q to quit or to continue enter any key')
            quit=input()
            if quit=='q':
                break
            elif quit!='q':
                continue
        else:
            print('division by zero is not allowed')
            print('enter q to quit or to continue enter any key')
            quit=input()
            if quit=='q':
                break
            else:
                continue
    else:
        print('invalid operator, please enter a valid operator')
        operator=input('enter the operator(+,-,*,/):')
        continue