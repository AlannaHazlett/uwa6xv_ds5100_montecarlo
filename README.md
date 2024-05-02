# uwa6xv_ds5100_montecarlo
### Metadata: 
Creator: Alanna Hazlett\
Project: Monte Carlo Simulator

### Synopsis:
##### To install:        
```{python}
pip install montecarlo
```
##### To import:         
```{python}
from montecarlo.montecarlo import Die, Game, Analyzer
import numpy as np
import pandas as pd
import itertools
```
##### To create die:     
```{python}
faces_object = np.array([1,2,3,4,5,6])
die1=Die(faces_object)
```
##### To play a game:    
First create game object, this is reliant on die object(s) already being made.
```{python}
game1 = Game([die1,die2,die3])
```
Then utilize play method on game object.
```{python}
game1.play(5)
```
##### To analyze a game: 
First create analyzer object, this is reliant on die object(s) and game object already being made. 
```{python}
analyze1 = Analyzer(game1)
```
Utilize method of choice for analyzation needs.
```{python}
analyze1.jackpot()
```
```{python}
analyze1.faces_per_roll()
```
```{python}
analyze1.count_combo()
```
```{python}
analyze1.count_permutation()
```
                             

### API description: 
#### class Die: 
'''Creates a die object that has elements, face values and weights.'''\
INPUT: faces, a numpy array comprised of numbers or letters.

change_weight(face_value,new_weight):
'''Change the weight of a single face based on inputs.\
INPUTS: face_value, an value that is present on the die that you wish to change.
new_weight, an integer or float that will be assigned to the face of the die.'''

roll_die(num_roll = 1):
'''Rolls the die one or more times. \
INPUT: num_roll, integer to dictate number of times to roll the die. One time is the default.\
OUTPUT: outcome, list of the result(s) of roll(s).'''

current_state():
'''Displays a pandas DataFrame of the current state of the die, comprising of the face values and weights.'''
            
            
#### class Game:
'''Utilizes die object(s) to play a game, store the results, and display the results.'''\
INPUT: dice_in_play, a list of die objects. '''

play(num_rolls):
'''Rolls the di(c)e passed into the game object. Stores the results in a pandas DataFrame in wide format with roll number as index, columns as die index value, and results as entries.\
INPUT: num_rolls, an integer to specify number of times the di(c)e should be rolled, with default value of 1.'''

show_result(form = 'wide'):
'''Displays the pandas DataFrame of results. Checks to see if form argument is string of 'narrow' or 'wide'.\
INPUT: form, string to specify display type of pandas DataFrame, as narrow or wide. Default display is in wide format with roll number as index, columns as die index value, and results as entries.\
OUTPUT: pandas DataFrame of results.'''


#### class Analyzer:
'''Utilizes game object to analyze and display the results of the game.'''\
INPUT: game object

jackpot():
'''Computes how many times the game resulted in all faces being the same.\
OUTPUT: num_jackpot, an integer that indicates how many times the game resulted in all faces being the same.'''

faces_per_roll():
'''Computes how many times a given face is rolled in each event.\
OUTPUT: face_count_df, a pandas DataFrame with index of roll number, columns of face values, and entries for number of occurances.'''

count_combo():
'''Computes the distinct combinations of faces rolled, along with their counts.\
OUTPUT: cc_df, a pandas DataFrame with Index of distinct combinations and a column for the associated counts.'''

count_permutation():           
'''Computes the distinct permutations of faces rolled, along with their counts.\
OUTPUT: perm, a pandas DataFrame that has a MultiIndex of distinct permutations and a column for the associated counts. '''




