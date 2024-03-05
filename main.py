import function
from function import *
from colorama import Style
from collections.abc import Sequence

def game_play():
     # Crear número secreto random
    secret_number = random_number()
    print(secret_number)
    
    # variable para guardar cantidad de rondas
    number_round = 1
    attemp_player = []   
    
    print("\033[0;33m"+"""
             ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 
             ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
             **   *   *   *   *  *  *  *  *  *  *  *  *  *  *   **
             **   *                                         *   **
             **   *        ¡¡¡Bienvenido al juego!!!        *   **
             **   *                                         *   **
             **   *                                         *   **
             **   *   *   *   *  *  *  *  *  *  *  *  *  *  *   **
             ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 
             ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **""")
 
    while True:
        
   
     print( "\033[37;44m"+ f"========================> ROUND {number_round} <=========================")
     print(Style.RESET_ALL)
     
     number_round += 1  
   
     # Pedido de turno de jugador y validación de número
     number_player1 = number_player()
     
     # Guardado de intento 
     attemp_player.append(number_player1)     
     
     # Generar turno de jugador     
     
     if  play_start(number_player1, secret_number):
         print("\033[1;33m"+f"Tus jugadas ---> {attemp_player}" )
         break
     
     else:
       
        computer_number = random_number()
        print("\033[1;37m"+f"COMPUTADORA, jugada ---> {computer_number}" ) 
        play_start(computer_number, secret_number)
        
 
  

game_play()



