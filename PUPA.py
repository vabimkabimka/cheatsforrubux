import tkinter as tk
from pynput import keyboard
import sys
import os

# Список натиснутих клавіш
pressed_keys = set()

# Функція для виходу з програми при натисканні A + S
def on_press(key):
    global pressed_keys
    try:
        if key.char in ('a', 's'):
            pressed_keys.add(key.char)
        if pressed_keys == {'a', 's'}:  # Якщо обидві клавіші натиснуті
            os._exit(0)  # Повне завершення процесу
    except AttributeError:
        pass

def on_release(key):
    global pressed_keys
    try:
        if key.char in ('a', 's'):
            pressed_keys.discard(key.char)  # Видаляємо клавішу при відпусканні
    except AttributeError:
        pass

# Створюємо головне вікно
root = tk.Tk()
root.title("Persistent Tkinter Window")
root.geometry("400x300")

# Запускаємо слухач клавіатури
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Запускаємо Tkinter
root.mainloop()
