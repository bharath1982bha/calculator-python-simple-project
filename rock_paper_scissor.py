import random
a=['rock','paper','scissors']
user_score=0
system_score=0
while system_score <3 and user_score <3:
    system=random.choice(a)
    user=input('enter (rock or paper or scissors) or q to quit:').lower()
    if user=='q':
        break
    if user in a :
        if user == system:
            print(f'system choice: {system}')
            continue
        if (user=='rock' and system=='scissors') or (user=='paper' and system=='rock') or (user=='scissors' and system=='paper'):
            user_score+=1
            print(f'system choice: {system}')
            print('user_score:',user_score)
        else:
            system_score+=1
            print(f'system choice: {system}')
            print('system_score:',system_score)
    else:
        print("enter a valid input")
if user_score > system_score:
    print('you win!😍')
    print(f'user score: {user_score}')
elif user_score==system_score:
    print('game draw 😊')
else:
    print("system wins😢")
    print(f'system score: {system_score}')
        
