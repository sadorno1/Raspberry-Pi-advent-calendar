from machine import Pin
import time

pete = Pin(14, Pin.OUT)
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}

def point():
    pete.value(1)  
    time.sleep(0.2)  
    pete.value(0)  
    time.sleep(0.2)
    
def dash():
    pete.value(1)  
    time.sleep(1)  
    pete.value(0)  
    time.sleep(1)

def morse(palabra):
    for x in palabra:
        if  x == '.':
            point()
        else:
            dash()
    time.sleep(0.6)
            
    
def main():
    palabra = input('Enter a word: ').upper().strip()
    for x in palabra:
        morse(morse_code_dict[x])

main()
        
        
    

