import random

# Función para generar número secreto 

def random_number():
  number = random.randint(0,100) 
  return number 
# Función para guardar jugada del "jugador 1"
def input_number_player():
  return input("\033[1;37m"+"JUGADOR 1, realice su jugada ---> ")


def number_player ():
   
    while True:
       
           try:
             number_player =  input_number_player()    
             number_player = int(number_player)
             
             if number_player > 100:
                 print("\033[3;35m"+'Ingrese un valor válido (número menor a 100)')
                 
             else: 
                break
             
           except ValueError:  
                 print("\033[3;35m"+'Ingrese un valor númerico (número entero)')
    
    return number_player        
         # Condicional en caso el número sea mayor a 100
   
 
    
# Función para turno de cada jugador   
def play_start(number_player, secret_number):
     
   
        # Condicionales para el comparativo del valor ingresado y el número secreto.
        if number_player == secret_number :
                 print("\033[1;33m"+'¡Felicitaciones, lo lograste!')
                #  print( number_player())
                 return True
        
        elif number_player < secret_number:
     
                 print ("\033[3;35m"+'Es muy bajo')
                 return False
         
        else :
                 print("\033[3;35m"+'Es muy alto')
                 return False



 

# FUNCIÓN PARA MEJORAR LAS JUGADAS DE LA COMPUTADOR

# def guess_computer( secret_number):

#   low=0
#   high=0
#   # number_computer= random.randint(0, 100);
#   number_computer =10
#   print(f'number_initial { number_computer}')
#   if number_computer < secret_number:
#     low=number_computer + 1
#     high=100
#     guess= random.randint(low, high) 
#     print(f' menor{high, low}')
#     return guess
#   else: 
   
#     high = number_computer - 1
#     low = 0
#     print(f'mayor{ low, high}')
#   guess= random.randint(low, high) 
#   print(f' mayor_guess{guess}')
#   return guess
  



# guess_computer(15)

