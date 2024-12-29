import pyautogui
import keyboard
import threading
import sys
import os
print('KeyboardMouse')
print('By Parry-Utkanos')
# Default mouse movement step
MOVE_STEP = 1
# Default keys for clicks
RIGHT_CLICK_KEY = 'r'
LEFT_CLICK_KEY = 'y'
MIDDLE_CLICK_KEY = 't'
# Default movement mode
MOVE_MODE = 'ARROWS'

ALT_PRESSED = False
CONSOLE_OPENED = False  # New variable to track console state
console_thread_obj = None  # Global variable for console thread


def on_key_event(event):
    global ALT_PRESSED
    global MOVE_STEP
    global RIGHT_CLICK_KEY
    global LEFT_CLICK_KEY
    global MIDDLE_CLICK_KEY
    global MOVE_MODE
    global CONSOLE_OPENED
    global console_thread_obj

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'alt':
            ALT_PRESSED = True
        elif ALT_PRESSED:
            if event.name == '`' or event.name == '~':
                if not CONSOLE_OPENED:
                    open_console()
                    CONSOLE_OPENED = True
                else:
                    print("Console is already opened.")
            elif MOVE_MODE == 'ARROWS':
                if event.name == 'left':
                    pyautogui.move(-MOVE_STEP, 0)
                elif event.name == 'up':
                    pyautogui.move(0, -MOVE_STEP)
                elif event.name == 'right':
                    pyautogui.move(MOVE_STEP, 0)
                elif event.name == 'down':
                    pyautogui.move(0, MOVE_STEP)
            elif MOVE_MODE == 'AWSD':
                if event.name == 'a':
                    pyautogui.move(-MOVE_STEP, 0)
                elif event.name == 'w':
                    pyautogui.move(0, -MOVE_STEP)
                elif event.name == 'd':
                    pyautogui.move(MOVE_STEP, 0)
                elif event.name == 's':
                    pyautogui.move(0, MOVE_STEP)
            elif event.name == RIGHT_CLICK_KEY:
                pyautogui.click(button='right')
            elif event.name == LEFT_CLICK_KEY:
                pyautogui.click(button='left')
            elif event.name == MIDDLE_CLICK_KEY:
                pyautogui.click(button='middle')

    elif event.event_type == keyboard.KEY_UP:
        if event.name == 'alt':
            ALT_PRESSED = False


def parse_command(command):
    global MOVE_STEP
    global RIGHT_CLICK_KEY
    global LEFT_CLICK_KEY
    global MIDDLE_CLICK_KEY
    global MOVE_MODE

    parts = command.split(' ')
    if len(parts) < 1:
        print("Invalid input")
        return
    cmd = parts[0].lower()
    if cmd == "/mpx":
        if len(parts) > 1:
            try:
                MOVE_STEP = int(parts[1])
                print(f"Movement step changed to: {MOVE_STEP}")
            except ValueError:
                print("Invalid number format")
        else:
            print("Please enter a movement step.")
    elif cmd == "/mrc":
        if len(parts) > 1:
            RIGHT_CLICK_KEY = parts[1].lower()
            print(f"Right click key changed to: {RIGHT_CLICK_KEY}")
        else:
            print("Please enter a key for the right click.")
    elif cmd == "/mlc":
        if len(parts) > 1:
            LEFT_CLICK_KEY = parts[1].lower()
            print(f"Left click key changed to: {LEFT_CLICK_KEY}")
        else:
            print("Please enter a key for the left click.")
    elif cmd == "/mcc":
        if len(parts) > 1:
            MIDDLE_CLICK_KEY = parts[1].lower()
            print(f"Middle click key changed to: {MIDDLE_CLICK_KEY}")
        else:
            print("Please enter a key for the middle click.")
    elif cmd == "/mck":
        if len(parts) > 1:
            key_name = parts[1].lower()
            if key_name in ['enter', 'right_alt', 'left_alt', 'delete', 'end', 'home', 'pgup', 'pgdn', '!', '1']:
                print(f"Selected key: {key_name}")
            else:
                print("Invalid key.")
        else:
            print("Enter a key.")
    elif cmd == "/mc":
        if len(parts) > 1:
            mode = parts[1].upper()
            if mode == "AWSD" or mode == "ARROWS":
                MOVE_MODE = mode
                print(f"Movement mode changed to: {MOVE_MODE}")
            else:
                print("Unknown movement mode.")
        else:
            print("Choose a movement mode: ARROWS or AWSD")
    else:
        print("Unknown command")


def console_thread():
    while True:
        command = input("Enter command: ")
        parse_command(command)


def open_console():
    global console_thread_obj
    if console_thread_obj is None:
        console_thread_obj = threading.Thread(target=console_thread)
        console_thread_obj.daemon = True  # For termination with the main thread.
        console_thread_obj.start()

def main():
    keyboard.hook(on_key_event)  # Set keyboard hook
    keyboard.wait('esc')  # Wait for Esc key


if __name__ == '__main__':
    main()
