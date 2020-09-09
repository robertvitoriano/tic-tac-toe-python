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

def place_character(char, x, y):
    if(position[x][y] == '|___|' or position[x][y] == '|   |'):

        position[x][y] = position[x][y][0] + position[x][y][1] + char + position[x][y][3] + position[x][y][4]

    elif(position[x][y] == '___' or position[x][y] == '   '):

        position[x][y] = position[x][y][0] + char + position[x][y][2]

def check_victory(symbol):
    was_game_won = False
     #vitoria X
    if(position[0][0][1] == symbol and position[0][1][2] == symbol and position[0][2][1] == symbol        # linha 1
       or position[1][0][1] == symbol and position[1][1][2] == symbol and position[1][2][1] == symbol     # linha 2
       or position[2][0][1] == symbol and position[2][1][2] == symbol and position[2][2][1] == symbol     # linha 3
       or position[0][0][1] == symbol and position[1][0][1] == symbol and position[2][0][1] == symbol     # coluna 1
       or position[0][1][2] == symbol and position[1][1][2] == symbol and position[2][1][2] == symbol     # coluna 2
       or position[0][2][1] == symbol and position[1][2][2] == symbol and position[2][2][1] == symbol     # coluna 3
       or position[0][0][1] == symbol and position[1][1][2] == symbol and position[2][2][1] == symbol     # diagonal 2
       or position[0][2][1] == symbol and position[1][1][2] == symbol and position[2][0][1]==  symbol ):  # diagonal 2
          print(symbol +"  ganhou") 
          was_game_won = True

    return  was_game_won 

def clean_table():
    position = [['___', '|___|', '___'], ['___', '|___|', '___'], ['   ', '|   |', '   ']]
    return position



while(is_running):
     
    print("Você quer jogar com 'O' ou 'X' ? Digite abaixo")
    input_symbol = input().upper()
    position = clean_table()
    while(not was_game_won):

       inform_turn()

       print_table()

       print("Digite a Posição desejada")
       x_position = int(input()) - 1
       y_position = int(input()) - 1

       if(player_turn==1):
           current_character = "X"
           place_character(current_character, x_position, y_position)
           was_game_won =  check_victory(current_character)
           if(was_game_won):
              print_table()
           player_turn = 2
       else:
           current_character = "O"
           place_character(current_character, x_position, y_position)
           was_game_won =  check_victory(current_character)
           if(was_game_won):
              print_table()
           player_turn = 1

    right_response = False

    while(right_response == False):
       print("Você deseja Jogar novamente ? Digite Sim ou Não")

       response = input().lower()
       if(response == "sim" or response == "não"):
          right_response = True
          if(response =="sim"):
              is_running = True
              was_game_won = False
          else:
              is_running = False
       else:
            print("Informação incorreta ! Digite novamente abaixo !")
            right_response = False


