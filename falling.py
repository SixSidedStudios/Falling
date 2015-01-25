import time
import os
from threading import Timer
import variables

# Intro
print '"Look", you say. "I didn\'t want to do this."'
time.sleep(3)
print '"So why are you taking me up anyway?"'
time.sleep(2)
os.system('cls')

# Use pausing to imitate animation
print '----FALLING----'
time.sleep(1)
os.system('cls')
print '----       ----'
print '    FALLING    '
time.sleep(0.5)
os.system('cls')
print '----       ----'
print '               '
print '    FALLING    '
time.sleep(0.5)
os.system('cls')
print '----       ----'
print '               '
print '               '
print '    FALLING    '
time.sleep(0.5)
os.system('cls')
print '----       ----'
print '               '
print '               '
print '               '
print '    FALLING    '
time.sleep(0.5)
os.system('cls')
print '----       ----'
print '               '
print '               '
print '               '
print '               '
print '    FALLING    '

time.sleep(1)
print ''
print 'Press ENTER to begin'
x = raw_input('')
os.system('cls')

# Game begins!
print '"Don\'t push me off! Stop!" you say.'
time.sleep(2)
print '"Too bad," the pilot says as he shoves you off.'
time.sleep(2)
print 'As you fall, you yell, "I\'m going to sue youuuuuuuu..."'
time.sleep(3)
os.system('cls')

print 'You are falling.'
time.sleep(1.5)
print 'Suddenly, you see a coin! It is golden, and has a cloud on it.'
time.sleep(3)
print 'To get the coin, type this quick!'
time.sleep(2)
print 'coin'
t = time.gmtime()
startTime = time.mktime(t)
word = raw_input('')
endTime = time.mktime(t)
if endTime - startTime > 3:
    print 'Too slow! Sorry, no coin for you.'
elif word.lower() != 'coin':
    print 'Didn\'t type it correct! Sorry, no coin for you.'
print 'Congrats you got the coin!'
variables.coins = variables.coins + 1

time.sleep(2)

# The end of the begining






















