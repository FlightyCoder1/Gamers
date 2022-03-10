player_won = False
tutorial_check = 'a'
answera = []
answerb = []
wins = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9] ]
answers = []
def printnewboard():
    if 1 in answera:
        print('O|', end = '')
    elif 1 in answerb:
        print('X|', end = '')
    else:
        print('_|', end = '')
    if 2 in answera:
        print('O|', end = '')
    elif 2 in answerb:
        print('X|', end = '')
    else:
        print('_|', end = '')
    if 3 in answera:
        print('O')
    elif 3 in answerb:
        print('X')
    else:
        print('_')
    if 4 in answera:
        print('O|', end = '')
    elif 4 in answerb:
        print('X|', end = '')
    else:
        print('_|', end = '')
    if 5 in answera:
        print('O|', end = '')
    elif 5 in answerb:
        print('X|', end = '')
    else:
        print('_|', end = '')
    if 6 in answera:
        print('O')
    elif 6 in answerb:
        print('X')
    else:
        print('_')
    if 7 in answera:
        print('O|', end = '')
    elif 7 in answerb:
        print('X|', end = '')
    else:
        print(' |', end = '')
    if 8 in answera:
        print('O|', end = '')
    elif 8 in answerb:
        print('X|', end = '')
    else:
        print(' |', end = '')
    if 9 in answera:
        print('O')
    elif 9 in answerb:
        print('X')
    else:
        print('')
        
def ask_answer(ask, turn):
    global player_won
    global answers
    global answerb
    global answera
    x = 0
    x = input(ask)
    try:
        print(int(x))
    except:
        print("That answer is invalid")
        ask_answer(ask, turn)
        return
    if int(x) in answers or int(x) > 9 or int(x) < 1 or not int(x)%1 == 0:
        print("That answer is invalid")
        ask_answer(ask, turn)
    else:
        answers.append(int(x))
        answers = sorted(answers)
        if answers == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("It's a draw!")
            player_won = True
            return
        if turn == 1:
            answera.append(int(x))
            answera = sorted(answera)
        elif turn == 2:
            answerb.append(int(x))
            answerb = sorted(answerb)
        print(answera)
        print(answerb)
        printnewboard()
        for element in wins:
            if set(element).issubset(set(answera)):
                print("Player 1 won.")
                player_won = True
                return
            if set(element).issubset(set(answerb)):
                print("Player 2 won.")
                player_won = True
                return
    return 
         

print(' | | ')
print('‾|‾|‾')
print('‾|‾|‾')
#two_player_check = input('a = one-player b = two-player') 
while tutorial_check == "a":
    tutorial_check = input("a = Tutorial. b = skip.") 
    #if two_player_check == 'b':
    if tutorial_check == 'a':
        print('1|2|3')
        print('4|5|6')
        print('7|8|9')
        tutorial_check = 'b'
    else:
        print("Skipping Tutorial")
        tutorial_check = 'b'

while player_won == False:
    ask_answer("Player 1, type your answer", 1)
    if player_won == False:
        ask_answer("Player 2, type your answer", 2)
print("GG!")
