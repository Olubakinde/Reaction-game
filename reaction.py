from sense_hat import SenseHat
import time
import random

# Initialize Sense HAT
sense = SenseHat()

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Function to display a random pixel and measure reaction time
def reaction_time_test():
    sense.clear()
    # Pick a random position to light up
    x = random.randint(0, 7)
    y = random.randint(0, 7)

    # Display the pixel
    sense.set_pixel(x, y, green)

    start_time = time.time()

    # Wait for the joystick button press
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                reaction_time = time.time() - start_time
                sense.clear()
                sense.show_message(f"{reaction_time:.2f} s", text_colour=red, back_colour=black)
                return
        time.sleep(0.1)

# Main loop
try:
    while True:
        # Wait for joystick press to start the game
        game_started = False
        while not game_started:
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    game_started = True
                    reaction_time_test()

except KeyboardInterrupt:
    sense.clear()  # Clear display on exit
    print("Reaction time game terminated")
