is_running = True
position = [['___', '|___|', '___'], ['___', '|___|', '___'], ['   ', '|   |', '   ']]
player_turn = 1
was_game_won = False
current_character = None


def print_table():
        print("   1   2   3")
        print("1 "+position[0][0]+position[0][1]+position[0][2])
        print("2 "+position[1][0]+position[1][1]+position[1][2])
        print("3 "+position[2][0]+position[2][1]+position[2][2])


def inform_turn():
    if(player_turn == 1):
         print("Vez do jogador 1")
    else:
        print("Vez do jogador 2")


def check_game_state():
    if(was_game_won):
        is_running = False
    else:
        is_running = True


def place_character(char, x, y):
    if(position[x][y] == '|___|' or position[x][y] == '|   |'):

        position[x][y] = position[x][y][0] + position[x][y][1] + char + position[x][y][3] + position[x][y][4]

    elif(position[x][y] == '___' or position[x][y] == '   '):

        position[x][y] = position[x][y][0] + char + position[x][y][2]


def switch_turn(player_turn,current_character,x,y):

      if(player_turn == 1):
          place_character(player1_symbol, player1_x_position,
                          player1_y_position)
          player_turn = 2
      else:
          place_character(player2_symbol, player1_x_position,
                          player1_y_position)
          player_turn = 1

def check_victory():
     #vitoria X
    if(position[0][0][1] == "X" and position[0][1][2] == "X" and position[0][2][1] == "X"     # linha 1
       or position[1][0][1] == "X" and position[1][1][2] == "X" and position[1][2][1] == "X"  # linha 2
       or position[2][0][1] == "X" and position[2][1][2] == "X" and position[2][2][1] == "X"  # linha 3
       or position[0][0][1] == "X" and position[1][0][1] == "X" and position[2][0][1] == "X"  # coluna 1
       or position[0][1][2] == "X" and position[1][1][2] == "X" and position[2][1][2] == "X"  # coluna 2
       or position[0][2][1] == "X" and position[1][2][2] == "X" and position[2][2][1] == "X"):# coluna 3
        print("Jogador 1 ganhou")
        was_game_won = True

    elif(position[0][0][1] == "O" and position[0][1][2] == "O" and position[0][2][1] == "O"     # linha 1
       or position[1][0][1] == "O" and position[1][1][2] == "O" and position[1][2][1] == "O"  # linha 2
       or position[2][0][1] == "O" and position[2][1][2] == "O" and position[2][2][1] == "O"  # linha 3
       or position[0][0][1] == "O" and position[1][0][1] == "O" and position[2][0][1] == "O"  # coluna 1
       or position[0][1][2] == "O" and position[1][1][2] == "O" and position[2][1][2] == "O"  # coluna 2
       or position[0][2][1] == "O" and position[1][2][2] == "O" and position[2][2][1] == "O"):# coluna 3
          print("Jogador 1 ganhou")
          was_game_won = True

while(is_running):

    print("Você quer jogar com 'O' ou 'X' ? Digite abaixo")
    player1_symbol = input().upper()
    while(not was_game_won):
       print_table()

       inform_turn()

       if(player1_symbol == "X"):
           player2_symbol = "O"
       else:
           player2_symbol = "X"



       print("Digite a Posição desejada")
       player1_x_position = int(input()) - 1
       player1_y_position = int(input()) - 1

       if(player_turn==1):
          place_character(player1_symbol, player1_x_position, player1_y_position)
          player_turn = 2
       else:
          place_character(player2_symbol, player1_x_position, player1_y_position)
          player_turn = 1

       check_victory()


       
       

