import random
import pyautogui
import keyboard
import mouse

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

# Блокування скрипта, поки не натиснуто 'Esc'
keyboard.wait("esc")