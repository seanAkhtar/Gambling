#!/usr/bin/python3

import random, time, sys, string, logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

death = 0
luck = 50
cash = 150
count = 1

def typeIt(string):
    for i in range(len(string)):
        print(string[i],flush=True,end='')
        time.sleep(0.03)

def typeItSlow(slowValue):
    for i in range(slowValue):
        print('.',flush=True,end='')
        time.sleep(0.4)        
        
typeIt('\n\t\t\tGAMBLING MAN I\n\t\t\tTHE LIFE OF A DEGENERATE\n')

typeIt('\t\tWhere do you work? ')

answer = input()
workplace = string.capwords(answer)

def cutscene():
    typeIt('\n\t\tIt is Tuesday 9:00PM.')
    time.sleep(.7)
    typeIt(f'\n\t\tYou just did a 15 hour shift at {workplace} for $10.00 / hour.')
    time.sleep(.7)
    typeIt('\n\t\tYou dread going to work the next day. ')
    time.sleep(.7)
    typeIt('And the next day. ')
    time.sleep(.7)
    typeIt('And the next day. ')
    time.sleep(.7)
    typeIt('For the rest of your life.')
    time.sleep(1)

typeIt('\t\tSKIP CUTSCENE? (y/n): ')
cutAnswer = input()
if cutAnswer.lower() == 'n':
    cutscene()

age = str(random.randint(65,99))
typeIt('\n\t\tYou dream of starting a new life but you need $1000 first.')
typeIt(f'\n\t\tYou are in the {workplace} parking-lot walking towards your car when you come across an Old Man of age')
typeIt(f' {age}.')
time.sleep(0.7)
print()
    
def rob():
    global cash,death
    winning_number = random.randint(0,100)
    mans_cash = random.randint(130,250)
    print('\t\t', end='')
    logging.debug(f"winning number: {winning_number}") 
    for i in range(luck):
        if winning_number == i:
            cash += mans_cash
            typeItSlow(4)
            typeIt(f'Success! +${mans_cash}\n')
            return 0       
    knife = 50
    death += knife
    typeItSlow(6)
    typeIt(f'Failed. You have been reported. Danger level: {death}\n')

def kindness():
    global cash,luck
    add_luck = random.randint(8,12)
    print('\t\t',end='')
    typeItSlow(7)
    typeIt(f'+{add_luck} LUCK')
    oldmanphrases()
    time.sleep(0.7)
    print()
    if luck < 100:
        luck += add_luck

def oldmanphrases():
    if count < 5:
        typeIt(f'\n\t\t\tOld Man: "Bless your kind soul."')
    elif count >= 5:
        typeIt(f'\n\t\t\tOld Man: "You startin\' to get on my nerves!"')    
    
def level1():
    print()
    typeIt(f'\t\tAttempt({count})\n\t\tYour STATS:\tLUCK ~ [{luck}]\tCASH ~ $[{cash}]')
    typeIt(f'\n\t\tRob him? (y/n): ')
    answer = input()
    if answer.lower() == 'y':
        rob()
    if answer.lower() == 'n':
        kindness()

def degenerate():
    prisonSentence = random.randint(30,100)
    typeIt(f"\t\tPolice have stormed your home.\n\t\tYou have been convicted and sentenced to {prisonSentence} years in prison.\n\t\t")
    time.sleep(1)
    typeIt("DEGENERATE!")
    time.sleep(1)
    print('\n')
    sys.exit()

def annoying():
    print('\t\t', end='')
    typeItSlow(8)
    typeIt("The Old Man has had enough.\n\t\tHe puts you in a chokehold until you pass out.")
    time.sleep(.7)
    typeItSlow(6)
    typeIt("\n\t\tYou wake up the next morning.\n\t\t")
    time.sleep(.8)
    typeIt("Your cash is missing.\n\t\t")
    time.sleep(.8)
    typeIt("Your car is gone too. ")
    time.sleep(.8)
    typeIt(f"And you have been fired from {workplace}")
    time.sleep(2)
    typeIt("\n\t\tGAME OVER!")
    time.sleep(1)
    print('\n')
    sys.exit()

def level2():
    print('\t\t',end='')
    typeItSlow(7)
    typeIt(f'You quit your job, take the ${cash} and drive West.')
    typeItSlow(4)
    typeIt('\n\t\tYou start a small online business.')
    typeItSlow(4)
    time.sleep(1)
    typeIt('\n\t\t10 Years pass.')
    typeItSlow(13)
    time.sleep(1)
    typeIt('\n\t\tYour small business has expanded to a multi-million dollar corporation.')
    time.sleep(1)
    typeIt('\n\t\tYou buy an awesome loft.')
    time.sleep(1)
    typeIt('\n\t\tYou meet the person of your dreams and start a family')
    typeItSlow(4)
    time.sleep(1)
    typeIt('Congratulations')
    typeItSlow(4)
    typeIt('You have attained inner peace!')
    time.sleep(1)
    print('\n')
    print('\t\t',end='')
    typeItSlow(5)
    typeIt('Thank you for playing! :-)')
    print('\n')
    time.sleep(2)

while cash < 1000: 
    if count > 10:
        annoying()  
    if death > 99:
        degenerate() 
    level1()
    count += 1

level2()
    
