

from gameit.aqeelshamz import treasureHunt

from gameit.urmila import HuntingBirds




from gameit.aayahda import snakesGame
from gameit.MohdShibin import snakeGame
from gameit.AditiAjithkumar import SnakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.majid_2002 import jumpMan
from gameit.abhijithram import abhiGame
from gameit.kmSidharthM import Space_Invader
from gameit.anuragrajanp import feedTheSnake
from gameit.AnnMol_2002 import sudoku
from gameit.example import exampleGame
from gameit.ash394 import pongGame
from gameit.vishakh import car_game
from gameit.ebinjose02 import Snake

def main():
    games = {
      "aayahda": snakesGame,
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "majid-2002":jumpMan,
      "sreni":Tic_Tac_Toe, 
      "abhijithram":abhiGame,
      "kmSidharthM":Space_Invader,
      "anuragrajanp":feedTheSnake,
      "AditiAjithkumar":SnakeGame,
<<<<<<< HEAD
      "urmila":HuntingBirds
=======
      'AnnMol_2002':sudoku,
<<<<<<< HEAD
      "Ash-394": pongGame
>>>>>>> ad5d34bbd12b3a51f342122ffeb1665e1f802c0c
=======
      "Ash-394": pongGame,
      "vishakh": car_game,
      "ebinjose02":Snake
>>>>>>> 05ce253c4947893a0c8f89819108da399b0b4682
    }

    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except KeyError:
            print("Username not found!!.")


if __name__ == "__main__":
  main()
