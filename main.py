import random
from colorama import Fore, Back, Style, init

init()

# Crear el número aleatorio del 1-100
secret_number = random.randint(0,100)
print(secret_number )

#print(secret_number)

# Obtener el valor dado por el jugador
#player_number = int(input("Player 1, enter your guess "))

# Generar número de la computadora




#Comparar número secreto con número dado por la jugadora

correct_answer= True
number_round = 1;

while  correct_answer:
   
    # number_round = number_round+1
    print()
    print ( "\033[37;44m"+ f"---> Round {number_round } <---")
    print(Style.RESET_ALL)
    number_round +=1
    # try: 
    # # Turno del jugarerdor 01  
    #  player_number = int(input("Player 1, enter your guess "))

    # except ValueError:
    #    print('Debe ingresar un número válido')
    #    continue
    player_number = input("\033[1;37m"+"JUGADOR 1, realice su jugada ---> ")

    
    if not player_number.isdigit():
        print('Ingrese un valor válido (número entero)')
     
    elif int(player_number) > 100 :
        print('Ingrese un número válido menor no mayor a 100')   
    else:
     
     player_number = int(player_number)
     
     if player_number == secret_number:
          
           print("\033[0;33m"+'¡Felicitaciones, lo lograste!')
           correct_answer = False
           break
     elif player_number < secret_number:
           print("\033[3;35m"+'Es un número muy bajo')
       
     else :
           print("\033[3;35m"+'Es un número muy alto')
          
    # Tturno de la computadora 
     computer_number = random.randint(0, 100)
    
     print ("\033[1;37m" + f'TU COMPUTADORA ---> {computer_number}')
 
     if computer_number == secret_number :
           print("\033[1;33m"+'¡Felicitaciones, lo lograste!')
           correct_answer = False
        
     elif computer_number < secret_number:
     
           print ("\033[3;35m"+'Es un número muy bajo') 
         
     else :
           print("\033[3;35m"+'Es un número muy alto')
          
           
       
   
 

 