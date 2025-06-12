from pystubit.board import pino, pin2
from pystubit_iot import wifi_config, wifi_connect, wifi_ifconfig, get_request
import time

wifi_config(ssid='SSID', pwd = 'PASSWORD')
wifi_connect(trytime=5)
wifi_ifconfig(('A', 'B', 'C', 'D'))
url = 'http://example.com/cgi-bin/device1.py/'

while True:
    time.sleep (1)
    val = int(330 * pin2.read_analog() / 1023 - 60)
    response = get_request(url, {'sens': str(val)})
    r = response.splitlines()
    if r[0] == 'ON':
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)