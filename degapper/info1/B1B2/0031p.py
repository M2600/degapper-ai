from ModuleName import pino, pin2, display
while True:
    val = int(330*pin2. read_analog()/1023 - 60)
    display.scroll(str(val)+ 'C')
    if val >= 30:
        pin0.write_digital(1)
    else:
        pinO.write_digital(0)