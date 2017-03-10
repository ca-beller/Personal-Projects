# This module will be the main page for the project and will be the executable python script
# import required libraries
import setup
from time import sleep



intro, guests = setup.setup()

print (intro, guests)

sleep(60)

print('Is everything ok?')