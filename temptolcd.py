import utime
from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd


i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
 
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    lcd.clear()
    lcd.putstr(f"Temp: {temperature:.2f} {chr(223)}C")
    utime.sleep(2)