from ModuleName import pin2, display
while True:
    val =int(330*pin2.read_analog()/1023 - 60)
    display.scroll(str(val)+'C')