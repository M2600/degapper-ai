setRadioGroup(1)
if radio.received():
	receivedNumber = radioReceived()
	serialWrite(f"'a' = {receivedNumber}")
	wait(100)
