import numpy as np
import pandas as pd
import itertools

class Die():
    '''Creates a die object that has elements, face values and weights.'''
    def __init__(self,faces):
        '''INPUT: faces, a numpy array comprised of numbers or letters.
           Initializes the die object creating a pandas DataFrame with index of face values and a column of the weights, which are defaulted to one for each face value.
           Checks to make sure faces is a numpy array and that the face values are distinct.'''
        self.faces = faces
        self.weights = [1.0 for i in self.faces]
        self._df = pd.DataFrame(dict(faces=self.faces, weights=self.weights)).set_index(['faces'])
                
        if type(self.faces) != np.ndarray:
            raise TypeError ("faces must be NumPy Array")
        else:
            pass
        
        _s = set()
        for i in range(0,len(self.faces)):
            _s.add(self.faces[i])
        if (len(_s) != len(self.faces)):
            raise ValueError ("Each face of die must be distinct")
            
            
    def change_weight(self,face_value,new_weight):
        '''Change the weight of a single face based on inputs.
           INPUTS: face_value, an value that is present on the die that you wish to change.
                   new_weight, an integer or float that will be assigned to the face of the die.'''
        if face_value in self.faces:
            if isinstance(new_weight, (float,int)):
                self._df.loc[face_value, 'weights'] = new_weight
            else: 
                raise TypeError ("The new weight must be a number")
        else:
            raise IndexError ("The face value you entered to be changed is not currently on the die")
    
    
    def roll_die(self,num_roll = 1):
        '''Rolls the die one or more times. 
           INPUT: num_roll, integer to dictate number of times to roll the die. One time is the default.
           OUTPUT: outcome, list of the result(s) of roll(s).'''
        outcome = [self._df.sample(weights=[i/sum(self._df.weights) for i in self._df.weights]).index[0] for i in range(num_roll)]
        return outcome    
   

    def current_state(self):
        '''Displays a pandas DataFrame of the current state of the die, comprising of the face values and weights.'''
        return self._df
            
        
class Game():
    '''Utilizes die object(s) to play a game, store the results, and display the results.'''
    def __init__(self,dice_in_play):
        '''Initializes game object utilizing die objects.
           INPUT: dice_in_play, a list of die objects. '''
        self.dice_in_play = dice_in_play
        
        
    def play(self,num_rolls):
        '''Rolls the di(c)e passed into the game object. Stores the results in a pandas DataFrame in wide format with roll number as index, columns as die index value, and results as entries.
           INPUT: num_rolls, an integer to specify number of times the di(c)e should be rolled.'''        
        roll_result = []
        for die in self.dice_in_play:
            outcome = die.roll_die(num_rolls)
            roll_result.append(outcome)
        d_result = dict(enumerate(roll_result))
        _df2 = pd.DataFrame(d_result)
        _df2.index = np.arange(1, len(_df2) + 1)
        _df2.index.name = "Roll Number"
        self._df2 = _df2
        
        #List of dice indices
        keys_list = list(d_result.keys())
        self.keys_list = keys_list
        
    
    def show_result(self,form = 'wide'):
        '''Displays the pandas DataFrame of results. Checks to see if form argument is string of 'narrow' or 'wide'.
           INPUT: form, string to specify display type of pandas DataFrame, as narrow or wide. Default display is in wide format with roll number as index, columns as die index value, and results as entries.
           OUTPUT: self._df2 or narrow, pandas DataFrame of results.'''
        if form == 'wide':
            return self._df2
        elif form == 'narrow': 
            narrow = pd.DataFrame(self._df2.stack([0]))
            narrow.index.names = ['Roll Number','Die ID']
            narrow.columns = ['Results']
            return narrow
        else:
            raise ValueError ("Results must be in 'wide' or 'narrow' form. Default is 'wide'.")
        

class Analyzer():
    '''Utilizes game object to analyze and display the results of the game.'''
    
    
    def __init__(self,game):
        '''Receives game object, checks to make sure it is a game object, and initalizes it.
        INPUT: game object.'''
        if isinstance(game, Game) == True:
            self.game = game
        else:
            raise ValueError ("Parameter passed must be a Game object")
       
    
    def jackpot(self):
        '''Computes how many times the game resulted in all faces being the same.
           OUTPUT: num_jackpot, an integer that indicates how many times the game resulted in all faces being the same.'''
        num_jackpot = 0
        num_jackpot = sum(self.game._df2.eq(self.game._df2.iloc[:, 0], axis=0).all(1)) 
        return num_jackpot  
    
    
    def faces_per_roll(self):
        '''Computes how many times a given face is rolled in each event.
           OUTPUT: face_count_df, a pandas DataFrame with index of roll number, columns of face values, and entries for number of occurances.'''
        face_count_df = self.game._df2.stack().groupby(level=0).value_counts().unstack(fill_value=0)
        self.face_count_df = face_count_df
        return face_count_df
    
    
    def count_combo(self):
        '''Computes the distinct combinations of faces rolled, along with their counts.
           OUTPUT: combinations, a pandas DataFrame with Index of distinct combinations and a column for the associated counts.'''       
        combinations = list(itertools.combinations_with_replacement(self.face_count_df,self.game._df2.shape[1]))    
        combo = [str(list(i)) for i in combinations]
        cc_df = pd.DataFrame(index = combo)
        cc_df.index.names = ['Combinations']
        cc_df['Count'] = 0
        #Getting counts for cc_df by finding matching rows in self.game._df2
        for i in range(1,len(self.game._df2) + 1):
            match = str(sorted(list(self.game._df2.loc[i])))
            cc_df.loc[match][0] = cc_df.loc[match][0] + 1
        return cc_df
    
    
    def count_permutation(self):           
        '''Computes the distinct permutations of faces rolled, along with their counts.
           OUTPUT: perm, a pandas DataFrame that has a MultiIndex of distinct permutations and a column for the associated counts. '''
        perm = pd.DataFrame(self.game._df2.value_counts(self.game.keys_list).sort_index())
        return perm        