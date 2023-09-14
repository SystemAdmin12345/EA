"""
E
"""

import time

# Vars
COUNTER = 0
MAX = 100
MODE = 0
UPPER = 10
LOWER = 5

while COUNTER < MAX:
    UPPER = COUNTER + 10
    LOWER = UPPER - 5
    print(f"Upper: {UPPER}")
    print(f'lower: {LOWER}')
    while MODE == 0:
        if COUNTER <= UPPER:
            print("LIFT GOING UP")
            COUNTER += 1
            print(COUNTER)
        if COUNTER > UPPER:
            print("MAX FLOOR")
            MODE = 1
    while MODE == 1:
        if COUNTER >= LOWER:
            print("LIFT GOING DOWN")
            COUNTER -= 1
            print(COUNTER)
        if COUNTER < LOWER:
            print("MIN FLOOR")
            MODE = 0
    time.sleep(1)

