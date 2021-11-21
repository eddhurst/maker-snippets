import plasma
from plasma import plasma2040
import time

# Import helpers for RGB LEDs, Buttons, and Analog
from pimoroni import RGBLED, Button, Analog

# Press "A" to change between 4 speed settings slow to fast
# Press "B" to change the color cycle. Blue, Red, Yellow, Full
# Press "Boot" to toggle pulse function

# Set how many LEDs you have
NUM_LEDS = 50
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

# The speed that the LEDs will start cycling at
DEFAULT_SPEED = 4

# How many times the LEDs will be updated per second
UPDATES = 60

# Color spectrum
COLOR_FULL = 0
COLOR_BLUE = 1
COLOR_PINK = 2
COLOR_YELLOW = 3

color_options = [
    [0.0, 1.0], # FULL
    [0.4, 0.7], # BLUE
    [0.79, 0.935], # PINK
    [0.1, 0.15], # YELLOW
]

# instantiate references
button_boot = Button(plasma2040.USER_SW) # boot
button_a = Button(plasma2040.BUTTON_A) # button a
button_b = Button(plasma2040.BUTTON_B) # button b
led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B) # onboard LED

# Start updating the LED strip
led_strip.start()

# LED defaults
speed = DEFAULT_SPEED
selected_color = COLOR_PINK
offset = 0.0
should_pulse = False

# Smoothly pulse forwards and backwards in a given range on the color spectrum
def pulseInRange(selected_color, val):
    min = color_options[selected_color][0]
    max = color_options[selected_color][1]
    pulse_range = (max - min) * 2.0
    progress = val % pulse_range
    pulse = progress if progress < pulse_range / 2.0 else pulse_range - progress
    return pulse + min

# Make rainbows
while True:
    boot = button_boot.read()
    a = button_a.read()
    b = button_b.read()

    if boot:
        should_pulse = not should_pulse
        print(should_pulse)
    else:
        if a:
            if speed > 20:
                speed = 4
            else:
                speed += 4
            print("Speed: ", speed)
        if b:
            if selected_color is COLOR_PINK:
                selected_color = COLOR_BLUE
            elif selected_color is COLOR_BLUE:
                selected_color = COLOR_YELLOW
            elif selected_color is COLOR_YELLOW:
                selected_color = COLOR_FULL
            else:
                selected_color = COLOR_PINK

    speed = min(255, max(1, speed))
    offset += float(speed) / 2000.0
    
    for i in range(NUM_LEDS):
        
        if should_pulse:
            current_color = pulseInRange(selected_color, offset)
        else:
            current_color = color_options[selected_color][0]
        
        led_strip.set_hsv(i, current_color, 1.0, 1.0)

    # onboard led
    led.set_rgb(50,50,50)

    time.sleep(1.0 / UPDATES)
