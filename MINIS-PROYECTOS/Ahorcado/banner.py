
titulo = f'''
============================================================================================================
     ___       __    __    ______   .______        ______      ___       _______    ______        _______.
    /   \     |  |  |  |  /  __  \  |   _  \      /      |    /   \     |       \  /  __  \      /       |
   /  ^  \    |  |__|  | |  |  |  | |  |_)  |    |  ,----'   /  ^  \    |  .--.  ||  |  |  |    |   (----`
  /  /_\  \   |   __   | |  |  |  | |      /     |  |       /  /_\  \   |  |  |  ||  |  |  |     \   \    
 /  _____  \  |  |  |  | |  `--'  | |  |\  \----.|  `----. /  _____  \  |  '--'  ||  `--'  | .----)   |   
/__/     \__\ |__|  |__|  \______/  | _| `._____| \______|/__/     \__\ |_______/  \______/  |_______/    
============================================================================================================'''

ganador = f'''
==================================================================
____    __    ____  __  .__   __. .__   __.  _______ .______         
\   \  /  \  /   / |  | |  \ |  | |  \ |  | |   ____||   _  \        
 \   \/    \/   /  |  | |   \|  | |   \|  | |  |__   |  |_)  |       
  \            /   |  | |  . `  | |  . `  | |   __|  |      /        
   \    /\    /    |  | |  |\   | |  |\   | |  |____ |  |\  \----.   
    \__/  \__/     |__| |__| \__| |__| \__| |_______|| _| `._____|   
=================================================================='''

perdedor = f'''
==============================================================================================
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|   
==============================================================================================='''
    
          
def dibujo_ahorcado(intento):
        # Gestionar los mensajes se los intentos 
       if intento == 4:
            return '''
             -----
             |   \|
             O    |
             |    |
                  |
                  |
            ---------'''
       elif intento == 3:
             return '''
             -----
             |   \|
             O    |
            /|    |
                  |
                  |
            ---------'''
       elif intento == 2 :
            return '''
             -----
             |   \|
             O    |
            /|\   |
                  |
                  |
            ---------'''
       elif intento == 1:
            return '''
             -----
             |   \|
             O    |
            /|\   |
            /     |
                  |
            ---------'''
       elif intento == 0:
            return f'''
            {perdedor}'''
       