from machine import Pin, SoftI2C
import utime
import ahtx0

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.2f C" % sensor.temperature())
    print("Humidity: %0.2f %%" % sensor.humidity())
    utime.sleep(5)
    
    
    