input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
    for (let index = 0; index < 4; index++) {
        basic.showString("HAPPY BIRTHDAY")
    }
})
input.onButtonPressed(Button.B, function () {
    music.stopMelody(MelodyStopOptions.All)
})
for (let index = 0; index < 4; index++) {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.pause(500)
    basic.showLeds(`
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.pause(500)
}
