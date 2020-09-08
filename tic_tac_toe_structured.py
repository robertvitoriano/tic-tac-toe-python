is_running = True
position = [['___', '|___|', '___'], ['___', '|___|', '___'], ['   ', '|   |', '   ']]
player_turn = 1
was_game_won = False

def print_table():
        print(position[0][0]+position[0][1]+position[0][2])
        print(position[1][0]+position[1][1]+position[1][2])
        print(position[2][0]+position[2][1]+position[2][2])

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



while(is_running):

    print("Você quer jogar com 'O' ou 'X' ? Digite abaixo")
    player1_symbol = input().upper()
    while(was_game_won):

       inform_turn()

       if(player1_symbol == "X"):
           player2_symbol = "O"
       else:
           player2_symbol = "X"

       print("Digite a Posição desejada")
       player1_x_position = int(input())
       player1_y_position = int(input())
       if(player_turn==1):
          place_character(player1_symbol, player1_x_position, player1_y_position)

       print_table()
     