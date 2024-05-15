import random

print('ROCK PAPER SCISSIOR GAME! \n' + 
        'Game Rules \n' +
        'Rock vs Paper --> Paper wins \n' +
        'Rock vs Scissior --> Rock wins \n' +
        'Paper vs Scissor --> Scissor wins \n')

while True:
    print('Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor')

    choice=int(input('Enter you choice: '))

    while choice>3 or choice<1:
        choice=int(input('Enter a valid choice please: '))
        
    if choice==1:
            choice_name='Rock'
    elif choice==2:
            choice_name='Paper'
    else:
            choice_name='Scissor'
    
    print('User choice is: ', choice_name)
    print('Now its computers turn!')

    comp_choice=random.randint(1,3)
    while comp_choice== choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'
    print("Computer choice is: ",comp_choice_name)
    print(choice_name,' VS ',comp_choice_name)
rocRock
