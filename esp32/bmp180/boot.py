from bmp180 import BMP180
from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

temp = bmp180.temperature
p = bmp180.pressure
altitude = bmp180.altitude
print(temp, p, altitude)