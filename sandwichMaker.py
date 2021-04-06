#! python3
# Practice prosjekt som lager en sandwich

import pyinputplus as pyip
import random

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'])
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheeseYesNo = pyip.inputYesNo('Do you want cheese?')
if cheeseYesNo == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
condiments = pyip.inputYesNo('Do you want mayo, mustard, lettuce or tomato?')
numSandwiches = pyip.inputInt('How many sandwiches do you want?', min=1)
