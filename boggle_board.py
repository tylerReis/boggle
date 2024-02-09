import random
import re

class BoggleBoard:
  DICE = ["AAEEGN",
          "ELRTTY", 
          "AOOTTW",
          "ABBJOO",
          "EHRTVW",
          "CIMOTU",
          "DISTTY",
          "EIOSST",
          "DELRVY",
          "ACHOPS",
          "HIMNQU",
          "EEINSU",
          "EEGHNW",
          "AFFKPS",
          "HLNNRZ",
          "DEILRX",
          ]

  
  def __init__(self):
    self.board = [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]
    
    self.print_board() 
    
  

  def shake(self):
    print("shaker ran")
    counter = 0
    for r in range(4):
      for c in range(4):
        letter = random.choice(BoggleBoard.DICE[counter])
        if letter == "Q":
          self.board[r][c] = "Qu"
        else:
          self.board[r][c] = letter + " "
        counter += 1
    self.print_board()
  
 

  
  def print_board(self):
    for line in self.board:
      print(" ".join(line))

        


    


    

game = BoggleBoard()
game.shake()

