import random
from colorama import Fore, Back, Style, init



# Crear el número aleatorio del 1-100
secret_number = random.randint(0,100)
print(secret_number )

correct_answer= True
number_round = 1;
attemps_player = []
attemps_computer = []

while  correct_answer:
   
    print()
    print ( "\033[37;44m"+ f"-----------> Round {number_round } <-----------")
    print(Style.RESET_ALL)
    # Conteo de round para cada inicio de bucle
    number_round +=1

    # =====================> Turno del jugador <==================================
    player_number = input("\033[1;37m"+"JUGADOR 1, realice su jugada ---> ")

    # Condicional en caso el número ingresado no sea int
    if not player_number.isdigit():
        print("\033[3;35m"+'Ingrese un valor válido (número entero)')
    # Condicional en caso el número sea mayor a 100
    elif int(player_number) > 100 :
        print("\033[3;35m"+'Ingrese un número válido menor no mayor a 100')   
    else:
    # Conversión de número de jugador a un int (dato númerico)
     player_number = int(player_number)
     attemps_player.append(player_number)
     # Condicional en caso el valor sea igual al número secreto
     if player_number == secret_number:
           
           print("\033[0;33m"+'¡Felicitaciones, lo lograste!')
           print (attemps_player)
           correct_answer = False
        
     # Condicional en caso el valor sea menor al número secreto
     elif player_number < secret_number:
           print("\033[3;35m"+'Es un número muy bajo')
    # Condicional en caso el valor sea mayor al número secreto 
     else :
           print("\033[3;35m"+'Es un número muy alto')
          
    # =====================> Turno de la computadora <================================== 
    
     computer_number = random.randint(0, 100)
     attemps_computer.append(computer_number)
    
     print ("\033[1;37m" + f'TU COMPUTADORA ---> {computer_number}')
    # Condicionales para el comparativo del valor ingresado y el número secreto.
     if computer_number == secret_number :
           print("\033[1;33m"+'¡Felicitaciones, lo lograste!')
           print(computer_number)
           correct_answer = False
        
     elif computer_number < secret_number:
     
           print ("\033[3;35m"+'Es un número muy bajo') 
         
     else :
           print("\033[3;35m"+'Es un número muy alto')
          
           
       
   
 

 