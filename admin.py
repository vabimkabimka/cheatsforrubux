import os

PAYLOAD = r"V:\test\топтест\button.py"  # Вкажи правильний шлях!

# Створюємо VBS-файл для запуску Python без вікна
vbs_script = rf'''
Set objShell = CreateObject("Shell.Application")
objShell.ShellExecute "pythonw.exe", "{PAYLOAD}", "", "runas", 0
'''

# Записуємо VBS-файл
vbs_path = r"C:\Users\Public\bypass.vbs"
with open(vbs_path, "w") as f:
    f.write(vbs_script)

# Запускаємо його
os.system(f"wscript.exe {vbs_path}")

# Видаляємо файл після запуску
os.remove(vbs_path)

print("✅ Скрипт запущено з адмінськими правами!")
