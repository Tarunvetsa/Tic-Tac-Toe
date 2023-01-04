import sys
from multipledispatch import dispatch

#it is a decorator to be used in python for method overloading (it changes the signature of the function) 

class greeting(object):
    def greet_user(self, currplayer):
        print("It's your turn player " + currplayer.symbol)

#used to greet a player

class Player(object):
    # can have human or computer players
    pass


class Player1(Player):
#class inherited from the parent class Player
    def __init__(self):
        self.symbol = "X"
		#initialising the object and setting the symbol for the player.

    def __move():
        print(f"player1 you won in moves which can be improved")
		#printing the code after knowing the no.of moves
    def fun(self):
        self.__move()

class Player2(Player):

    def __init__(self):
        self.symbol = "O"
#polymorphism being used in the classes player1 and player2
    def __move():
        print(f"player2 you won in moves which can be improved")

    def fun(self):
        self.__move()

class ComputerPlayer(Player):
    # an instance of the player class
    pass


class checkings(object):
    def __init__(self, board):
        self.board = board
#The base class of the class hierarchy.
    def check_win(self, player_symbol):
        tiles = self.board.tiles

        for i in range(3):
            if tiles[i] == player_symbol and tiles[i+3] == player_symbol and tiles[i+6] == player_symbol:  # vertical
                return (player_symbol, "vertically")
            elif tiles[(i*3)] == player_symbol and tiles[(i*3) + 1] == player_symbol and tiles[(i*3) + 2] == player_symbol:  # horizontal
                return (player_symbol, "horizontally")

            if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
                return (player_symbol, "diagonally")
            elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
                return (player_symbol, "diagonally")

        return False

    @dispatch(str, str, int, int)
	#using the dispatch method mentioned earlier
    def game_over(self, player_symbol, k, player_move, player1_moves):
        if player1_moves < 3:
            print("It's over! player1 with " + player_symbol + " wins!\n" +
                  f"By placing {player_symbol} at {player_move} and " + "by completing "+k)
        else:
            print("It's over! player1 with " + player_symbol + " wins!\n" +
                  f"By placing {player_symbol} at {player_move} and " + "by completing "+k)
            #Player1.move(player1_moves)
            obj1._Player1__move()
	#method overloading being used here 
    @dispatch(str, str, int)
    def game_over(self, player_symbol, k, player2_moves):
        if player2_moves < 3:
            print("It's over! player2 " + player_symbol +
                  " wins!\n" + "By completing "+k)
        else:
            print("It's over! player2 " + player_symbol +
                  " wins!\n" + "By completing "+k)
            #Player2.move(player2_moves)
            

class playGame(checkings, greeting, Player1, Player2):
    def __init__(self, board, obj1, obj2):
        self.board = board
        self.players = [obj1, obj2]
        self.turn = 0

    def play(self):
        flag = False
        player1_moves = 0
        player2_moves = 0

        while flag == False:
            currplayer = self.players[self.turn]
            # print board
            self.board.print_board()

            self.greet_user(currplayer)
            if self.turn == 0:
                move = Move(self.board, currplayer)
                player_move = move.ask_for_move()
                self.board.tiles[player_move] = currplayer.symbol
                player1_moves += 1
            else:
                move = Move(self.board, currplayer)
                player_move = move.ask_for_move()
                self.board.tiles[player_move] = currplayer.symbol
                player2_moves += 1
            # checks for a win
            winner = self.check_win(currplayer.symbol)
            if winner != False:
                if currplayer == obj1:
                    checkings.game_over(
                        winner[0], winner[1], player_move, player1_moves)
                    flag = True
                    self.board.print_board()
                if currplayer == obj2:
                    checkings.game_over(winner[0], winner[1], player2_moves)
                    flag = True
                    self.board.print_board()
            else:
                self.turn = 1 - self.turn


class Board(object):
    # has a list of tiles
    def __init__(self):
        self.tiles = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    def arrange_board(self):
        board = [self.tiles[0], self.tiles[1], self.tiles[2]], [self.tiles[3],
                                                                self.tiles[4], self.tiles[5]], [self.tiles[6], self.tiles[7], self.tiles[8]]
        return board

    def print_board(self):
        board = self.arrange_board()
        for row in board:
            sys.stdout.write("|")
            for tile in row:
                sys.stdout.write(str(tile) + "|")
            sys.stdout.write("\n")


class Move(object):
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def ask_for_move(self):
        flag = False
        possible_moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        while (flag != True):
            move = input(
                "Please enter the number where you wanna move your " + self.player.symbol + ":")

            # check to see if user entered a number 0-8, if so, convert to int.
            if move in possible_moves:
                move = int(move)
            else:
                print("please enter valid move")
                return self.ask_for_move()

            # check to see if tile user wants to use is empty, or if someone has already played a piece there.
            if str(move) != self.board.tiles[move]:
                print("Someone has already moved to that spot. Move to an open tile.")
                return self.ask_for_move()

            return move


obj1 = Player1()
obj2 = Player2()
my_board = Board()
my_game = playGame(my_board, obj1, obj2)
my_game.play()
