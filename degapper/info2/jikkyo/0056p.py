from pystubit.board import pin0, pin2
from pystuit_iot import wifi_config, wifi_connect, wifi_ifconfig, get_request
import time
wifi_config(ssid='SSID', pwd='PASSWORD')
wifi_connect(trytime=5)
wifi_ifconfig('IP_ADRESS', 'SUBNET_MASK', 'DEFAULT_GW', 'DNS')
url = 'http://example.net/cgi-bin/device.py'
while True:
    time.sleep(1)
    val = int(330 * pin2.read_analog() / 1023 - 60)
    response = get_request(url, {'sens': str(val)})
    r = response.splitlines()
    if r[0] == 'ON':
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)