# KeyboardMouse
![Icon](ico.png)
### Language: [python (3.11)](https://www.python.org/downloads/release/python-3110/)
### OS: Windows ([7](https://www.microsoft.com/ru-ru/software-download/windows7)/[10](https://www.microsoft.com/ru-ru/software-download/windows10)/[11](https://www.microsoft.com/ru-ru/software-download/windows11))
##### Requirements:  At least [Python 3.11](https://www.python.org/downloads/release/python-3110/), Libraries pyautogui; keyboard; threading; os; sys.

## Software setup:


##### Mouse Control Configuration Commands

The following commands can be used in the console (activated with `Alt + ~`) to configure the mouse control program:

•   **`/mpx <number>`**
    *   **Description:** Sets the mouse movement step size. The mouse will move this many pixels on each press of the movement keys.
    *   **Example:** `/mpx 5`  (Sets the step to 5 pixels).
    *   **Note:** Must be a whole number.

•   **`/mrc <key>`**
    *   **Description:** Sets the key used for right mouse click.
    *   **Example:** `/mrc e` (Sets right click key to `e`).
    *   **Note:** Must be a single character.

•   **`/mlc <key>`**
    *   **Description:** Sets the key used for left mouse click.
    *   **Example:** `/mlc q` (Sets left click key to `q`).
     *   **Note:** Must be a single character.

•  **`/mcc <key>`**
    *   **Description:** Sets the key used for the middle mouse click (scroll wheel).
    *   **Example:** `/mcc v` (Sets middle click to `v`).
    *   **Note:** Must be a single character.

•   **`/mck <key>`**
    *   **Description:** Selects the key that can be used for a command. Supported keys are: `enter`,`right_alt`,`left_alt`,`delete`,`end`,`home`,`pgup`,`pgdn`,`!`,`1`
    *   **Example:** `/mck home` (Select the Home key)
    *   **Note:** One key must be selected from the list.

•   **`/mc <mode>`**
    *   **Description:** Sets the movement mode. Allows you to choose if you want to move the mouse with arrow keys or with AWSD keys.
    *   **Example:** `/mc AWSD` (Sets the movement mode to use `AWSD` keys)
    *   **Available modes:** `ARROWS`, `AWSD`.
    *    **Note:** Must be one of the provided modes.

**Important Notes:**

•   Commands are not case-sensitive.
•   Commands should be entered in the console activated by `Alt + ~`.
•   After changing a setting, the program must continue to run for changes to take effect.
•   Invalid command or value formats will be reported in the console.
•   The program can be terminated by pressing the `Esc` key.

