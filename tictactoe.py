# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:02:05 2022

@author: Jam
"""

import numpy as np

class Board():
    
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
        
    def show_board(self):
        board_print = f"""
        | {self.board[0]} | {self.board[1]} | {self.board[2]} |
        _____________
        
        | {self.board[3]} | {self.board[4]} | {self.board[5]} |
        _____________
        
        | {self.board[6]} | {self.board[7]} | {self.board[8]} |        
        """
        print(board_print)
        
    def valid_move(self, move):
        try:
            move = int(move)
            remaining_moves = [int(i) for i in self.board if i not in ['X', 'O']]
            if move > 9 or move < 1:
                print('Move out of range, please choose a number between 1 and 9')
                return False
            elif move not in remaining_moves:
                print('Space already taken, please choose an available space.')
                return False
            else:
                return True
        except:
            print('Invalid move, please choose a number between 1 and 9.')
            return False
    
    def update_board(self, player_token, user_input):
        space = int(user_input) - 1
        self.board[space] = player_token
        
    def check_win(self, player_token):
        if all(i == player_token for i in self.board[0:3]):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in self.board[3:6]):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in self.board[6:9]):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in list(np.array(self.board)[[0,3,6]])):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in list(np.array(self.board)[[1,4,7]])):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in list(np.array(self.board)[[2,5,8]])):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in list(np.array(self.board)[[0,4,8]])):
            print(f'Player {player_token} is the winner!')
            return True
        if all(i == player_token for i in list(np.array(self.board)[[2,4,6]])):
            print(f'Player {player_token} is the winner!')
            return True
        
        
        
class Player():
    
    def __init__(self, player_token):
        self.player_token = player_token
        

class Game():
    
    def setup_game(self):
        self.board = Board()
        self.player_1 = Player('X')
        self.player_2 = Player('O')
        
    def take_turn(self, player_token):
        valid = False
        while not valid:
            self.board.show_board()
            user_input = input('Please choose a space: ')
            valid = self.board.valid_move(user_input)
        self.board.update_board(player_token, user_input)
    
    def play_game(self):
        self.setup_game()
        game_over = False
        while not game_over:
            for player in [self.player_1, self.player_2]:
                if len([i for i in self.board.board if i not in ['X', 'O']]) == 0:
                    print('No spaces left. Game Over!')
                    game_over = True
                    break
                else:
                    self.take_turn(player.player_token)
                game_over = self.board.check_win(player.player_token)
                if game_over:
                    break
        self.board.show_board()
        
if __name__ == '__main__':
    new_game = Game()
    
    new_game.play_game()
