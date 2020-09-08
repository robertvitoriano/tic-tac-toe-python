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


def switch_turn():

      if(player_turn == 1):
          player_turn = 2
      else:
          player_turn = 1


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
          

            
       else:
         place_character(player2_symbol, player1_x_position, player1_y_position)
    switch_turn()




       

