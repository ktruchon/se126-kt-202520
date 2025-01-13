#a file with some simple functions i utilize often in class code


#--CLEAR SCREEN FUNCTION-----------------------------------------
from os import system, name #required!

def clear():
    if name == 'nt':#for windows
        __ = system('cls')
    else:#for linux and mac
        __ = system('clear')
        
        
        
#--VALIDITY CHECK------------------------------------------------




#--INPUT CHECKS-------------------------------------------------
