def on_button_pressed_a():
    basic.show_string("HAPPY BIRTHDAY")
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.B, on_button_pressed_b)

for index in range(4):
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.pause(500)