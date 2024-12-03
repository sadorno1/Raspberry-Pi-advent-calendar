from machine import Pin
import time
import ujson

red_led = Pin(14, Pin.OUT)
green_led = Pin(25, Pin.OUT)

def music_color(file_path):

    with open(file_path, 'r') as f:
        midi_data = ujson.load(f)

    start_time = time.time()  # Record the starting time
    for note_data in midi_data:
        # Wait until the correct time for the note
        while time.time() - start_time < note_data['time']:
            pass

        # Light up the corresponding LED based on the note type
        if note_data['type'] == 'high':
            light_green()
        else:
            light_red()

def light_green():

    green_led.value(1)  
    time.sleep(0.2)     
    green_led.value(0)  
    time.sleep(0.1)     

def light_red():
    red_led.value(1)  
    time.sleep(0.2)   
    red_led.value(0)  
    time.sleep(0.1)   

def main():
    time.sleep(1)
    music_color('midi_data.json')

main()
