GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Down, GAME_ZIP64.ZIP64ButtonEvents.Up, function () {
    B = 0
    display.setMatrixColor(3, 4, GAME_ZIP64.colors(ZipLedColors.Black))
    display.setMatrixColor(3, 5, GAME_ZIP64.colors(ZipLedColors.Black))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Down, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    B = 1
    display.setMatrixColor(3, 4, GAME_ZIP64.colors(ZipLedColors.Red))
    display.setMatrixColor(3, 5, GAME_ZIP64.colors(ZipLedColors.Red))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Up, GAME_ZIP64.ZIP64ButtonEvents.Up, function () {
    F = 0
    display.setMatrixColor(3, 1, GAME_ZIP64.colors(ZipLedColors.Black))
    display.setMatrixColor(3, 2, GAME_ZIP64.colors(ZipLedColors.Black))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Right, GAME_ZIP64.ZIP64ButtonEvents.Up, function () {
    H = 0
    display.setMatrixColor(4, 3, GAME_ZIP64.colors(ZipLedColors.Black))
    display.setMatrixColor(5, 3, GAME_ZIP64.colors(ZipLedColors.Black))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Left, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    V = 1
    display.setMatrixColor(1, 3, GAME_ZIP64.colors(ZipLedColors.Red))
    display.setMatrixColor(2, 3, GAME_ZIP64.colors(ZipLedColors.Red))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Fire1, GAME_ZIP64.ZIP64ButtonEvents.Click, function () {
    if (fart < 100) {
        fart += 5
    }
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Left, GAME_ZIP64.ZIP64ButtonEvents.Up, function () {
    V = 0
    display.setMatrixColor(1, 3, GAME_ZIP64.colors(ZipLedColors.Black))
    display.setMatrixColor(2, 3, GAME_ZIP64.colors(ZipLedColors.Black))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Right, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    H = 1
    display.setMatrixColor(4, 3, GAME_ZIP64.colors(ZipLedColors.Red))
    display.setMatrixColor(5, 3, GAME_ZIP64.colors(ZipLedColors.Red))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Up, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    F = 1
    display.setMatrixColor(3, 1, GAME_ZIP64.colors(ZipLedColors.Red))
    display.setMatrixColor(3, 2, GAME_ZIP64.colors(ZipLedColors.Red))
    display.show()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Fire2, GAME_ZIP64.ZIP64ButtonEvents.Click, function () {
    if (fart > 0) {
        fart += -5
    }
})
let fartDisplay = 0
let V = 0
let H = 0
let F = 0
let B = 0
let fart = 0
let display: GAME_ZIP64.ZIP64Display = null
radio.setGroup(62)
basic.showNumber(62)
display = GAME_ZIP64.createZIP64Display()
display.setBrightness(40)
fart = 50
basic.forever(function () {
    fartDisplay = Math.map(fart, 0, 100, 0, 7)
    for (let indeks = 0; indeks <= 7; indeks++) {
        if (indeks < fartDisplay) {
            display.setMatrixColor(7, 7 - indeks, GAME_ZIP64.colors(ZipLedColors.Blue))
        } else {
            display.setMatrixColor(7, 7 - indeks, GAME_ZIP64.colors(ZipLedColors.Black))
        }
        display.show()
    }
    radio.sendValue("F", F)
    radio.sendValue("B", B)
    radio.sendValue("V", V)
    radio.sendValue("H", H)
    radio.sendValue("fart", fart)
})
