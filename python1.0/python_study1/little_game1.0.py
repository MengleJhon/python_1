# Lin Xin

import random

def roll_dice(numbers = 3,points = None): # numbers:骰子个数 points:预置骰子点数列表
    print('<<<<< ROLL THE DICE ! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game(initial_money = 1000):
    choices = ['Big','Small']
    flag = 1
    while flag:
        print('<<<<<<<<< GAME STARTS ! >>>>>>>>>')
        your_choice = input('Big or Small :')
        if your_choice.lower().title() in choices:
            bet_money = input('How much you wanna bet ? - ')
            while not bet_money.isdigit():
                print('Please input a positive number !')
                bet_money = input('How much you wanna bet ? - ')
            points = roll_dice()
            total = sum(points)
            youWin = your_choice.lower().title() == roll_result(total)
            if youWin:
                initial_money = initial_money + int(bet_money)
                print('The points are',points,'You win !')
                print('You gained ' + bet_money + ', you have ' + str(initial_money) + ' now !')
                flag = 1
            else:
                initial_money = initial_money - int(bet_money)
                print('The points are', points, 'You lose ! But, come on !')
                print('You lose ' + bet_money + ', you have ' + str(initial_money) + ' now !')
                if initial_money > 0:
                    flag = 1
                else:
                    print('GAME OVER !')
                    flag = 0
            # start_game()
        elif your_choice.lower().title() == 'Stop':
            print('Let\'s play next time !\nBye !')
            flag = 0
        else:
            print('Invalid Words')
            flag = 1

start_game()