import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer


class DieTestSuite(unittest.TestCase):
    def test_01_die_init(self):
        # Create instance
        die_test_object = Die(np.array([1,2,3,4,5,6]))
        self.assertEqual(type(die_test_object._df),pd.core.frame.DataFrame)
        
    def test_02_change_weight(self):
        # Create instance
        die_test_object = Die(np.array([1,2,3,4,5,6]))
        # Change weight 
        die_test_object.change_weight(1,5)
        # Test change
        self.assertEqual(die_test_object._df.iloc[0,0], 5)
        self.assertEqual(type(die_test_object._df),pd.core.frame.DataFrame)  
        
    def test_03_roll_die(self):
        # Create instance
        die_test_object = Die(np.array([1,2,3,4,5,6]))
        # Roll the die 5 times and test that it rolled 5 times
        self.assertEqual(len(die_test_object.roll_die(5)),5)
        
    def test_04_current_state(self):
        # Create instance
        die_test_object = Die(np.array([1,2,3,4,5,6]))
        die_test_object.change_weight(6,3)
        # Tests
        self.assertEqual(type(die_test_object.current_state()),pd.core.frame.DataFrame)   
        
          
class GameTestSuite(unittest.TestCase): 
    
    def test_05_game_init(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game_test_object = Game([die1,die2,die3])
        self.assertTrue(isinstance(game_test_object,Game))
        
    def test_06_play(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game_test_object = Game([die1,die2,die3])
        # Play game
        game_test_object.play(5)
        # Test
        self.assertEqual(type(game_test_object._df2),pd.core.frame.DataFrame)
        self.assertEqual(len(game_test_object._df2),5)
                         
    def test_07_show_result(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game_test_object = Game([die1,die2,die3])
        # Play game
        game_test_object.play(5)
        # Test
        self.assertEqual(type(game_test_object.show_result('wide')),pd.core.frame.DataFrame)
        self.assertEqual(type(game_test_object.show_result('narrow')),pd.core.frame.DataFrame)
        self.assertTrue(len(game_test_object.show_result('wide')) == 5)
        self.assertTrue(len(game_test_object.show_result('narrow')) == 15)

                         
class AnalyzerTestSuite(unittest.TestCase):  
                         
    def test_08_analyze_init(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game1 = Game([die1,die2,die3])
        # Play game
        game1.play(5)                 
        # Create Analyzer
        analyze_test_object = Analyzer(game1)
        self.assertTrue(isinstance(analyze_test_object, Analyzer))
                         
    def test_09_jackpot(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game1 = Game([die1,die2,die3]) 
        # Play game
        game1.play(5)
        # Create Analyzer
        analyze_test_object = Analyzer(game1) 
        self.assertTrue(isinstance(analyze_test_object.jackpot(),int))
                         
    def test_10_faces_per_roll(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game1 = Game([die1,die2,die3]) 
        # Play game
        game1.play(5)                 
        # Create Analyzer
        analyze_test_object = Analyzer(game1)
        self.assertTrue(isinstance(analyze_test_object.faces_per_roll(),pd.core.frame.DataFrame))
        self.assertEqual(len(analyze_test_object.faces_per_roll()),5)
                         
                         
    def test_11_count_combo(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game1 = Game([die1,die2,die3])
        # Play game
        game1.play(5)                 
        # Create Analyzer
        analyze_test_object = Analyzer(game1)
        analyze_test_object.faces_per_roll()
        # Test
        self.assertEqual(type(analyze_test_object.count_combo()),pd.core.frame.DataFrame)
                         
    def test_12_count_permutation(self):
        # Create Dice
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die3 = Die(np.array([1,2,3,4,5,6]))
        # Create Game
        game1 = Game([die1,die2,die3])
        # Play game
        game1.play(5)                 
        # Create Analyzer
        analyze_test_object = Analyzer(game1)
        # Test
        self.assertEqual(type(analyze_test_object.count_permutation()),pd.core.frame.DataFrame)
   
             
if __name__ == '__main__':
    
    unittest.main(verbosity=3)