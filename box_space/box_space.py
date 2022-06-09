from pynput import keyboard
import playsound
import pathlib

BASE_DIR=pathlib.Path(__file__).resolve().parent
 
def on_key_press(key):

    if key == keyboard.Key.esc: 
        return False
    if key== keyboard.Key.space:

        playsound.playsound(BASE_DIR.joinpath('ee-er-sound-effect.mp3').absolute())

         

     
def box_space():  
    with keyboard.Listener(on_press=on_key_press) as listener:
        try:
            listener.join()   
        except: 
            pass 



if __name__ == '__main__':
    box_space()
    
