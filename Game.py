'''Game Assignment
Creat following games with def function concepts

Number guessing game

Colour guessing game

Rock Paper Scissor game'''

#### Number Guessing Game
def number_guess():
    print('*'*8,"Welcome to Number Guessing Game",8*'*')
    import random
    s_num=random.randint(1,100)
    att=1
    while att<8:
        num= int(input("Enter the Guess"))
        if num>0  and num<=100:
            if num > s_num:
                print(f'Your guess is higher than secret number, You have {7-att} attempts remaining')
            elif num < s_num:
                print(f'Your guess is lower than the secret number, You have {7-att} attempts remaining')
            else:
                print(f'You have found the secret Number!!! in {att} attempts')
                break
        else:
            print("You have to enter the guess number between 1 to 100")
        att += 1
    if num == s_num:
        print(8*'*',"You won the game", 8*'*')
    else:
        print("Your attempts are over, Better luck next time")
        
### Colour Guessing Game
def colour_guess():
    print('*'*8,"Welcome to Colour Guessing Game",8*'*')
    import random
    color=["orange","red", "green", "white","blue"]
    s_color=random.choice(color)
    att=1
    while att<4:
        user_color=input("Enter Your Colour Guess\n 1.Orange\n 2.Red\n 3.Green\n 4.White\n 5.Blue\n >>>")
        if user_color.lower() in color:
            if user_color.lower() == s_color:
                print(f'You have guessed the {s_color.title()} Colour Correctly in {att} attempts')
                break
            else:
                print(f'Your Guess is Wrong, You have {3-att} attempts remaining\n')
        else:
            print("Invalid entry, Select Colours from \n 1.Orange\n 2.Red\n 3.Green\n 4.White\n 5.Blue")
        att+=1
    if user_color.lower() == s_color:
        print("*"*8,"Well Done, You won the Colour Guessing Game","*"*8)
    else:
        print("Sorry Your Attempts are over, Try again later!!!")

###Rock, Paper, Scissor Game
def rps_game():
    print('*'*8,"Welcome to Rock(✊), Paper(✋), Scissor(✌️) Game",8*'*')
    import random
    item=["rock","paper","scissor"]
   
    att=1
    name=input("Enter Your name")
    rounds=int(input("Enter the no. of rounds to play"))
     
    s_score=0
    u_score=0
    while att<=rounds:
        print("______________________\n")
        system=random.choice(item)
        user_choice=input("Enter Your Choice: ").lower()
        if user_choice in item:
            if(system == "rock" and user_choice == "paper" or system == "paper" and user_choice == "scissor" or system =="scissor" and user_choice == "rock"):
                print(f'Round {att}: {name} wins the round')
                u_score+=1
            elif(system == "rock" and user_choice == "scissor" or system == "paper" and user_choice == "rock" or system =="scissor" and user_choice == "paper"):
                print(f'Round {att}: System wins the round')
                s_score+=1
            else:
                print(f'Round {att}: Tie Round')
                s_score+=0.5
                u_score+=0.5
        else:
            print("Enter Valid Input")
            att=att-1
        att+=1
    print('*'*8"\nGame Result",'*'*8)
    if (s_score> u_score):
        print(f'System : {s_score} \n{name} : {u_score} \nSorry!!! You lost the Game')
    elif(u_score> s_score):
        print(f'System : {s_score} \n{name} : {u_score} \nCongratulations!!! You Won the Game')
    else:
        print(f"System : {s_score} \n{name} : {u_score} \nThe match ends with tie !!!")

    