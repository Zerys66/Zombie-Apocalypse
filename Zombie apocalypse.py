import random
import webbrowser
turn=0
health=100
amunition=0
day=0
survivors=["you"]
random_cards=["Someone must die","You find fred","landmine 1-4 means you die","A plane drops supplies",]
global card1
def diceone(num):
    global dice1
    dice1=random.randint(1,num)
    return dice1
def dicetwo(num):
    global dice2
    dice2=random.ranint(1,num)
    return dice2
def next_turn(a):
    turn=a+1
    print(str(turn))
def change_time(a,b):
    time=a+b
    if time==2400:
        time=0000
    print(time)
def amo(a,b):
    amunition=a+b
    print(amunition)
def pickupcard():
    global card1
    length=len(random_cards)
    card1 = random_cards[random.randint(0,length)]
    random_cards.remove(card1)
    return card1
change_time(2300,100)
amo(amunition,60)
print("Welcome to zombie apocalypse")
print("You run to the themepark and meet the mystery gang, here are your comrades:")
survivors=["Shaggy","Scooby","Velma","Daphne"]
print(survivors)
print("you must pick up a card")
pickupcard()
print(card1)
if card1==random_cards[0]:
    print("you must roll the dice to find out who must die in your group")
    print(survivors)
    diceone(len(survivors))
    survivors.remove(survivors[dice1])
    random_cards.remove(card1[dice1])
    print(survivors)
if card1==random_cards[1]:
    survivors.append("Fred")
    random_cards.remove(card1[dice1])
    print(survivors)
if card1==random_cards[2]:
    random_cards.remove(card1[dice1])
print("hello")

