def my_function():
    global B
    B = 0
    display.set_matrix_color(3, 4, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.set_matrix_color(3, 5, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.DOWN,
    GAME_ZIP64.ZIP64ButtonEvents.UP,
    my_function)

def my_function2():
    global B
    B = 1
    display.set_matrix_color(3, 4, GAME_ZIP64.colors(ZipLedColors.RED))
    display.set_matrix_color(3, 5, GAME_ZIP64.colors(ZipLedColors.RED))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.DOWN,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function2)

def my_function3():
    global F
    F = 0
    display.set_matrix_color(3, 1, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.set_matrix_color(3, 2, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.UP,
    GAME_ZIP64.ZIP64ButtonEvents.UP,
    my_function3)

def my_function4():
    global H
    H = 0
    display.set_matrix_color(4, 3, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.set_matrix_color(5, 3, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.RIGHT,
    GAME_ZIP64.ZIP64ButtonEvents.UP,
    my_function4)

def my_function5():
    global V
    V = 1
    display.set_matrix_color(1, 3, GAME_ZIP64.colors(ZipLedColors.RED))
    display.set_matrix_color(2, 3, GAME_ZIP64.colors(ZipLedColors.RED))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.LEFT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function5)

def my_function6():
    global fart
    if fart < 100:
        fart += 5
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.FIRE1,
    GAME_ZIP64.ZIP64ButtonEvents.CLICK,
    my_function6)

def my_function7():
    global V
    V = 0
    display.set_matrix_color(1, 3, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.set_matrix_color(2, 3, GAME_ZIP64.colors(ZipLedColors.BLACK))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.LEFT,
    GAME_ZIP64.ZIP64ButtonEvents.UP,
    my_function7)

def my_function8():
    global H
    H = 1
    display.set_matrix_color(4, 3, GAME_ZIP64.colors(ZipLedColors.RED))
    display.set_matrix_color(5, 3, GAME_ZIP64.colors(ZipLedColors.RED))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.RIGHT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function8)

def my_function9():
    global F
    F = 1
    display.set_matrix_color(3, 1, GAME_ZIP64.colors(ZipLedColors.RED))
    display.set_matrix_color(3, 2, GAME_ZIP64.colors(ZipLedColors.RED))
    display.show()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.UP,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function9)

def my_function10():
    global fart
    if fart > 0:
        fart += -5
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.FIRE2,
    GAME_ZIP64.ZIP64ButtonEvents.CLICK,
    my_function10)

fartDisplay = 0
V = 0
H = 0
F = 0
B = 0
fart = 0
display: GAME_ZIP64.ZIP64Display = None
radio.set_group(62)
display = GAME_ZIP64.create_zip64_display()
display.set_brightness(40)
fart = 50

def on_forever():
    global fartDisplay
    fartDisplay = Math.map(fart, 0, 100, 0, 7)
    for indeks in range(8):
        if indeks < fartDisplay:
            display.set_matrix_color(7, 7 - indeks, GAME_ZIP64.colors(ZipLedColors.BLUE))
        else:
            display.set_matrix_color(7, 7 - indeks, GAME_ZIP64.colors(ZipLedColors.BLACK))
        display.show()
basic.forever(on_forever)
