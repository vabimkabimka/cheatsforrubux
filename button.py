import time
import keyboard
import threading

def delayed_print(key_name): time.sleep(5) # Затримка на 5 секунд
while True: event = keyboard.read_event(suppress=True) # Зчитуємо натиснуту клавішу 
if event.event_type == keyboard.KEY_DOWN: threading.Thread(target=delayed_print, args=(event.name,)).start()