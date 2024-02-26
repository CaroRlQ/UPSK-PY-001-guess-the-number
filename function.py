import random

# Función para generar número secreto 

def random_number():
  number = random.randint(0,100) 
  return number 



def number_player ():
 
    # number_player=[]
    # number_player.append(number)   
    while True:
        number_player = input("\033[1;37m"+"JUGADOR 1, realice su jugada ---> ")   
              
        if not number_player.isdigit():
            print("\033[3;35m"+'Ingrese un valor númerico (número entero)')
     
            
        elif int(number_player) > 100:   
           print("\033[3;35m"+'Ingrese un valor válido (número menor a 100)')
         # Condicional en caso el número sea mayor a 100
         
        
        else:
         return int(number_player)
 
    
   
def play_start(number_player, secret_number):
     
   
        # print ("\033[1;37m" + f'{player} ---> {number}')
        # Condicionales para el comparativo del valor ingresado y el número secreto.
        if number_player == secret_number :
                 print("\033[1;33m"+'¡Felicitaciones, lo lograste!')
                #  print( number_player())
                 return True
        
        elif number_player < secret_number:
     
                 print ("\033[3;35m"+'Es muy bajo') 
         
        else :
                 print("\033[3;35m"+'Es muy alto')
                 return False
   